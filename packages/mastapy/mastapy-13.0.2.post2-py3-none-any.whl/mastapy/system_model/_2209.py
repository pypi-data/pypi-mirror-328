"""ConceptCouplingSpeedRatioSpecificationMethod"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_SPEED_RATIO_SPECIFICATION_METHOD = python_net_import(
    "SMT.MastaAPI.SystemModel", "ConceptCouplingSpeedRatioSpecificationMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingSpeedRatioSpecificationMethod",)


Self = TypeVar("Self", bound="ConceptCouplingSpeedRatioSpecificationMethod")


class ConceptCouplingSpeedRatioSpecificationMethod(Enum):
    """ConceptCouplingSpeedRatioSpecificationMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CONCEPT_COUPLING_SPEED_RATIO_SPECIFICATION_METHOD

    FIXED = 0
    VARYING_WITH_TIME = 1
    PID_CONTROL = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ConceptCouplingSpeedRatioSpecificationMethod.__setattr__ = __enum_setattr
ConceptCouplingSpeedRatioSpecificationMethod.__delattr__ = __enum_delattr
