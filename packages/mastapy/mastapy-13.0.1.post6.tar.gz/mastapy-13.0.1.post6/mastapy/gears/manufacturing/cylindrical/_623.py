"""CylindricalMftFinishingMethods"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MFT_FINISHING_METHODS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "CylindricalMftFinishingMethods"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalMftFinishingMethods",)


Self = TypeVar("Self", bound="CylindricalMftFinishingMethods")


class CylindricalMftFinishingMethods(Enum):
    """CylindricalMftFinishingMethods

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CYLINDRICAL_MFT_FINISHING_METHODS

    HOBBING = 0
    SHAPING = 1
    SHAVING = 2
    FORM_WHEEL_GRINDING = 3
    WORM_GRINDING = 4
    NONE = 5
    PLUNGE_SHAVING_WITH_MICROGEOMETRY = 6


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


CylindricalMftFinishingMethods.__setattr__ = __enum_setattr
CylindricalMftFinishingMethods.__delattr__ = __enum_delattr
