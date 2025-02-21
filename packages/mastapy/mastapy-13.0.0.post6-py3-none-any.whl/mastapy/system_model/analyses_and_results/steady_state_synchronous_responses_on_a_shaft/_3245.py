"""AbstractAssemblySteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3324,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2434
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3250,
        _3252,
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
        _3339,
        _3343,
        _3345,
        _3349,
        _3352,
        _3355,
        _3362,
        _3365,
        _3370,
        _3373,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblySteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="AbstractAssemblySteadyStateSynchronousResponseOnAShaft")


class AbstractAssemblySteadyStateSynchronousResponseOnAShaft(
    _3324.PartSteadyStateSynchronousResponseOnAShaft
):
    """AbstractAssemblySteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting AbstractAssemblySteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
            parent: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3324.PartSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(_3324.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3250.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3250,
            )

            return self._parent._cast(
                _3250.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def assembly_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3252.AssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3252,
            )

            return self._parent._cast(
                _3252.AssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_drive_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3255.BeltDriveSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3255,
            )

            return self._parent._cast(
                _3255.BeltDriveSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3257.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3257,
            )

            return self._parent._cast(
                _3257.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3262.BevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3262,
            )

            return self._parent._cast(
                _3262.BevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolted_joint_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3264.BoltedJointSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3264,
            )

            return self._parent._cast(
                _3264.BoltedJointSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3268.ClutchSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3268,
            )

            return self._parent._cast(
                _3268.ClutchSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3273.ConceptCouplingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3273,
            )

            return self._parent._cast(
                _3273.ConceptCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3275.ConceptGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3275,
            )

            return self._parent._cast(
                _3275.ConceptGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3278.ConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3278,
            )

            return self._parent._cast(
                _3278.ConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3284.CouplingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3284,
            )

            return self._parent._cast(
                _3284.CouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3287.CVTSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3287,
            )

            return self._parent._cast(_3287.CVTSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3288.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3288,
            )

            return self._parent._cast(
                _3288.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3293.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3293,
            )

            return self._parent._cast(
                _3293.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3299.FaceGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3299,
            )

            return self._parent._cast(
                _3299.FaceGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3302.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3302,
            )

            return self._parent._cast(
                _3302.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3304.GearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3304,
            )

            return self._parent._cast(
                _3304.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3308.HypoidGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3308,
            )

            return self._parent._cast(
                _3308.HypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3312.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3312,
            )

            return self._parent._cast(
                _3312.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3315.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3315,
            )

            return self._parent._cast(
                _3315.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3318.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3318,
            )

            return self._parent._cast(
                _3318.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3327.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3327,
            )

            return self._parent._cast(
                _3327.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3329.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3329,
            )

            return self._parent._cast(
                _3329.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3336.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3336,
            )

            return self._parent._cast(
                _3336.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def root_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3339.RootAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3339,
            )

            return self._parent._cast(
                _3339.RootAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3343.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3343,
            )

            return self._parent._cast(
                _3343.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3345.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(
                _3345.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3349.SpringDamperSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3349,
            )

            return self._parent._cast(
                _3349.SpringDamperSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3352.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3352,
            )

            return self._parent._cast(
                _3352.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3355.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3355,
            )

            return self._parent._cast(
                _3355.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3362.SynchroniserSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3362,
            )

            return self._parent._cast(
                _3362.SynchroniserSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3365.TorqueConverterSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3365,
            )

            return self._parent._cast(
                _3365.TorqueConverterSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3370.WormGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3370,
            )

            return self._parent._cast(
                _3370.WormGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3373.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3373,
            )

            return self._parent._cast(
                _3373.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2434.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2434.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

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
    ) -> "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
        return self._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft(self)
