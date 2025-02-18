#!/usr/venv/python3
"""
Customized configuration.
"""

from pydantic.dataclasses import dataclass

from ....dataclass.decorators.registry.decorator import registry
from ....dataclass.decorators.exportable.decorator import exportable
from ....fallback.typing import Dict

from .custom import CustomOperator


@registry(base_cls=CustomOperator, submod=None)
@exportable(strategy="registry")
@dataclass
class CustomOperatorConfig:
    """Custom operator configuration."""

    name: str
    settings: Dict = None

    def get_custom_operator(self, man=None, workenv=None):
        """Get operator instance"""
        return CustomOperator.get_registered(self.name).init_from_config(
            self, man, workenv
        )
