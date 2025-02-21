"""MountableComponentAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7044,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "MountableComponentAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.system_deflections import _2790
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7022,
        _7027,
        _7030,
        _7033,
        _7034,
        _7035,
        _7042,
        _7047,
        _7048,
        _7051,
        _7055,
        _7058,
        _7061,
        _7066,
        _7069,
        _7072,
        _7077,
        _7082,
        _7086,
        _7089,
        _7092,
        _7095,
        _7096,
        _7098,
        _7102,
        _7105,
        _7106,
        _7107,
        _7108,
        _7109,
        _7111,
        _7116,
        _7119,
        _7124,
        _7125,
        _7128,
        _7131,
        _7132,
        _7134,
        _7135,
        _7136,
        _7139,
        _7140,
        _7141,
        _7142,
        _7143,
        _7146,
        _7099,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="MountableComponentAdvancedTimeSteppingAnalysisForModulation"
)


class MountableComponentAdvancedTimeSteppingAnalysisForModulation(
    _7044.ComponentAdvancedTimeSteppingAnalysisForModulation
):
    """MountableComponentAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting MountableComponentAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
            parent: "MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7044.ComponentAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7044.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7099.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7099,
            )

            return self._parent._cast(
                _7099.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7022.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7022,
            )

            return self._parent._cast(
                _7022.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bearing_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7027.BearingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7027,
            )

            return self._parent._cast(
                _7027.BearingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7030.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7030,
            )

            return self._parent._cast(
                _7030.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7033.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7033,
            )

            return self._parent._cast(
                _7033.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7034.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7034,
            )

            return self._parent._cast(
                _7034.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7035.BevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7035,
            )

            return self._parent._cast(
                _7035.BevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7042.ClutchHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7042,
            )

            return self._parent._cast(
                _7042.ClutchHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7047.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7047,
            )

            return self._parent._cast(
                _7047.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7048.ConceptGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7048,
            )

            return self._parent._cast(
                _7048.ConceptGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7051.ConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7051,
            )

            return self._parent._cast(
                _7051.ConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connector_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7055.ConnectorAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7055,
            )

            return self._parent._cast(
                _7055.ConnectorAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7058.CouplingHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7058,
            )

            return self._parent._cast(
                _7058.CouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_pulley_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7061.CVTPulleyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7061,
            )

            return self._parent._cast(
                _7061.CVTPulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7066.CylindricalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7066,
            )

            return self._parent._cast(
                _7066.CylindricalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7069.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7069,
            )

            return self._parent._cast(
                _7069.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7072.FaceGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7072,
            )

            return self._parent._cast(
                _7072.FaceGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7077.GearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7077,
            )

            return self._parent._cast(
                _7077.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7082.HypoidGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7082,
            )

            return self._parent._cast(
                _7082.HypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7086.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7086,
            )

            return self._parent._cast(
                _7086.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7089.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7089,
            )

            return self._parent._cast(
                _7089.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7092.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7092,
            )

            return self._parent._cast(
                _7092.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mass_disc_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7095.MassDiscAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7095,
            )

            return self._parent._cast(
                _7095.MassDiscAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def measurement_component_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7096.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7096,
            )

            return self._parent._cast(
                _7096.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def oil_seal_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7098.OilSealAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7098,
            )

            return self._parent._cast(
                _7098.OilSealAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7102.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7102,
            )

            return self._parent._cast(
                _7102.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planet_carrier_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7105.PlanetCarrierAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7105,
            )

            return self._parent._cast(
                _7105.PlanetCarrierAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def point_load_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7106.PointLoadAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7106,
            )

            return self._parent._cast(
                _7106.PointLoadAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def power_load_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7107.PowerLoadAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7107,
            )

            return self._parent._cast(
                _7107.PowerLoadAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def pulley_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7108.PulleyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7108,
            )

            return self._parent._cast(
                _7108.PulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7109.RingPinsAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7109,
            )

            return self._parent._cast(
                _7109.RingPinsAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7111.RollingRingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7111,
            )

            return self._parent._cast(
                _7111.RollingRingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_hub_connection_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7116.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7116,
            )

            return self._parent._cast(
                _7116.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7119.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7119,
            )

            return self._parent._cast(
                _7119.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7124.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7124,
            )

            return self._parent._cast(
                _7124.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7125.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7125,
            )

            return self._parent._cast(
                _7125.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7128.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7128,
            )

            return self._parent._cast(
                _7128.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7131.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7131,
            )

            return self._parent._cast(
                _7131.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7132.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7132,
            )

            return self._parent._cast(
                _7132.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7134.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7134,
            )

            return self._parent._cast(
                _7134.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_part_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7135.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7135,
            )

            return self._parent._cast(
                _7135.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_sleeve_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7136.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7136,
            )

            return self._parent._cast(
                _7136.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_pump_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7139.TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7139,
            )

            return self._parent._cast(
                _7139.TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_turbine_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7140.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7140,
            )

            return self._parent._cast(
                _7140.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def unbalanced_mass_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7141.UnbalancedMassAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7141,
            )

            return self._parent._cast(
                _7141.UnbalancedMassAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def virtual_component_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7142.VirtualComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7142,
            )

            return self._parent._cast(
                _7142.VirtualComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7143.WormGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7143,
            )

            return self._parent._cast(
                _7143.WormGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7146.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7146,
            )

            return self._parent._cast(
                _7146.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "MountableComponentAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2471.MountableComponent":
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
    def system_deflection_results(
        self: Self,
    ) -> "_2790.MountableComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.MountableComponentSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation(
            self
        )
