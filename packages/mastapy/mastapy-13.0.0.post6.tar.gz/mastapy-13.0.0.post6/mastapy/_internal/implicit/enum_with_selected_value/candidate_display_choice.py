"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.gear_set_pareto_optimiser import _903
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_CandidateDisplayChoice",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_CandidateDisplayChoice")


class EnumWithSelectedValue_CandidateDisplayChoice(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_CandidateDisplayChoice

    A specific implementation of 'EnumWithSelectedValue' for 'CandidateDisplayChoice' types.
    """

    __qualname__ = "CandidateDisplayChoice"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_903.CandidateDisplayChoice":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _903.CandidateDisplayChoice

    @classmethod
    def implicit_type(cls) -> "_903.CandidateDisplayChoice.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _903.CandidateDisplayChoice.type_()

    @property
    def selected_value(self: Self) -> "_903.CandidateDisplayChoice":
        """mastapy.gears.gear_set_pareto_optimiser.CandidateDisplayChoice

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_903.CandidateDisplayChoice]":
        """List[mastapy.gears.gear_set_pareto_optimiser.CandidateDisplayChoice]

        Note:
            This property is readonly.
        """
        return None
