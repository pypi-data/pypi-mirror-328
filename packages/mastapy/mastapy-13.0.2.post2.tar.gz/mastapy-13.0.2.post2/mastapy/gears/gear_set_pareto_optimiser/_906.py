"""CandidateDisplayChoice"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CANDIDATE_DISPLAY_CHOICE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser", "CandidateDisplayChoice"
)


__docformat__ = "restructuredtext en"
__all__ = ("CandidateDisplayChoice",)


Self = TypeVar("Self", bound="CandidateDisplayChoice")


class CandidateDisplayChoice(Enum):
    """CandidateDisplayChoice

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CANDIDATE_DISPLAY_CHOICE

    ALL_FEASIBLE_CANDIDATES = 0
    CANDIDATES_AFTER_FILTERING = 1
    DOMINANT_CANDIDATES = 2
    CANDIDATES_SELECTED_IN_CHART = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


CandidateDisplayChoice.__setattr__ = __enum_setattr
CandidateDisplayChoice.__delattr__ = __enum_delattr
