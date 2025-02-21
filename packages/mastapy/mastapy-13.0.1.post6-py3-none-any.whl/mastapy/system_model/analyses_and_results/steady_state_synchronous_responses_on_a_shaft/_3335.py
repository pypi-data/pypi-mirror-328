"""RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3310,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2341
    from mastapy.system_model.analyses_and_results.static_loads import _6945
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3280,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft"
)


class RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft(
    _3310.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
):
    """RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft",
            parent: "RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3310.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3310.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3280.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3280,
            )

            return self._parent._cast(
                _3280.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response_on_a_shaft(
            self: "RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2341.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6945.RingPinsToDiscConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsToDiscConnectionLoadCase

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
    ) -> "RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft":
        return (
            self._Cast_RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )
