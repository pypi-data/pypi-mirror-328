"""AbstractAssemblySteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3591,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2441
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3517,
        _3519,
        _3522,
        _3524,
        _3529,
        _3531,
        _3535,
        _3540,
        _3542,
        _3545,
        _3551,
        _3554,
        _3555,
        _3560,
        _3566,
        _3569,
        _3571,
        _3575,
        _3579,
        _3582,
        _3585,
        _3594,
        _3596,
        _3603,
        _3606,
        _3610,
        _3612,
        _3616,
        _3619,
        _3622,
        _3629,
        _3632,
        _3637,
        _3640,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblySteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="AbstractAssemblySteadyStateSynchronousResponseAtASpeed")


class AbstractAssemblySteadyStateSynchronousResponseAtASpeed(
    _3591.PartSteadyStateSynchronousResponseAtASpeed
):
    """AbstractAssemblySteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting AbstractAssemblySteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
            parent: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3591.PartSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(_3591.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3517.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3517,
            )

            return self._parent._cast(
                _3517.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def assembly_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3519.AssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3519,
            )

            return self._parent._cast(
                _3519.AssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_drive_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3522.BeltDriveSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3522,
            )

            return self._parent._cast(
                _3522.BeltDriveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3524.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3524,
            )

            return self._parent._cast(
                _3524.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3529.BevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3529,
            )

            return self._parent._cast(
                _3529.BevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolted_joint_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3531.BoltedJointSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3531,
            )

            return self._parent._cast(
                _3531.BoltedJointSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3535.ClutchSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3535,
            )

            return self._parent._cast(
                _3535.ClutchSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3540.ConceptCouplingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3540,
            )

            return self._parent._cast(
                _3540.ConceptCouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3542.ConceptGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3542,
            )

            return self._parent._cast(
                _3542.ConceptGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3545.ConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3545,
            )

            return self._parent._cast(
                _3545.ConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3551.CouplingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3551,
            )

            return self._parent._cast(
                _3551.CouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3554.CVTSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3554,
            )

            return self._parent._cast(_3554.CVTSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3555.CycloidalAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3555,
            )

            return self._parent._cast(
                _3555.CycloidalAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3560.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3560,
            )

            return self._parent._cast(
                _3560.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3566.FaceGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3566,
            )

            return self._parent._cast(
                _3566.FaceGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3569.FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3569,
            )

            return self._parent._cast(
                _3569.FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3571.GearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3571,
            )

            return self._parent._cast(
                _3571.GearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3575.HypoidGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3575,
            )

            return self._parent._cast(
                _3575.HypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3579.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3579,
            )

            return self._parent._cast(
                _3579.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3582.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3582,
            )

            return self._parent._cast(
                _3582.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3585.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3585,
            )

            return self._parent._cast(
                _3585.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3594.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3594,
            )

            return self._parent._cast(
                _3594.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3596.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3596,
            )

            return self._parent._cast(
                _3596.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3603.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3603,
            )

            return self._parent._cast(
                _3603.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def root_assembly_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3606.RootAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3606,
            )

            return self._parent._cast(
                _3606.RootAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3610.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3610,
            )

            return self._parent._cast(
                _3610.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3612.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3612,
            )

            return self._parent._cast(
                _3612.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3616.SpringDamperSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3616,
            )

            return self._parent._cast(
                _3616.SpringDamperSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3619.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3619,
            )

            return self._parent._cast(
                _3619.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3622.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3622,
            )

            return self._parent._cast(
                _3622.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3629.SynchroniserSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3629,
            )

            return self._parent._cast(
                _3629.SynchroniserSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3632.TorqueConverterSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3632,
            )

            return self._parent._cast(
                _3632.TorqueConverterSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3637.WormGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3637,
            )

            return self._parent._cast(
                _3637.WormGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3640.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3640,
            )

            return self._parent._cast(
                _3640.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "AbstractAssemblySteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "AbstractAssemblySteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2441.AbstractAssembly":
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
    def assembly_design(self: Self) -> "_2441.AbstractAssembly":
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
    ) -> "AbstractAssemblySteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed":
        return self._Cast_AbstractAssemblySteadyStateSynchronousResponseAtASpeed(self)
