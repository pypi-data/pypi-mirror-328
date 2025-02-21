"""StraightBevelSunGearPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4142
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "StraightBevelSunGearPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4049,
        _4037,
        _4065,
        _4093,
        _4111,
        _4057,
        _4113,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearPowerFlow",)


Self = TypeVar("Self", bound="StraightBevelSunGearPowerFlow")


class StraightBevelSunGearPowerFlow(_4142.StraightBevelDiffGearPowerFlow):
    """StraightBevelSunGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelSunGearPowerFlow")

    class _Cast_StraightBevelSunGearPowerFlow:
        """Special nested class for casting StraightBevelSunGearPowerFlow to subclasses."""

        def __init__(
            self: "StraightBevelSunGearPowerFlow._Cast_StraightBevelSunGearPowerFlow",
            parent: "StraightBevelSunGearPowerFlow",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "StraightBevelSunGearPowerFlow._Cast_StraightBevelSunGearPowerFlow",
        ) -> "_4142.StraightBevelDiffGearPowerFlow":
            return self._parent._cast(_4142.StraightBevelDiffGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "StraightBevelSunGearPowerFlow._Cast_StraightBevelSunGearPowerFlow",
        ) -> "_4049.BevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4049

            return self._parent._cast(_4049.BevelGearPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "StraightBevelSunGearPowerFlow._Cast_StraightBevelSunGearPowerFlow",
        ) -> "_4037.AGMAGleasonConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4037

            return self._parent._cast(_4037.AGMAGleasonConicalGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "StraightBevelSunGearPowerFlow._Cast_StraightBevelSunGearPowerFlow",
        ) -> "_4065.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ConicalGearPowerFlow)

        @property
        def gear_power_flow(
            self: "StraightBevelSunGearPowerFlow._Cast_StraightBevelSunGearPowerFlow",
        ) -> "_4093.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4093

            return self._parent._cast(_4093.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "StraightBevelSunGearPowerFlow._Cast_StraightBevelSunGearPowerFlow",
        ) -> "_4111.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "StraightBevelSunGearPowerFlow._Cast_StraightBevelSunGearPowerFlow",
        ) -> "_4057.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "StraightBevelSunGearPowerFlow._Cast_StraightBevelSunGearPowerFlow",
        ) -> "_4113.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelSunGearPowerFlow._Cast_StraightBevelSunGearPowerFlow",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelSunGearPowerFlow._Cast_StraightBevelSunGearPowerFlow",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearPowerFlow._Cast_StraightBevelSunGearPowerFlow",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearPowerFlow._Cast_StraightBevelSunGearPowerFlow",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearPowerFlow._Cast_StraightBevelSunGearPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "StraightBevelSunGearPowerFlow._Cast_StraightBevelSunGearPowerFlow",
        ) -> "StraightBevelSunGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearPowerFlow._Cast_StraightBevelSunGearPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelSunGearPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2550.StraightBevelSunGear":
        """mastapy.system_model.part_model.gears.StraightBevelSunGear

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
    ) -> "StraightBevelSunGearPowerFlow._Cast_StraightBevelSunGearPowerFlow":
        return self._Cast_StraightBevelSunGearPowerFlow(self)
