"""StraightBevelGearCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5894
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "StraightBevelGearCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2547
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5821
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5882,
        _5910,
        _5936,
        _5955,
        _5903,
        _5957,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelGearCompoundHarmonicAnalysis")


class StraightBevelGearCompoundHarmonicAnalysis(
    _5894.BevelGearCompoundHarmonicAnalysis
):
    """StraightBevelGearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearCompoundHarmonicAnalysis"
    )

    class _Cast_StraightBevelGearCompoundHarmonicAnalysis:
        """Special nested class for casting StraightBevelGearCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelGearCompoundHarmonicAnalysis._Cast_StraightBevelGearCompoundHarmonicAnalysis",
            parent: "StraightBevelGearCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_harmonic_analysis(
            self: "StraightBevelGearCompoundHarmonicAnalysis._Cast_StraightBevelGearCompoundHarmonicAnalysis",
        ) -> "_5894.BevelGearCompoundHarmonicAnalysis":
            return self._parent._cast(_5894.BevelGearCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(
            self: "StraightBevelGearCompoundHarmonicAnalysis._Cast_StraightBevelGearCompoundHarmonicAnalysis",
        ) -> "_5882.AGMAGleasonConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5882,
            )

            return self._parent._cast(
                _5882.AGMAGleasonConicalGearCompoundHarmonicAnalysis
            )

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "StraightBevelGearCompoundHarmonicAnalysis._Cast_StraightBevelGearCompoundHarmonicAnalysis",
        ) -> "_5910.ConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5910,
            )

            return self._parent._cast(_5910.ConicalGearCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "StraightBevelGearCompoundHarmonicAnalysis._Cast_StraightBevelGearCompoundHarmonicAnalysis",
        ) -> "_5936.GearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5936,
            )

            return self._parent._cast(_5936.GearCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "StraightBevelGearCompoundHarmonicAnalysis._Cast_StraightBevelGearCompoundHarmonicAnalysis",
        ) -> "_5955.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5955,
            )

            return self._parent._cast(_5955.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "StraightBevelGearCompoundHarmonicAnalysis._Cast_StraightBevelGearCompoundHarmonicAnalysis",
        ) -> "_5903.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5903,
            )

            return self._parent._cast(_5903.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "StraightBevelGearCompoundHarmonicAnalysis._Cast_StraightBevelGearCompoundHarmonicAnalysis",
        ) -> "_5957.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5957,
            )

            return self._parent._cast(_5957.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelGearCompoundHarmonicAnalysis._Cast_StraightBevelGearCompoundHarmonicAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearCompoundHarmonicAnalysis._Cast_StraightBevelGearCompoundHarmonicAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearCompoundHarmonicAnalysis._Cast_StraightBevelGearCompoundHarmonicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_compound_harmonic_analysis(
            self: "StraightBevelGearCompoundHarmonicAnalysis._Cast_StraightBevelGearCompoundHarmonicAnalysis",
        ) -> "StraightBevelGearCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearCompoundHarmonicAnalysis._Cast_StraightBevelGearCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelGearCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2547.StraightBevelGear":
        """mastapy.system_model.part_model.gears.StraightBevelGear

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
    ) -> "List[_5821.StraightBevelGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelGearHarmonicAnalysis]

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
    ) -> "List[_5821.StraightBevelGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelGearHarmonicAnalysis]

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
    ) -> "StraightBevelGearCompoundHarmonicAnalysis._Cast_StraightBevelGearCompoundHarmonicAnalysis":
        return self._Cast_StraightBevelGearCompoundHarmonicAnalysis(self)
