#!/usr/bin/env python3
"""
Workflow application decorator.
"""

from pydantic.dataclasses import dataclass, is_pydantic_dataclass

from ....workflow.config.base import WorkflowConfig
from ..wenv.validation import is_wenv
from .exceptions import WorkflowAppSetupError


def workflow_app(_cls=None):
    """Decorator to ensure the configuration structure of a workflow application.

    - Checks the presence of the workflow attribute: WorkflowConfig
    - Checks that workenv is a class decorated with @wenv
    - Adds utility methods for integration with Hydra
    """

    def wrap(cls):
        if not is_pydantic_dataclass(cls):
            cls = dataclass(cls)

        class WorkflowAppConfig(cls):  # pylint: disable=C0115, R0903
            def __post_init__(self):
                if hasattr(super(), "__post_init__"):
                    super().__post_init__()

                if not hasattr(self, "workflow"):
                    raise WorkflowAppSetupError(
                        f"Missing required attribute 'workflow' in {self.__class__.__name__}. "
                        "Ensure you define a 'workflow' attribute in your workflow app dataclass."
                    )
                if not hasattr(self, "workenv"):
                    raise WorkflowAppSetupError(
                        f"Missing required attribute 'workenv' in {self.__class__.__name__}. "
                        "Ensure you define a 'workenv' attribute in your workflow app dataclass."
                    )

                if not isinstance(self.workflow, WorkflowConfig):
                    raise WorkflowAppSetupError(
                        f"Invalid type for 'workflow' in {self.__class__.__name__}. "
                        f"Expected 'WorkflowConfig', got {type(self.workflow).__name__}."
                    )
                if not is_wenv(self.workenv):
                    raise WorkflowAppSetupError(
                        f"Invalid work environment in {self.__class__.__name__}. "
                        "The 'workenv' attribute must be decorated with @wenv."
                    )

        WorkflowAppConfig.__name__ = cls.__name__
        WorkflowAppConfig.__qualname__ = cls.__qualname__
        WorkflowAppConfig.__module__ = cls.__module__
        return WorkflowAppConfig

    if _cls is None:
        return wrap
    return wrap(_cls)
