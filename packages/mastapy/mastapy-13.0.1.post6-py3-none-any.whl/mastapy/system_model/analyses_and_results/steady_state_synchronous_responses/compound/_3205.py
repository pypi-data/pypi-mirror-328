"""RingPinsCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3193,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "RingPinsCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2570
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3073,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3141,
        _3195,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="RingPinsCompoundSteadyStateSynchronousResponse")


class RingPinsCompoundSteadyStateSynchronousResponse(
    _3193.MountableComponentCompoundSteadyStateSynchronousResponse
):
    """RingPinsCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _RING_PINS_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_RingPinsCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting RingPinsCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "RingPinsCompoundSteadyStateSynchronousResponse._Cast_RingPinsCompoundSteadyStateSynchronousResponse",
            parent: "RingPinsCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "RingPinsCompoundSteadyStateSynchronousResponse._Cast_RingPinsCompoundSteadyStateSynchronousResponse",
        ) -> "_3193.MountableComponentCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3193.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "RingPinsCompoundSteadyStateSynchronousResponse._Cast_RingPinsCompoundSteadyStateSynchronousResponse",
        ) -> "_3141.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3141,
            )

            return self._parent._cast(
                _3141.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "RingPinsCompoundSteadyStateSynchronousResponse._Cast_RingPinsCompoundSteadyStateSynchronousResponse",
        ) -> "_3195.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3195,
            )

            return self._parent._cast(_3195.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "RingPinsCompoundSteadyStateSynchronousResponse._Cast_RingPinsCompoundSteadyStateSynchronousResponse",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RingPinsCompoundSteadyStateSynchronousResponse._Cast_RingPinsCompoundSteadyStateSynchronousResponse",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsCompoundSteadyStateSynchronousResponse._Cast_RingPinsCompoundSteadyStateSynchronousResponse",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def ring_pins_compound_steady_state_synchronous_response(
            self: "RingPinsCompoundSteadyStateSynchronousResponse._Cast_RingPinsCompoundSteadyStateSynchronousResponse",
        ) -> "RingPinsCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "RingPinsCompoundSteadyStateSynchronousResponse._Cast_RingPinsCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "RingPinsCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2570.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3073.RingPinsSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.RingPinsSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3073.RingPinsSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.RingPinsSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RingPinsCompoundSteadyStateSynchronousResponse._Cast_RingPinsCompoundSteadyStateSynchronousResponse":
        return self._Cast_RingPinsCompoundSteadyStateSynchronousResponse(self)
