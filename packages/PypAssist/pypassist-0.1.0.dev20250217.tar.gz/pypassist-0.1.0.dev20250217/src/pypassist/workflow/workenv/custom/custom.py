#!/usr/venv/python3
"""
Customized working environment
"""

from abc import ABC, abstractmethod

from ....mixin.registrable import Registrable
from ....mixin.settings import SettingsMixin
from ..operator import DagsterOperator


class CustomOperator(ABC, Registrable, SettingsMixin, DagsterOperator):
    """Base class for custom operators."""

    _REGISTER = {}

    def __init__(self, settings):
        Registrable.__init__(self)
        SettingsMixin.__init__(self, settings)
        DagsterOperator.__init__(self)

    @classmethod
    @abstractmethod
    def init_from_config(cls, config, man=None, workenv=None):
        """Initialize the operator from configuration."""
