"""PowerLoadSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3627,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "PowerLoadSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2472
    from mastapy.system_model.analyses_and_results.static_loads import _6940
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3581,
        _3529,
        _3583,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="PowerLoadSteadyStateSynchronousResponseAtASpeed")


class PowerLoadSteadyStateSynchronousResponseAtASpeed(
    _3627.VirtualComponentSteadyStateSynchronousResponseAtASpeed
):
    """PowerLoadSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PowerLoadSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_PowerLoadSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting PowerLoadSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "PowerLoadSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadSteadyStateSynchronousResponseAtASpeed",
            parent: "PowerLoadSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def virtual_component_steady_state_synchronous_response_at_a_speed(
            self: "PowerLoadSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3627.VirtualComponentSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3627.VirtualComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "PowerLoadSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3581.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3581,
            )

            return self._parent._cast(
                _3581.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "PowerLoadSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3529.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3529,
            )

            return self._parent._cast(
                _3529.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "PowerLoadSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3583.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(_3583.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "PowerLoadSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PowerLoadSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PowerLoadSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PowerLoadSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def power_load_steady_state_synchronous_response_at_a_speed(
            self: "PowerLoadSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadSteadyStateSynchronousResponseAtASpeed",
        ) -> "PowerLoadSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "PowerLoadSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "PowerLoadSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2472.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6940.PowerLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase

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
    ) -> "PowerLoadSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_PowerLoadSteadyStateSynchronousResponseAtASpeed(self)
