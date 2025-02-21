"""MeasurementComponentCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _6022
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "MeasurementComponentCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2483
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5806
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5977,
        _5925,
        _5979,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="MeasurementComponentCompoundHarmonicAnalysis")


class MeasurementComponentCompoundHarmonicAnalysis(
    _6022.VirtualComponentCompoundHarmonicAnalysis
):
    """MeasurementComponentCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MeasurementComponentCompoundHarmonicAnalysis"
    )

    class _Cast_MeasurementComponentCompoundHarmonicAnalysis:
        """Special nested class for casting MeasurementComponentCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "MeasurementComponentCompoundHarmonicAnalysis._Cast_MeasurementComponentCompoundHarmonicAnalysis",
            parent: "MeasurementComponentCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_harmonic_analysis(
            self: "MeasurementComponentCompoundHarmonicAnalysis._Cast_MeasurementComponentCompoundHarmonicAnalysis",
        ) -> "_6022.VirtualComponentCompoundHarmonicAnalysis":
            return self._parent._cast(_6022.VirtualComponentCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "MeasurementComponentCompoundHarmonicAnalysis._Cast_MeasurementComponentCompoundHarmonicAnalysis",
        ) -> "_5977.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5977,
            )

            return self._parent._cast(_5977.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "MeasurementComponentCompoundHarmonicAnalysis._Cast_MeasurementComponentCompoundHarmonicAnalysis",
        ) -> "_5925.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5925,
            )

            return self._parent._cast(_5925.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "MeasurementComponentCompoundHarmonicAnalysis._Cast_MeasurementComponentCompoundHarmonicAnalysis",
        ) -> "_5979.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(_5979.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "MeasurementComponentCompoundHarmonicAnalysis._Cast_MeasurementComponentCompoundHarmonicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MeasurementComponentCompoundHarmonicAnalysis._Cast_MeasurementComponentCompoundHarmonicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentCompoundHarmonicAnalysis._Cast_MeasurementComponentCompoundHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def measurement_component_compound_harmonic_analysis(
            self: "MeasurementComponentCompoundHarmonicAnalysis._Cast_MeasurementComponentCompoundHarmonicAnalysis",
        ) -> "MeasurementComponentCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentCompoundHarmonicAnalysis._Cast_MeasurementComponentCompoundHarmonicAnalysis",
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
        instance_to_wrap: "MeasurementComponentCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2483.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

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
    ) -> "List[_5806.MeasurementComponentHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.MeasurementComponentHarmonicAnalysis]

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
    ) -> "List[_5806.MeasurementComponentHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.MeasurementComponentHarmonicAnalysis]

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
    ) -> "MeasurementComponentCompoundHarmonicAnalysis._Cast_MeasurementComponentCompoundHarmonicAnalysis":
        return self._Cast_MeasurementComponentCompoundHarmonicAnalysis(self)
