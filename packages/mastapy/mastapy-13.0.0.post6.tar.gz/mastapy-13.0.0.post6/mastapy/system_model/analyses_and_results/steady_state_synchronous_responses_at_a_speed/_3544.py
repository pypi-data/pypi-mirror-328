"""CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3513,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2273
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3569,
        _3539,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7540, _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed")


class CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed(
    _3513.BeltConnectionSteadyStateSynchronousResponseAtASpeed
):
    """CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed",
            parent: "CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def belt_connection_steady_state_synchronous_response_at_a_speed(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3513.BeltConnectionSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3513.BeltConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3569.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3569,
            )

            return self._parent._cast(
                _3569.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3539.ConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3539,
            )

            return self._parent._cast(
                _3539.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7540.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_steady_state_synchronous_response_at_a_speed(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2273.CVTBeltConnection":
        """mastapy.system_model.connections_and_sockets.CVTBeltConnection

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
    ) -> "CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed(self)
