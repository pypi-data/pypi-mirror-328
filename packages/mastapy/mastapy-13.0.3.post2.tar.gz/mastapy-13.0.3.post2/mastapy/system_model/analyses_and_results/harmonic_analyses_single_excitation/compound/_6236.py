"""MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6282,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2483
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6106,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6237,
        _6185,
        _6239,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation"
)


class MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation(
    _6282.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation
):
    """MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_harmonic_analysis_of_single_excitation(
            self: "MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6282.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6282.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6237.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6237,
            )

            return self._parent._cast(
                _6237.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6185.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6185,
            )

            return self._parent._cast(
                _6185.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6239.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6239,
            )

            return self._parent._cast(
                _6239.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def measurement_component_compound_harmonic_analysis_of_single_excitation(
            self: "MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
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
    ) -> "List[_6106.MeasurementComponentHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.MeasurementComponentHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6106.MeasurementComponentHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.MeasurementComponentHarmonicAnalysisOfSingleExcitation]

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
    ) -> "MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation":
        return (
            self._Cast_MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation(
                self
            )
        )
