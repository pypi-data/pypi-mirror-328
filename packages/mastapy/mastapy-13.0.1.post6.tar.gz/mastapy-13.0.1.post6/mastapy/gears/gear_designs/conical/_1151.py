"""BacklashDistributionRule"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_BACKLASH_DISTRIBUTION_RULE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "BacklashDistributionRule"
)


__docformat__ = "restructuredtext en"
__all__ = ("BacklashDistributionRule",)


Self = TypeVar("Self", bound="BacklashDistributionRule")


class BacklashDistributionRule(Enum):
    """BacklashDistributionRule

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BACKLASH_DISTRIBUTION_RULE

    AUTO = 0
    ALL_ON_PINION = 1
    ALL_ON_WHEEL = 2
    DISTRIBUTED_EQUALLY = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


BacklashDistributionRule.__setattr__ = __enum_setattr
BacklashDistributionRule.__delattr__ = __enum_delattr
