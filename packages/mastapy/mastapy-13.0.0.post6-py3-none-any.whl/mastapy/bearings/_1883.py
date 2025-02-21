"""ExponentAndReductionFactorsInISO16281Calculation"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_EXPONENT_AND_REDUCTION_FACTORS_IN_ISO16281_CALCULATION = python_net_import(
    "SMT.MastaAPI.Bearings", "ExponentAndReductionFactorsInISO16281Calculation"
)


__docformat__ = "restructuredtext en"
__all__ = ("ExponentAndReductionFactorsInISO16281Calculation",)


Self = TypeVar("Self", bound="ExponentAndReductionFactorsInISO16281Calculation")


class ExponentAndReductionFactorsInISO16281Calculation(Enum):
    """ExponentAndReductionFactorsInISO16281Calculation

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _EXPONENT_AND_REDUCTION_FACTORS_IN_ISO16281_CALCULATION

    DIVIDE_BY_EXPONENT_AND_REDUCTION_FACTORS = 0
    DONT_INCLUDE_EXPONENT_AND_REDUCTION_FACTORS = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ExponentAndReductionFactorsInISO16281Calculation.__setattr__ = __enum_setattr
ExponentAndReductionFactorsInISO16281Calculation.__delattr__ = __enum_delattr
