"""CoordinateSystemForRotationOrigin"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_COORDINATE_SYSTEM_FOR_ROTATION_ORIGIN = python_net_import(
    "SMT.MastaAPI.MathUtility", "CoordinateSystemForRotationOrigin"
)


__docformat__ = "restructuredtext en"
__all__ = ("CoordinateSystemForRotationOrigin",)


Self = TypeVar("Self", bound="CoordinateSystemForRotationOrigin")


class CoordinateSystemForRotationOrigin(Enum):
    """CoordinateSystemForRotationOrigin

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _COORDINATE_SYSTEM_FOR_ROTATION_ORIGIN

    WORLD_COORDINATE_SYSTEM = 0
    LOCAL_COORDINATE_SYSTEM = 1
    USERSPECIFIED = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


CoordinateSystemForRotationOrigin.__setattr__ = __enum_setattr
CoordinateSystemForRotationOrigin.__delattr__ = __enum_delattr
