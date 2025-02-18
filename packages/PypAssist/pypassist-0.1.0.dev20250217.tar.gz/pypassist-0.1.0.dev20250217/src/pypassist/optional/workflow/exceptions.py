#!/usr/bin/env python3
"""Workflow-specific optional dependency errors."""

from ..exceptions import BaseOptionalDependencyError


class WorkflowDependencyError(BaseOptionalDependencyError):
    """Error raised when a workflow-related optional dependency is missing."""

    def __init__(self, package_name: str):
        super().__init__(package_name, extra_name="workflow")
