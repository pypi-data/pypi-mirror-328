#!/usr/bin/env python3
"""Unit tests for custom workflow operators."""

import tempfile
import unittest
from pathlib import Path

from pydantic.dataclasses import dataclass

from pypassist.workflow.workenv.custom import CustomOperator
from pypassist.dataclass.decorators.viewer import viewer


class TestCustomOperator(unittest.TestCase):
    """Test cases for custom workflow operators."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.output_dir = Path(self.temp_dir)

    def test_basic_operator(self):
        """Test basic custom operator functionality."""

        @viewer
        @dataclass
        class ReverserSettings:
            """Settings for string reversal."""

            capitalize: bool = False

        class Reverser(CustomOperator, register_name="reverse"):
            """A simple string reverser operator."""

            SETTINGS_DATACLASS = ReverserSettings

            def __init__(self, settings=None):
                if settings is None:
                    settings = ReverserSettings()
                CustomOperator.__init__(self, settings)

            @classmethod
            def init_from_config(cls, config, man=None, workenv=None):
                return cls(config.settings)

            def __call__(self, text):
                """Reverse the input text."""
                result = text[::-1]
                if self.settings.capitalize:
                    result = result.upper()
                return result

            def get_assetable_func(self):
                """Get function for asset generation."""

                def asset_fun(text, export=False, output_dir=None, exist_ok=True):
                    result = self(text)
                    if export and output_dir:
                        # Export result
                        result_file = (
                            output_dir / f"{self.__class__.__name__.lower()}.txt"
                        )
                        result_file.parent.mkdir(parents=True, exist_ok=True)
                        result_file.write_text(result)

                        # Export settings
                        settings_str = self.settings.to_str(format_type="yaml")
                        settings_file = (
                            output_dir
                            / f"{self.__class__.__name__.lower()}_settings.txt"
                        )
                        settings_file.write_text(settings_str)
                    return result

                asset_fun.__name__ = self.__class__.__name__
                return asset_fun

        # Test basic operation
        reverser = Reverser(ReverserSettings(capitalize=False))
        self.assertEqual(reverser("hello"), "olleh")

        # Test with settings
        reverser = Reverser(ReverserSettings(capitalize=True))
        self.assertEqual(reverser("hello"), "OLLEH")

        # Test asset generation
        asset_func = reverser.get_assetable_func()
        result = asset_func("hello", export=True, output_dir=self.output_dir)
        self.assertEqual(result, "OLLEH")

        # Verify exported files
        result_file = self.output_dir / "reverser.txt"
        settings_file = self.output_dir / "reverser_settings.txt"
        self.assertTrue(result_file.exists())
        self.assertTrue(settings_file.exists())
        self.assertEqual(result_file.read_text(), "OLLEH")

    def test_operator_registration(self):
        """Test operator registration and retrieval."""

        @viewer
        @dataclass
        class DummySettings:
            """Dummy settings."""

            value: str = "test"

        class DummyOperator(CustomOperator, register_name="dummy"):
            """A dummy operator for testing registration."""

            SETTINGS_DATACLASS = DummySettings

            def __init__(self, settings=None):
                if settings is None:
                    settings = DummySettings()
                CustomOperator.__init__(self, settings)

            @classmethod
            def init_from_config(cls, config, man=None, workenv=None):
                return cls(config.settings)

            def __call__(self, text):
                return f"{text}_{self.settings.value}"

            def get_assetable_func(self):
                def asset_fun(text, export=False, output_dir=None, exist_ok=True):
                    return self(text)

                asset_fun.__name__ = self.__class__.__name__
                return asset_fun

        # Verify registration
        self.assertTrue(hasattr(DummyOperator, "_REGISTER"))
        self.assertIn("dummy", DummyOperator._REGISTER)

        # Test operator retrieval
        retrieved = CustomOperator.get_registered("dummy")
        self.assertEqual(retrieved, DummyOperator)

        # Test operator functionality
        operator = DummyOperator()
        self.assertEqual(operator("input"), "input_test")

    def test_invalid_operator(self):
        """Test handling of invalid operator configurations."""
        with self.assertRaises(TypeError):
            # Missing required methods
            class InvalidOperator(CustomOperator, register_name="invalid"):
                """An invalid operator missing required methods."""

                pass

            InvalidOperator()


if __name__ == "__main__":
    unittest.main()
