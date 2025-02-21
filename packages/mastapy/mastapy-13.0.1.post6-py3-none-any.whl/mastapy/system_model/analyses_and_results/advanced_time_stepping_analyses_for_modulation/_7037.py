"""ConceptCouplingAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7048,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581
    from mastapy.system_model.analyses_and_results.static_loads import _6841
    from mastapy.system_model.analyses_and_results.system_deflections import _2719
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7110,
        _7006,
        _7091,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="ConceptCouplingAdvancedTimeSteppingAnalysisForModulation")


class ConceptCouplingAdvancedTimeSteppingAnalysisForModulation(
    _7048.CouplingAdvancedTimeSteppingAnalysisForModulation
):
    """ConceptCouplingAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_ConceptCouplingAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ConceptCouplingAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
            parent: "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def coupling_advanced_time_stepping_analysis_for_modulation(
            self: "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7048.CouplingAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7048.CouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7110.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7110,
            )

            return self._parent._cast(
                _7110.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7006.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7006,
            )

            return self._parent._cast(
                _7006.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7091.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7091,
            )

            return self._parent._cast(
                _7091.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_coupling_advanced_time_stepping_analysis_for_modulation(
            self: "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
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
        self: Self,
        instance_to_wrap: "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2581.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6841.ConceptCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2719.ConceptCouplingSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_ConceptCouplingAdvancedTimeSteppingAnalysisForModulation(self)
