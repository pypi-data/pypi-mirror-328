"""CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3007,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
        "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2335
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3081,
        _2986,
        _3018,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7540, _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse"
)


class CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse(
    _3007.CoaxialConnectionSteadyStateSynchronousResponse
):
    """CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse",
            parent: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coaxial_connection_steady_state_synchronous_response(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse",
        ) -> "_3007.CoaxialConnectionSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3007.CoaxialConnectionSteadyStateSynchronousResponse
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse",
        ) -> "_3081.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3081,
            )

            return self._parent._cast(
                _3081.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse",
        ) -> "_2986.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2986,
            )

            return self._parent._cast(
                _2986.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse",
        ) -> "_3018.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3018,
            )

            return self._parent._cast(_3018.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse",
        ) -> "_7540.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse",
        ) -> "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2335.CycloidalDiscCentralBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection

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
    ) -> "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse":
        return self._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse(
            self
        )
