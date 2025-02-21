"""Implementations of 'ListWithSelectedItem' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from typing import List, TypeVar

from mastapy._internal import conversion, mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_LIST_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Property", "ListWithSelectedItem"
)


__docformat__ = "restructuredtext en"
__all__ = ("ListWithSelectedItem_int",)


Self = TypeVar("Self", bound="ListWithSelectedItem_int")


class ListWithSelectedItem_int(int, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_int

    A specific implementation of 'ListWithSelectedItem' for 'int' types.
    """

    __qualname__ = "int"

    def __new__(cls, instance_to_wrap: "ListWithSelectedItem_int.TYPE"):
        return int.__new__(
            cls,
            instance_to_wrap.SelectedValue
            if instance_to_wrap.SelectedValue is not None
            else 0,
        )

    def __init__(self, instance_to_wrap: "ListWithSelectedItem_int.TYPE"):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> "_LIST_WITH_SELECTED_ITEM":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> "int":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return int

    @property
    def selected_value(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.enclosing.SelectedValue

        if temp is None:
            return 0

        return temp

    @property
    def available_values(self: Self) -> "List[int]":
        """List[int]

        Note:
            This property is readonly.
        """
        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, int)

        if value is None:
            return None

        return value
