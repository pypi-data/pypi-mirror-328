"""SynchroniserPartCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5926
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "SynchroniserPartCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5837
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _6001,
        _6003,
        _5964,
        _5912,
        _5966,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartCompoundHarmonicAnalysis")


class SynchroniserPartCompoundHarmonicAnalysis(
    _5926.CouplingHalfCompoundHarmonicAnalysis
):
    """SynchroniserPartCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartCompoundHarmonicAnalysis"
    )

    class _Cast_SynchroniserPartCompoundHarmonicAnalysis:
        """Special nested class for casting SynchroniserPartCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
            parent: "SynchroniserPartCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
        ) -> "_5926.CouplingHalfCompoundHarmonicAnalysis":
            return self._parent._cast(_5926.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
        ) -> "_5964.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5964,
            )

            return self._parent._cast(_5964.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
        ) -> "_5912.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(_5912.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
        ) -> "_5966.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_harmonic_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
        ) -> "_6001.SynchroniserHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6001,
            )

            return self._parent._cast(_6001.SynchroniserHalfCompoundHarmonicAnalysis)

        @property
        def synchroniser_sleeve_compound_harmonic_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
        ) -> "_6003.SynchroniserSleeveCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6003,
            )

            return self._parent._cast(_6003.SynchroniserSleeveCompoundHarmonicAnalysis)

        @property
        def synchroniser_part_compound_harmonic_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
        ) -> "SynchroniserPartCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserPartCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5837.SynchroniserPartHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.SynchroniserPartHarmonicAnalysis]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5837.SynchroniserPartHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.SynchroniserPartHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis":
        return self._Cast_SynchroniserPartCompoundHarmonicAnalysis(self)
