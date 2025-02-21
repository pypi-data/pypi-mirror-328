"""ComponentHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5787
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ComponentHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2444
    from mastapy.system_model.analyses_and_results.modal_analyses import _4596
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5864,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2715
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5679,
        _5680,
        _5682,
        _5686,
        _5689,
        _5692,
        _5693,
        _5694,
        _5698,
        _5700,
        _5706,
        _5708,
        _5711,
        _5715,
        _5717,
        _5721,
        _5724,
        _5726,
        _5729,
        _5730,
        _5745,
        _5746,
        _5749,
        _5752,
        _5759,
        _5770,
        _5774,
        _5777,
        _5780,
        _5783,
        _5784,
        _5785,
        _5786,
        _5789,
        _5794,
        _5795,
        _5796,
        _5797,
        _5799,
        _5803,
        _5805,
        _5806,
        _5811,
        _5815,
        _5818,
        _5821,
        _5824,
        _5825,
        _5826,
        _5828,
        _5829,
        _5832,
        _5833,
        _5835,
        _5836,
        _5837,
        _5840,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ComponentHarmonicAnalysis",)


Self = TypeVar("Self", bound="ComponentHarmonicAnalysis")


class ComponentHarmonicAnalysis(_5787.PartHarmonicAnalysis):
    """ComponentHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentHarmonicAnalysis")

    class _Cast_ComponentHarmonicAnalysis:
        """Special nested class for casting ComponentHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
            parent: "ComponentHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def part_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5787.PartHarmonicAnalysis":
            return self._parent._cast(_5787.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5679.AbstractShaftHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5679,
            )

            return self._parent._cast(_5679.AbstractShaftHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5680.AbstractShaftOrHousingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5680,
            )

            return self._parent._cast(_5680.AbstractShaftOrHousingHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5682.AGMAGleasonConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5682,
            )

            return self._parent._cast(_5682.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def bearing_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5686.BearingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5686,
            )

            return self._parent._cast(_5686.BearingHarmonicAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5689.BevelDifferentialGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5689,
            )

            return self._parent._cast(_5689.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5692.BevelDifferentialPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5692,
            )

            return self._parent._cast(_5692.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5693.BevelDifferentialSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5693,
            )

            return self._parent._cast(_5693.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5694.BevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5694,
            )

            return self._parent._cast(_5694.BevelGearHarmonicAnalysis)

        @property
        def bolt_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5698.BoltHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5698,
            )

            return self._parent._cast(_5698.BoltHarmonicAnalysis)

        @property
        def clutch_half_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5700.ClutchHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5700,
            )

            return self._parent._cast(_5700.ClutchHalfHarmonicAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5706.ConceptCouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5706,
            )

            return self._parent._cast(_5706.ConceptCouplingHalfHarmonicAnalysis)

        @property
        def concept_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5708.ConceptGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5708,
            )

            return self._parent._cast(_5708.ConceptGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5711.ConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5711,
            )

            return self._parent._cast(_5711.ConicalGearHarmonicAnalysis)

        @property
        def connector_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5715.ConnectorHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5715,
            )

            return self._parent._cast(_5715.ConnectorHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5717.CouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5717,
            )

            return self._parent._cast(_5717.CouplingHalfHarmonicAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5721.CVTPulleyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5721,
            )

            return self._parent._cast(_5721.CVTPulleyHarmonicAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5724.CycloidalDiscHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5724,
            )

            return self._parent._cast(_5724.CycloidalDiscHarmonicAnalysis)

        @property
        def cylindrical_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5726.CylindricalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(_5726.CylindricalGearHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5729.CylindricalPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5729,
            )

            return self._parent._cast(_5729.CylindricalPlanetGearHarmonicAnalysis)

        @property
        def datum_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5730.DatumHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5730,
            )

            return self._parent._cast(_5730.DatumHarmonicAnalysis)

        @property
        def external_cad_model_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5745.ExternalCADModelHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5745,
            )

            return self._parent._cast(_5745.ExternalCADModelHarmonicAnalysis)

        @property
        def face_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5746.FaceGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5746,
            )

            return self._parent._cast(_5746.FaceGearHarmonicAnalysis)

        @property
        def fe_part_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5749.FEPartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5749,
            )

            return self._parent._cast(_5749.FEPartHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5752.GearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5752,
            )

            return self._parent._cast(_5752.GearHarmonicAnalysis)

        @property
        def guide_dxf_model_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5759.GuideDxfModelHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5759,
            )

            return self._parent._cast(_5759.GuideDxfModelHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5770.HypoidGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5770,
            )

            return self._parent._cast(_5770.HypoidGearHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5774.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5774,
            )

            return self._parent._cast(
                _5774.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5777.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5777,
            )

            return self._parent._cast(
                _5777.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5780.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5780,
            )

            return self._parent._cast(
                _5780.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
            )

        @property
        def mass_disc_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5783.MassDiscHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5783,
            )

            return self._parent._cast(_5783.MassDiscHarmonicAnalysis)

        @property
        def measurement_component_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5784.MeasurementComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.MeasurementComponentHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5785.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(_5785.MountableComponentHarmonicAnalysis)

        @property
        def oil_seal_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5786.OilSealHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5786,
            )

            return self._parent._cast(_5786.OilSealHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5789.PartToPartShearCouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5789,
            )

            return self._parent._cast(_5789.PartToPartShearCouplingHalfHarmonicAnalysis)

        @property
        def planet_carrier_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5794.PlanetCarrierHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5794,
            )

            return self._parent._cast(_5794.PlanetCarrierHarmonicAnalysis)

        @property
        def point_load_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5795.PointLoadHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5795,
            )

            return self._parent._cast(_5795.PointLoadHarmonicAnalysis)

        @property
        def power_load_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5796.PowerLoadHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PowerLoadHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5797.PulleyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5797,
            )

            return self._parent._cast(_5797.PulleyHarmonicAnalysis)

        @property
        def ring_pins_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5799.RingPinsHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5799,
            )

            return self._parent._cast(_5799.RingPinsHarmonicAnalysis)

        @property
        def rolling_ring_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5803.RollingRingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5803,
            )

            return self._parent._cast(_5803.RollingRingHarmonicAnalysis)

        @property
        def shaft_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5805.ShaftHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5805,
            )

            return self._parent._cast(_5805.ShaftHarmonicAnalysis)

        @property
        def shaft_hub_connection_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5806.ShaftHubConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5806,
            )

            return self._parent._cast(_5806.ShaftHubConnectionHarmonicAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5811.SpiralBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5811,
            )

            return self._parent._cast(_5811.SpiralBevelGearHarmonicAnalysis)

        @property
        def spring_damper_half_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5815.SpringDamperHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5815,
            )

            return self._parent._cast(_5815.SpringDamperHalfHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5818.StraightBevelDiffGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5818,
            )

            return self._parent._cast(_5818.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5821.StraightBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5821,
            )

            return self._parent._cast(_5821.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5824.StraightBevelPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5824,
            )

            return self._parent._cast(_5824.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5825.StraightBevelSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5825,
            )

            return self._parent._cast(_5825.StraightBevelSunGearHarmonicAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5826.SynchroniserHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5826,
            )

            return self._parent._cast(_5826.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5828.SynchroniserPartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5828,
            )

            return self._parent._cast(_5828.SynchroniserPartHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5829.SynchroniserSleeveHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5829,
            )

            return self._parent._cast(_5829.SynchroniserSleeveHarmonicAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5832.TorqueConverterPumpHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5832,
            )

            return self._parent._cast(_5832.TorqueConverterPumpHarmonicAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5833.TorqueConverterTurbineHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5833,
            )

            return self._parent._cast(_5833.TorqueConverterTurbineHarmonicAnalysis)

        @property
        def unbalanced_mass_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5835.UnbalancedMassHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5835,
            )

            return self._parent._cast(_5835.UnbalancedMassHarmonicAnalysis)

        @property
        def virtual_component_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5836.VirtualComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5836,
            )

            return self._parent._cast(_5836.VirtualComponentHarmonicAnalysis)

        @property
        def worm_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5837.WormGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5837,
            )

            return self._parent._cast(_5837.WormGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5840.ZerolBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5840,
            )

            return self._parent._cast(_5840.ZerolBevelGearHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "ComponentHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2444.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def coupled_modal_analysis(self: Self) -> "_4596.ComponentModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ComponentModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def results(self: Self) -> "_5864.HarmonicAnalysisResultsPropertyAccessor":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.HarmonicAnalysisResultsPropertyAccessor

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Results

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2715.ComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection

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
    ) -> "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis":
        return self._Cast_ComponentHarmonicAnalysis(self)
