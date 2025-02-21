"""FlankDataSource"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FLANK_DATA_SOURCE = python_net_import(
    "SMT.MastaAPI.Gears.FEModel.Conical", "FlankDataSource"
)


__docformat__ = "restructuredtext en"
__all__ = ("FlankDataSource",)


Self = TypeVar("Self", bound="FlankDataSource")


class FlankDataSource(Enum):
    """FlankDataSource

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FLANK_DATA_SOURCE

    MACRODESIGN = 0
    MANUFACTURING = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FlankDataSource.__setattr__ = __enum_setattr
FlankDataSource.__delattr__ = __enum_delattr
