"""ComponentCompoundSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3475,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3291,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3397,
        _3398,
        _3400,
        _3404,
        _3407,
        _3410,
        _3411,
        _3412,
        _3415,
        _3419,
        _3424,
        _3425,
        _3428,
        _3432,
        _3435,
        _3438,
        _3441,
        _3443,
        _3446,
        _3447,
        _3448,
        _3449,
        _3452,
        _3454,
        _3457,
        _3458,
        _3462,
        _3465,
        _3468,
        _3471,
        _3472,
        _3473,
        _3474,
        _3478,
        _3481,
        _3482,
        _3483,
        _3484,
        _3485,
        _3488,
        _3491,
        _3492,
        _3495,
        _3500,
        _3501,
        _3504,
        _3507,
        _3508,
        _3510,
        _3511,
        _3512,
        _3515,
        _3516,
        _3517,
        _3518,
        _3519,
        _3522,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="ComponentCompoundSteadyStateSynchronousResponseOnAShaft")


class ComponentCompoundSteadyStateSynchronousResponseOnAShaft(
    _3475.PartCompoundSteadyStateSynchronousResponseOnAShaft
):
    """ComponentCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ComponentCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3475.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3475.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3397.AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3397,
            )

            return self._parent._cast(
                _3397.AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3398.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3398,
            )

            return self._parent._cast(
                _3398.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3400.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3400,
            )

            return self._parent._cast(
                _3400.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bearing_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3404.BearingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3404,
            )

            return self._parent._cast(
                _3404.BearingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3407.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3407,
            )

            return self._parent._cast(
                _3407.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3410.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3410,
            )

            return self._parent._cast(
                _3410.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3411.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3411,
            )

            return self._parent._cast(
                _3411.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3412.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3412,
            )

            return self._parent._cast(
                _3412.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolt_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3415.BoltCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3415,
            )

            return self._parent._cast(
                _3415.BoltCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3419.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3419,
            )

            return self._parent._cast(
                _3419.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3424.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3424,
            )

            return self._parent._cast(
                _3424.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3425.ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3425,
            )

            return self._parent._cast(
                _3425.ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3428.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3428,
            )

            return self._parent._cast(
                _3428.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connector_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3432.ConnectorCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3432,
            )

            return self._parent._cast(
                _3432.ConnectorCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3435.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3435,
            )

            return self._parent._cast(
                _3435.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3438.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3438,
            )

            return self._parent._cast(
                _3438.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3441.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3441,
            )

            return self._parent._cast(
                _3441.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3443.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3443,
            )

            return self._parent._cast(
                _3443.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3446.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3446,
            )

            return self._parent._cast(
                _3446.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def datum_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3447.DatumCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3447,
            )

            return self._parent._cast(
                _3447.DatumCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def external_cad_model_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3448.ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3448,
            )

            return self._parent._cast(
                _3448.ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3449.FaceGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3449,
            )

            return self._parent._cast(
                _3449.FaceGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def fe_part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3452.FEPartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3452,
            )

            return self._parent._cast(
                _3452.FEPartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3454.GearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3454,
            )

            return self._parent._cast(
                _3454.GearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3457.GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3457,
            )

            return self._parent._cast(
                _3457.GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3458.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3458,
            )

            return self._parent._cast(
                _3458.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3462.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3462,
            )

            return self._parent._cast(
                _3462.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3465.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3465,
            )

            return self._parent._cast(
                _3465.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3468.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3468,
            )

            return self._parent._cast(
                _3468.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3471.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3471,
            )

            return self._parent._cast(
                _3471.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3472.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3472,
            )

            return self._parent._cast(
                _3472.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3473.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3473,
            )

            return self._parent._cast(
                _3473.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3474.OilSealCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3474,
            )

            return self._parent._cast(
                _3474.OilSealCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3478.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3478,
            )

            return self._parent._cast(
                _3478.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3481.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3481,
            )

            return self._parent._cast(
                _3481.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def point_load_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3482.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3482,
            )

            return self._parent._cast(
                _3482.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def power_load_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3483.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3483,
            )

            return self._parent._cast(
                _3483.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def pulley_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3484.PulleyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3484,
            )

            return self._parent._cast(
                _3484.PulleyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3485.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3485,
            )

            return self._parent._cast(
                _3485.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3488.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3488,
            )

            return self._parent._cast(
                _3488.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3491.ShaftCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3491,
            )

            return self._parent._cast(
                _3491.ShaftCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3492.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3492,
            )

            return self._parent._cast(
                _3492.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3495.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3495,
            )

            return self._parent._cast(
                _3495.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3500.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3500,
            )

            return self._parent._cast(
                _3500.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3501.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3501,
            )

            return self._parent._cast(
                _3501.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3504.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3504,
            )

            return self._parent._cast(
                _3504.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3507.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3507,
            )

            return self._parent._cast(
                _3507.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3508.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3508,
            )

            return self._parent._cast(
                _3508.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3510.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3510,
            )

            return self._parent._cast(
                _3510.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3511.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3511,
            )

            return self._parent._cast(
                _3511.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3512.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3512,
            )

            return self._parent._cast(
                _3512.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3515.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3515,
            )

            return self._parent._cast(
                _3515.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3516.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3516,
            )

            return self._parent._cast(
                _3516.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3517.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3517,
            )

            return self._parent._cast(
                _3517.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3518.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3518,
            )

            return self._parent._cast(
                _3518.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3519.WormGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3519,
            )

            return self._parent._cast(
                _3519.WormGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3522.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3522,
            )

            return self._parent._cast(
                _3522.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ComponentCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3291.ComponentSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ComponentSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3291.ComponentSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ComponentSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "ComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ComponentCompoundSteadyStateSynchronousResponseOnAShaft(self)
