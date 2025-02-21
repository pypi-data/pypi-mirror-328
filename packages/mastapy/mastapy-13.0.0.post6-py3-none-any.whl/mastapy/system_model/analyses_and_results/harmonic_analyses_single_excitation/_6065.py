"""GearHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6086,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "GearHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2530
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6011,
        _6018,
        _6021,
        _6022,
        _6023,
        _6036,
        _6039,
        _6054,
        _6057,
        _6060,
        _6070,
        _6074,
        _6077,
        _6080,
        _6108,
        _6114,
        _6117,
        _6120,
        _6121,
        _6132,
        _6135,
        _6032,
        _6088,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("GearHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="GearHarmonicAnalysisOfSingleExcitation")


class GearHarmonicAnalysisOfSingleExcitation(
    _6086.MountableComponentHarmonicAnalysisOfSingleExcitation
):
    """GearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_GearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting GearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
            parent: "GearHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6086.MountableComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6086.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6032.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6032,
            )

            return self._parent._cast(_6032.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6088.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6088,
            )

            return self._parent._cast(_6088.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6011.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6011,
            )

            return self._parent._cast(
                _6011.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6018.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6018,
            )

            return self._parent._cast(
                _6018.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6021.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6021,
            )

            return self._parent._cast(
                _6021.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6022.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6022,
            )

            return self._parent._cast(
                _6022.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6023.BevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6023,
            )

            return self._parent._cast(_6023.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6036.ConceptGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6036,
            )

            return self._parent._cast(
                _6036.ConceptGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6039.ConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6039,
            )

            return self._parent._cast(
                _6039.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6054.CylindricalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6054,
            )

            return self._parent._cast(
                _6054.CylindricalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6057.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6057,
            )

            return self._parent._cast(
                _6057.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6060.FaceGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6060,
            )

            return self._parent._cast(_6060.FaceGearHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6070.HypoidGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6070,
            )

            return self._parent._cast(
                _6070.HypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6074.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6074,
            )

            return self._parent._cast(
                _6074.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6077.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6077,
            )

            return self._parent._cast(
                _6077.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6080.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6080,
            )

            return self._parent._cast(
                _6080.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6108.SpiralBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6108,
            )

            return self._parent._cast(
                _6108.SpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6114.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6114,
            )

            return self._parent._cast(
                _6114.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6117.StraightBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6117,
            )

            return self._parent._cast(
                _6117.StraightBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6120.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6120,
            )

            return self._parent._cast(
                _6120.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6121.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6121,
            )

            return self._parent._cast(
                _6121.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6132.WormGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6132,
            )

            return self._parent._cast(_6132.WormGearHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6135.ZerolBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6135,
            )

            return self._parent._cast(
                _6135.ZerolBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "GearHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "GearHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2530.Gear":
        """mastapy.system_model.part_model.gears.Gear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation":
        return self._Cast_GearHarmonicAnalysisOfSingleExcitation(self)
