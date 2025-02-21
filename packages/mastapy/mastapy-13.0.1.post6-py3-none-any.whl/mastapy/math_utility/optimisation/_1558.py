"""TargetingPropertyTo"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_TARGETING_PROPERTY_TO = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "TargetingPropertyTo"
)


__docformat__ = "restructuredtext en"
__all__ = ("TargetingPropertyTo",)


Self = TypeVar("Self", bound="TargetingPropertyTo")


class TargetingPropertyTo(Enum):
    """TargetingPropertyTo

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _TARGETING_PROPERTY_TO

    RANGE = 0
    MINIMUM_VALUE = 1
    MAXIMUM_VALUE = 2
    TARGET_VALUE = 3
    SYMMETRIC_DEVIATION_FROM_ORIGINAL_DESIGN = 4
    ASYMMETRIC_DEVIATION_FROM_ORIGINAL_DESIGN = 5


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


TargetingPropertyTo.__setattr__ = __enum_setattr
TargetingPropertyTo.__delattr__ = __enum_delattr
