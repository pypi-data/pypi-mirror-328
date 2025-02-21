"""TransmissionApplications"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_TRANSMISSION_APPLICATIONS = python_net_import(
    "SMT.MastaAPI.Materials", "TransmissionApplications"
)


__docformat__ = "restructuredtext en"
__all__ = ("TransmissionApplications",)


Self = TypeVar("Self", bound="TransmissionApplications")


class TransmissionApplications(Enum):
    """TransmissionApplications

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _TRANSMISSION_APPLICATIONS

    GENERAL_INDUSTRIAL = 0
    AUTOMOTIVE = 1
    AIRCRAFT = 2
    MARINE = 3
    WIND_TURBINE = 4


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


TransmissionApplications.__setattr__ = __enum_setattr
TransmissionApplications.__delattr__ = __enum_delattr
