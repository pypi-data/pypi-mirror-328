"""TorqueConverterConnectionCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3154,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "TorqueConverterConnectionCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2352
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3104,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3181,
        _3151,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="TorqueConverterConnectionCompoundSteadyStateSynchronousResponse"
)


class TorqueConverterConnectionCompoundSteadyStateSynchronousResponse(
    _3154.CouplingConnectionCompoundSteadyStateSynchronousResponse
):
    """TorqueConverterConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting TorqueConverterConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponse",
            parent: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_steady_state_synchronous_response(
            self: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3154.CouplingConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3154.CouplingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3181.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3181,
            )

            return self._parent._cast(
                _3181.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3151.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3151,
            )

            return self._parent._cast(
                _3151.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response(
            self: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "TorqueConverterConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "TorqueConverterConnectionCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2352.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2352.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

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
    ) -> "List[_3104.TorqueConverterConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.TorqueConverterConnectionSteadyStateSynchronousResponse]

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
    ) -> "List[_3104.TorqueConverterConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.TorqueConverterConnectionSteadyStateSynchronousResponse]

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
    ) -> "TorqueConverterConnectionCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponse":
        return (
            self._Cast_TorqueConverterConnectionCompoundSteadyStateSynchronousResponse(
                self
            )
        )
