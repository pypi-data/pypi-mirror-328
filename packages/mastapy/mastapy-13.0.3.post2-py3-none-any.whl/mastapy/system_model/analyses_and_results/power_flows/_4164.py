"""StraightBevelDiffGearPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4070
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "StraightBevelDiffGearPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2565
    from mastapy.gears.rating.straight_bevel_diff import _402
    from mastapy.system_model.analyses_and_results.static_loads import _6981
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4169,
        _4170,
        _4058,
        _4086,
        _4115,
        _4133,
        _4078,
        _4135,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearPowerFlow",)


Self = TypeVar("Self", bound="StraightBevelDiffGearPowerFlow")


class StraightBevelDiffGearPowerFlow(_4070.BevelGearPowerFlow):
    """StraightBevelDiffGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearPowerFlow")

    class _Cast_StraightBevelDiffGearPowerFlow:
        """Special nested class for casting StraightBevelDiffGearPowerFlow to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearPowerFlow._Cast_StraightBevelDiffGearPowerFlow",
            parent: "StraightBevelDiffGearPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_power_flow(
            self: "StraightBevelDiffGearPowerFlow._Cast_StraightBevelDiffGearPowerFlow",
        ) -> "_4070.BevelGearPowerFlow":
            return self._parent._cast(_4070.BevelGearPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "StraightBevelDiffGearPowerFlow._Cast_StraightBevelDiffGearPowerFlow",
        ) -> "_4058.AGMAGleasonConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4058

            return self._parent._cast(_4058.AGMAGleasonConicalGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "StraightBevelDiffGearPowerFlow._Cast_StraightBevelDiffGearPowerFlow",
        ) -> "_4086.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4086

            return self._parent._cast(_4086.ConicalGearPowerFlow)

        @property
        def gear_power_flow(
            self: "StraightBevelDiffGearPowerFlow._Cast_StraightBevelDiffGearPowerFlow",
        ) -> "_4115.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4115

            return self._parent._cast(_4115.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "StraightBevelDiffGearPowerFlow._Cast_StraightBevelDiffGearPowerFlow",
        ) -> "_4133.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "StraightBevelDiffGearPowerFlow._Cast_StraightBevelDiffGearPowerFlow",
        ) -> "_4078.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "StraightBevelDiffGearPowerFlow._Cast_StraightBevelDiffGearPowerFlow",
        ) -> "_4135.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearPowerFlow._Cast_StraightBevelDiffGearPowerFlow",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearPowerFlow._Cast_StraightBevelDiffGearPowerFlow",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearPowerFlow._Cast_StraightBevelDiffGearPowerFlow",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearPowerFlow._Cast_StraightBevelDiffGearPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearPowerFlow._Cast_StraightBevelDiffGearPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "StraightBevelDiffGearPowerFlow._Cast_StraightBevelDiffGearPowerFlow",
        ) -> "_4169.StraightBevelPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4169

            return self._parent._cast(_4169.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "StraightBevelDiffGearPowerFlow._Cast_StraightBevelDiffGearPowerFlow",
        ) -> "_4170.StraightBevelSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4170

            return self._parent._cast(_4170.StraightBevelSunGearPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "StraightBevelDiffGearPowerFlow._Cast_StraightBevelDiffGearPowerFlow",
        ) -> "StraightBevelDiffGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearPowerFlow._Cast_StraightBevelDiffGearPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelDiffGearPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2565.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_402.StraightBevelDiffGearRating":
        """mastapy.gears.rating.straight_bevel_diff.StraightBevelDiffGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6981.StraightBevelDiffGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearPowerFlow._Cast_StraightBevelDiffGearPowerFlow":
        return self._Cast_StraightBevelDiffGearPowerFlow(self)
