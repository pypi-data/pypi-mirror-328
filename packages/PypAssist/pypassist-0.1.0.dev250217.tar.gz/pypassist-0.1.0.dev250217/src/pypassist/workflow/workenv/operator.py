#!/usr/bin/env python3
"""
Operator implementations for workflow execution.
"""

from ...fallback.protocol import Protocol, runtime_checkable


@runtime_checkable
class BaseOperator(Protocol):
    """Protocol defining the interface for workflow operators."""

    def get_assetable_func(self):
        """Get function that can be converted to a dagster asset.

        Returns:
            Callable: A function that can be used as a dagster asset
        """


class DagsterOperator(BaseOperator):
    """Operator implementation for workflow execution."""

    def get_assetable_func(self):
        """Implement the asset function getter.

        Returns:
            Callable: A function that can be used as a dagster asset

        Raises:
            NotImplementedError: If not implemented by subclass
        """
        raise NotImplementedError("Must be implemented by subclasses")
