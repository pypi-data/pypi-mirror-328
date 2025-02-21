"""ZerolBevelGearPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4049
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ZerolBevelGearPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2553
    from mastapy.gears.rating.zerol_bevel import _370
    from mastapy.system_model.analyses_and_results.static_loads import _6986
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4037,
        _4065,
        _4094,
        _4112,
        _4057,
        _4114,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearPowerFlow",)


Self = TypeVar("Self", bound="ZerolBevelGearPowerFlow")


class ZerolBevelGearPowerFlow(_4049.BevelGearPowerFlow):
    """ZerolBevelGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearPowerFlow")

    class _Cast_ZerolBevelGearPowerFlow:
        """Special nested class for casting ZerolBevelGearPowerFlow to subclasses."""

        def __init__(
            self: "ZerolBevelGearPowerFlow._Cast_ZerolBevelGearPowerFlow",
            parent: "ZerolBevelGearPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_power_flow(
            self: "ZerolBevelGearPowerFlow._Cast_ZerolBevelGearPowerFlow",
        ) -> "_4049.BevelGearPowerFlow":
            return self._parent._cast(_4049.BevelGearPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "ZerolBevelGearPowerFlow._Cast_ZerolBevelGearPowerFlow",
        ) -> "_4037.AGMAGleasonConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4037

            return self._parent._cast(_4037.AGMAGleasonConicalGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "ZerolBevelGearPowerFlow._Cast_ZerolBevelGearPowerFlow",
        ) -> "_4065.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ConicalGearPowerFlow)

        @property
        def gear_power_flow(
            self: "ZerolBevelGearPowerFlow._Cast_ZerolBevelGearPowerFlow",
        ) -> "_4094.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4094

            return self._parent._cast(_4094.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "ZerolBevelGearPowerFlow._Cast_ZerolBevelGearPowerFlow",
        ) -> "_4112.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4112

            return self._parent._cast(_4112.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "ZerolBevelGearPowerFlow._Cast_ZerolBevelGearPowerFlow",
        ) -> "_4057.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "ZerolBevelGearPowerFlow._Cast_ZerolBevelGearPowerFlow",
        ) -> "_4114.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearPowerFlow._Cast_ZerolBevelGearPowerFlow",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearPowerFlow._Cast_ZerolBevelGearPowerFlow",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearPowerFlow._Cast_ZerolBevelGearPowerFlow",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearPowerFlow._Cast_ZerolBevelGearPowerFlow",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearPowerFlow._Cast_ZerolBevelGearPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_power_flow(
            self: "ZerolBevelGearPowerFlow._Cast_ZerolBevelGearPowerFlow",
        ) -> "ZerolBevelGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearPowerFlow._Cast_ZerolBevelGearPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGearPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2553.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_370.ZerolBevelGearRating":
        """mastapy.gears.rating.zerol_bevel.ZerolBevelGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6986.ZerolBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ZerolBevelGearPowerFlow._Cast_ZerolBevelGearPowerFlow":
        return self._Cast_ZerolBevelGearPowerFlow(self)
