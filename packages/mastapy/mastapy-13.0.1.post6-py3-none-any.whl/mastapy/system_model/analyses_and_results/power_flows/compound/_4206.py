"""CouplingHalfCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4244
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "CouplingHalfCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4070
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4190,
        _4195,
        _4209,
        _4249,
        _4255,
        _4259,
        _4271,
        _4281,
        _4282,
        _4283,
        _4286,
        _4287,
        _4192,
        _4246,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundPowerFlow",)


Self = TypeVar("Self", bound="CouplingHalfCompoundPowerFlow")


class CouplingHalfCompoundPowerFlow(_4244.MountableComponentCompoundPowerFlow):
    """CouplingHalfCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfCompoundPowerFlow")

    class _Cast_CouplingHalfCompoundPowerFlow:
        """Special nested class for casting CouplingHalfCompoundPowerFlow to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
            parent: "CouplingHalfCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4244.MountableComponentCompoundPowerFlow":
            return self._parent._cast(_4244.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4192.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4246.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_half_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4190.ClutchHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4190,
            )

            return self._parent._cast(_4190.ClutchHalfCompoundPowerFlow)

        @property
        def concept_coupling_half_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4195.ConceptCouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4195,
            )

            return self._parent._cast(_4195.ConceptCouplingHalfCompoundPowerFlow)

        @property
        def cvt_pulley_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4209.CVTPulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4209,
            )

            return self._parent._cast(_4209.CVTPulleyCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_half_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4249.PartToPartShearCouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4249,
            )

            return self._parent._cast(
                _4249.PartToPartShearCouplingHalfCompoundPowerFlow
            )

        @property
        def pulley_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4255.PulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4255,
            )

            return self._parent._cast(_4255.PulleyCompoundPowerFlow)

        @property
        def rolling_ring_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4259.RollingRingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4259,
            )

            return self._parent._cast(_4259.RollingRingCompoundPowerFlow)

        @property
        def spring_damper_half_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4271.SpringDamperHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4271,
            )

            return self._parent._cast(_4271.SpringDamperHalfCompoundPowerFlow)

        @property
        def synchroniser_half_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4281.SynchroniserHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4281,
            )

            return self._parent._cast(_4281.SynchroniserHalfCompoundPowerFlow)

        @property
        def synchroniser_part_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4282.SynchroniserPartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4282,
            )

            return self._parent._cast(_4282.SynchroniserPartCompoundPowerFlow)

        @property
        def synchroniser_sleeve_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4283.SynchroniserSleeveCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4283,
            )

            return self._parent._cast(_4283.SynchroniserSleeveCompoundPowerFlow)

        @property
        def torque_converter_pump_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4286.TorqueConverterPumpCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4286,
            )

            return self._parent._cast(_4286.TorqueConverterPumpCompoundPowerFlow)

        @property
        def torque_converter_turbine_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4287.TorqueConverterTurbineCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4287,
            )

            return self._parent._cast(_4287.TorqueConverterTurbineCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "CouplingHalfCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4070.CouplingHalfPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CouplingHalfPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4070.CouplingHalfPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CouplingHalfPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow":
        return self._Cast_CouplingHalfCompoundPowerFlow(self)
