"""ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6178,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2582
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6035,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6216,
        _6164,
        _6218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation"
)


class ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation(
    _6178.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
):
    """ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6178.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6178.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6216.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6216,
            )

            return self._parent._cast(
                _6216.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6164.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6164,
            )

            return self._parent._cast(
                _6164.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6218.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6218,
            )

            return self._parent._cast(
                _6218.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2582.ConceptCouplingHalf":
        """mastapy.system_model.part_model.couplings.ConceptCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6035.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6035.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation]

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
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
