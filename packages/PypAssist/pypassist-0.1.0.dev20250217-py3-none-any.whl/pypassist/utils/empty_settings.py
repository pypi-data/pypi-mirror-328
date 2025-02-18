#!/usr/bin/env python3

"""
Empty settings dataclass for types that don't require configuration
"""

from pydantic.dataclasses import dataclass

from ..dataclass.decorators.viewer.decorator import viewer


@viewer
@dataclass
class EmptySettings:  # pylint: disable=too-few-public-methods
    """Empty settings dataclass for types that don't require configuration"""
