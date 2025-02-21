"""SinglePointSelectionMethod"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_SINGLE_POINT_SELECTION_METHOD = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.VaryingInputComponents", "SinglePointSelectionMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("SinglePointSelectionMethod",)


Self = TypeVar("Self", bound="SinglePointSelectionMethod")


class SinglePointSelectionMethod(Enum):
    """SinglePointSelectionMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SINGLE_POINT_SELECTION_METHOD

    CURRENT_TIME = 0
    MEAN_VALUE = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


SinglePointSelectionMethod.__setattr__ = __enum_setattr
SinglePointSelectionMethod.__delattr__ = __enum_delattr
