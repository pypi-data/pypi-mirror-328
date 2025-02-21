"""CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3549,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2355
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3622,
        _3528,
        _3560,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = (
    "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
)


Self = TypeVar(
    "Self",
    bound="CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
)


class CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed(
    _3549.CoaxialConnectionSteadyStateSynchronousResponseAtASpeed
):
    """CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
            parent: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coaxial_connection_steady_state_synchronous_response_at_a_speed(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3549.CoaxialConnectionSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3549.CoaxialConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3622.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3622,
            )

            return self._parent._cast(
                _3622.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3528.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3528,
            )

            return self._parent._cast(
                _3528.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3560.ConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3560,
            )

            return self._parent._cast(
                _3560.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_at_a_speed(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2355.CycloidalDiscCentralBearingConnection":
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
    ) -> "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed(
            self
        )
