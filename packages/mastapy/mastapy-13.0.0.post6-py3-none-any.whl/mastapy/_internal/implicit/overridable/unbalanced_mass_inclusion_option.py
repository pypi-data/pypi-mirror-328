"""Implementations of 'Overridable' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import TypeVar

from mastapy.system_model.part_model import _2478
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_OVERRIDABLE = python_net_import("SMT.MastaAPI.Utility.Property", "Overridable")


__docformat__ = "restructuredtext en"
__all__ = ("Overridable_UnbalancedMassInclusionOption",)


Self = TypeVar("Self", bound="Overridable_UnbalancedMassInclusionOption")


class Overridable_UnbalancedMassInclusionOption(mixins.OverridableMixin, Enum):
    """Overridable_UnbalancedMassInclusionOption

    A specific implementation of 'Overridable' for 'UnbalancedMassInclusionOption' types.
    """

    __qualname__ = "UnbalancedMassInclusionOption"

    @classmethod
    def wrapper_type(cls) -> "_OVERRIDABLE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> "_2478.UnbalancedMassInclusionOption":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2478.UnbalancedMassInclusionOption

    @classmethod
    def implicit_type(cls) -> "_2478.UnbalancedMassInclusionOption.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2478.UnbalancedMassInclusionOption.type_()

    @property
    def value(self: Self) -> "_2478.UnbalancedMassInclusionOption":
        """mastapy.system_model.part_model.UnbalancedMassInclusionOption

        Note:
            This property is readonly.
        """
        return None

    @property
    def overridden(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        return None

    @property
    def override_value(self: Self) -> "_2478.UnbalancedMassInclusionOption":
        """mastapy.system_model.part_model.UnbalancedMassInclusionOption

        Note:
            This property is readonly.
        """
        return None

    @property
    def calculated_value(self: Self) -> "_2478.UnbalancedMassInclusionOption":
        """mastapy.system_model.part_model.UnbalancedMassInclusionOption

        Note:
            This property is readonly.
        """
        return None
