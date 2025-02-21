"""MaxMinMean"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MAX_MIN_MEAN = python_net_import("SMT.MastaAPI.MathUtility", "MaxMinMean")


__docformat__ = "restructuredtext en"
__all__ = ("MaxMinMean",)


Self = TypeVar("Self", bound="MaxMinMean")


class MaxMinMean(Enum):
    """MaxMinMean

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MAX_MIN_MEAN

    MAX = 0
    MIN = 1
    MEAN = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


MaxMinMean.__setattr__ = __enum_setattr
MaxMinMean.__delattr__ = __enum_delattr
