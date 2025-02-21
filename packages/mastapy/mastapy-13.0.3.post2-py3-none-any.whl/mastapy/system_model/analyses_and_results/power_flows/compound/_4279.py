"""RollingRingAssemblyCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4286
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "RollingRingAssemblyCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2618
    from mastapy.system_model.analyses_and_results.power_flows import _4149
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4188,
        _4267,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyCompoundPowerFlow",)


Self = TypeVar("Self", bound="RollingRingAssemblyCompoundPowerFlow")


class RollingRingAssemblyCompoundPowerFlow(_4286.SpecialisedAssemblyCompoundPowerFlow):
    """RollingRingAssemblyCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingAssemblyCompoundPowerFlow")

    class _Cast_RollingRingAssemblyCompoundPowerFlow:
        """Special nested class for casting RollingRingAssemblyCompoundPowerFlow to subclasses."""

        def __init__(
            self: "RollingRingAssemblyCompoundPowerFlow._Cast_RollingRingAssemblyCompoundPowerFlow",
            parent: "RollingRingAssemblyCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_power_flow(
            self: "RollingRingAssemblyCompoundPowerFlow._Cast_RollingRingAssemblyCompoundPowerFlow",
        ) -> "_4286.SpecialisedAssemblyCompoundPowerFlow":
            return self._parent._cast(_4286.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "RollingRingAssemblyCompoundPowerFlow._Cast_RollingRingAssemblyCompoundPowerFlow",
        ) -> "_4188.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "RollingRingAssemblyCompoundPowerFlow._Cast_RollingRingAssemblyCompoundPowerFlow",
        ) -> "_4267.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "RollingRingAssemblyCompoundPowerFlow._Cast_RollingRingAssemblyCompoundPowerFlow",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingAssemblyCompoundPowerFlow._Cast_RollingRingAssemblyCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyCompoundPowerFlow._Cast_RollingRingAssemblyCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_compound_power_flow(
            self: "RollingRingAssemblyCompoundPowerFlow._Cast_RollingRingAssemblyCompoundPowerFlow",
        ) -> "RollingRingAssemblyCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyCompoundPowerFlow._Cast_RollingRingAssemblyCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "RollingRingAssemblyCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2618.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2618.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4149.RollingRingAssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.RollingRingAssemblyPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4149.RollingRingAssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.RollingRingAssemblyPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingAssemblyCompoundPowerFlow._Cast_RollingRingAssemblyCompoundPowerFlow":
        return self._Cast_RollingRingAssemblyCompoundPowerFlow(self)
