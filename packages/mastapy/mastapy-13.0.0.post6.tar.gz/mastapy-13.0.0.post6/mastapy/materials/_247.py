"""BHCurveExtrapolationMethod"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_BH_CURVE_EXTRAPOLATION_METHOD = python_net_import(
    "SMT.MastaAPI.Materials", "BHCurveExtrapolationMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("BHCurveExtrapolationMethod",)


Self = TypeVar("Self", bound="BHCurveExtrapolationMethod")


class BHCurveExtrapolationMethod(Enum):
    """BHCurveExtrapolationMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BH_CURVE_EXTRAPOLATION_METHOD

    NONE = 0
    STRAIGHT_LINE = 1
    LAW_OF_APPROACH_TO_SATURATION = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


BHCurveExtrapolationMethod.__setattr__ = __enum_setattr
BHCurveExtrapolationMethod.__delattr__ = __enum_delattr
