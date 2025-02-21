"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.micro_geometry import _573
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_LocationOfEvaluationLowerLimit",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_LocationOfEvaluationLowerLimit")


class EnumWithSelectedValue_LocationOfEvaluationLowerLimit(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_LocationOfEvaluationLowerLimit

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfEvaluationLowerLimit' types.
    """

    __qualname__ = "LocationOfEvaluationLowerLimit"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_573.LocationOfEvaluationLowerLimit":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _573.LocationOfEvaluationLowerLimit

    @classmethod
    def implicit_type(cls) -> "_573.LocationOfEvaluationLowerLimit.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _573.LocationOfEvaluationLowerLimit.type_()

    @property
    def selected_value(self: Self) -> "_573.LocationOfEvaluationLowerLimit":
        """mastapy.gears.micro_geometry.LocationOfEvaluationLowerLimit

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_573.LocationOfEvaluationLowerLimit]":
        """List[mastapy.gears.micro_geometry.LocationOfEvaluationLowerLimit]

        Note:
            This property is readonly.
        """
        return None
