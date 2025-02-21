"""ConceptCouplingHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6068,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "ConceptCouplingHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2601
    from mastapy.system_model.analyses_and_results.static_loads import _6862
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6129,
        _6029,
        _6110,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="ConceptCouplingHarmonicAnalysisOfSingleExcitation")


class ConceptCouplingHarmonicAnalysisOfSingleExcitation(
    _6068.CouplingHarmonicAnalysisOfSingleExcitation
):
    """ConceptCouplingHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_ConceptCouplingHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ConceptCouplingHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ConceptCouplingHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHarmonicAnalysisOfSingleExcitation",
            parent: "ConceptCouplingHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coupling_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "_6068.CouplingHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6068.CouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "_6129.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6129,
            )

            return self._parent._cast(
                _6129.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "_6029.AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6029,
            )

            return self._parent._cast(
                _6029.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "_6110.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6110,
            )

            return self._parent._cast(_6110.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def concept_coupling_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "ConceptCouplingHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ConceptCouplingHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2601.ConceptCoupling":
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
    def assembly_load_case(self: Self) -> "_6862.ConceptCouplingLoadCase":
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
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ConceptCouplingHarmonicAnalysisOfSingleExcitation(self)
