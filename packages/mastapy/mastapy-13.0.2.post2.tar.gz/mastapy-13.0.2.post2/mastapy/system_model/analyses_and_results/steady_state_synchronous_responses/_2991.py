"""AbstractAssemblySteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3071,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "AbstractAssemblySteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2441
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2996,
        _2998,
        _3001,
        _3003,
        _3008,
        _3010,
        _3014,
        _3019,
        _3021,
        _3024,
        _3030,
        _3033,
        _3034,
        _3039,
        _3046,
        _3049,
        _3051,
        _3055,
        _3059,
        _3062,
        _3065,
        _3074,
        _3076,
        _3083,
        _3086,
        _3090,
        _3092,
        _3096,
        _3101,
        _3104,
        _3111,
        _3114,
        _3119,
        _3122,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblySteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="AbstractAssemblySteadyStateSynchronousResponse")


class AbstractAssemblySteadyStateSynchronousResponse(
    _3071.PartSteadyStateSynchronousResponse
):
    """AbstractAssemblySteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblySteadyStateSynchronousResponse"
    )

    class _Cast_AbstractAssemblySteadyStateSynchronousResponse:
        """Special nested class for casting AbstractAssemblySteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
            parent: "AbstractAssemblySteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def part_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3071.PartSteadyStateSynchronousResponse":
            return self._parent._cast(_3071.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_2996.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2996,
            )

            return self._parent._cast(
                _2996.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def assembly_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_2998.AssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2998,
            )

            return self._parent._cast(_2998.AssemblySteadyStateSynchronousResponse)

        @property
        def belt_drive_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3001.BeltDriveSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3001,
            )

            return self._parent._cast(_3001.BeltDriveSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3003.BevelDifferentialGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3003,
            )

            return self._parent._cast(
                _3003.BevelDifferentialGearSetSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3008.BevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3008,
            )

            return self._parent._cast(_3008.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def bolted_joint_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3010.BoltedJointSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3010,
            )

            return self._parent._cast(_3010.BoltedJointSteadyStateSynchronousResponse)

        @property
        def clutch_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3014.ClutchSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3014,
            )

            return self._parent._cast(_3014.ClutchSteadyStateSynchronousResponse)

        @property
        def concept_coupling_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3019.ConceptCouplingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3019,
            )

            return self._parent._cast(
                _3019.ConceptCouplingSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3021.ConceptGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3021,
            )

            return self._parent._cast(
                _3021.ConceptGearSetSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3024.ConicalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3024,
            )

            return self._parent._cast(
                _3024.ConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def coupling_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3030.CouplingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3030,
            )

            return self._parent._cast(_3030.CouplingSteadyStateSynchronousResponse)

        @property
        def cvt_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3033.CVTSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3033,
            )

            return self._parent._cast(_3033.CVTSteadyStateSynchronousResponse)

        @property
        def cycloidal_assembly_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3034.CycloidalAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3034,
            )

            return self._parent._cast(
                _3034.CycloidalAssemblySteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3039.CylindricalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3039,
            )

            return self._parent._cast(
                _3039.CylindricalGearSetSteadyStateSynchronousResponse
            )

        @property
        def face_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3046.FaceGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3046,
            )

            return self._parent._cast(_3046.FaceGearSetSteadyStateSynchronousResponse)

        @property
        def flexible_pin_assembly_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3049.FlexiblePinAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3049,
            )

            return self._parent._cast(
                _3049.FlexiblePinAssemblySteadyStateSynchronousResponse
            )

        @property
        def gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3051.GearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3051,
            )

            return self._parent._cast(_3051.GearSetSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3055.HypoidGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3055,
            )

            return self._parent._cast(_3055.HypoidGearSetSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> (
            "_3059.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3059,
            )

            return self._parent._cast(
                _3059.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> (
            "_3062.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3062,
            )

            return self._parent._cast(
                _3062.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3065.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(
                _3065.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3074.PartToPartShearCouplingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3074,
            )

            return self._parent._cast(
                _3074.PartToPartShearCouplingSteadyStateSynchronousResponse
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3076.PlanetaryGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3076,
            )

            return self._parent._cast(
                _3076.PlanetaryGearSetSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3083.RollingRingAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3083,
            )

            return self._parent._cast(
                _3083.RollingRingAssemblySteadyStateSynchronousResponse
            )

        @property
        def root_assembly_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3086.RootAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.RootAssemblySteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3090.SpecialisedAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3090,
            )

            return self._parent._cast(
                _3090.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3092.SpiralBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3092,
            )

            return self._parent._cast(
                _3092.SpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3096.SpringDamperSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3096,
            )

            return self._parent._cast(_3096.SpringDamperSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3101.StraightBevelDiffGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3101,
            )

            return self._parent._cast(
                _3101.StraightBevelDiffGearSetSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3104.StraightBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3104,
            )

            return self._parent._cast(
                _3104.StraightBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3111.SynchroniserSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3111,
            )

            return self._parent._cast(_3111.SynchroniserSteadyStateSynchronousResponse)

        @property
        def torque_converter_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3114.TorqueConverterSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3114,
            )

            return self._parent._cast(
                _3114.TorqueConverterSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3119.WormGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3119,
            )

            return self._parent._cast(_3119.WormGearSetSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "_3122.ZerolBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3122,
            )

            return self._parent._cast(
                _3122.ZerolBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
        ) -> "AbstractAssemblySteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
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
        instance_to_wrap: "AbstractAssemblySteadyStateSynchronousResponse.TYPE",
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
    ) -> "AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse":
        return self._Cast_AbstractAssemblySteadyStateSynchronousResponse(self)
