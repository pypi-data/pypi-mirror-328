"""RollingRingConnectionSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3049,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "RollingRingConnectionSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2292
    from mastapy.system_model.analyses_and_results.static_loads import _6947
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3018,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingConnectionSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="RollingRingConnectionSteadyStateSynchronousResponse")


class RollingRingConnectionSteadyStateSynchronousResponse(
    _3049.InterMountableComponentConnectionSteadyStateSynchronousResponse
):
    """RollingRingConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingConnectionSteadyStateSynchronousResponse"
    )

    class _Cast_RollingRingConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting RollingRingConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "RollingRingConnectionSteadyStateSynchronousResponse._Cast_RollingRingConnectionSteadyStateSynchronousResponse",
            parent: "RollingRingConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "RollingRingConnectionSteadyStateSynchronousResponse._Cast_RollingRingConnectionSteadyStateSynchronousResponse",
        ) -> "_3049.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3049.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "RollingRingConnectionSteadyStateSynchronousResponse._Cast_RollingRingConnectionSteadyStateSynchronousResponse",
        ) -> "_3018.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3018,
            )

            return self._parent._cast(_3018.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "RollingRingConnectionSteadyStateSynchronousResponse._Cast_RollingRingConnectionSteadyStateSynchronousResponse",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RollingRingConnectionSteadyStateSynchronousResponse._Cast_RollingRingConnectionSteadyStateSynchronousResponse",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RollingRingConnectionSteadyStateSynchronousResponse._Cast_RollingRingConnectionSteadyStateSynchronousResponse",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingConnectionSteadyStateSynchronousResponse._Cast_RollingRingConnectionSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingConnectionSteadyStateSynchronousResponse._Cast_RollingRingConnectionSteadyStateSynchronousResponse",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def rolling_ring_connection_steady_state_synchronous_response(
            self: "RollingRingConnectionSteadyStateSynchronousResponse._Cast_RollingRingConnectionSteadyStateSynchronousResponse",
        ) -> "RollingRingConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "RollingRingConnectionSteadyStateSynchronousResponse._Cast_RollingRingConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "RollingRingConnectionSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2292.RollingRingConnection":
        """mastapy.system_model.connections_and_sockets.RollingRingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6947.RollingRingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(
        self: Self,
    ) -> "List[RollingRingConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.RollingRingConnectionSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingConnectionSteadyStateSynchronousResponse._Cast_RollingRingConnectionSteadyStateSynchronousResponse":
        return self._Cast_RollingRingConnectionSteadyStateSynchronousResponse(self)
