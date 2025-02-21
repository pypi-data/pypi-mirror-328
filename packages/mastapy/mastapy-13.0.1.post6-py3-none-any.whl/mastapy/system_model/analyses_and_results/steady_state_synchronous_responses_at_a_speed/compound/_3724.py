"""RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3699,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2341
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3594,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3669,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self",
    bound="RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
)


class RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed(
    _3699.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
):
    """RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3699.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3699.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3669.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3669,
            )

            return self._parent._cast(
                _3669.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_analysis(
            self: "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2341.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3594.RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3594.RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
