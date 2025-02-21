"""AGMAGleasonConicalGearSetPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4066
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "AGMAGleasonConicalGearSetPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2514
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4045,
        _4050,
        _4099,
        _4138,
        _4144,
        _4147,
        _4166,
        _4095,
        _4135,
        _4032,
        _4114,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetPowerFlow",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetPowerFlow")


class AGMAGleasonConicalGearSetPowerFlow(_4066.ConicalGearSetPowerFlow):
    """AGMAGleasonConicalGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetPowerFlow")

    class _Cast_AGMAGleasonConicalGearSetPowerFlow:
        """Special nested class for casting AGMAGleasonConicalGearSetPowerFlow to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
            parent: "AGMAGleasonConicalGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_set_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ) -> "_4066.ConicalGearSetPowerFlow":
            return self._parent._cast(_4066.ConicalGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ) -> "_4095.GearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4095

            return self._parent._cast(_4095.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ) -> "_4135.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ) -> "_4032.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4032

            return self._parent._cast(_4032.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ) -> "_4114.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ) -> "_4045.BevelDifferentialGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4045

            return self._parent._cast(_4045.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_gear_set_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ) -> "_4050.BevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4050

            return self._parent._cast(_4050.BevelGearSetPowerFlow)

        @property
        def hypoid_gear_set_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ) -> "_4099.HypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4099

            return self._parent._cast(_4099.HypoidGearSetPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ) -> "_4138.SpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4138

            return self._parent._cast(_4138.SpiralBevelGearSetPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ) -> "_4144.StraightBevelDiffGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4144

            return self._parent._cast(_4144.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ) -> "_4147.StraightBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4147

            return self._parent._cast(_4147.StraightBevelGearSetPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ) -> "_4166.ZerolBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4166

            return self._parent._cast(_4166.ZerolBevelGearSetPowerFlow)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ) -> "AGMAGleasonConicalGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearSetPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2514.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow":
        return self._Cast_AGMAGleasonConicalGearSetPowerFlow(self)
