"""HypoidWindUpRemovalMethod"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_HYPOID_WIND_UP_REMOVAL_METHOD = python_net_import(
    "SMT.MastaAPI.SystemModel", "HypoidWindUpRemovalMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("HypoidWindUpRemovalMethod",)


Self = TypeVar("Self", bound="HypoidWindUpRemovalMethod")


class HypoidWindUpRemovalMethod(Enum):
    """HypoidWindUpRemovalMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _HYPOID_WIND_UP_REMOVAL_METHOD

    INVARIANT_UNDER_RIGID_BODY_TRANSLATIONS_AND_ROTATIONS = 0
    ZERO_WIND_UP_SAE_750152 = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


HypoidWindUpRemovalMethod.__setattr__ = __enum_setattr
HypoidWindUpRemovalMethod.__delattr__ = __enum_delattr
