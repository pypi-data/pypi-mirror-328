#!/usr/bin/env python3
"""Optional Dagster imports."""

from .exceptions import WorkflowDependencyError

try:
    from dagster import (
        asset,
        AssetIn,
        Definitions,
        define_asset_job,
        mem_io_manager,
    )
except ImportError as err:
    raise WorkflowDependencyError("dagster") from err


__all__ = [
    "asset",
    "AssetIn",
    "Definitions",
    "define_asset_job",
    "mem_io_manager",
]
