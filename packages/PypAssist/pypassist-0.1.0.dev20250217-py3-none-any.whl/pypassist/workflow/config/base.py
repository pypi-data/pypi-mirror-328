#!/usr/bin/env python3
"""
Base configuration types for workflow module.
"""

import pathlib

from typing import Optional

from pydantic.dataclasses import dataclass

from ...dataclass.decorators.wenv.validation import is_wenv
from ...dataclass.decorators.exportable.decorator import exportable
from ...fallback.typing import Dict, List


@dataclass
class StepState:
    """Step state."""

    name: str
    op_path: str
    settings: Dict
    inputs: Optional[Dict] = None


@dataclass
class StepConfig:
    """Step configuration."""

    op_path: str  # Format: "category.name" (e.g. "generators.generator")
    name: Optional[str] = None
    settings: Optional[Dict] = None
    inputs: Optional[Dict[str, str]] = None
    description: Optional[str] = None
    save_results: bool = True
    exist_ok: bool = False
    _output_dir: Optional[str] = None
    _workflow_output_dir: Optional[str] = None

    def __post_init__(self):
        if self.name is None:
            self.name = self.op_path.split(".")[-1]

    @property
    def output_dir(self):
        """Return Path to output directory."""
        if self._output_dir:
            return pathlib.Path(self._output_dir).resolve()
        return pathlib.Path(self._workflow_output_dir).resolve() / self.name

    def get_operator(self, workenv):
        """Get operator from nested sections."""
        op_path = self.op_path
        *attr_path, dict_key = op_path.split(".")
        section_name = attr_path[0]
        current = getattr(workenv.config, section_name)

        if is_wenv(current):
            remaining_path = ".".join([*attr_path[1:], dict_key])
            return current.get_operator(remaining_path)
        op_dict = getattr(workenv, f"get_{section_name}")()
        return op_dict[dict_key]


@exportable(stem_file="template")
@dataclass
class WorkflowConfig:
    """Workflow configuration."""

    name: str
    steps: List[Dict]
    output_dir: str
    save_results: bool = True
    exist_ok: bool = False

    def __post_init__(self):
        step_defaults = {"exist_ok": self.exist_ok, "save_results": self.save_results}
        self.steps = [
            StepConfig(
                **{**step_defaults, **step, "_workflow_output_dir": self.output_dir}
            )
            for step in self.steps
        ]
