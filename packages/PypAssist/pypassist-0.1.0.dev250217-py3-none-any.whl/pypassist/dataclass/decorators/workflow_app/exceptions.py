#!/usr/bin/env python3
"""
Workflow app exceptions.
"""

from ...exceptions import DataclassError


class WorkflowAppError(DataclassError):
    """Base exception for work environment related errors."""


class WorkflowAppSetupError(WorkflowAppError):
    """Exception for work environment setup errors."""
