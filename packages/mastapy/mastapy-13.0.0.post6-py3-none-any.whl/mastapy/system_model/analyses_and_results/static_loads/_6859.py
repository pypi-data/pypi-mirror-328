"""CycloidalDiscLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6807
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CycloidalDiscLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2569
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6808,
        _6837,
        _6928,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscLoadCase",)


Self = TypeVar("Self", bound="CycloidalDiscLoadCase")


class CycloidalDiscLoadCase(_6807.AbstractShaftLoadCase):
    """CycloidalDiscLoadCase

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscLoadCase")

    class _Cast_CycloidalDiscLoadCase:
        """Special nested class for casting CycloidalDiscLoadCase to subclasses."""

        def __init__(
            self: "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase",
            parent: "CycloidalDiscLoadCase",
        ):
            self._parent = parent

        @property
        def abstract_shaft_load_case(
            self: "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase",
        ) -> "_6807.AbstractShaftLoadCase":
            return self._parent._cast(_6807.AbstractShaftLoadCase)

        @property
        def abstract_shaft_or_housing_load_case(
            self: "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase",
        ) -> "_6808.AbstractShaftOrHousingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6808

            return self._parent._cast(_6808.AbstractShaftOrHousingLoadCase)

        @property
        def component_load_case(
            self: "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase",
        ) -> "_6837.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.ComponentLoadCase)

        @property
        def part_load_case(
            self: "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase",
        ) -> "_6928.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(
            self: "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_load_case(
            self: "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase",
        ) -> "CycloidalDiscLoadCase":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2569.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CycloidalDiscLoadCase._Cast_CycloidalDiscLoadCase":
        return self._Cast_CycloidalDiscLoadCase(self)
