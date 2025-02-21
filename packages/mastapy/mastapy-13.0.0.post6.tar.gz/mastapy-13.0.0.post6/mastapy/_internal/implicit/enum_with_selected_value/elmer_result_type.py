"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.nodal_analysis.elmer import _173
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ElmerResultType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_ElmerResultType")


class EnumWithSelectedValue_ElmerResultType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ElmerResultType

    A specific implementation of 'EnumWithSelectedValue' for 'ElmerResultType' types.
    """

    __qualname__ = "ElmerResultType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_173.ElmerResultType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _173.ElmerResultType

    @classmethod
    def implicit_type(cls) -> "_173.ElmerResultType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _173.ElmerResultType.type_()

    @property
    def selected_value(self: Self) -> "_173.ElmerResultType":
        """mastapy.nodal_analysis.elmer.ElmerResultType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_173.ElmerResultType]":
        """List[mastapy.nodal_analysis.elmer.ElmerResultType]

        Note:
            This property is readonly.
        """
        return None
