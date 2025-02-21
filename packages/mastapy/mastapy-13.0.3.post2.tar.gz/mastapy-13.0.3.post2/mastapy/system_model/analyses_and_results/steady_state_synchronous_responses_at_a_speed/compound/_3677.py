"""ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3693,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2362
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3546,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3720,
        _3690,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
)


class ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed(
    _3693.CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
):
    """ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3693.CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3693.CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3720.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3720,
            )

            return self._parent._cast(
                _3720.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3690.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3690,
            )

            return self._parent._cast(
                _3690.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_analysis(
            self: "ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2362.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2362.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

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
    ) -> "List[_3546.ClutchConnectionSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.ClutchConnectionSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3546.ClutchConnectionSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.ClutchConnectionSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        return (
            self._Cast_ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed(
                self
            )
        )
