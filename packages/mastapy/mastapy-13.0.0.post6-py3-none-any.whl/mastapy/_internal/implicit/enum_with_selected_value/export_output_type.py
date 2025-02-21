"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5744
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ExportOutputType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_ExportOutputType")


class EnumWithSelectedValue_ExportOutputType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ExportOutputType

    A specific implementation of 'EnumWithSelectedValue' for 'ExportOutputType' types.
    """

    __qualname__ = "ExportOutputType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_5744.ExportOutputType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5744.ExportOutputType

    @classmethod
    def implicit_type(cls) -> "_5744.ExportOutputType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5744.ExportOutputType.type_()

    @property
    def selected_value(self: Self) -> "_5744.ExportOutputType":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ExportOutputType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_5744.ExportOutputType]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ExportOutputType]

        Note:
            This property is readonly.
        """
        return None
