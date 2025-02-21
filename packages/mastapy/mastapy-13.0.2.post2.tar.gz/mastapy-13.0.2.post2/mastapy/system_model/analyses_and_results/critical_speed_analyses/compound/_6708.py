"""ComponentCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6762,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "ComponentCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6576
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6684,
        _6685,
        _6687,
        _6691,
        _6694,
        _6697,
        _6698,
        _6699,
        _6702,
        _6706,
        _6711,
        _6712,
        _6715,
        _6719,
        _6722,
        _6725,
        _6728,
        _6730,
        _6733,
        _6734,
        _6735,
        _6736,
        _6739,
        _6741,
        _6744,
        _6745,
        _6749,
        _6752,
        _6755,
        _6758,
        _6759,
        _6760,
        _6761,
        _6765,
        _6768,
        _6769,
        _6770,
        _6771,
        _6772,
        _6775,
        _6778,
        _6779,
        _6782,
        _6787,
        _6788,
        _6791,
        _6794,
        _6795,
        _6797,
        _6798,
        _6799,
        _6802,
        _6803,
        _6804,
        _6805,
        _6806,
        _6809,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ComponentCompoundCriticalSpeedAnalysis")


class ComponentCompoundCriticalSpeedAnalysis(_6762.PartCompoundCriticalSpeedAnalysis):
    """ComponentCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ComponentCompoundCriticalSpeedAnalysis"
    )

    class _Cast_ComponentCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ComponentCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
            parent: "ComponentCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6762.PartCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6762.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6684.AbstractShaftCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6684,
            )

            return self._parent._cast(_6684.AbstractShaftCompoundCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6685.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6685,
            )

            return self._parent._cast(
                _6685.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6687.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6687,
            )

            return self._parent._cast(
                _6687.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bearing_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6691.BearingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6691,
            )

            return self._parent._cast(_6691.BearingCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6694.BevelDifferentialGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6694,
            )

            return self._parent._cast(
                _6694.BevelDifferentialGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6697.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6697,
            )

            return self._parent._cast(
                _6697.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6698.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6698,
            )

            return self._parent._cast(
                _6698.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6699.BevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6699,
            )

            return self._parent._cast(_6699.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def bolt_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6702.BoltCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6702,
            )

            return self._parent._cast(_6702.BoltCompoundCriticalSpeedAnalysis)

        @property
        def clutch_half_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6706.ClutchHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6706,
            )

            return self._parent._cast(_6706.ClutchHalfCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6711.ConceptCouplingHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6711,
            )

            return self._parent._cast(
                _6711.ConceptCouplingHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6712.ConceptGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6712,
            )

            return self._parent._cast(_6712.ConceptGearCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6715.ConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6715,
            )

            return self._parent._cast(_6715.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def connector_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6719.ConnectorCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6719,
            )

            return self._parent._cast(_6719.ConnectorCompoundCriticalSpeedAnalysis)

        @property
        def coupling_half_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6722.CouplingHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6722,
            )

            return self._parent._cast(_6722.CouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def cvt_pulley_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6725.CVTPulleyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6725,
            )

            return self._parent._cast(_6725.CVTPulleyCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6728.CycloidalDiscCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6728,
            )

            return self._parent._cast(_6728.CycloidalDiscCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6730.CylindricalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6730,
            )

            return self._parent._cast(
                _6730.CylindricalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_planet_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6733.CylindricalPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6733,
            )

            return self._parent._cast(
                _6733.CylindricalPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def datum_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6734.DatumCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6734,
            )

            return self._parent._cast(_6734.DatumCompoundCriticalSpeedAnalysis)

        @property
        def external_cad_model_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6735.ExternalCADModelCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6735,
            )

            return self._parent._cast(
                _6735.ExternalCADModelCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6736.FaceGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6736,
            )

            return self._parent._cast(_6736.FaceGearCompoundCriticalSpeedAnalysis)

        @property
        def fe_part_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6739.FEPartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6739,
            )

            return self._parent._cast(_6739.FEPartCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6741.GearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6741,
            )

            return self._parent._cast(_6741.GearCompoundCriticalSpeedAnalysis)

        @property
        def guide_dxf_model_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6744.GuideDxfModelCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6744,
            )

            return self._parent._cast(_6744.GuideDxfModelCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6745.HypoidGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6745,
            )

            return self._parent._cast(_6745.HypoidGearCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6749.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6749,
            )

            return self._parent._cast(
                _6749.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6752.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6752,
            )

            return self._parent._cast(
                _6752.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> (
            "_6755.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6755,
            )

            return self._parent._cast(
                _6755.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def mass_disc_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6758.MassDiscCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6758,
            )

            return self._parent._cast(_6758.MassDiscCompoundCriticalSpeedAnalysis)

        @property
        def measurement_component_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6759.MeasurementComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6759,
            )

            return self._parent._cast(
                _6759.MeasurementComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6760.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6760,
            )

            return self._parent._cast(
                _6760.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def oil_seal_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6761.OilSealCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6761,
            )

            return self._parent._cast(_6761.OilSealCompoundCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6765.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6765,
            )

            return self._parent._cast(
                _6765.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def planet_carrier_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6768.PlanetCarrierCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6768,
            )

            return self._parent._cast(_6768.PlanetCarrierCompoundCriticalSpeedAnalysis)

        @property
        def point_load_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6769.PointLoadCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6769,
            )

            return self._parent._cast(_6769.PointLoadCompoundCriticalSpeedAnalysis)

        @property
        def power_load_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6770.PowerLoadCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6770,
            )

            return self._parent._cast(_6770.PowerLoadCompoundCriticalSpeedAnalysis)

        @property
        def pulley_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6771.PulleyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6771,
            )

            return self._parent._cast(_6771.PulleyCompoundCriticalSpeedAnalysis)

        @property
        def ring_pins_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6772.RingPinsCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6772,
            )

            return self._parent._cast(_6772.RingPinsCompoundCriticalSpeedAnalysis)

        @property
        def rolling_ring_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6775.RollingRingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(_6775.RollingRingCompoundCriticalSpeedAnalysis)

        @property
        def shaft_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6778.ShaftCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6778,
            )

            return self._parent._cast(_6778.ShaftCompoundCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6779.ShaftHubConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6779,
            )

            return self._parent._cast(
                _6779.ShaftHubConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6782.SpiralBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6782,
            )

            return self._parent._cast(
                _6782.SpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_half_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6787.SpringDamperHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6787,
            )

            return self._parent._cast(
                _6787.SpringDamperHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6788.StraightBevelDiffGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6788,
            )

            return self._parent._cast(
                _6788.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6791.StraightBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6791,
            )

            return self._parent._cast(
                _6791.StraightBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6794.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6794,
            )

            return self._parent._cast(
                _6794.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6795.StraightBevelSunGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6795,
            )

            return self._parent._cast(
                _6795.StraightBevelSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_half_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6797.SynchroniserHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6797,
            )

            return self._parent._cast(
                _6797.SynchroniserHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_part_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6798.SynchroniserPartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6798,
            )

            return self._parent._cast(
                _6798.SynchroniserPartCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_sleeve_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6799.SynchroniserSleeveCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6799,
            )

            return self._parent._cast(
                _6799.SynchroniserSleeveCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_pump_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6802.TorqueConverterPumpCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6802,
            )

            return self._parent._cast(
                _6802.TorqueConverterPumpCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_turbine_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6803.TorqueConverterTurbineCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6803,
            )

            return self._parent._cast(
                _6803.TorqueConverterTurbineCompoundCriticalSpeedAnalysis
            )

        @property
        def unbalanced_mass_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6804.UnbalancedMassCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6804,
            )

            return self._parent._cast(_6804.UnbalancedMassCompoundCriticalSpeedAnalysis)

        @property
        def virtual_component_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6805.VirtualComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6805,
            )

            return self._parent._cast(
                _6805.VirtualComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6806.WormGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6806,
            )

            return self._parent._cast(_6806.WormGearCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6809.ZerolBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6809,
            )

            return self._parent._cast(_6809.ZerolBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def component_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "ComponentCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "ComponentCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6576.ComponentCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ComponentCriticalSpeedAnalysis]

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
    ) -> "List[_6576.ComponentCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ComponentCriticalSpeedAnalysis]

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
    ) -> "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis":
        return self._Cast_ComponentCompoundCriticalSpeedAnalysis(self)
