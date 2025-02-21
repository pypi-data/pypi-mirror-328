"""BoltCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6163,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "BoltCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2442
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6027,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6217,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("BoltCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="BoltCompoundHarmonicAnalysisOfSingleExcitation")


class BoltCompoundHarmonicAnalysisOfSingleExcitation(
    _6163.ComponentCompoundHarmonicAnalysisOfSingleExcitation
):
    """BoltCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BOLT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BoltCompoundHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_BoltCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting BoltCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "BoltCompoundHarmonicAnalysisOfSingleExcitation._Cast_BoltCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "BoltCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "BoltCompoundHarmonicAnalysisOfSingleExcitation._Cast_BoltCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6163.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6163.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "BoltCompoundHarmonicAnalysisOfSingleExcitation._Cast_BoltCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6217.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6217,
            )

            return self._parent._cast(
                _6217.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "BoltCompoundHarmonicAnalysisOfSingleExcitation._Cast_BoltCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BoltCompoundHarmonicAnalysisOfSingleExcitation._Cast_BoltCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltCompoundHarmonicAnalysisOfSingleExcitation._Cast_BoltCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bolt_compound_harmonic_analysis_of_single_excitation(
            self: "BoltCompoundHarmonicAnalysisOfSingleExcitation._Cast_BoltCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "BoltCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "BoltCompoundHarmonicAnalysisOfSingleExcitation._Cast_BoltCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "BoltCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2442.Bolt":
        """mastapy.system_model.part_model.Bolt

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
    ) -> "List[_6027.BoltHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.BoltHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6027.BoltHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.BoltHarmonicAnalysisOfSingleExcitation]

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
    ) -> "BoltCompoundHarmonicAnalysisOfSingleExcitation._Cast_BoltCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_BoltCompoundHarmonicAnalysisOfSingleExcitation(self)
