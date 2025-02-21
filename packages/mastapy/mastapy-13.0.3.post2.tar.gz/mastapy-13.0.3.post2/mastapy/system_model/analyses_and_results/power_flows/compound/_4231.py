"""CycloidalAssemblyCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4286
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "CycloidalAssemblyCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2588
    from mastapy.system_model.analyses_and_results.power_flows import _4096
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4188,
        _4267,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalAssemblyCompoundPowerFlow",)


Self = TypeVar("Self", bound="CycloidalAssemblyCompoundPowerFlow")


class CycloidalAssemblyCompoundPowerFlow(_4286.SpecialisedAssemblyCompoundPowerFlow):
    """CycloidalAssemblyCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalAssemblyCompoundPowerFlow")

    class _Cast_CycloidalAssemblyCompoundPowerFlow:
        """Special nested class for casting CycloidalAssemblyCompoundPowerFlow to subclasses."""

        def __init__(
            self: "CycloidalAssemblyCompoundPowerFlow._Cast_CycloidalAssemblyCompoundPowerFlow",
            parent: "CycloidalAssemblyCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_power_flow(
            self: "CycloidalAssemblyCompoundPowerFlow._Cast_CycloidalAssemblyCompoundPowerFlow",
        ) -> "_4286.SpecialisedAssemblyCompoundPowerFlow":
            return self._parent._cast(_4286.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "CycloidalAssemblyCompoundPowerFlow._Cast_CycloidalAssemblyCompoundPowerFlow",
        ) -> "_4188.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "CycloidalAssemblyCompoundPowerFlow._Cast_CycloidalAssemblyCompoundPowerFlow",
        ) -> "_4267.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "CycloidalAssemblyCompoundPowerFlow._Cast_CycloidalAssemblyCompoundPowerFlow",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalAssemblyCompoundPowerFlow._Cast_CycloidalAssemblyCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalAssemblyCompoundPowerFlow._Cast_CycloidalAssemblyCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_assembly_compound_power_flow(
            self: "CycloidalAssemblyCompoundPowerFlow._Cast_CycloidalAssemblyCompoundPowerFlow",
        ) -> "CycloidalAssemblyCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "CycloidalAssemblyCompoundPowerFlow._Cast_CycloidalAssemblyCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "CycloidalAssemblyCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2588.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2588.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

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
    ) -> "List[_4096.CycloidalAssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CycloidalAssemblyPowerFlow]

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
    def assembly_analysis_cases(self: Self) -> "List[_4096.CycloidalAssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CycloidalAssemblyPowerFlow]

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
    ) -> "CycloidalAssemblyCompoundPowerFlow._Cast_CycloidalAssemblyCompoundPowerFlow":
        return self._Cast_CycloidalAssemblyCompoundPowerFlow(self)
