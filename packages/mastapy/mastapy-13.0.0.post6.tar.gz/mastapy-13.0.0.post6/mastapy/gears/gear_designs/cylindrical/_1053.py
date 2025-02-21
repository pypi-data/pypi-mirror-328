"""HeatTreatmentType"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_HEAT_TREATMENT_TYPE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "HeatTreatmentType"
)


__docformat__ = "restructuredtext en"
__all__ = ("HeatTreatmentType",)


Self = TypeVar("Self", bound="HeatTreatmentType")


class HeatTreatmentType(Enum):
    """HeatTreatmentType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _HEAT_TREATMENT_TYPE

    CARBURIZING = 0
    NITRIDING = 1
    INDUCTION_OR_FLAME = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


HeatTreatmentType.__setattr__ = __enum_setattr
HeatTreatmentType.__delattr__ = __enum_delattr
