"""ConceptGearPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4094
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ConceptGearPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2521
    from mastapy.gears.rating.concept import _551
    from mastapy.system_model.analyses_and_results.static_loads import _6842
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4112,
        _4057,
        _4114,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearPowerFlow",)


Self = TypeVar("Self", bound="ConceptGearPowerFlow")


class ConceptGearPowerFlow(_4094.GearPowerFlow):
    """ConceptGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearPowerFlow")

    class _Cast_ConceptGearPowerFlow:
        """Special nested class for casting ConceptGearPowerFlow to subclasses."""

        def __init__(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
            parent: "ConceptGearPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_power_flow(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
        ) -> "_4094.GearPowerFlow":
            return self._parent._cast(_4094.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
        ) -> "_4112.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4112

            return self._parent._cast(_4112.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
        ) -> "_4057.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
        ) -> "_4114.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_gear_power_flow(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
        ) -> "ConceptGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2521.ConceptGear":
        """mastapy.system_model.part_model.gears.ConceptGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_551.ConceptGearRating":
        """mastapy.gears.rating.concept.ConceptGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6842.ConceptGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow":
        return self._Cast_ConceptGearPowerFlow(self)
