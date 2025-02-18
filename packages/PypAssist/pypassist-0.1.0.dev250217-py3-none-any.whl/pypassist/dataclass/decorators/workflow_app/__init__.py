#!/usr/bin/env python3
"""Workflow application decorator package."""

from .decorator import workflow_app
from .exceptions import WorkflowAppSetupError

__all__ = ['workflow_app', 'WorkflowAppSetupError']
