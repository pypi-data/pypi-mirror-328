"""SpecialisedAssemblyCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3116,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3082,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3122,
        _3126,
        _3129,
        _3134,
        _3136,
        _3137,
        _3142,
        _3147,
        _3150,
        _3153,
        _3157,
        _3159,
        _3165,
        _3171,
        _3173,
        _3176,
        _3180,
        _3184,
        _3187,
        _3190,
        _3196,
        _3200,
        _3207,
        _3217,
        _3218,
        _3223,
        _3226,
        _3229,
        _3233,
        _3241,
        _3244,
        _3195,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="SpecialisedAssemblyCompoundSteadyStateSynchronousResponse"
)


class SpecialisedAssemblyCompoundSteadyStateSynchronousResponse(
    _3116.AbstractAssemblyCompoundSteadyStateSynchronousResponse
):
    """SpecialisedAssemblyCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting SpecialisedAssemblyCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
            parent: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3116.AbstractAssemblyCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3116.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3195.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3195,
            )

            return self._parent._cast(_3195.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3122.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3122,
            )

            return self._parent._cast(
                _3122.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def belt_drive_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3126.BeltDriveCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3126,
            )

            return self._parent._cast(
                _3126.BeltDriveCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3129.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3129,
            )

            return self._parent._cast(
                _3129.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3134.BevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3134,
            )

            return self._parent._cast(
                _3134.BevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bolted_joint_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3136.BoltedJointCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3136,
            )

            return self._parent._cast(
                _3136.BoltedJointCompoundSteadyStateSynchronousResponse
            )

        @property
        def clutch_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3137.ClutchCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3137,
            )

            return self._parent._cast(
                _3137.ClutchCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3142.ConceptCouplingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3142,
            )

            return self._parent._cast(
                _3142.ConceptCouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3147.ConceptGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3147,
            )

            return self._parent._cast(
                _3147.ConceptGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3150.ConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3150,
            )

            return self._parent._cast(
                _3150.ConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3153.CouplingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3153,
            )

            return self._parent._cast(
                _3153.CouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def cvt_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3157.CVTCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3157,
            )

            return self._parent._cast(_3157.CVTCompoundSteadyStateSynchronousResponse)

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3159.CycloidalAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3159,
            )

            return self._parent._cast(
                _3159.CycloidalAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3165.CylindricalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3165,
            )

            return self._parent._cast(
                _3165.CylindricalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3171.FaceGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3171,
            )

            return self._parent._cast(
                _3171.FaceGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3173.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3173,
            )

            return self._parent._cast(
                _3173.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3176.GearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3176,
            )

            return self._parent._cast(
                _3176.GearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3180.HypoidGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3180,
            )

            return self._parent._cast(
                _3180.HypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3184.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3184,
            )

            return self._parent._cast(
                _3184.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3187.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3187,
            )

            return self._parent._cast(
                _3187.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3190.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3190,
            )

            return self._parent._cast(
                _3190.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3196.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3196,
            )

            return self._parent._cast(
                _3196.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3200.PlanetaryGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3200,
            )

            return self._parent._cast(
                _3200.PlanetaryGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3207.RollingRingAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3207,
            )

            return self._parent._cast(
                _3207.RollingRingAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3217.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3217,
            )

            return self._parent._cast(
                _3217.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3218.SpringDamperCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(
                _3218.SpringDamperCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3223.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3223,
            )

            return self._parent._cast(
                _3223.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3226.StraightBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3226,
            )

            return self._parent._cast(
                _3226.StraightBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3229.SynchroniserCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3229,
            )

            return self._parent._cast(
                _3229.SynchroniserCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3233.TorqueConverterCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3233,
            )

            return self._parent._cast(
                _3233.TorqueConverterCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3241.WormGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3241,
            )

            return self._parent._cast(
                _3241.WormGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3244.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3244,
            )

            return self._parent._cast(
                _3244.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3082.SpecialisedAssemblySteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SpecialisedAssemblySteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3082.SpecialisedAssemblySteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SpecialisedAssemblySteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyCompoundSteadyStateSynchronousResponse._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
        return self._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponse(
            self
        )
