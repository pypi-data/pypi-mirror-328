"""AbstractShaftCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5881
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "AbstractShaftCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5680
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5924,
        _5974,
        _5904,
        _5958,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftCompoundHarmonicAnalysis")


class AbstractShaftCompoundHarmonicAnalysis(
    _5881.AbstractShaftOrHousingCompoundHarmonicAnalysis
):
    """AbstractShaftCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftCompoundHarmonicAnalysis"
    )

    class _Cast_AbstractShaftCompoundHarmonicAnalysis:
        """Special nested class for casting AbstractShaftCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
            parent: "AbstractShaftCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
        ) -> "_5881.AbstractShaftOrHousingCompoundHarmonicAnalysis":
            return self._parent._cast(
                _5881.AbstractShaftOrHousingCompoundHarmonicAnalysis
            )

        @property
        def component_compound_harmonic_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
        ) -> "_5904.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5904,
            )

            return self._parent._cast(_5904.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
        ) -> "_5958.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_harmonic_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
        ) -> "_5924.CycloidalDiscCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5924,
            )

            return self._parent._cast(_5924.CycloidalDiscCompoundHarmonicAnalysis)

        @property
        def shaft_compound_harmonic_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
        ) -> "_5974.ShaftCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5974,
            )

            return self._parent._cast(_5974.ShaftCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_compound_harmonic_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
        ) -> "AbstractShaftCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5680.AbstractShaftHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractShaftHarmonicAnalysis]

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
    ) -> "List[_5680.AbstractShaftHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractShaftHarmonicAnalysis]

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
    ) -> "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis":
        return self._Cast_AbstractShaftCompoundHarmonicAnalysis(self)
