"""OilSealLossCalculationMethod"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_OIL_SEAL_LOSS_CALCULATION_METHOD = python_net_import(
    "SMT.MastaAPI.Materials.Efficiency", "OilSealLossCalculationMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("OilSealLossCalculationMethod",)


Self = TypeVar("Self", bound="OilSealLossCalculationMethod")


class OilSealLossCalculationMethod(Enum):
    """OilSealLossCalculationMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _OIL_SEAL_LOSS_CALCULATION_METHOD

    ISOTR_1417912001 = 0
    ISOTR_1417922001 = 1
    USERSPECIFIED_DRAG_TORQUE_VS_SPEED = 2
    TAMAIS_METHOD = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


OilSealLossCalculationMethod.__setattr__ = __enum_setattr
OilSealLossCalculationMethod.__delattr__ = __enum_delattr
