"""SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3245,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2476
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3250,
        _3255,
        _3257,
        _3262,
        _3264,
        _3268,
        _3273,
        _3275,
        _3278,
        _3284,
        _3287,
        _3288,
        _3293,
        _3299,
        _3302,
        _3304,
        _3308,
        _3312,
        _3315,
        _3318,
        _3327,
        _3329,
        _3336,
        _3345,
        _3349,
        _3352,
        _3355,
        _3362,
        _3365,
        _3370,
        _3373,
        _3324,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft"
)


class SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft(
    _3245.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
):
    """SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
            parent: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3245.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3245.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3324.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(_3324.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3250.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3250,
            )

            return self._parent._cast(
                _3250.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_drive_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3255.BeltDriveSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3255,
            )

            return self._parent._cast(
                _3255.BeltDriveSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3257.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3257,
            )

            return self._parent._cast(
                _3257.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3262.BevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3262,
            )

            return self._parent._cast(
                _3262.BevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolted_joint_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3264.BoltedJointSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3264,
            )

            return self._parent._cast(
                _3264.BoltedJointSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3268.ClutchSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3268,
            )

            return self._parent._cast(
                _3268.ClutchSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3273.ConceptCouplingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3273,
            )

            return self._parent._cast(
                _3273.ConceptCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3275.ConceptGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3275,
            )

            return self._parent._cast(
                _3275.ConceptGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3278.ConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3278,
            )

            return self._parent._cast(
                _3278.ConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3284.CouplingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3284,
            )

            return self._parent._cast(
                _3284.CouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3287.CVTSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3287,
            )

            return self._parent._cast(_3287.CVTSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3288.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3288,
            )

            return self._parent._cast(
                _3288.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3293.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3293,
            )

            return self._parent._cast(
                _3293.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3299.FaceGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3299,
            )

            return self._parent._cast(
                _3299.FaceGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3302.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3302,
            )

            return self._parent._cast(
                _3302.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3304.GearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3304,
            )

            return self._parent._cast(
                _3304.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3308.HypoidGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3308,
            )

            return self._parent._cast(
                _3308.HypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3312.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3312,
            )

            return self._parent._cast(
                _3312.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3315.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3315,
            )

            return self._parent._cast(
                _3315.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3318.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3318,
            )

            return self._parent._cast(
                _3318.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3327.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3327,
            )

            return self._parent._cast(
                _3327.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3329.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3329,
            )

            return self._parent._cast(
                _3329.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3336.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3336,
            )

            return self._parent._cast(
                _3336.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3345.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(
                _3345.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3349.SpringDamperSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3349,
            )

            return self._parent._cast(
                _3349.SpringDamperSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3352.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3352,
            )

            return self._parent._cast(
                _3352.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3355.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3355,
            )

            return self._parent._cast(
                _3355.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3362.SynchroniserSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3362,
            )

            return self._parent._cast(
                _3362.SynchroniserSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3365.TorqueConverterSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3365,
            )

            return self._parent._cast(
                _3365.TorqueConverterSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3370.WormGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3370,
            )

            return self._parent._cast(
                _3370.WormGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3373.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3373,
            )

            return self._parent._cast(
                _3373.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2476.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
        return self._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft(
            self
        )
