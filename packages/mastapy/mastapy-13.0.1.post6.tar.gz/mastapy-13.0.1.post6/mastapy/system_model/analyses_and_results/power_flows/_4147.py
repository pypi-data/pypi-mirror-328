"""StraightBevelGearSetPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4050
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "StraightBevelGearSetPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.static_loads import _6965
    from mastapy.gears.rating.straight_bevel import _397
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4146,
        _4145,
        _4038,
        _4066,
        _4095,
        _4135,
        _4032,
        _4114,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearSetPowerFlow",)


Self = TypeVar("Self", bound="StraightBevelGearSetPowerFlow")


class StraightBevelGearSetPowerFlow(_4050.BevelGearSetPowerFlow):
    """StraightBevelGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelGearSetPowerFlow")

    class _Cast_StraightBevelGearSetPowerFlow:
        """Special nested class for casting StraightBevelGearSetPowerFlow to subclasses."""

        def __init__(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
            parent: "StraightBevelGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_power_flow(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_4050.BevelGearSetPowerFlow":
            return self._parent._cast(_4050.BevelGearSetPowerFlow)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_4038.AGMAGleasonConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4038

            return self._parent._cast(_4038.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_4066.ConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4066

            return self._parent._cast(_4066.ConicalGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_4095.GearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4095

            return self._parent._cast(_4095.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_4135.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_4032.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4032

            return self._parent._cast(_4032.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_4114.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "StraightBevelGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelGearSetPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2548.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6965.StraightBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_397.StraightBevelGearSetRating":
        """mastapy.gears.rating.straight_bevel.StraightBevelGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_397.StraightBevelGearSetRating":
        """mastapy.gears.rating.straight_bevel.StraightBevelGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_power_flow(self: Self) -> "List[_4146.StraightBevelGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_gears_power_flow(
        self: Self,
    ) -> "List[_4146.StraightBevelGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_power_flow(self: Self) -> "List[_4145.StraightBevelGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_meshes_power_flow(
        self: Self,
    ) -> "List[_4145.StraightBevelGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow":
        return self._Cast_StraightBevelGearSetPowerFlow(self)
