#!/usr/bin/env python3
"""
Base work environment functionality.
"""

from ...dataclass.decorators.wenv.validation import is_wenv


class BaseWorkEnv:
    """Base class for work environments."""

    def __init__(self, config):
        self.config = config
        self._validate_config()

    def _validate_config(self):
        if not is_wenv(self.config):
            raise ValueError(
                "Invalid work environment configuration. "
                "Expected a pydantic dataclass decorated with @wenv."
            )

    def get_operator(self, path):
        """
        Get operator by path.

        Args:
            path: Operator path in format "section.name"

        Returns:
            Operator instance

        Raises:
            ValueError: If operator path is invalid or operator not found
        """
        try:
            section_name, operator_name = path.split(".")
        except ValueError as err:
            raise ValueError(
                f"Invalid operator path: {path}. Expected format: 'section.name'"
            ) from err

        section = getattr(self, f"get_{section_name}")()
        if operator_name not in section:
            raise ValueError(
                f"Operator '{operator_name}' not found in section '{section_name}'"
            )

        return section[operator_name]

    def get_sections(self):
        """
        Get all available sections and their operators.

        Returns:
            Dictionary mapping section names to dictionaries of operator names and instances
        """
        sections = {}
        for attr_name in dir(self):
            if attr_name.startswith("get_") and attr_name != "get_operator":
                section_name = attr_name[4:]
                sections[section_name] = getattr(self, attr_name)()
        return sections
