#!/usr/bin/env python3

"""
Export utilities.
"""

import logging
import pathlib

from ..exceptions import PypassistError

LOGGER = logging.getLogger(__name__)


## -- Exceptions
class ExportError(PypassistError):
    """Base exception for export utilities."""


class DirectoryNotFoundError(ExportError):
    """Raised when the parent directory for export doesn't exist."""


## -- Utilities


def check_parent_dir_exists(filepath):
    """
    Check if the parent directory exists without creating it.

    Args:
        filepath: Path to check
    Returns:
        bool: True if parent directory exists, False otherwise
    """
    filepath = pathlib.Path(filepath)
    return filepath.parent.exists()


def export_to_csv(dataframe, filepath, sep="\t", **kwargs):
    """
    Export DataFrame to CSV, assuming parent directory exists.

    Args:
        dataframe: DataFrame to export
        filepath: Output filepath
        sep: Separator to use, defaults to tab
        **kwargs: Additional arguments for pandas.to_csv()

    Raises:
        DirectoryNotFoundError: If parent directory doesn't exist
        ExportError: If there's an error during export
    """
    filepath = pathlib.Path(filepath).resolve()

    if not check_parent_dir_exists(filepath):
        raise DirectoryNotFoundError(
            f"Parent directory does not exist: {filepath.parent}"
        )

    LOGGER.debug("Exporting DataFrame to: %s", filepath)
    dataframe.to_csv(filepath, sep=sep, **kwargs)


def export_string(string, filepath, exist_ok=False, encoding="utf-8", makedirs=False):
    """
    Export a string to a file.

    Args:
        string (str): The string to export
        filepath (str): Output filepath
        exist_ok (bool): Whether to overwrite existing file
        encoding (str): Encoding to use
        makedirs (bool): Whether to create parent directories

    Raises:
        DirectoryNotFoundError: If parent directory doesn't exist
        ExportError: If there's an error during export
    """
    filepath = pathlib.Path(filepath).resolve()

    if makedirs:
        create_directory(filepath.parent)

    if not check_parent_dir_exists(filepath):
        raise DirectoryNotFoundError(
            f"Parent directory does not exist: {filepath.parent}"
        )

    if filepath.exists() and not exist_ok:
        raise FileExistsError(
            f"File already exists: {filepath} (use exist_ok=True to overwrite)."
        )

    with open(filepath, "w", encoding=encoding) as file:
        file.write(string)

    LOGGER.debug("Exporting string to file: %s", filepath)


def create_directory(directory_path, mode=0o755, exist_ok=True, parents=True):
    """
    Create a directory.

    Args:
        directory_path (str): Path to directory
        mode (int): Permissions to set on the directory
        exist_ok (bool): Whether existing directory is acceptable
        parents (bool): Whether to create parent directories if they don't exist

    Returns:
        Path: The path to the created directory
    """
    path = pathlib.Path(directory_path).resolve()
    path.mkdir(mode=mode, parents=parents, exist_ok=exist_ok)
    return path
