"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.analyses_and_results.static_loads import _6897
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_HarmonicExcitationType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_HarmonicExcitationType")


class EnumWithSelectedValue_HarmonicExcitationType(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_HarmonicExcitationType

    A specific implementation of 'EnumWithSelectedValue' for 'HarmonicExcitationType' types.
    """

    __qualname__ = "HarmonicExcitationType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_6897.HarmonicExcitationType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6897.HarmonicExcitationType

    @classmethod
    def implicit_type(cls) -> "_6897.HarmonicExcitationType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6897.HarmonicExcitationType.type_()

    @property
    def selected_value(self: Self) -> "_6897.HarmonicExcitationType":
        """mastapy.system_model.analyses_and_results.static_loads.HarmonicExcitationType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_6897.HarmonicExcitationType]":
        """List[mastapy.system_model.analyses_and_results.static_loads.HarmonicExcitationType]

        Note:
            This property is readonly.
        """
        return None
