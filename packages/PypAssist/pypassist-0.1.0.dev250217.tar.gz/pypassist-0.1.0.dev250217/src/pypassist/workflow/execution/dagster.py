#!/usr/bin/env python3
"""
Dagster integration for workflow execution.
"""

import inspect
from functools import wraps

from ...optional.workflow.dagster import (
    asset,
    AssetIn,
    Definitions,
    define_asset_job,
    mem_io_manager,
)

from .base import BaseStep, BaseWorkflow


class DagsterStep(BaseStep):
    """Dagster-based workflow step."""

    def __init__(self, config, workenv):
        super().__init__(config, workenv)
        self._asset = None

    @property
    def asset(self):
        """Return dagster asset."""
        if self._asset is None:
            self._asset = self.get_asset()
        return self._asset

    def get_asset(self):
        """Get dagster asset."""
        asset_func = self.operator.get_assetable_func()

        def configured_func(**inputs):
            return asset_func(
                **inputs,
                export=self.save_results,
                output_dir=self.output_dir,
                exist_ok=self.exist_ok,
            )

        return self._create_asset(configured_func)

    def _create_asset(self, func):
        """Create dagster asset."""
        deps = {}
        sig = inspect.signature(func)

        if sig.parameters and self.inputs:
            deps = {
                param: AssetIn(asset_name) for param, asset_name in self.inputs.items()
            }

        @asset(key=self.config.name, ins=deps)
        @wraps(func)
        def wrapped(**inputs):
            return func(**inputs)

        return wrapped

    def execute(self, **inputs):
        """Execute the step using its dagster asset."""
        return self.asset(**inputs)


class DagsterWorkflow(BaseWorkflow):
    """Dagster-based workflow implementation."""

    def __init__(self, config, workenv):
        if not DAGSTER_AVAILABLE:
            raise ImportError(
                "Dagster is not installed. Install pypassist with [workflow] extra to use "
                "dagster-based workflows."
            )
        super().__init__(config, workenv)

    def _initialize_steps(self, workenv):
        """Initialize dagster workflow steps."""
        self._steps = [DagsterStep(step_cfg, workenv) for step_cfg in self.config.steps]

    @property
    def assets(self):
        """Return workflow assets."""
        return [step.asset for step in self.steps]

    def execute(self):
        """Execute the dagster workflow."""
        defs = Definitions(
            assets=self.assets,
            jobs=[define_asset_job(name=self.config.name)],
            resources={"io_manager": mem_io_manager},
        )

        return defs.get_job_def(self.config.name).execute_in_process(
            resources={"io_manager": mem_io_manager}
        )
