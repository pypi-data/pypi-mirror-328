"""SynchroniserHalfCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5994
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "SynchroniserHalfCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2604
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5827
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5918,
        _5956,
        _5904,
        _5958,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="SynchroniserHalfCompoundHarmonicAnalysis")


class SynchroniserHalfCompoundHarmonicAnalysis(
    _5994.SynchroniserPartCompoundHarmonicAnalysis
):
    """SynchroniserHalfCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserHalfCompoundHarmonicAnalysis"
    )

    class _Cast_SynchroniserHalfCompoundHarmonicAnalysis:
        """Special nested class for casting SynchroniserHalfCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserHalfCompoundHarmonicAnalysis._Cast_SynchroniserHalfCompoundHarmonicAnalysis",
            parent: "SynchroniserHalfCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_harmonic_analysis(
            self: "SynchroniserHalfCompoundHarmonicAnalysis._Cast_SynchroniserHalfCompoundHarmonicAnalysis",
        ) -> "_5994.SynchroniserPartCompoundHarmonicAnalysis":
            return self._parent._cast(_5994.SynchroniserPartCompoundHarmonicAnalysis)

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "SynchroniserHalfCompoundHarmonicAnalysis._Cast_SynchroniserHalfCompoundHarmonicAnalysis",
        ) -> "_5918.CouplingHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5918,
            )

            return self._parent._cast(_5918.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "SynchroniserHalfCompoundHarmonicAnalysis._Cast_SynchroniserHalfCompoundHarmonicAnalysis",
        ) -> "_5956.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5956,
            )

            return self._parent._cast(_5956.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "SynchroniserHalfCompoundHarmonicAnalysis._Cast_SynchroniserHalfCompoundHarmonicAnalysis",
        ) -> "_5904.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5904,
            )

            return self._parent._cast(_5904.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "SynchroniserHalfCompoundHarmonicAnalysis._Cast_SynchroniserHalfCompoundHarmonicAnalysis",
        ) -> "_5958.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserHalfCompoundHarmonicAnalysis._Cast_SynchroniserHalfCompoundHarmonicAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserHalfCompoundHarmonicAnalysis._Cast_SynchroniserHalfCompoundHarmonicAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfCompoundHarmonicAnalysis._Cast_SynchroniserHalfCompoundHarmonicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_harmonic_analysis(
            self: "SynchroniserHalfCompoundHarmonicAnalysis._Cast_SynchroniserHalfCompoundHarmonicAnalysis",
        ) -> "SynchroniserHalfCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfCompoundHarmonicAnalysis._Cast_SynchroniserHalfCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserHalfCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2604.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

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
    ) -> "List[_5827.SynchroniserHalfHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.SynchroniserHalfHarmonicAnalysis]

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
    ) -> "List[_5827.SynchroniserHalfHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.SynchroniserHalfHarmonicAnalysis]

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
    ) -> "SynchroniserHalfCompoundHarmonicAnalysis._Cast_SynchroniserHalfCompoundHarmonicAnalysis":
        return self._Cast_SynchroniserHalfCompoundHarmonicAnalysis(self)
