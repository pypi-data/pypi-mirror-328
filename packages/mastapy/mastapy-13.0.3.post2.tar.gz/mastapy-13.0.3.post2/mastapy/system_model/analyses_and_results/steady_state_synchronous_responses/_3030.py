"""ConceptCouplingConnectionSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3041,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ConceptCouplingConnectionSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2364
    from mastapy.system_model.analyses_and_results.static_loads import _6860
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3070,
        _3039,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ConceptCouplingConnectionSteadyStateSynchronousResponse")


class ConceptCouplingConnectionSteadyStateSynchronousResponse(
    _3041.CouplingConnectionSteadyStateSynchronousResponse
):
    """ConceptCouplingConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConceptCouplingConnectionSteadyStateSynchronousResponse",
    )

    class _Cast_ConceptCouplingConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting ConceptCouplingConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionSteadyStateSynchronousResponse",
            parent: "ConceptCouplingConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_connection_steady_state_synchronous_response(
            self: "ConceptCouplingConnectionSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3041.CouplingConnectionSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3041.CouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "ConceptCouplingConnectionSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3070.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3070,
            )

            return self._parent._cast(
                _3070.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "ConceptCouplingConnectionSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3039.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3039,
            )

            return self._parent._cast(_3039.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "ConceptCouplingConnectionSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConceptCouplingConnectionSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptCouplingConnectionSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingConnectionSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_steady_state_synchronous_response(
            self: "ConceptCouplingConnectionSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionSteadyStateSynchronousResponse",
        ) -> "ConceptCouplingConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ConceptCouplingConnectionSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2364.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6860.ConceptCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase

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
    ) -> "ConceptCouplingConnectionSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionSteadyStateSynchronousResponse":
        return self._Cast_ConceptCouplingConnectionSteadyStateSynchronousResponse(self)
