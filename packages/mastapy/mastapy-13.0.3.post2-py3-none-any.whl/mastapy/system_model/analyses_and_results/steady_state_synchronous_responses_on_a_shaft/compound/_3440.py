"""CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3420,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3310,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3493,
        _3399,
        _3431,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = (
    "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)


Self = TypeVar(
    "Self",
    bound="CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)


class CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
    _3420.CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft
):
    """CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3420.CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3420.CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3493.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3493,
            )

            return self._parent._cast(
                _3493.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3399.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3399,
            )

            return self._parent._cast(
                _3399.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3431.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3431,
            )

            return self._parent._cast(
                _3431.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3310.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3310.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
