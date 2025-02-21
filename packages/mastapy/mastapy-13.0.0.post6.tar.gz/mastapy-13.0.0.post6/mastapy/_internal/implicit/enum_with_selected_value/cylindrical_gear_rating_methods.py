"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.materials import _251
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_CylindricalGearRatingMethods",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_CylindricalGearRatingMethods")


class EnumWithSelectedValue_CylindricalGearRatingMethods(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_CylindricalGearRatingMethods

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalGearRatingMethods' types.
    """

    __qualname__ = "CylindricalGearRatingMethods"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_251.CylindricalGearRatingMethods":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _251.CylindricalGearRatingMethods

    @classmethod
    def implicit_type(cls) -> "_251.CylindricalGearRatingMethods.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _251.CylindricalGearRatingMethods.type_()

    @property
    def selected_value(self: Self) -> "_251.CylindricalGearRatingMethods":
        """mastapy.materials.CylindricalGearRatingMethods

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_251.CylindricalGearRatingMethods]":
        """List[mastapy.materials.CylindricalGearRatingMethods]

        Note:
            This property is readonly.
        """
        return None
