"""WormGearMeshSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3042,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "WormGearMeshSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2329
    from mastapy.system_model.analyses_and_results.static_loads import _6984
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3049,
        _3018,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="WormGearMeshSteadyStateSynchronousResponse")


class WormGearMeshSteadyStateSynchronousResponse(
    _3042.GearMeshSteadyStateSynchronousResponse
):
    """WormGearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_WormGearMeshSteadyStateSynchronousResponse"
    )

    class _Cast_WormGearMeshSteadyStateSynchronousResponse:
        """Special nested class for casting WormGearMeshSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "WormGearMeshSteadyStateSynchronousResponse._Cast_WormGearMeshSteadyStateSynchronousResponse",
            parent: "WormGearMeshSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "WormGearMeshSteadyStateSynchronousResponse._Cast_WormGearMeshSteadyStateSynchronousResponse",
        ) -> "_3042.GearMeshSteadyStateSynchronousResponse":
            return self._parent._cast(_3042.GearMeshSteadyStateSynchronousResponse)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "WormGearMeshSteadyStateSynchronousResponse._Cast_WormGearMeshSteadyStateSynchronousResponse",
        ) -> "_3049.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3049,
            )

            return self._parent._cast(
                _3049.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "WormGearMeshSteadyStateSynchronousResponse._Cast_WormGearMeshSteadyStateSynchronousResponse",
        ) -> "_3018.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3018,
            )

            return self._parent._cast(_3018.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "WormGearMeshSteadyStateSynchronousResponse._Cast_WormGearMeshSteadyStateSynchronousResponse",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "WormGearMeshSteadyStateSynchronousResponse._Cast_WormGearMeshSteadyStateSynchronousResponse",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "WormGearMeshSteadyStateSynchronousResponse._Cast_WormGearMeshSteadyStateSynchronousResponse",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearMeshSteadyStateSynchronousResponse._Cast_WormGearMeshSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshSteadyStateSynchronousResponse._Cast_WormGearMeshSteadyStateSynchronousResponse",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_steady_state_synchronous_response(
            self: "WormGearMeshSteadyStateSynchronousResponse._Cast_WormGearMeshSteadyStateSynchronousResponse",
        ) -> "WormGearMeshSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "WormGearMeshSteadyStateSynchronousResponse._Cast_WormGearMeshSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "WormGearMeshSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2329.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6984.WormGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase

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
    ) -> "WormGearMeshSteadyStateSynchronousResponse._Cast_WormGearMeshSteadyStateSynchronousResponse":
        return self._Cast_WormGearMeshSteadyStateSynchronousResponse(self)
