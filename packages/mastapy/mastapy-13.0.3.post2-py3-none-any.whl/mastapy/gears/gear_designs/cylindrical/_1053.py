"""DIN3967AllowanceSeries"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_DIN3967_ALLOWANCE_SERIES = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "DIN3967AllowanceSeries"
)


__docformat__ = "restructuredtext en"
__all__ = ("DIN3967AllowanceSeries",)


Self = TypeVar("Self", bound="DIN3967AllowanceSeries")


class DIN3967AllowanceSeries(Enum):
    """DIN3967AllowanceSeries

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _DIN3967_ALLOWANCE_SERIES

    A = 0
    AB = 1
    B = 2
    BC = 3
    C = 4
    CD = 5
    D = 6
    E = 7
    F = 8
    G = 9
    H = 10


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


DIN3967AllowanceSeries.__setattr__ = __enum_setattr
DIN3967AllowanceSeries.__delattr__ = __enum_delattr
