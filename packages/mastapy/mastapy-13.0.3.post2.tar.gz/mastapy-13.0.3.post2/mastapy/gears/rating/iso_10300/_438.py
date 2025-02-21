"""PittingFactorCalculationMethod"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_PITTING_FACTOR_CALCULATION_METHOD = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Iso10300", "PittingFactorCalculationMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("PittingFactorCalculationMethod",)


Self = TypeVar("Self", bound="PittingFactorCalculationMethod")


class PittingFactorCalculationMethod(Enum):
    """PittingFactorCalculationMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _PITTING_FACTOR_CALCULATION_METHOD

    METHOD_B = 0
    METHOD_C = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


PittingFactorCalculationMethod.__setattr__ = __enum_setattr
PittingFactorCalculationMethod.__delattr__ = __enum_delattr
