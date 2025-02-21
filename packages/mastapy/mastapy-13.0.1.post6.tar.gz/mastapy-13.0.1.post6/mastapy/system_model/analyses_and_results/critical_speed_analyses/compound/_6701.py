"""ConceptCouplingCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6712,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "ConceptCouplingCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6570
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6773,
        _6675,
        _6754,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingCompoundCriticalSpeedAnalysis")


class ConceptCouplingCompoundCriticalSpeedAnalysis(
    _6712.CouplingCompoundCriticalSpeedAnalysis
):
    """ConceptCouplingCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingCompoundCriticalSpeedAnalysis"
    )

    class _Cast_ConceptCouplingCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ConceptCouplingCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingCompoundCriticalSpeedAnalysis",
            parent: "ConceptCouplingCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_compound_critical_speed_analysis(
            self: "ConceptCouplingCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingCompoundCriticalSpeedAnalysis",
        ) -> "_6712.CouplingCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6712.CouplingCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "ConceptCouplingCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingCompoundCriticalSpeedAnalysis",
        ) -> "_6773.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6773,
            )

            return self._parent._cast(
                _6773.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "ConceptCouplingCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingCompoundCriticalSpeedAnalysis",
        ) -> "_6675.AbstractAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6675,
            )

            return self._parent._cast(
                _6675.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "ConceptCouplingCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingCompoundCriticalSpeedAnalysis",
        ) -> "_6754.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6754,
            )

            return self._parent._cast(_6754.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "ConceptCouplingCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingCompoundCriticalSpeedAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingCompoundCriticalSpeedAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingCompoundCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_coupling_compound_critical_speed_analysis(
            self: "ConceptCouplingCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingCompoundCriticalSpeedAnalysis",
        ) -> "ConceptCouplingCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "ConceptCouplingCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2581.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6570.ConceptCouplingCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConceptCouplingCriticalSpeedAnalysis]

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
    ) -> "List[_6570.ConceptCouplingCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConceptCouplingCriticalSpeedAnalysis]

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
    ) -> "ConceptCouplingCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingCompoundCriticalSpeedAnalysis":
        return self._Cast_ConceptCouplingCompoundCriticalSpeedAnalysis(self)
