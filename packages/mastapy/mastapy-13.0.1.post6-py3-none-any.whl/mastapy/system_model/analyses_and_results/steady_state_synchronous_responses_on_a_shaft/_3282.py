"""CouplingConnectionSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3310,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2346
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3266,
        _3271,
        _3325,
        _3347,
        _3363,
        _3280,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="CouplingConnectionSteadyStateSynchronousResponseOnAShaft")


class CouplingConnectionSteadyStateSynchronousResponseOnAShaft(
    _3310.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
):
    """CouplingConnectionSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CouplingConnectionSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
            parent: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3310.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3310.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3280.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3280,
            )

            return self._parent._cast(
                _3280.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3266.ClutchConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3266,
            )

            return self._parent._cast(
                _3266.ClutchConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3271.ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3271,
            )

            return self._parent._cast(
                _3271.ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3325.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3325,
            )

            return self._parent._cast(
                _3325.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3347.SpringDamperConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3347,
            )

            return self._parent._cast(
                _3347.SpringDamperConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3363.TorqueConverterConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3363,
            )

            return self._parent._cast(
                _3363.TorqueConverterConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "CouplingConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft.TYPE",
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
    ) -> "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft(self)
