"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.math_utility import _1494
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ComplexPartDisplayOption",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_ComplexPartDisplayOption")


class EnumWithSelectedValue_ComplexPartDisplayOption(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_ComplexPartDisplayOption

    A specific implementation of 'EnumWithSelectedValue' for 'ComplexPartDisplayOption' types.
    """

    __qualname__ = "ComplexPartDisplayOption"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1494.ComplexPartDisplayOption":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1494.ComplexPartDisplayOption

    @classmethod
    def implicit_type(cls) -> "_1494.ComplexPartDisplayOption.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1494.ComplexPartDisplayOption.type_()

    @property
    def selected_value(self: Self) -> "_1494.ComplexPartDisplayOption":
        """mastapy.math_utility.ComplexPartDisplayOption

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1494.ComplexPartDisplayOption]":
        """List[mastapy.math_utility.ComplexPartDisplayOption]

        Note:
            This property is readonly.
        """
        return None
