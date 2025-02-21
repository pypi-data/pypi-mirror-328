"""ScuffingTemperatureMethodsAGMA"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_SCUFFING_TEMPERATURE_METHODS_AGMA = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "ScuffingTemperatureMethodsAGMA"
)


__docformat__ = "restructuredtext en"
__all__ = ("ScuffingTemperatureMethodsAGMA",)


Self = TypeVar("Self", bound="ScuffingTemperatureMethodsAGMA")


class ScuffingTemperatureMethodsAGMA(Enum):
    """ScuffingTemperatureMethodsAGMA

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SCUFFING_TEMPERATURE_METHODS_AGMA

    USER_INPUT = 0
    FROM_TEST_GEARS = 1
    FROM_LUBRICANT_VISCOSITY = 2
    FROM_FZG_FAILURE_LOAD_STAGE = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ScuffingTemperatureMethodsAGMA.__setattr__ = __enum_setattr
ScuffingTemperatureMethodsAGMA.__delattr__ = __enum_delattr
