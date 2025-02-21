"""LubricantViscosityClassification"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_LUBRICANT_VISCOSITY_CLASSIFICATION = python_net_import(
    "SMT.MastaAPI.Materials", "LubricantViscosityClassification"
)


__docformat__ = "restructuredtext en"
__all__ = ("LubricantViscosityClassification",)


Self = TypeVar("Self", bound="LubricantViscosityClassification")


class LubricantViscosityClassification(Enum):
    """LubricantViscosityClassification

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _LUBRICANT_VISCOSITY_CLASSIFICATION

    ISO = 0
    AGMA = 1
    SAE = 2
    USERSPECIFIED = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


LubricantViscosityClassification.__setattr__ = __enum_setattr
LubricantViscosityClassification.__delattr__ = __enum_delattr
