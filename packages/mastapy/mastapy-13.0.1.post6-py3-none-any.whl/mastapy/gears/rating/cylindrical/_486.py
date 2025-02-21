"""TipReliefScuffingOptions"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_TIP_RELIEF_SCUFFING_OPTIONS = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "TipReliefScuffingOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("TipReliefScuffingOptions",)


Self = TypeVar("Self", bound="TipReliefScuffingOptions")


class TipReliefScuffingOptions(Enum):
    """TipReliefScuffingOptions

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _TIP_RELIEF_SCUFFING_OPTIONS

    CALCULATE_USING_MICRO_GEOMETRY = 0
    CALCULATE_USING_MICRO_GEOMETRY_LIMIT_TO_OPTIMAL = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


TipReliefScuffingOptions.__setattr__ = __enum_setattr
TipReliefScuffingOptions.__delattr__ = __enum_delattr
