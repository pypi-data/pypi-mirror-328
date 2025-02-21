"""CutterGaugeLengths"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CUTTER_GAUGE_LENGTHS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "CutterGaugeLengths"
)


__docformat__ = "restructuredtext en"
__all__ = ("CutterGaugeLengths",)


Self = TypeVar("Self", bound="CutterGaugeLengths")


class CutterGaugeLengths(Enum):
    """CutterGaugeLengths

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CUTTER_GAUGE_LENGTHS

    _1143MM = 0
    _92075MM = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


CutterGaugeLengths.__setattr__ = __enum_setattr
CutterGaugeLengths.__delattr__ = __enum_delattr
