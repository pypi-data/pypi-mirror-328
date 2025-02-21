"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.fe import _2411
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ThermalExpansionOption",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_ThermalExpansionOption")


class EnumWithSelectedValue_ThermalExpansionOption(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_ThermalExpansionOption

    A specific implementation of 'EnumWithSelectedValue' for 'ThermalExpansionOption' types.
    """

    __qualname__ = "ThermalExpansionOption"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_2411.ThermalExpansionOption":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2411.ThermalExpansionOption

    @classmethod
    def implicit_type(cls) -> "_2411.ThermalExpansionOption.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2411.ThermalExpansionOption.type_()

    @property
    def selected_value(self: Self) -> "_2411.ThermalExpansionOption":
        """mastapy.system_model.fe.ThermalExpansionOption

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_2411.ThermalExpansionOption]":
        """List[mastapy.system_model.fe.ThermalExpansionOption]

        Note:
            This property is readonly.
        """
        return None
