"""ComponentCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6753,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "ComponentCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6567
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6675,
        _6676,
        _6678,
        _6682,
        _6685,
        _6688,
        _6689,
        _6690,
        _6693,
        _6697,
        _6702,
        _6703,
        _6706,
        _6710,
        _6713,
        _6716,
        _6719,
        _6721,
        _6724,
        _6725,
        _6726,
        _6727,
        _6730,
        _6732,
        _6735,
        _6736,
        _6740,
        _6743,
        _6746,
        _6749,
        _6750,
        _6751,
        _6752,
        _6756,
        _6759,
        _6760,
        _6761,
        _6762,
        _6763,
        _6766,
        _6769,
        _6770,
        _6773,
        _6778,
        _6779,
        _6782,
        _6785,
        _6786,
        _6788,
        _6789,
        _6790,
        _6793,
        _6794,
        _6795,
        _6796,
        _6797,
        _6800,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ComponentCompoundCriticalSpeedAnalysis")


class ComponentCompoundCriticalSpeedAnalysis(_6753.PartCompoundCriticalSpeedAnalysis):
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
        ) -> "_6753.PartCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6753.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6675.AbstractShaftCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6675,
            )

            return self._parent._cast(_6675.AbstractShaftCompoundCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6676.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6676,
            )

            return self._parent._cast(
                _6676.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6678.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6678,
            )

            return self._parent._cast(
                _6678.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bearing_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6682.BearingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6682,
            )

            return self._parent._cast(_6682.BearingCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6685.BevelDifferentialGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6685,
            )

            return self._parent._cast(
                _6685.BevelDifferentialGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6688.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6688,
            )

            return self._parent._cast(
                _6688.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6689.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6689,
            )

            return self._parent._cast(
                _6689.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6690.BevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6690,
            )

            return self._parent._cast(_6690.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def bolt_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6693.BoltCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6693,
            )

            return self._parent._cast(_6693.BoltCompoundCriticalSpeedAnalysis)

        @property
        def clutch_half_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6697.ClutchHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6697,
            )

            return self._parent._cast(_6697.ClutchHalfCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6702.ConceptCouplingHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6702,
            )

            return self._parent._cast(
                _6702.ConceptCouplingHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6703.ConceptGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6703,
            )

            return self._parent._cast(_6703.ConceptGearCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6706.ConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6706,
            )

            return self._parent._cast(_6706.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def connector_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6710.ConnectorCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6710,
            )

            return self._parent._cast(_6710.ConnectorCompoundCriticalSpeedAnalysis)

        @property
        def coupling_half_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6713.CouplingHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6713,
            )

            return self._parent._cast(_6713.CouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def cvt_pulley_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6716.CVTPulleyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6716,
            )

            return self._parent._cast(_6716.CVTPulleyCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6719.CycloidalDiscCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6719,
            )

            return self._parent._cast(_6719.CycloidalDiscCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6721.CylindricalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6721,
            )

            return self._parent._cast(
                _6721.CylindricalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_planet_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6724.CylindricalPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6724,
            )

            return self._parent._cast(
                _6724.CylindricalPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def datum_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6725.DatumCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6725,
            )

            return self._parent._cast(_6725.DatumCompoundCriticalSpeedAnalysis)

        @property
        def external_cad_model_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6726.ExternalCADModelCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6726,
            )

            return self._parent._cast(
                _6726.ExternalCADModelCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6727.FaceGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6727,
            )

            return self._parent._cast(_6727.FaceGearCompoundCriticalSpeedAnalysis)

        @property
        def fe_part_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6730.FEPartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6730,
            )

            return self._parent._cast(_6730.FEPartCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6732.GearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6732,
            )

            return self._parent._cast(_6732.GearCompoundCriticalSpeedAnalysis)

        @property
        def guide_dxf_model_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6735.GuideDxfModelCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6735,
            )

            return self._parent._cast(_6735.GuideDxfModelCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6736.HypoidGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6736,
            )

            return self._parent._cast(_6736.HypoidGearCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6740.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6740,
            )

            return self._parent._cast(
                _6740.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6743.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6743,
            )

            return self._parent._cast(
                _6743.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> (
            "_6746.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6746,
            )

            return self._parent._cast(
                _6746.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def mass_disc_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6749.MassDiscCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6749,
            )

            return self._parent._cast(_6749.MassDiscCompoundCriticalSpeedAnalysis)

        @property
        def measurement_component_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6750.MeasurementComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6750,
            )

            return self._parent._cast(
                _6750.MeasurementComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6751.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(
                _6751.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def oil_seal_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6752.OilSealCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6752,
            )

            return self._parent._cast(_6752.OilSealCompoundCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6756.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6756,
            )

            return self._parent._cast(
                _6756.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def planet_carrier_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6759.PlanetCarrierCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6759,
            )

            return self._parent._cast(_6759.PlanetCarrierCompoundCriticalSpeedAnalysis)

        @property
        def point_load_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6760.PointLoadCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6760,
            )

            return self._parent._cast(_6760.PointLoadCompoundCriticalSpeedAnalysis)

        @property
        def power_load_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6761.PowerLoadCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6761,
            )

            return self._parent._cast(_6761.PowerLoadCompoundCriticalSpeedAnalysis)

        @property
        def pulley_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6762.PulleyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6762,
            )

            return self._parent._cast(_6762.PulleyCompoundCriticalSpeedAnalysis)

        @property
        def ring_pins_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6763.RingPinsCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6763,
            )

            return self._parent._cast(_6763.RingPinsCompoundCriticalSpeedAnalysis)

        @property
        def rolling_ring_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6766.RollingRingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6766,
            )

            return self._parent._cast(_6766.RollingRingCompoundCriticalSpeedAnalysis)

        @property
        def shaft_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6769.ShaftCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6769,
            )

            return self._parent._cast(_6769.ShaftCompoundCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6770.ShaftHubConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6770,
            )

            return self._parent._cast(
                _6770.ShaftHubConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6773.SpiralBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6773,
            )

            return self._parent._cast(
                _6773.SpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_half_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6778.SpringDamperHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6778,
            )

            return self._parent._cast(
                _6778.SpringDamperHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6779.StraightBevelDiffGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6779,
            )

            return self._parent._cast(
                _6779.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6782.StraightBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6782,
            )

            return self._parent._cast(
                _6782.StraightBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6785.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6785,
            )

            return self._parent._cast(
                _6785.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6786.StraightBevelSunGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6786,
            )

            return self._parent._cast(
                _6786.StraightBevelSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_half_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6788.SynchroniserHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6788,
            )

            return self._parent._cast(
                _6788.SynchroniserHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_part_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6789.SynchroniserPartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6789,
            )

            return self._parent._cast(
                _6789.SynchroniserPartCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_sleeve_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6790.SynchroniserSleeveCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6790,
            )

            return self._parent._cast(
                _6790.SynchroniserSleeveCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_pump_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6793.TorqueConverterPumpCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6793,
            )

            return self._parent._cast(
                _6793.TorqueConverterPumpCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_turbine_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6794.TorqueConverterTurbineCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6794,
            )

            return self._parent._cast(
                _6794.TorqueConverterTurbineCompoundCriticalSpeedAnalysis
            )

        @property
        def unbalanced_mass_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6795.UnbalancedMassCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6795,
            )

            return self._parent._cast(_6795.UnbalancedMassCompoundCriticalSpeedAnalysis)

        @property
        def virtual_component_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6796.VirtualComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6796,
            )

            return self._parent._cast(
                _6796.VirtualComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6797.WormGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6797,
            )

            return self._parent._cast(_6797.WormGearCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6800.ZerolBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6800,
            )

            return self._parent._cast(_6800.ZerolBevelGearCompoundCriticalSpeedAnalysis)

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
    ) -> "List[_6567.ComponentCriticalSpeedAnalysis]":
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
    ) -> "List[_6567.ComponentCriticalSpeedAnalysis]":
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
