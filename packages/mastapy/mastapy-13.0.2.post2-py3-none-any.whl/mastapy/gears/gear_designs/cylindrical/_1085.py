"""ThicknessType"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_THICKNESS_TYPE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "ThicknessType"
)


__docformat__ = "restructuredtext en"
__all__ = ("ThicknessType",)


Self = TypeVar("Self", bound="ThicknessType")


class ThicknessType(Enum):
    """ThicknessType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _THICKNESS_TYPE

    UNSPECIFIED = 0
    NORMAL_THICKNESS = 1
    CHORDAL_SPAN = 2
    OVER_BALLS = 3
    TRANSVERSE_THICKNESS = 4
    PROFILE_SHIFT = 5
    NORMAL_THICKNESS_AT_DIAMETER = 6
    TRANSVERSE_THICKNESS_AT_DIAMETER = 7
    OVER_TWO_PINS_FREE_PIN_METHOD = 8
    OVER_TWO_PINS_TRANSVERSE_METHOD = 9
    PROFILE_SHIFT_COEFFICIENT = 1024
    CALCULATED = -2
    SPECIFICATION_FROM_STANDARD = -1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ThicknessType.__setattr__ = __enum_setattr
ThicknessType.__delattr__ = __enum_delattr
