"""TableAndChartOptions"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_TABLE_AND_CHART_OPTIONS = python_net_import(
    "SMT.MastaAPI.Utility.Enums", "TableAndChartOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("TableAndChartOptions",)


Self = TypeVar("Self", bound="TableAndChartOptions")


class TableAndChartOptions(Enum):
    """TableAndChartOptions

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _TABLE_AND_CHART_OPTIONS

    CHART_THEN_TABLE = 0
    TABLE_THEN_CHART = 1
    TABLE = 2
    CHART = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


TableAndChartOptions.__setattr__ = __enum_setattr
TableAndChartOptions.__delattr__ = __enum_delattr
