"""Implementations of 'Overridable' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import TypeVar

from mastapy.bearings import _1898
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_OVERRIDABLE = python_net_import("SMT.MastaAPI.Utility.Property", "Overridable")


__docformat__ = "restructuredtext en"
__all__ = ("Overridable_SealLocation",)


Self = TypeVar("Self", bound="Overridable_SealLocation")


class Overridable_SealLocation(mixins.OverridableMixin, Enum):
    """Overridable_SealLocation

    A specific implementation of 'Overridable' for 'SealLocation' types.
    """

    __qualname__ = "SealLocation"

    @classmethod
    def wrapper_type(cls) -> "_OVERRIDABLE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> "_1898.SealLocation":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1898.SealLocation

    @classmethod
    def implicit_type(cls) -> "_1898.SealLocation.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1898.SealLocation.type_()

    @property
    def value(self: Self) -> "_1898.SealLocation":
        """mastapy.bearings.SealLocation

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
    def override_value(self: Self) -> "_1898.SealLocation":
        """mastapy.bearings.SealLocation

        Note:
            This property is readonly.
        """
        return None

    @property
    def calculated_value(self: Self) -> "_1898.SealLocation":
        """mastapy.bearings.SealLocation

        Note:
            This property is readonly.
        """
        return None
