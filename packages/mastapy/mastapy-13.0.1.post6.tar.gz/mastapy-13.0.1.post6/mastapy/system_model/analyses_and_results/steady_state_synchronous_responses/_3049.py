"""InterMountableComponentConnectionSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3018,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
        "InterMountableComponentConnectionSteadyStateSynchronousResponse",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2281
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2987,
        _2992,
        _2994,
        _2999,
        _3004,
        _3009,
        _3012,
        _3015,
        _3020,
        _3023,
        _3030,
        _3037,
        _3042,
        _3046,
        _3050,
        _3053,
        _3056,
        _3064,
        _3074,
        _3076,
        _3083,
        _3086,
        _3092,
        _3095,
        _3104,
        _3110,
        _3113,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionSteadyStateSynchronousResponse"
)


class InterMountableComponentConnectionSteadyStateSynchronousResponse(
    _3018.ConnectionSteadyStateSynchronousResponse
):
    """InterMountableComponentConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
    )

    class _Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting InterMountableComponentConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
            parent: "InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def connection_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3018.ConnectionSteadyStateSynchronousResponse":
            return self._parent._cast(_3018.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_2987.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2987,
            )

            return self._parent._cast(
                _2987.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def belt_connection_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_2992.BeltConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2992,
            )

            return self._parent._cast(
                _2992.BeltConnectionSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_2994.BevelDifferentialGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2994,
            )

            return self._parent._cast(
                _2994.BevelDifferentialGearMeshSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_2999.BevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2999,
            )

            return self._parent._cast(_2999.BevelGearMeshSteadyStateSynchronousResponse)

        @property
        def clutch_connection_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3004.ClutchConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3004,
            )

            return self._parent._cast(
                _3004.ClutchConnectionSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3009.ConceptCouplingConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3009,
            )

            return self._parent._cast(
                _3009.ConceptCouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_mesh_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3012.ConceptGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3012,
            )

            return self._parent._cast(
                _3012.ConceptGearMeshSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3015.ConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3015,
            )

            return self._parent._cast(
                _3015.ConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def coupling_connection_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3020.CouplingConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3020,
            )

            return self._parent._cast(
                _3020.CouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def cvt_belt_connection_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3023.CVTBeltConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3023,
            )

            return self._parent._cast(
                _3023.CVTBeltConnectionSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3030.CylindricalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3030,
            )

            return self._parent._cast(
                _3030.CylindricalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3037.FaceGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3037,
            )

            return self._parent._cast(_3037.FaceGearMeshSteadyStateSynchronousResponse)

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3042.GearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3042,
            )

            return self._parent._cast(_3042.GearMeshSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3046.HypoidGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3046,
            )

            return self._parent._cast(
                _3046.HypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3050.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3050,
            )

            return self._parent._cast(
                _3050.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> (
            "_3053.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3053,
            )

            return self._parent._cast(
                _3053.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3056.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3056,
            )

            return self._parent._cast(
                _3056.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3064.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3064,
            )

            return self._parent._cast(
                _3064.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3074.RingPinsToDiscConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3074,
            )

            return self._parent._cast(
                _3074.RingPinsToDiscConnectionSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_connection_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3076.RollingRingConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3076,
            )

            return self._parent._cast(
                _3076.RollingRingConnectionSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3083.SpiralBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3083,
            )

            return self._parent._cast(
                _3083.SpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3086.SpringDamperConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(
                _3086.SpringDamperConnectionSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3092.StraightBevelDiffGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3092,
            )

            return self._parent._cast(
                _3092.StraightBevelDiffGearMeshSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3095.StraightBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3095,
            )

            return self._parent._cast(
                _3095.StraightBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3104.TorqueConverterConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3104,
            )

            return self._parent._cast(
                _3104.TorqueConverterConnectionSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3110.WormGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3110,
            )

            return self._parent._cast(_3110.WormGearMeshSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3113.ZerolBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3113,
            )

            return self._parent._cast(
                _3113.ZerolBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "InterMountableComponentConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "InterMountableComponentConnectionSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2281.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse":
        return (
            self._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse(
                self
            )
        )
