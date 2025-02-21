"""CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3384,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3285,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3440,
        _3410,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
)


class CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
    _3384.BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
):
    """CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def belt_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3384.BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3384.BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3440.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3440,
            )

            return self._parent._cast(
                _3440.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3410.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3410,
            )

            return self._parent._cast(
                _3410.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_analysis(
            self: "CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3285.CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3285.CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
        return (
            self._Cast_CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )
