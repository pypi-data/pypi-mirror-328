"""InertiaAdjustedLoadCaseResultsToCreate"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_INERTIA_ADJUSTED_LOAD_CASE_RESULTS_TO_CREATE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "InertiaAdjustedLoadCaseResultsToCreate",
)


__docformat__ = "restructuredtext en"
__all__ = ("InertiaAdjustedLoadCaseResultsToCreate",)


Self = TypeVar("Self", bound="InertiaAdjustedLoadCaseResultsToCreate")


class InertiaAdjustedLoadCaseResultsToCreate(Enum):
    """InertiaAdjustedLoadCaseResultsToCreate

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _INERTIA_ADJUSTED_LOAD_CASE_RESULTS_TO_CREATE

    LOAD_CASES_OVER_TIME = 0
    PEAK_LOADS_FOR_GEARS = 1
    ALL = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


InertiaAdjustedLoadCaseResultsToCreate.__setattr__ = __enum_setattr
InertiaAdjustedLoadCaseResultsToCreate.__delattr__ = __enum_delattr
