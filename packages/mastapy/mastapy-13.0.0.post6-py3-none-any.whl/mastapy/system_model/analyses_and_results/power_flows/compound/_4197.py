"""ConceptGearSetCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4226
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ConceptGearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2522
    from mastapy.system_model.analyses_and_results.power_flows import _4063
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4195,
        _4196,
        _4264,
        _4166,
        _4245,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="ConceptGearSetCompoundPowerFlow")


class ConceptGearSetCompoundPowerFlow(_4226.GearSetCompoundPowerFlow):
    """ConceptGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearSetCompoundPowerFlow")

    class _Cast_ConceptGearSetCompoundPowerFlow:
        """Special nested class for casting ConceptGearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ConceptGearSetCompoundPowerFlow._Cast_ConceptGearSetCompoundPowerFlow",
            parent: "ConceptGearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_set_compound_power_flow(
            self: "ConceptGearSetCompoundPowerFlow._Cast_ConceptGearSetCompoundPowerFlow",
        ) -> "_4226.GearSetCompoundPowerFlow":
            return self._parent._cast(_4226.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "ConceptGearSetCompoundPowerFlow._Cast_ConceptGearSetCompoundPowerFlow",
        ) -> "_4264.SpecialisedAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4264,
            )

            return self._parent._cast(_4264.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "ConceptGearSetCompoundPowerFlow._Cast_ConceptGearSetCompoundPowerFlow",
        ) -> "_4166.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4166,
            )

            return self._parent._cast(_4166.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "ConceptGearSetCompoundPowerFlow._Cast_ConceptGearSetCompoundPowerFlow",
        ) -> "_4245.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4245,
            )

            return self._parent._cast(_4245.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "ConceptGearSetCompoundPowerFlow._Cast_ConceptGearSetCompoundPowerFlow",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptGearSetCompoundPowerFlow._Cast_ConceptGearSetCompoundPowerFlow",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearSetCompoundPowerFlow._Cast_ConceptGearSetCompoundPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_gear_set_compound_power_flow(
            self: "ConceptGearSetCompoundPowerFlow._Cast_ConceptGearSetCompoundPowerFlow",
        ) -> "ConceptGearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConceptGearSetCompoundPowerFlow._Cast_ConceptGearSetCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearSetCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2522.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2522.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

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
    ) -> "List[_4063.ConceptGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConceptGearSetPowerFlow]

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
    def concept_gears_compound_power_flow(
        self: Self,
    ) -> "List[_4195.ConceptGearCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.ConceptGearCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearsCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes_compound_power_flow(
        self: Self,
    ) -> "List[_4196.ConceptGearMeshCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.ConceptGearMeshCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshesCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4063.ConceptGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConceptGearSetPowerFlow]

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
    ) -> "ConceptGearSetCompoundPowerFlow._Cast_ConceptGearSetCompoundPowerFlow":
        return self._Cast_ConceptGearSetCompoundPowerFlow(self)
