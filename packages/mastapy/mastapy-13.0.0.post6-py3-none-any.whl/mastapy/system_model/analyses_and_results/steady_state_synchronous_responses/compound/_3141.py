"""ComponentCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3195,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "ComponentCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3008,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3117,
        _3118,
        _3120,
        _3124,
        _3127,
        _3130,
        _3131,
        _3132,
        _3135,
        _3139,
        _3144,
        _3145,
        _3148,
        _3152,
        _3155,
        _3158,
        _3161,
        _3163,
        _3166,
        _3167,
        _3168,
        _3169,
        _3172,
        _3174,
        _3177,
        _3178,
        _3182,
        _3185,
        _3188,
        _3191,
        _3192,
        _3193,
        _3194,
        _3198,
        _3201,
        _3202,
        _3203,
        _3204,
        _3205,
        _3208,
        _3211,
        _3212,
        _3215,
        _3220,
        _3221,
        _3224,
        _3227,
        _3228,
        _3230,
        _3231,
        _3232,
        _3235,
        _3236,
        _3237,
        _3238,
        _3239,
        _3242,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ComponentCompoundSteadyStateSynchronousResponse")


class ComponentCompoundSteadyStateSynchronousResponse(
    _3195.PartCompoundSteadyStateSynchronousResponse
):
    """ComponentCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ComponentCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_ComponentCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting ComponentCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
            parent: "ComponentCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def part_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3195.PartCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(_3195.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3117.AbstractShaftCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3117,
            )

            return self._parent._cast(
                _3117.AbstractShaftCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3118.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3118,
            )

            return self._parent._cast(
                _3118.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3120.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3120,
            )

            return self._parent._cast(
                _3120.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bearing_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3124.BearingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3124,
            )

            return self._parent._cast(
                _3124.BearingCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3127.BevelDifferentialGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3127,
            )

            return self._parent._cast(
                _3127.BevelDifferentialGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3130.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3130,
            )

            return self._parent._cast(
                _3130.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3131.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3131,
            )

            return self._parent._cast(
                _3131.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3132.BevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3132,
            )

            return self._parent._cast(
                _3132.BevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bolt_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3135.BoltCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3135,
            )

            return self._parent._cast(_3135.BoltCompoundSteadyStateSynchronousResponse)

        @property
        def clutch_half_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3139.ClutchHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3139,
            )

            return self._parent._cast(
                _3139.ClutchHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3144.ConceptCouplingHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3144,
            )

            return self._parent._cast(
                _3144.ConceptCouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3145.ConceptGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3145,
            )

            return self._parent._cast(
                _3145.ConceptGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3148.ConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3148,
            )

            return self._parent._cast(
                _3148.ConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def connector_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3152.ConnectorCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3152,
            )

            return self._parent._cast(
                _3152.ConnectorCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3155.CouplingHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3155,
            )

            return self._parent._cast(
                _3155.CouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3158.CVTPulleyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3158,
            )

            return self._parent._cast(
                _3158.CVTPulleyCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3161.CycloidalDiscCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3161,
            )

            return self._parent._cast(
                _3161.CycloidalDiscCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3163.CylindricalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3163,
            )

            return self._parent._cast(
                _3163.CylindricalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3166.CylindricalPlanetGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3166,
            )

            return self._parent._cast(
                _3166.CylindricalPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def datum_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3167.DatumCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3167,
            )

            return self._parent._cast(_3167.DatumCompoundSteadyStateSynchronousResponse)

        @property
        def external_cad_model_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3168.ExternalCADModelCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3168,
            )

            return self._parent._cast(
                _3168.ExternalCADModelCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3169.FaceGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3169,
            )

            return self._parent._cast(
                _3169.FaceGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def fe_part_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3172.FEPartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3172,
            )

            return self._parent._cast(
                _3172.FEPartCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3174.GearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3174,
            )

            return self._parent._cast(_3174.GearCompoundSteadyStateSynchronousResponse)

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3177.GuideDxfModelCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3177,
            )

            return self._parent._cast(
                _3177.GuideDxfModelCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3178.HypoidGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3178,
            )

            return self._parent._cast(
                _3178.HypoidGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3182.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3182,
            )

            return self._parent._cast(
                _3182.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3185.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3185,
            )

            return self._parent._cast(
                _3185.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3188.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3188,
            )

            return self._parent._cast(
                _3188.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3191.MassDiscCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3191,
            )

            return self._parent._cast(
                _3191.MassDiscCompoundSteadyStateSynchronousResponse
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3192.MeasurementComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3192,
            )

            return self._parent._cast(
                _3192.MeasurementComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3193.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(
                _3193.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3194.OilSealCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3194,
            )

            return self._parent._cast(
                _3194.OilSealCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3198.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3198,
            )

            return self._parent._cast(
                _3198.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3201.PlanetCarrierCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3201,
            )

            return self._parent._cast(
                _3201.PlanetCarrierCompoundSteadyStateSynchronousResponse
            )

        @property
        def point_load_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3202.PointLoadCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3202,
            )

            return self._parent._cast(
                _3202.PointLoadCompoundSteadyStateSynchronousResponse
            )

        @property
        def power_load_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3203.PowerLoadCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3203,
            )

            return self._parent._cast(
                _3203.PowerLoadCompoundSteadyStateSynchronousResponse
            )

        @property
        def pulley_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3204.PulleyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3204,
            )

            return self._parent._cast(
                _3204.PulleyCompoundSteadyStateSynchronousResponse
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3205.RingPinsCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3205,
            )

            return self._parent._cast(
                _3205.RingPinsCompoundSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3208.RollingRingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3208,
            )

            return self._parent._cast(
                _3208.RollingRingCompoundSteadyStateSynchronousResponse
            )

        @property
        def shaft_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3211.ShaftCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3211,
            )

            return self._parent._cast(_3211.ShaftCompoundSteadyStateSynchronousResponse)

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3212.ShaftHubConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3212,
            )

            return self._parent._cast(
                _3212.ShaftHubConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3215.SpiralBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3215,
            )

            return self._parent._cast(
                _3215.SpiralBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3220.SpringDamperHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3220,
            )

            return self._parent._cast(
                _3220.SpringDamperHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3221.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3221,
            )

            return self._parent._cast(
                _3221.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3224.StraightBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3224,
            )

            return self._parent._cast(
                _3224.StraightBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3227.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3227,
            )

            return self._parent._cast(
                _3227.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3228.StraightBevelSunGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3228,
            )

            return self._parent._cast(
                _3228.StraightBevelSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3230.SynchroniserHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3230,
            )

            return self._parent._cast(
                _3230.SynchroniserHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3231.SynchroniserPartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3231,
            )

            return self._parent._cast(
                _3231.SynchroniserPartCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3232.SynchroniserSleeveCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3232,
            )

            return self._parent._cast(
                _3232.SynchroniserSleeveCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3235.TorqueConverterPumpCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3235,
            )

            return self._parent._cast(
                _3235.TorqueConverterPumpCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3236.TorqueConverterTurbineCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3236,
            )

            return self._parent._cast(
                _3236.TorqueConverterTurbineCompoundSteadyStateSynchronousResponse
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3237.UnbalancedMassCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3237,
            )

            return self._parent._cast(
                _3237.UnbalancedMassCompoundSteadyStateSynchronousResponse
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3238.VirtualComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3238,
            )

            return self._parent._cast(
                _3238.VirtualComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3239.WormGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3239,
            )

            return self._parent._cast(
                _3239.WormGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3242.ZerolBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3242,
            )

            return self._parent._cast(
                _3242.ZerolBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "ComponentCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ComponentCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3008.ComponentSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ComponentSteadyStateSynchronousResponse]

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
    ) -> "List[_3008.ComponentSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ComponentSteadyStateSynchronousResponse]

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
    ) -> "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse":
        return self._Cast_ComponentCompoundSteadyStateSynchronousResponse(self)
