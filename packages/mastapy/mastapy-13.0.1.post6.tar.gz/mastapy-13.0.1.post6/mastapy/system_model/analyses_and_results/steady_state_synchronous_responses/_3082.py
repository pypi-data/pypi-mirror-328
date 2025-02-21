"""SpecialisedAssemblySteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2983,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "SpecialisedAssemblySteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2476
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2988,
        _2993,
        _2995,
        _3000,
        _3002,
        _3006,
        _3011,
        _3013,
        _3016,
        _3022,
        _3025,
        _3026,
        _3031,
        _3038,
        _3041,
        _3043,
        _3047,
        _3051,
        _3054,
        _3057,
        _3066,
        _3068,
        _3075,
        _3084,
        _3088,
        _3093,
        _3096,
        _3103,
        _3106,
        _3111,
        _3114,
        _3063,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblySteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="SpecialisedAssemblySteadyStateSynchronousResponse")


class SpecialisedAssemblySteadyStateSynchronousResponse(
    _2983.AbstractAssemblySteadyStateSynchronousResponse
):
    """SpecialisedAssemblySteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblySteadyStateSynchronousResponse"
    )

    class _Cast_SpecialisedAssemblySteadyStateSynchronousResponse:
        """Special nested class for casting SpecialisedAssemblySteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
            parent: "SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_2983.AbstractAssemblySteadyStateSynchronousResponse":
            return self._parent._cast(
                _2983.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3063.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3063,
            )

            return self._parent._cast(_3063.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_2988.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2988,
            )

            return self._parent._cast(
                _2988.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def belt_drive_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_2993.BeltDriveSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2993,
            )

            return self._parent._cast(_2993.BeltDriveSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_2995.BevelDifferentialGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2995,
            )

            return self._parent._cast(
                _2995.BevelDifferentialGearSetSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3000.BevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3000,
            )

            return self._parent._cast(_3000.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def bolted_joint_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3002.BoltedJointSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3002,
            )

            return self._parent._cast(_3002.BoltedJointSteadyStateSynchronousResponse)

        @property
        def clutch_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3006.ClutchSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(_3006.ClutchSteadyStateSynchronousResponse)

        @property
        def concept_coupling_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3011.ConceptCouplingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3011,
            )

            return self._parent._cast(
                _3011.ConceptCouplingSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3013.ConceptGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3013,
            )

            return self._parent._cast(
                _3013.ConceptGearSetSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3016.ConicalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(
                _3016.ConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def coupling_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3022.CouplingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3022,
            )

            return self._parent._cast(_3022.CouplingSteadyStateSynchronousResponse)

        @property
        def cvt_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3025.CVTSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3025,
            )

            return self._parent._cast(_3025.CVTSteadyStateSynchronousResponse)

        @property
        def cycloidal_assembly_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3026.CycloidalAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3026,
            )

            return self._parent._cast(
                _3026.CycloidalAssemblySteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3031.CylindricalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3031,
            )

            return self._parent._cast(
                _3031.CylindricalGearSetSteadyStateSynchronousResponse
            )

        @property
        def face_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3038.FaceGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3038,
            )

            return self._parent._cast(_3038.FaceGearSetSteadyStateSynchronousResponse)

        @property
        def flexible_pin_assembly_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3041.FlexiblePinAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3041,
            )

            return self._parent._cast(
                _3041.FlexiblePinAssemblySteadyStateSynchronousResponse
            )

        @property
        def gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3043.GearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3043,
            )

            return self._parent._cast(_3043.GearSetSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3047.HypoidGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3047,
            )

            return self._parent._cast(_3047.HypoidGearSetSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> (
            "_3051.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3051,
            )

            return self._parent._cast(
                _3051.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> (
            "_3054.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3054,
            )

            return self._parent._cast(
                _3054.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3057.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3057,
            )

            return self._parent._cast(
                _3057.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3066.PartToPartShearCouplingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3066,
            )

            return self._parent._cast(
                _3066.PartToPartShearCouplingSteadyStateSynchronousResponse
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3068.PlanetaryGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3068,
            )

            return self._parent._cast(
                _3068.PlanetaryGearSetSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3075.RollingRingAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3075,
            )

            return self._parent._cast(
                _3075.RollingRingAssemblySteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3084.SpiralBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(
                _3084.SpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3088.SpringDamperSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3088,
            )

            return self._parent._cast(_3088.SpringDamperSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3093.StraightBevelDiffGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3093,
            )

            return self._parent._cast(
                _3093.StraightBevelDiffGearSetSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3096.StraightBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3096,
            )

            return self._parent._cast(
                _3096.StraightBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3103.SynchroniserSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3103,
            )

            return self._parent._cast(_3103.SynchroniserSteadyStateSynchronousResponse)

        @property
        def torque_converter_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3106.TorqueConverterSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3106,
            )

            return self._parent._cast(
                _3106.TorqueConverterSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3111.WormGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3111,
            )

            return self._parent._cast(_3111.WormGearSetSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "_3114.ZerolBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3114,
            )

            return self._parent._cast(
                _3114.ZerolBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "SpecialisedAssemblySteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
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
        instance_to_wrap: "SpecialisedAssemblySteadyStateSynchronousResponse.TYPE",
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
    ) -> "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse":
        return self._Cast_SpecialisedAssemblySteadyStateSynchronousResponse(self)
