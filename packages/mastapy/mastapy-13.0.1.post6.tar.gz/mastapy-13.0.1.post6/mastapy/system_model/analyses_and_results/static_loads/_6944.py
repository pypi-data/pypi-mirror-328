"""RingPinsLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6925
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "RingPinsLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6817,
        _6838,
        _6929,
    )
    from mastapy.system_model.part_model.cycloidal import _2570
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsLoadCase",)


Self = TypeVar("Self", bound="RingPinsLoadCase")


class RingPinsLoadCase(_6925.MountableComponentLoadCase):
    """RingPinsLoadCase

    This is a mastapy class.
    """

    TYPE = _RING_PINS_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsLoadCase")

    class _Cast_RingPinsLoadCase:
        """Special nested class for casting RingPinsLoadCase to subclasses."""

        def __init__(
            self: "RingPinsLoadCase._Cast_RingPinsLoadCase", parent: "RingPinsLoadCase"
        ):
            self._parent = parent

        @property
        def mountable_component_load_case(
            self: "RingPinsLoadCase._Cast_RingPinsLoadCase",
        ) -> "_6925.MountableComponentLoadCase":
            return self._parent._cast(_6925.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "RingPinsLoadCase._Cast_RingPinsLoadCase",
        ) -> "_6838.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6838

            return self._parent._cast(_6838.ComponentLoadCase)

        @property
        def part_load_case(
            self: "RingPinsLoadCase._Cast_RingPinsLoadCase",
        ) -> "_6929.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(_6929.PartLoadCase)

        @property
        def part_analysis(
            self: "RingPinsLoadCase._Cast_RingPinsLoadCase",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsLoadCase._Cast_RingPinsLoadCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsLoadCase._Cast_RingPinsLoadCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def ring_pins_load_case(
            self: "RingPinsLoadCase._Cast_RingPinsLoadCase",
        ) -> "RingPinsLoadCase":
            return self._parent

        def __getattr__(self: "RingPinsLoadCase._Cast_RingPinsLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinsLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def all_ring_pins_manufacturing_error(
        self: Self,
    ) -> "_6817.AllRingPinsManufacturingError":
        """mastapy.system_model.analyses_and_results.static_loads.AllRingPinsManufacturingError

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllRingPinsManufacturingError

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_design(self: Self) -> "_2570.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "RingPinsLoadCase._Cast_RingPinsLoadCase":
        return self._Cast_RingPinsLoadCase(self)
