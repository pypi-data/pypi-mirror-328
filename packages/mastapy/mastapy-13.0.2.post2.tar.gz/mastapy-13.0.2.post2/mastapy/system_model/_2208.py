"""ComponentDampingOption"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_COMPONENT_DAMPING_OPTION = python_net_import(
    "SMT.MastaAPI.SystemModel", "ComponentDampingOption"
)


__docformat__ = "restructuredtext en"
__all__ = ("ComponentDampingOption",)


Self = TypeVar("Self", bound="ComponentDampingOption")


class ComponentDampingOption(Enum):
    """ComponentDampingOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _COMPONENT_DAMPING_OPTION

    LOAD_CASE_GLOBAL_DAMPING = 0
    SPECIFIED = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ComponentDampingOption.__setattr__ = __enum_setattr
ComponentDampingOption.__delattr__ = __enum_delattr
