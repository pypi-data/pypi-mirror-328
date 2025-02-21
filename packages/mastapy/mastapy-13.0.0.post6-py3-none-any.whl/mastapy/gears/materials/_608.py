"""SNCurveDefinition"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_SN_CURVE_DEFINITION = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "SNCurveDefinition"
)


__docformat__ = "restructuredtext en"
__all__ = ("SNCurveDefinition",)


Self = TypeVar("Self", bound="SNCurveDefinition")


class SNCurveDefinition(Enum):
    """SNCurveDefinition

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SN_CURVE_DEFINITION

    AGMA = 0
    GLEASON = 1
    CUSTOM = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


SNCurveDefinition.__setattr__ = __enum_setattr
SNCurveDefinition.__delattr__ = __enum_delattr
