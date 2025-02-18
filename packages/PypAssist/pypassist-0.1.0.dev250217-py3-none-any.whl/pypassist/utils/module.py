#!/usr/bin/env python3
"""
Dynamic imports.
Largely inspired from a code made by Mike Rye.
"""

import importlib
import inspect
import logging
import pathlib
import pkgutil
import sys

LOGGER = logging.getLogger(__name__)


def find_modules(search_path, prefix=""):
    """
    Find Python modules in the specified directory.

    Args:
        search_path: Path to directory to search in
        prefix: Module name prefix for imports
    """
    if not search_path.exists():
        raise ImportError(f"Module path not found: {search_path}")

    LOGGER.debug("Searching for modules in %s with prefix %s", search_path, prefix)
    mods = pkgutil.iter_modules(path=[str(search_path)], prefix=prefix)

    return [m for m in mods if not m.ispkg]


def import_types(suffix, base_class, submod="type"):
    """
    Import types from submodules dynamically.

    Args:
        suffix: Class name suffix to match (e.g., "Generator")
        base_class: Base class whose location will be used to find types
        submod: Subdirectory name to search in (default: "type")
    """
    # Get module info from the base class
    base_module = ".".join(base_class.__module__.split(".")[:-1])
    base_path = pathlib.Path(inspect.getfile(base_class)).parent

    # Build path and prefix based on base class location
    path = base_path / submod
    prefix = f"{base_module}.{submod}."

    LOGGER.debug("Looking for types in %s with prefix %s", path, prefix)

    for modinfo in find_modules(path, prefix=prefix):
        try:
            LOGGER.debug("Importing %s", modinfo.name)
            mod = importlib.import_module(modinfo.name)

            for name, cls in inspect.getmembers(mod):
                if name.endswith(suffix) and cls != base_class:
                    LOGGER.debug("Found %s", name)
                    yield cls

        except ImportError as e:
            LOGGER.warning("Failed to import %s: %s", modinfo.name, e)


def reload_self():
    """
    Reload the calling module and update all references.

    Returns:
        Reloaded class object
    """
    stack = inspect.stack()
    prev_frame = stack[1]
    cls = prev_frame[0].f_locals["cls"]
    mod_name = cls.__module__

    mod = sys.modules[mod_name]
    LOGGER.debug("Reloading module: %s", mod)
    importlib.reload(mod)
    reloaded_cls = getattr(mod, cls.__name__)

    for frame in stack:
        for namespace in ("f_locals", "f_globals"):
            try:
                ns_vars = getattr(frame[0], namespace)
            except AttributeError:
                continue

            for key, val in list(ns_vars.items()):
                if val is cls:
                    ns_vars[key] = reloaded_cls

    return reloaded_cls
