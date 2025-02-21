"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2109
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_StressConcentrationMethod",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_StressConcentrationMethod")


class EnumWithSelectedValue_StressConcentrationMethod(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_StressConcentrationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'StressConcentrationMethod' types.
    """

    __qualname__ = "StressConcentrationMethod"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_2109.StressConcentrationMethod":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2109.StressConcentrationMethod

    @classmethod
    def implicit_type(cls) -> "_2109.StressConcentrationMethod.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2109.StressConcentrationMethod.type_()

    @property
    def selected_value(self: Self) -> "_2109.StressConcentrationMethod":
        """mastapy.bearings.bearing_results.rolling.iso_rating_results.StressConcentrationMethod

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_2109.StressConcentrationMethod]":
        """List[mastapy.bearings.bearing_results.rolling.iso_rating_results.StressConcentrationMethod]

        Note:
            This property is readonly.
        """
        return None
