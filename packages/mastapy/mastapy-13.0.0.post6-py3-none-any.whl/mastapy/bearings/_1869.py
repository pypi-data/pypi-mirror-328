"""BearingCatalog"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_BEARING_CATALOG = python_net_import("SMT.MastaAPI.Bearings", "BearingCatalog")


__docformat__ = "restructuredtext en"
__all__ = ("BearingCatalog",)


Self = TypeVar("Self", bound="BearingCatalog")


class BearingCatalog(Enum):
    """BearingCatalog

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BEARING_CATALOG

    ALL = 0
    TIMKEN = 1
    SKF = 2
    NSK = 3
    INA = 4
    FAG = 5
    JTEKT_KOYO = 6
    NTN = 7
    CUSTOM = 8
    SKF_LEGACY = 9
    SCHAEFFLER_LEGACY = 10
    TIMKEN_LEGACY = 11
    NACHI = 12


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


BearingCatalog.__setattr__ = __enum_setattr
BearingCatalog.__delattr__ = __enum_delattr
