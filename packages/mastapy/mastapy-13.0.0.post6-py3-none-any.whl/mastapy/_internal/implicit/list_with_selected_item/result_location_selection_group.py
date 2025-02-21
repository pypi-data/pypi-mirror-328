"""Implementations of 'ListWithSelectedItem' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from typing import List, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses.results import _5850
from mastapy._internal import constructor, conversion, mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_LIST_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Property", "ListWithSelectedItem"
)


__docformat__ = "restructuredtext en"
__all__ = ("ListWithSelectedItem_ResultLocationSelectionGroup",)


Self = TypeVar("Self", bound="ListWithSelectedItem_ResultLocationSelectionGroup")


class ListWithSelectedItem_ResultLocationSelectionGroup(
    _5850.ResultLocationSelectionGroup, mixins.ListWithSelectedItemMixin
):
    """ListWithSelectedItem_ResultLocationSelectionGroup

    A specific implementation of 'ListWithSelectedItem' for 'ResultLocationSelectionGroup' types.
    """

    __qualname__ = "ResultLocationSelectionGroup"

    def __init__(
        self, instance_to_wrap: "ListWithSelectedItem_ResultLocationSelectionGroup.TYPE"
    ):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> "_LIST_WITH_SELECTED_ITEM":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> "_5850.ResultLocationSelectionGroup.TYPE":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5850.ResultLocationSelectionGroup.TYPE

    @property
    def selected_value(self: Self) -> "_5850.ResultLocationSelectionGroup":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.results.ResultLocationSelectionGroup

        Note:
            This property is readonly.
        """
        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def available_values(self: Self) -> "List[_5850.ResultLocationSelectionGroup]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.results.ResultLocationSelectionGroup]

        Note:
            This property is readonly.
        """
        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value
