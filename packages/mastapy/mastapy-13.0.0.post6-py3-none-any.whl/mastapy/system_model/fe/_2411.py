"""ThermalExpansionOption"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_THERMAL_EXPANSION_OPTION = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "ThermalExpansionOption"
)


__docformat__ = "restructuredtext en"
__all__ = ("ThermalExpansionOption",)


Self = TypeVar("Self", bound="ThermalExpansionOption")


class ThermalExpansionOption(Enum):
    """ThermalExpansionOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _THERMAL_EXPANSION_OPTION

    UNIFORM = 0
    SPECIFIED_FORCE = 1
    SPECIFIED_DISPLACEMENT = 2
    CALCULATED_USING_MATERIAL_PROPERTIES = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ThermalExpansionOption.__setattr__ = __enum_setattr
ThermalExpansionOption.__delattr__ = __enum_delattr
