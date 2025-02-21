"""CVTBeltConnectionCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3125,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "CVTBeltConnectionCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3023,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3181,
        _3151,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CVTBeltConnectionCompoundSteadyStateSynchronousResponse")


class CVTBeltConnectionCompoundSteadyStateSynchronousResponse(
    _3125.BeltConnectionCompoundSteadyStateSynchronousResponse
):
    """CVTBeltConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting CVTBeltConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CVTBeltConnectionCompoundSteadyStateSynchronousResponse._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponse",
            parent: "CVTBeltConnectionCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def belt_connection_compound_steady_state_synchronous_response(
            self: "CVTBeltConnectionCompoundSteadyStateSynchronousResponse._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3125.BeltConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3125.BeltConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "CVTBeltConnectionCompoundSteadyStateSynchronousResponse._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3181.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3181,
            )

            return self._parent._cast(
                _3181.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "CVTBeltConnectionCompoundSteadyStateSynchronousResponse._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3151.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3151,
            )

            return self._parent._cast(
                _3151.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "CVTBeltConnectionCompoundSteadyStateSynchronousResponse._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTBeltConnectionCompoundSteadyStateSynchronousResponse._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionCompoundSteadyStateSynchronousResponse._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response(
            self: "CVTBeltConnectionCompoundSteadyStateSynchronousResponse._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "CVTBeltConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionCompoundSteadyStateSynchronousResponse._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CVTBeltConnectionCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3023.CVTBeltConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CVTBeltConnectionSteadyStateSynchronousResponse]

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
    ) -> "List[_3023.CVTBeltConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CVTBeltConnectionSteadyStateSynchronousResponse]

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
    ) -> "CVTBeltConnectionCompoundSteadyStateSynchronousResponse._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponse":
        return self._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponse(self)
