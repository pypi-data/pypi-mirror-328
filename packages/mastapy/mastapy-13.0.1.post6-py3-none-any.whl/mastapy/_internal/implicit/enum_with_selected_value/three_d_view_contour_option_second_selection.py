"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.utility.enums import _1823
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection",)


Self = TypeVar(
    "Self", bound="EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection"
)


class EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection

    A specific implementation of 'EnumWithSelectedValue' for 'ThreeDViewContourOptionSecondSelection' types.
    """

    __qualname__ = "ThreeDViewContourOptionSecondSelection"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1823.ThreeDViewContourOptionSecondSelection":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1823.ThreeDViewContourOptionSecondSelection

    @classmethod
    def implicit_type(cls) -> "_1823.ThreeDViewContourOptionSecondSelection.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1823.ThreeDViewContourOptionSecondSelection.type_()

    @property
    def selected_value(self: Self) -> "_1823.ThreeDViewContourOptionSecondSelection":
        """mastapy.utility.enums.ThreeDViewContourOptionSecondSelection

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(
        self: Self,
    ) -> "List[_1823.ThreeDViewContourOptionSecondSelection]":
        """List[mastapy.utility.enums.ThreeDViewContourOptionSecondSelection]

        Note:
            This property is readonly.
        """
        return None
