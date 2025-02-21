"""CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3472,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2269
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3269,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3419,
        _3378,
        _3410,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
)


class CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
    _3472.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
):
    """CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3472.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3472.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3378.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3378,
            )

            return self._parent._cast(
                _3378.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3410.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3410,
            )

            return self._parent._cast(
                _3410.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_analysis(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3419.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3419,
            )

            return self._parent._cast(
                _3419.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coaxial_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2269.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2269.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

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
    ) -> "List[_3269.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3269.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
        return (
            self._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )
