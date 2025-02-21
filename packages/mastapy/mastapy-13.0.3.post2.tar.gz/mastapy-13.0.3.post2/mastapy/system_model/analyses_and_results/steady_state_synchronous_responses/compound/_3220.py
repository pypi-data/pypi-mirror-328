"""PlanetaryConnectionCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3234,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "PlanetaryConnectionCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2307
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3088,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3140,
        _3172,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="PlanetaryConnectionCompoundSteadyStateSynchronousResponse"
)


class PlanetaryConnectionCompoundSteadyStateSynchronousResponse(
    _3234.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
):
    """PlanetaryConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting PlanetaryConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponse._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponse",
            parent: "PlanetaryConnectionCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponse._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3234.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3234.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponse._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3140.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3140,
            )

            return self._parent._cast(
                _3140.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponse._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3172.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3172,
            )

            return self._parent._cast(
                _3172.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponse._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponse._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponse._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_connection_compound_steady_state_synchronous_response(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponse._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "PlanetaryConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionCompoundSteadyStateSynchronousResponse._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "PlanetaryConnectionCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2307.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2307.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

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
    ) -> "List[_3088.PlanetaryConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.PlanetaryConnectionSteadyStateSynchronousResponse]

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
    ) -> "List[_3088.PlanetaryConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.PlanetaryConnectionSteadyStateSynchronousResponse]

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
    ) -> "PlanetaryConnectionCompoundSteadyStateSynchronousResponse._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponse":
        return self._Cast_PlanetaryConnectionCompoundSteadyStateSynchronousResponse(
            self
        )
