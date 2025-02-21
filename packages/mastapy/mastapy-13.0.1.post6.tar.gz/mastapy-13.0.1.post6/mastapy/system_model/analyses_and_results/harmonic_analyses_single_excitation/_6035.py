"""ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6046,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2582
    from mastapy.system_model.analyses_and_results.static_loads import _6840
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6087,
        _6033,
        _6089,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation")


class ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation(
    _6046.CouplingHalfHarmonicAnalysisOfSingleExcitation
):
    """ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
            parent: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6046.CouplingHalfHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6046.CouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6087.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6087,
            )

            return self._parent._cast(
                _6087.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6033.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6033,
            )

            return self._parent._cast(_6033.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6089.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(_6089.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation.TYPE",
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
    def component_load_case(self: Self) -> "_6840.ConceptCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation(self)
