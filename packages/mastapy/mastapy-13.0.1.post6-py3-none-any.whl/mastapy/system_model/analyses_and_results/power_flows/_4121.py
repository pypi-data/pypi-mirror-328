"""PointLoadPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4160
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "PointLoadPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.static_loads import _6939
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4112,
        _4057,
        _4114,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadPowerFlow",)


Self = TypeVar("Self", bound="PointLoadPowerFlow")


class PointLoadPowerFlow(_4160.VirtualComponentPowerFlow):
    """PointLoadPowerFlow

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointLoadPowerFlow")

    class _Cast_PointLoadPowerFlow:
        """Special nested class for casting PointLoadPowerFlow to subclasses."""

        def __init__(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
            parent: "PointLoadPowerFlow",
        ):
            self._parent = parent

        @property
        def virtual_component_power_flow(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_4160.VirtualComponentPowerFlow":
            return self._parent._cast(_4160.VirtualComponentPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_4112.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4112

            return self._parent._cast(_4112.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_4057.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_4114.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def point_load_power_flow(
            self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow",
        ) -> "PointLoadPowerFlow":
            return self._parent

        def __getattr__(self: "PointLoadPowerFlow._Cast_PointLoadPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PointLoadPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2471.PointLoad":
        """mastapy.system_model.part_model.PointLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6939.PointLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PointLoadPowerFlow._Cast_PointLoadPowerFlow":
        return self._Cast_PointLoadPowerFlow(self)
