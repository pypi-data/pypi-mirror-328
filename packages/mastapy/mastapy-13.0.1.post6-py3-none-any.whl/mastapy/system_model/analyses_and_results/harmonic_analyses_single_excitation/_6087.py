"""MountableComponentHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6033,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "MountableComponentHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2464
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6012,
        _6016,
        _6019,
        _6022,
        _6023,
        _6024,
        _6030,
        _6035,
        _6037,
        _6040,
        _6044,
        _6046,
        _6050,
        _6055,
        _6058,
        _6061,
        _6066,
        _6071,
        _6075,
        _6078,
        _6081,
        _6084,
        _6085,
        _6088,
        _6091,
        _6095,
        _6096,
        _6097,
        _6098,
        _6099,
        _6103,
        _6106,
        _6109,
        _6113,
        _6115,
        _6118,
        _6121,
        _6122,
        _6123,
        _6125,
        _6126,
        _6129,
        _6130,
        _6131,
        _6132,
        _6133,
        _6136,
        _6089,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="MountableComponentHarmonicAnalysisOfSingleExcitation")


class MountableComponentHarmonicAnalysisOfSingleExcitation(
    _6033.ComponentHarmonicAnalysisOfSingleExcitation
):
    """MountableComponentHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_MountableComponentHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting MountableComponentHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
            parent: "MountableComponentHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6033.ComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6033.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6089.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(_6089.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6012.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6012,
            )

            return self._parent._cast(
                _6012.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bearing_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6016.BearingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6016,
            )

            return self._parent._cast(_6016.BearingHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6019.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6019,
            )

            return self._parent._cast(
                _6019.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6022.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6022,
            )

            return self._parent._cast(
                _6022.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6023.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6023,
            )

            return self._parent._cast(
                _6023.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6024.BevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6024,
            )

            return self._parent._cast(_6024.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_half_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6030.ClutchHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6030,
            )

            return self._parent._cast(
                _6030.ClutchHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_half_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6035.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6035,
            )

            return self._parent._cast(
                _6035.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6037.ConceptGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6037,
            )

            return self._parent._cast(
                _6037.ConceptGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6040.ConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6040,
            )

            return self._parent._cast(
                _6040.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connector_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6044.ConnectorHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6044,
            )

            return self._parent._cast(_6044.ConnectorHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6046.CouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6046,
            )

            return self._parent._cast(
                _6046.CouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_pulley_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6050.CVTPulleyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6050,
            )

            return self._parent._cast(_6050.CVTPulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6055.CylindricalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6055,
            )

            return self._parent._cast(
                _6055.CylindricalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6058.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6058,
            )

            return self._parent._cast(
                _6058.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6061.FaceGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6061,
            )

            return self._parent._cast(_6061.FaceGearHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6066.GearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6066,
            )

            return self._parent._cast(_6066.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6071.HypoidGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6071,
            )

            return self._parent._cast(
                _6071.HypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6075.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6075,
            )

            return self._parent._cast(
                _6075.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6078.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6078,
            )

            return self._parent._cast(
                _6078.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6081.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6081,
            )

            return self._parent._cast(
                _6081.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mass_disc_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6084.MassDiscHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6084,
            )

            return self._parent._cast(_6084.MassDiscHarmonicAnalysisOfSingleExcitation)

        @property
        def measurement_component_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6085.MeasurementComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(
                _6085.MeasurementComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def oil_seal_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6088.OilSealHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6088,
            )

            return self._parent._cast(_6088.OilSealHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6091.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(
                _6091.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planet_carrier_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6095.PlanetCarrierHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6095,
            )

            return self._parent._cast(
                _6095.PlanetCarrierHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6096.PointLoadHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6096,
            )

            return self._parent._cast(_6096.PointLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def power_load_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6097.PowerLoadHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(_6097.PowerLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def pulley_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6098.PulleyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6098,
            )

            return self._parent._cast(_6098.PulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6099.RingPinsHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6099,
            )

            return self._parent._cast(_6099.RingPinsHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6103.RollingRingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6103,
            )

            return self._parent._cast(
                _6103.RollingRingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_hub_connection_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6106.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6106,
            )

            return self._parent._cast(
                _6106.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6109.SpiralBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6109,
            )

            return self._parent._cast(
                _6109.SpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6113.SpringDamperHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6113,
            )

            return self._parent._cast(
                _6113.SpringDamperHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6115.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(
                _6115.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6118.StraightBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6118,
            )

            return self._parent._cast(
                _6118.StraightBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6121.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6121,
            )

            return self._parent._cast(
                _6121.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6122.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6122,
            )

            return self._parent._cast(
                _6122.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6123.SynchroniserHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6123,
            )

            return self._parent._cast(
                _6123.SynchroniserHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6125.SynchroniserPartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6125,
            )

            return self._parent._cast(
                _6125.SynchroniserPartHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6126.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6126,
            )

            return self._parent._cast(
                _6126.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6129.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6129,
            )

            return self._parent._cast(
                _6129.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6130.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6130,
            )

            return self._parent._cast(
                _6130.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation
            )

        @property
        def unbalanced_mass_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6131.UnbalancedMassHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6131,
            )

            return self._parent._cast(
                _6131.UnbalancedMassHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6132.VirtualComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6132,
            )

            return self._parent._cast(
                _6132.VirtualComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6133.WormGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6133,
            )

            return self._parent._cast(_6133.WormGearHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6136.ZerolBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6136,
            )

            return self._parent._cast(
                _6136.ZerolBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "MountableComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "MountableComponentHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2464.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

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
    ) -> "MountableComponentHarmonicAnalysisOfSingleExcitation._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation":
        return self._Cast_MountableComponentHarmonicAnalysisOfSingleExcitation(self)
