"""RollingBearingRaceType"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ROLLING_BEARING_RACE_TYPE = python_net_import(
    "SMT.MastaAPI.Bearings", "RollingBearingRaceType"
)


__docformat__ = "restructuredtext en"
__all__ = ("RollingBearingRaceType",)


Self = TypeVar("Self", bound="RollingBearingRaceType")


class RollingBearingRaceType(Enum):
    """RollingBearingRaceType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ROLLING_BEARING_RACE_TYPE

    NONE = 0
    DRAWN = 1
    MACHINED = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


RollingBearingRaceType.__setattr__ = __enum_setattr
RollingBearingRaceType.__delattr__ = __enum_delattr
