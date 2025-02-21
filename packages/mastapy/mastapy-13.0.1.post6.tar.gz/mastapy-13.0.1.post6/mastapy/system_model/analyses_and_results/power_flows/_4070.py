"""CouplingHalfPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4112
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "CouplingHalfPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2584
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4054,
        _4059,
        _4074,
        _4116,
        _4125,
        _4130,
        _4140,
        _4150,
        _4151,
        _4153,
        _4157,
        _4158,
        _4057,
        _4114,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfPowerFlow",)


Self = TypeVar("Self", bound="CouplingHalfPowerFlow")


class CouplingHalfPowerFlow(_4112.MountableComponentPowerFlow):
    """CouplingHalfPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfPowerFlow")

    class _Cast_CouplingHalfPowerFlow:
        """Special nested class for casting CouplingHalfPowerFlow to subclasses."""

        def __init__(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
            parent: "CouplingHalfPowerFlow",
        ):
            self._parent = parent

        @property
        def mountable_component_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "_4112.MountableComponentPowerFlow":
            return self._parent._cast(_4112.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "_4057.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "_4114.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_half_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "_4054.ClutchHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4054

            return self._parent._cast(_4054.ClutchHalfPowerFlow)

        @property
        def concept_coupling_half_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "_4059.ConceptCouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.ConceptCouplingHalfPowerFlow)

        @property
        def cvt_pulley_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "_4074.CVTPulleyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4074

            return self._parent._cast(_4074.CVTPulleyPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "_4116.PartToPartShearCouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PartToPartShearCouplingHalfPowerFlow)

        @property
        def pulley_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "_4125.PulleyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4125

            return self._parent._cast(_4125.PulleyPowerFlow)

        @property
        def rolling_ring_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "_4130.RollingRingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4130

            return self._parent._cast(_4130.RollingRingPowerFlow)

        @property
        def spring_damper_half_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "_4140.SpringDamperHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4140

            return self._parent._cast(_4140.SpringDamperHalfPowerFlow)

        @property
        def synchroniser_half_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "_4150.SynchroniserHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4150

            return self._parent._cast(_4150.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "_4151.SynchroniserPartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4151

            return self._parent._cast(_4151.SynchroniserPartPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "_4153.SynchroniserSleevePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4153

            return self._parent._cast(_4153.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_pump_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "_4157.TorqueConverterPumpPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4157

            return self._parent._cast(_4157.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "_4158.TorqueConverterTurbinePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.TorqueConverterTurbinePowerFlow)

        @property
        def coupling_half_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "CouplingHalfPowerFlow":
            return self._parent

        def __getattr__(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2584.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow":
        return self._Cast_CouplingHalfPowerFlow(self)
