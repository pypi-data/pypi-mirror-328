"""BearingCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5936
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "BearingCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2459
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5708
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5977,
        _5925,
        _5979,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BearingCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="BearingCompoundHarmonicAnalysis")


class BearingCompoundHarmonicAnalysis(_5936.ConnectorCompoundHarmonicAnalysis):
    """BearingCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEARING_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingCompoundHarmonicAnalysis")

    class _Cast_BearingCompoundHarmonicAnalysis:
        """Special nested class for casting BearingCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BearingCompoundHarmonicAnalysis._Cast_BearingCompoundHarmonicAnalysis",
            parent: "BearingCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def connector_compound_harmonic_analysis(
            self: "BearingCompoundHarmonicAnalysis._Cast_BearingCompoundHarmonicAnalysis",
        ) -> "_5936.ConnectorCompoundHarmonicAnalysis":
            return self._parent._cast(_5936.ConnectorCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "BearingCompoundHarmonicAnalysis._Cast_BearingCompoundHarmonicAnalysis",
        ) -> "_5977.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5977,
            )

            return self._parent._cast(_5977.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "BearingCompoundHarmonicAnalysis._Cast_BearingCompoundHarmonicAnalysis",
        ) -> "_5925.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5925,
            )

            return self._parent._cast(_5925.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "BearingCompoundHarmonicAnalysis._Cast_BearingCompoundHarmonicAnalysis",
        ) -> "_5979.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(_5979.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "BearingCompoundHarmonicAnalysis._Cast_BearingCompoundHarmonicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BearingCompoundHarmonicAnalysis._Cast_BearingCompoundHarmonicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BearingCompoundHarmonicAnalysis._Cast_BearingCompoundHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bearing_compound_harmonic_analysis(
            self: "BearingCompoundHarmonicAnalysis._Cast_BearingCompoundHarmonicAnalysis",
        ) -> "BearingCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BearingCompoundHarmonicAnalysis._Cast_BearingCompoundHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingCompoundHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2459.Bearing":
        """mastapy.system_model.part_model.Bearing

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
    ) -> "List[_5708.BearingHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BearingHarmonicAnalysis]

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
    def planetaries(self: Self) -> "List[BearingCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.BearingCompoundHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(self: Self) -> "List[_5708.BearingHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BearingHarmonicAnalysis]

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
    ) -> "BearingCompoundHarmonicAnalysis._Cast_BearingCompoundHarmonicAnalysis":
        return self._Cast_BearingCompoundHarmonicAnalysis(self)
