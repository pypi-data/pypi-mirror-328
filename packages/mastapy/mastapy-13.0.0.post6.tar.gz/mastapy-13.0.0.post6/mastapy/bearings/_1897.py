"""RotationalDirections"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ROTATIONAL_DIRECTIONS = python_net_import(
    "SMT.MastaAPI.Bearings", "RotationalDirections"
)


__docformat__ = "restructuredtext en"
__all__ = ("RotationalDirections",)


Self = TypeVar("Self", bound="RotationalDirections")


class RotationalDirections(Enum):
    """RotationalDirections

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ROTATIONAL_DIRECTIONS

    CLOCKWISE = 0
    ANTICLOCKWISE = 1
    BIDIRECTIONAL = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


RotationalDirections.__setattr__ = __enum_setattr
RotationalDirections.__delattr__ = __enum_delattr
