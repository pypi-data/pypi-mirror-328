"""CouplingConnectionSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3049,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "CouplingConnectionSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2346
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3004,
        _3009,
        _3064,
        _3086,
        _3104,
        _3018,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CouplingConnectionSteadyStateSynchronousResponse")


class CouplingConnectionSteadyStateSynchronousResponse(
    _3049.InterMountableComponentConnectionSteadyStateSynchronousResponse
):
    """CouplingConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionSteadyStateSynchronousResponse"
    )

    class _Cast_CouplingConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting CouplingConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
            parent: "CouplingConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3049.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3049.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3018.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3018,
            )

            return self._parent._cast(_3018.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3004.ClutchConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3004,
            )

            return self._parent._cast(
                _3004.ClutchConnectionSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3009.ConceptCouplingConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3009,
            )

            return self._parent._cast(
                _3009.ConceptCouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3064.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3064,
            )

            return self._parent._cast(
                _3064.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3086.SpringDamperConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(
                _3086.SpringDamperConnectionSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3104.TorqueConverterConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3104,
            )

            return self._parent._cast(
                _3104.TorqueConverterConnectionSteadyStateSynchronousResponse
            )

        @property
        def coupling_connection_steady_state_synchronous_response(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
        ) -> "CouplingConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CouplingConnectionSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2346.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

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
    ) -> "CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse":
        return self._Cast_CouplingConnectionSteadyStateSynchronousResponse(self)
