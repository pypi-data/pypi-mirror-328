"""ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6176,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6036,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6237,
        _6139,
        _6218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation"
)


class ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation(
    _6176.CouplingCompoundHarmonicAnalysisOfSingleExcitation
):
    """ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coupling_compound_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6176.CouplingCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6176.CouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6237.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6237,
            )

            return self._parent._cast(
                _6237.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6139.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6139,
            )

            return self._parent._cast(
                _6139.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6218.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6218,
            )

            return self._parent._cast(
                _6218.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
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
    ) -> "List[_6036.ConceptCouplingHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ConceptCouplingHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6036.ConceptCouplingHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ConceptCouplingHarmonicAnalysisOfSingleExcitation]

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
    ) -> "ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
