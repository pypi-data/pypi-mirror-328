"""FaceGearCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6196,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "FaceGearCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2528
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6060,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6215,
        _6163,
        _6217,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="FaceGearCompoundHarmonicAnalysisOfSingleExcitation")


class FaceGearCompoundHarmonicAnalysisOfSingleExcitation(
    _6196.GearCompoundHarmonicAnalysisOfSingleExcitation
):
    """FaceGearCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearCompoundHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_FaceGearCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting FaceGearCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "FaceGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_FaceGearCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "FaceGearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def gear_compound_harmonic_analysis_of_single_excitation(
            self: "FaceGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_FaceGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6196.GearCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6196.GearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "FaceGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_FaceGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6215.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6215,
            )

            return self._parent._cast(
                _6215.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "FaceGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_FaceGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6163.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6163,
            )

            return self._parent._cast(
                _6163.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "FaceGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_FaceGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6217.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6217,
            )

            return self._parent._cast(
                _6217.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "FaceGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_FaceGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FaceGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_FaceGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_FaceGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def face_gear_compound_harmonic_analysis_of_single_excitation(
            self: "FaceGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_FaceGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "FaceGearCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "FaceGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_FaceGearCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "FaceGearCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2528.FaceGear":
        """mastapy.system_model.part_model.gears.FaceGear

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
    ) -> "List[_6060.FaceGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.FaceGearHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6060.FaceGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.FaceGearHarmonicAnalysisOfSingleExcitation]

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
    ) -> "FaceGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_FaceGearCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_FaceGearCompoundHarmonicAnalysisOfSingleExcitation(self)
