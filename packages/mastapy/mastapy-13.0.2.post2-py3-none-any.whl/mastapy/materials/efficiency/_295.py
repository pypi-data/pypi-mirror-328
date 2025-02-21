"""BearingEfficiencyRatingMethod"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_BEARING_EFFICIENCY_RATING_METHOD = python_net_import(
    "SMT.MastaAPI.Materials.Efficiency", "BearingEfficiencyRatingMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("BearingEfficiencyRatingMethod",)


Self = TypeVar("Self", bound="BearingEfficiencyRatingMethod")


class BearingEfficiencyRatingMethod(Enum):
    """BearingEfficiencyRatingMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BEARING_EFFICIENCY_RATING_METHOD

    ISOTR_1417912001 = 0
    ISOTR_1417922001 = 1
    SKF_LOSS_MODEL = 2
    SMT_ADVANCED_MODEL = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


BearingEfficiencyRatingMethod.__setattr__ = __enum_setattr
BearingEfficiencyRatingMethod.__delattr__ = __enum_delattr
