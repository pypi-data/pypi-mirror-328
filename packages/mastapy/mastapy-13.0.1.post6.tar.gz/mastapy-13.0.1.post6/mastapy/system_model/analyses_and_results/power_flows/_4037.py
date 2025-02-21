"""AGMAGleasonConicalGearPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4065
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "AGMAGleasonConicalGearPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2513
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4044,
        _4046,
        _4047,
        _4049,
        _4098,
        _4137,
        _4143,
        _4146,
        _4148,
        _4149,
        _4165,
        _4094,
        _4112,
        _4057,
        _4114,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearPowerFlow",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearPowerFlow")


class AGMAGleasonConicalGearPowerFlow(_4065.ConicalGearPowerFlow):
    """AGMAGleasonConicalGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearPowerFlow")

    class _Cast_AGMAGleasonConicalGearPowerFlow:
        """Special nested class for casting AGMAGleasonConicalGearPowerFlow to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
            parent: "AGMAGleasonConicalGearPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4065.ConicalGearPowerFlow":
            return self._parent._cast(_4065.ConicalGearPowerFlow)

        @property
        def gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4094.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4094

            return self._parent._cast(_4094.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4112.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4112

            return self._parent._cast(_4112.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4057.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4114.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4044.BevelDifferentialGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4044

            return self._parent._cast(_4044.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4046.BevelDifferentialPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4046

            return self._parent._cast(_4046.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4047.BevelDifferentialSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4047

            return self._parent._cast(_4047.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4049.BevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4049

            return self._parent._cast(_4049.BevelGearPowerFlow)

        @property
        def hypoid_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4098.HypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4098

            return self._parent._cast(_4098.HypoidGearPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4137.SpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.SpiralBevelGearPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4143.StraightBevelDiffGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4146.StraightBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4146

            return self._parent._cast(_4146.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4148.StraightBevelPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4148

            return self._parent._cast(_4148.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4149.StraightBevelSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4149

            return self._parent._cast(_4149.StraightBevelSunGearPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4165.ZerolBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4165

            return self._parent._cast(_4165.ZerolBevelGearPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "AGMAGleasonConicalGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2513.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow":
        return self._Cast_AGMAGleasonConicalGearPowerFlow(self)
