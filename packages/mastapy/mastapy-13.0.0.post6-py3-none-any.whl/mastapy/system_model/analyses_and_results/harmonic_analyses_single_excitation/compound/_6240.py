"""SpringDamperCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6175,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "SpringDamperCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2600
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6113,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6236,
        _6138,
        _6217,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="SpringDamperCompoundHarmonicAnalysisOfSingleExcitation")


class SpringDamperCompoundHarmonicAnalysisOfSingleExcitation(
    _6175.CouplingCompoundHarmonicAnalysisOfSingleExcitation
):
    """SpringDamperCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpringDamperCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_SpringDamperCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting SpringDamperCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "SpringDamperCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "SpringDamperCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coupling_compound_harmonic_analysis_of_single_excitation(
            self: "SpringDamperCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6175.CouplingCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6175.CouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "SpringDamperCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6236.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6236,
            )

            return self._parent._cast(
                _6236.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "SpringDamperCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6138.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6138,
            )

            return self._parent._cast(
                _6138.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "SpringDamperCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6217.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6217,
            )

            return self._parent._cast(
                _6217.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "SpringDamperCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spring_damper_compound_harmonic_analysis_of_single_excitation(
            self: "SpringDamperCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "SpringDamperCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "SpringDamperCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "SpringDamperCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2600.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2600.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

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
    ) -> "List[_6113.SpringDamperHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.SpringDamperHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6113.SpringDamperHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.SpringDamperHarmonicAnalysisOfSingleExcitation]

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
    ) -> "SpringDamperCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_SpringDamperCompoundHarmonicAnalysisOfSingleExcitation(self)
