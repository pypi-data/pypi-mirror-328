"""PlanetCarrierPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4112
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "PlanetCarrierPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2469
    from mastapy.system_model.analyses_and_results.static_loads import _6936
    from mastapy.system_model.analyses_and_results.power_flows import _4057, _4114
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierPowerFlow",)


Self = TypeVar("Self", bound="PlanetCarrierPowerFlow")


class PlanetCarrierPowerFlow(_4112.MountableComponentPowerFlow):
    """PlanetCarrierPowerFlow

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetCarrierPowerFlow")

    class _Cast_PlanetCarrierPowerFlow:
        """Special nested class for casting PlanetCarrierPowerFlow to subclasses."""

        def __init__(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow",
            parent: "PlanetCarrierPowerFlow",
        ):
            self._parent = parent

        @property
        def mountable_component_power_flow(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow",
        ) -> "_4112.MountableComponentPowerFlow":
            return self._parent._cast(_4112.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow",
        ) -> "_4057.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow",
        ) -> "_4114.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planet_carrier_power_flow(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow",
        ) -> "PlanetCarrierPowerFlow":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetCarrierPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2469.PlanetCarrier":
        """mastapy.system_model.part_model.PlanetCarrier

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6936.PlanetCarrierLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow":
        return self._Cast_PlanetCarrierPowerFlow(self)
