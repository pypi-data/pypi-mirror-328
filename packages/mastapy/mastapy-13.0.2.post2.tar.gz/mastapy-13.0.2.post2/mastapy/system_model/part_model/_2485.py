"""UnbalancedMassInclusionOption"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_INCLUSION_OPTION = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "UnbalancedMassInclusionOption"
)


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassInclusionOption",)


Self = TypeVar("Self", bound="UnbalancedMassInclusionOption")


class UnbalancedMassInclusionOption(Enum):
    """UnbalancedMassInclusionOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _UNBALANCED_MASS_INCLUSION_OPTION

    ALL_ANALYSES = 0
    ADVANCED_SYSTEM_DEFLECTION_AND_DYNAMICS = 1
    DYNAMIC_ANALYSES = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


UnbalancedMassInclusionOption.__setattr__ = __enum_setattr
UnbalancedMassInclusionOption.__delattr__ = __enum_delattr
