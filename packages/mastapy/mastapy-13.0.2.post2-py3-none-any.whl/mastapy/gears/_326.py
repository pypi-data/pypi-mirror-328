"""CylindricalFlanks"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_FLANKS = python_net_import("SMT.MastaAPI.Gears", "CylindricalFlanks")


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalFlanks",)


Self = TypeVar("Self", bound="CylindricalFlanks")


class CylindricalFlanks(Enum):
    """CylindricalFlanks

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CYLINDRICAL_FLANKS

    LEFT = 0
    RIGHT = 1
    WORST = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


CylindricalFlanks.__setattr__ = __enum_setattr
CylindricalFlanks.__delattr__ = __enum_delattr
