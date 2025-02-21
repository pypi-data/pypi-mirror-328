"""RollingRingSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3542,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "RollingRingSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2596
    from mastapy.system_model.analyses_and_results.static_loads import _6947
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3581,
        _3529,
        _3583,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="RollingRingSteadyStateSynchronousResponseAtASpeed")


class RollingRingSteadyStateSynchronousResponseAtASpeed(
    _3542.CouplingHalfSteadyStateSynchronousResponseAtASpeed
):
    """RollingRingSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_RollingRingSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting RollingRingSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "RollingRingSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingSteadyStateSynchronousResponseAtASpeed",
            parent: "RollingRingSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "RollingRingSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3542.CouplingHalfSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3542.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "RollingRingSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3581.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3581,
            )

            return self._parent._cast(
                _3581.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "RollingRingSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3529.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3529,
            )

            return self._parent._cast(
                _3529.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "RollingRingSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3583.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(_3583.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def rolling_ring_steady_state_synchronous_response_at_a_speed(
            self: "RollingRingSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingSteadyStateSynchronousResponseAtASpeed",
        ) -> "RollingRingSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "RollingRingSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "RollingRingSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2596.RollingRing":
        """mastapy.system_model.part_model.couplings.RollingRing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6947.RollingRingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(
        self: Self,
    ) -> "List[RollingRingSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.RollingRingSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_RollingRingSteadyStateSynchronousResponseAtASpeed(self)
