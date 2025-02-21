"""Implementations of 'Overridable' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import TypeVar

from mastapy.gears import _322
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_OVERRIDABLE = python_net_import("SMT.MastaAPI.Utility.Property", "Overridable")


__docformat__ = "restructuredtext en"
__all__ = ("Overridable_ContactRatioRequirements",)


Self = TypeVar("Self", bound="Overridable_ContactRatioRequirements")


class Overridable_ContactRatioRequirements(mixins.OverridableMixin, Enum):
    """Overridable_ContactRatioRequirements

    A specific implementation of 'Overridable' for 'ContactRatioRequirements' types.
    """

    __qualname__ = "ContactRatioRequirements"

    @classmethod
    def wrapper_type(cls) -> "_OVERRIDABLE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> "_322.ContactRatioRequirements":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _322.ContactRatioRequirements

    @classmethod
    def implicit_type(cls) -> "_322.ContactRatioRequirements.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _322.ContactRatioRequirements.type_()

    @property
    def value(self: Self) -> "_322.ContactRatioRequirements":
        """mastapy.gears.ContactRatioRequirements

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
    def override_value(self: Self) -> "_322.ContactRatioRequirements":
        """mastapy.gears.ContactRatioRequirements

        Note:
            This property is readonly.
        """
        return None

    @property
    def calculated_value(self: Self) -> "_322.ContactRatioRequirements":
        """mastapy.gears.ContactRatioRequirements

        Note:
            This property is readonly.
        """
        return None
