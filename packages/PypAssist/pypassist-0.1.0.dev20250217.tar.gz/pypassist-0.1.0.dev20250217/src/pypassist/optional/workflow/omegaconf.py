#!/usr/bin/env python3
"""Optional OmegaConf imports."""

from .exceptions import WorkflowDependencyError

try:
    from omegaconf import OmegaConf
except ImportError as err:
    raise WorkflowDependencyError("omegaconf") from err

__all__ = ["OmegaConf"]
