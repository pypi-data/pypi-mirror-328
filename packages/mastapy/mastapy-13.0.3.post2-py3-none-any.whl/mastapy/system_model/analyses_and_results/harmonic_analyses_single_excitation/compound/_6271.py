"""StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6265,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6142,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6176,
        _6164,
        _6192,
        _6218,
        _6237,
        _6185,
        _6239,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation"
)


class StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation(
    _6265.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation
):
    """StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6265.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6265.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6176.BevelGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6176,
            )

            return self._parent._cast(
                _6176.BevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6164.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6164,
            )

            return self._parent._cast(
                _6164.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6192.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6192,
            )

            return self._parent._cast(
                _6192.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6218.GearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6218,
            )

            return self._parent._cast(
                _6218.GearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6237.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6237,
            )

            return self._parent._cast(
                _6237.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6185.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6185,
            )

            return self._parent._cast(
                _6185.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6239.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6239,
            )

            return self._parent._cast(
                _6239.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6142.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6142.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation]

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
    ) -> "StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
