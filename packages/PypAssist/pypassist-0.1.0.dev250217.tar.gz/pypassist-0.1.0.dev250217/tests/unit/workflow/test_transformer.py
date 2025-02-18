#!/usr/bin/env python3
"""Unit tests for workflow transformers."""

from abc import ABC, abstractmethod
import tempfile
import unittest
from pathlib import Path
from pydantic.dataclasses import dataclass

from pypassist.dataclass.decorators.viewer import viewer
from pypassist.workflow.workenv.operator import DagsterOperator
from pypassist.mixin.settings import SettingsMixin
from pypassist.mixin.registrable import Registrable
from pypassist.utils.export import export_string


class Transformer(ABC, Registrable, SettingsMixin, DagsterOperator):
    """Base class for transformers."""

    _REGISTER = {}

    def __init__(self, settings):
        Registrable.__init__(self)
        SettingsMixin.__init__(self, settings)
        DagsterOperator.__init__(self)

    @abstractmethod
    def __call__(self, text):
        """Transform text."""

    def get_assetable_func(self):
        """Return assetable function."""

        def asset_fun(text, export=False, output_dir=None, exist_ok=True):
            text = self(text)
            if export and output_dir:
                filepath = output_dir / f"{self.__class__.__name__.lower()}.txt"
                export_string(text, filepath=filepath, exist_ok=exist_ok, makedirs=True)
                content = self.settings.to_str(format_type="yaml")
                filepath = (
                    output_dir / f"{self.__class__.__name__.lower()}_settings.txt"
                )
                export_string(
                    content, filepath=filepath, exist_ok=exist_ok, makedirs=True
                )
            return text

        asset_fun.__name__ = self.__class__.__name__
        return asset_fun


class TestTransformer(unittest.TestCase):
    """Test cases for workflow transformers."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.output_dir = Path(self.temp_dir)

    def test_basic_transformer(self):
        """Test basic transformer functionality."""

        @viewer
        @dataclass
        class UppercaseSettings:
            """Settings for uppercase transformer."""

            prefix: str = ""
            suffix: str = ""

        class Uppercaser(Transformer, register_name="uppercase"):
            """A simple uppercase transformer."""

            SETTINGS_DATACLASS = UppercaseSettings

            def __init__(self, settings=None):
                if settings is None:
                    settings = UppercaseSettings()
                super().__init__(settings)

            def __call__(self, text):
                """Transform text to uppercase with optional prefix/suffix."""
                result = text.upper()
                if self.settings.prefix:
                    result = f"{self.settings.prefix}{result}"
                if self.settings.suffix:
                    result = f"{result}{self.settings.suffix}"
                return result

        # Test basic transformation
        transformer = Uppercaser()
        self.assertEqual(transformer("hello"), "HELLO")

        # Test with settings
        settings = UppercaseSettings(prefix=">> ", suffix=" <<")
        transformer = Uppercaser(settings)
        self.assertEqual(transformer("hello"), ">> HELLO <<")

        # Test asset generation
        asset_func = transformer.get_assetable_func()
        result = asset_func("hello", export=True, output_dir=self.output_dir)
        self.assertEqual(result, ">> HELLO <<")

        # Verify exported files
        result_file = self.output_dir / "uppercaser.txt"
        settings_file = self.output_dir / "uppercaser_settings.txt"
        self.assertTrue(result_file.exists())
        self.assertTrue(settings_file.exists())
        self.assertEqual(result_file.read_text(), ">> HELLO <<")

    def test_transformer_registration(self):
        """Test transformer registration and retrieval."""

        @viewer
        @dataclass
        class DummySettings:
            """Dummy transformer settings."""

            value: str = "test"

        class DummyTransformer(Transformer, register_name="dummy_transform"):
            """A dummy transformer for testing registration."""

            SETTINGS_DATACLASS = DummySettings

            def __init__(self, settings=None):
                if settings is None:
                    settings = DummySettings()
                super().__init__(settings)

            def __call__(self, text):
                return f"{text}_{self.settings.value}"

        # Verify registration
        self.assertTrue(hasattr(DummyTransformer, "_REGISTER"))
        self.assertIn(
            "dummy_transform", DummyTransformer._REGISTER
        )  # pylint: disable=protected-access

        # Test transformer retrieval
        retrieved = Transformer.get_registered("dummy_transform")
        self.assertEqual(retrieved, DummyTransformer)

        # Test transformer functionality
        transformer = DummyTransformer()
        self.assertEqual(transformer("input"), "input_test")

    def test_abstract_transformer(self):
        """Test that abstract transformer cannot be instantiated directly."""

        @viewer
        @dataclass
        class InvalidSettings:
            """Invalid transformer settings."""

            pass

        with self.assertRaises(TypeError):
            # Cannot instantiate abstract class
            # pylint: disable=abstract-class-instantiated
            class InvalidTransformer(Transformer, register_name="invalid"):
                """An invalid transformer missing required methods."""

                SETTINGS_DATACLASS = InvalidSettings

                def __init__(self, settings=None):
                    if settings is None:
                        settings = InvalidSettings()
                    super().__init__(settings)

            InvalidTransformer()  # This should raise TypeError due to missing __call__

    def test_settings_validation(self):
        """Test transformer settings validation."""

        @viewer
        @dataclass
        class ValidatorSettings:
            """Settings with validation."""

            min_length: int = 1

        class TextValidator(Transformer, register_name="validator"):
            """A transformer that validates text length."""

            SETTINGS_DATACLASS = ValidatorSettings

            def __init__(self, settings=None):
                if settings is None:
                    settings = ValidatorSettings()
                super().__init__(settings)

            def __call__(self, text):
                if len(text) < self.settings.min_length:
                    raise ValueError(
                        f"Text length must be at least {self.settings.min_length}"
                    )
                return text

        # Test valid input
        validator = TextValidator(ValidatorSettings(min_length=3))
        self.assertEqual(validator("hello"), "hello")

        # Test invalid input
        with self.assertRaises(ValueError):
            validator("hi")


if __name__ == "__main__":
    unittest.main()
