"""RingPinsSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3602,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "RingPinsSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2590
    from mastapy.system_model.analyses_and_results.static_loads import _6965
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3550,
        _3604,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="RingPinsSteadyStateSynchronousResponseAtASpeed")


class RingPinsSteadyStateSynchronousResponseAtASpeed(
    _3602.MountableComponentSteadyStateSynchronousResponseAtASpeed
):
    """RingPinsSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _RING_PINS_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_RingPinsSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting RingPinsSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "RingPinsSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsSteadyStateSynchronousResponseAtASpeed",
            parent: "RingPinsSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "RingPinsSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3602.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3602.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "RingPinsSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3550.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3550,
            )

            return self._parent._cast(
                _3550.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "RingPinsSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3604.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(_3604.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "RingPinsSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RingPinsSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RingPinsSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def ring_pins_steady_state_synchronous_response_at_a_speed(
            self: "RingPinsSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsSteadyStateSynchronousResponseAtASpeed",
        ) -> "RingPinsSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "RingPinsSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "RingPinsSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2590.RingPins":
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
    def component_load_case(self: Self) -> "_6965.RingPinsLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RingPinsSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_RingPinsSteadyStateSynchronousResponseAtASpeed(self)
