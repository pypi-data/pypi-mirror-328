"""GearCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5956
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "GearCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5753
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5883,
        _5890,
        _5893,
        _5894,
        _5895,
        _5908,
        _5911,
        _5926,
        _5929,
        _5932,
        _5941,
        _5945,
        _5948,
        _5951,
        _5978,
        _5984,
        _5987,
        _5990,
        _5991,
        _6002,
        _6005,
        _5904,
        _5958,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="GearCompoundHarmonicAnalysis")


class GearCompoundHarmonicAnalysis(_5956.MountableComponentCompoundHarmonicAnalysis):
    """GearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearCompoundHarmonicAnalysis")

    class _Cast_GearCompoundHarmonicAnalysis:
        """Special nested class for casting GearCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
            parent: "GearCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5956.MountableComponentCompoundHarmonicAnalysis":
            return self._parent._cast(_5956.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5904.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5904,
            )

            return self._parent._cast(_5904.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5958.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5883.AGMAGleasonConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5883,
            )

            return self._parent._cast(
                _5883.AGMAGleasonConicalGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5890.BevelDifferentialGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5890,
            )

            return self._parent._cast(
                _5890.BevelDifferentialGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5893.BevelDifferentialPlanetGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5893,
            )

            return self._parent._cast(
                _5893.BevelDifferentialPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5894.BevelDifferentialSunGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5894,
            )

            return self._parent._cast(
                _5894.BevelDifferentialSunGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5895.BevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5895,
            )

            return self._parent._cast(_5895.BevelGearCompoundHarmonicAnalysis)

        @property
        def concept_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5908.ConceptGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5908,
            )

            return self._parent._cast(_5908.ConceptGearCompoundHarmonicAnalysis)

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5911.ConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5911,
            )

            return self._parent._cast(_5911.ConicalGearCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5926.CylindricalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5926,
            )

            return self._parent._cast(_5926.CylindricalGearCompoundHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5929.CylindricalPlanetGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5929,
            )

            return self._parent._cast(
                _5929.CylindricalPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def face_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5932.FaceGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5932,
            )

            return self._parent._cast(_5932.FaceGearCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5941.HypoidGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5941,
            )

            return self._parent._cast(_5941.HypoidGearCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5945.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5945,
            )

            return self._parent._cast(
                _5945.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5948.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5948,
            )

            return self._parent._cast(
                _5948.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5951.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5951,
            )

            return self._parent._cast(
                _5951.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5978.SpiralBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5978,
            )

            return self._parent._cast(_5978.SpiralBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5984.StraightBevelDiffGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5984,
            )

            return self._parent._cast(
                _5984.StraightBevelDiffGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5987.StraightBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5987,
            )

            return self._parent._cast(_5987.StraightBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5990.StraightBevelPlanetGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5990,
            )

            return self._parent._cast(
                _5990.StraightBevelPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_5991.StraightBevelSunGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5991,
            )

            return self._parent._cast(
                _5991.StraightBevelSunGearCompoundHarmonicAnalysis
            )

        @property
        def worm_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_6002.WormGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6002,
            )

            return self._parent._cast(_6002.WormGearCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "_6005.ZerolBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6005,
            )

            return self._parent._cast(_6005.ZerolBevelGearCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
        ) -> "GearCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearCompoundHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_5753.GearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.GearHarmonicAnalysis]

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
    ) -> "List[_5753.GearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.GearHarmonicAnalysis]

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
    ) -> "GearCompoundHarmonicAnalysis._Cast_GearCompoundHarmonicAnalysis":
        return self._Cast_GearCompoundHarmonicAnalysis(self)
