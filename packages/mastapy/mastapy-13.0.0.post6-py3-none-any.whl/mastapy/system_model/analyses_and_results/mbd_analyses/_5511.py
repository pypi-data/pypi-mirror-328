"""TorqueConverterStatus"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_STATUS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses", "TorqueConverterStatus"
)


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterStatus",)


Self = TypeVar("Self", bound="TorqueConverterStatus")


class TorqueConverterStatus(Enum):
    """TorqueConverterStatus

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _TORQUE_CONVERTER_STATUS

    FULLY_LOCKED = 0
    CURRENTLY_LOCKING = 1
    CURRENTLY_UNLOCKING = 2
    FULLY_UNLOCKED = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


TorqueConverterStatus.__setattr__ = __enum_setattr
TorqueConverterStatus.__delattr__ = __enum_delattr
