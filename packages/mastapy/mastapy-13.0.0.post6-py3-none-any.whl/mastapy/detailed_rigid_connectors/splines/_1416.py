"""SplineRatingTypes"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_SPLINE_RATING_TYPES = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "SplineRatingTypes"
)


__docformat__ = "restructuredtext en"
__all__ = ("SplineRatingTypes",)


Self = TypeVar("Self", bound="SplineRatingTypes")


class SplineRatingTypes(Enum):
    """SplineRatingTypes

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SPLINE_RATING_TYPES

    GBT_178551999 = 0
    SAE_B9211996 = 1
    DIN_5466 = 2
    AGMA_6123C16 = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


SplineRatingTypes.__setattr__ = __enum_setattr
SplineRatingTypes.__delattr__ = __enum_delattr
