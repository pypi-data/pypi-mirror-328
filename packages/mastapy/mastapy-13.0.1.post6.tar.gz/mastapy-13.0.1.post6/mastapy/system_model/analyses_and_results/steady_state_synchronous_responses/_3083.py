"""SpiralBevelGearMeshSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2999,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "SpiralBevelGearMeshSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323
    from mastapy.system_model.analyses_and_results.static_loads import _6955
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2987,
        _3015,
        _3042,
        _3049,
        _3018,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshSteadyStateSynchronousResponse")


class SpiralBevelGearMeshSteadyStateSynchronousResponse(
    _2999.BevelGearMeshSteadyStateSynchronousResponse
):
    """SpiralBevelGearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMeshSteadyStateSynchronousResponse"
    )

    class _Cast_SpiralBevelGearMeshSteadyStateSynchronousResponse:
        """Special nested class for casting SpiralBevelGearMeshSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponse",
            parent: "SpiralBevelGearMeshSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_steady_state_synchronous_response(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_2999.BevelGearMeshSteadyStateSynchronousResponse":
            return self._parent._cast(_2999.BevelGearMeshSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_2987.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2987,
            )

            return self._parent._cast(
                _2987.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3015.ConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3015,
            )

            return self._parent._cast(
                _3015.ConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3042.GearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3042,
            )

            return self._parent._cast(_3042.GearMeshSteadyStateSynchronousResponse)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3049.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3049,
            )

            return self._parent._cast(
                _3049.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3018.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3018,
            )

            return self._parent._cast(_3018.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "SpiralBevelGearMeshSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponse",
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
        instance_to_wrap: "SpiralBevelGearMeshSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2323.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6955.SpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponse":
        return self._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponse(self)
