"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.part_model.couplings import _2595
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_RigidConnectorTypes",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_RigidConnectorTypes")


class EnumWithSelectedValue_RigidConnectorTypes(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_RigidConnectorTypes

    A specific implementation of 'EnumWithSelectedValue' for 'RigidConnectorTypes' types.
    """

    __qualname__ = "RigidConnectorTypes"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_2595.RigidConnectorTypes":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2595.RigidConnectorTypes

    @classmethod
    def implicit_type(cls) -> "_2595.RigidConnectorTypes.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2595.RigidConnectorTypes.type_()

    @property
    def selected_value(self: Self) -> "_2595.RigidConnectorTypes":
        """mastapy.system_model.part_model.couplings.RigidConnectorTypes

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_2595.RigidConnectorTypes]":
        """List[mastapy.system_model.part_model.couplings.RigidConnectorTypes]

        Note:
            This property is readonly.
        """
        return None
