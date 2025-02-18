#!/usr/bin/env python3
"""Unit tests for the @workflow_app decorator."""

import unittest
from typing import Dict, Any, List
from pydantic.dataclasses import dataclass

from pypassist.dataclass.decorators.workflow_app import workflow_app, WorkflowAppSetupError
from pypassist.dataclass.decorators.wenv import wenv
from pypassist.workflow.config.base import WorkflowConfig


class TestWorkflowAppDecorator(unittest.TestCase):
    """Test cases for the @workflow_app decorator functionality."""

    @classmethod
    def setUpClass(cls):
        """Set up test fixtures."""
        @dataclass
        class MinimalWorkflow(WorkflowConfig):
            """Minimal workflow for testing."""
            name: str = "test"
            steps: List[Dict] = None
            output_dir: str = "./output"

            def __post_init__(self):
                if self.steps is None:
                    self.steps = [{"op_path": "test.op"}]
                super().__post_init__()
        cls.MinimalWorkflow = MinimalWorkflow

    def test_basic_decoration(self):
        """Test basic decoration of a dataclass."""
        @wenv
        @dataclass
        class TestWorkEnv:
            """Test work environment."""
            settings: Dict[str, Any] = None

        @workflow_app
        @dataclass
        class TestConfig:
            """Test configuration class."""
            workflow: self.MinimalWorkflow
            workenv: TestWorkEnv

        # Create an instance with valid workflow and workenv
        config = TestConfig(
            workflow=self.MinimalWorkflow(),
            workenv=TestWorkEnv(settings={"param": "value"})
        )

        # Verify instance creation succeeds
        self.assertIsInstance(config.workflow, WorkflowConfig)
        self.assertTrue(hasattr(config.workenv, '_WENV_'))

    def test_invalid_setup(self):
        """Test handling of invalid setup configuration."""
        # Test missing workflow attribute
        @workflow_app
        @dataclass
        class MissingWorkflowConfig:
            """Test config missing workflow attribute."""
            workenv: Dict[str, Any]

            def __post_init__(self):
                if hasattr(super(), "__post_init__"):
                    super().__post_init__()

        with self.assertRaises(WorkflowAppSetupError):
            MissingWorkflowConfig(workenv={"settings": {}})

        # Test missing workenv attribute
        @workflow_app
        @dataclass
        class MissingWorkEnvConfig:
            """Test config missing workenv attribute."""
            workflow: self.MinimalWorkflow

            def __post_init__(self):
                if hasattr(super(), "__post_init__"):
                    super().__post_init__()

        with self.assertRaises(WorkflowAppSetupError):
            MissingWorkEnvConfig(workflow=self.MinimalWorkflow())

        # Test invalid workflow type
        @dataclass
        class InvalidWorkflow:
            """Invalid workflow (not inheriting from WorkflowConfig)."""
            name: str = "test"

        @workflow_app
        @dataclass
        class InvalidWorkflowConfig:
            """Test config with invalid workflow type."""
            workflow: InvalidWorkflow
            workenv: Dict[str, Any]

            def __post_init__(self):
                if hasattr(super(), "__post_init__"):
                    super().__post_init__()

        with self.assertRaises(WorkflowAppSetupError):
            InvalidWorkflowConfig(
                workflow=InvalidWorkflow(name="test"),
                workenv={"settings": {}}
            )

        # Test invalid workenv type
        @dataclass
        class InvalidWorkEnv:
            """Invalid work environment (missing @wenv decorator)."""
            settings: Dict[str, Any] = None

        @workflow_app
        @dataclass
        class InvalidWorkEnvConfig:
            """Test config with invalid workenv type."""
            workflow: self.MinimalWorkflow
            workenv: InvalidWorkEnv

            def __post_init__(self):
                if hasattr(super(), "__post_init__"):
                    super().__post_init__()

        with self.assertRaises(WorkflowAppSetupError):
            InvalidWorkEnvConfig(
                workflow=self.MinimalWorkflow(),
                workenv=InvalidWorkEnv()
            )


if __name__ == '__main__':
    unittest.main()
