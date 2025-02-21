"""PlanetCarrierSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3581,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "PlanetCarrierSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2469
    from mastapy.system_model.analyses_and_results.static_loads import _6936
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3529,
        _3583,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="PlanetCarrierSteadyStateSynchronousResponseAtASpeed")


class PlanetCarrierSteadyStateSynchronousResponseAtASpeed(
    _3581.MountableComponentSteadyStateSynchronousResponseAtASpeed
):
    """PlanetCarrierSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetCarrierSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_PlanetCarrierSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting PlanetCarrierSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "PlanetCarrierSteadyStateSynchronousResponseAtASpeed._Cast_PlanetCarrierSteadyStateSynchronousResponseAtASpeed",
            parent: "PlanetCarrierSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "PlanetCarrierSteadyStateSynchronousResponseAtASpeed._Cast_PlanetCarrierSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3581.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3581.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "PlanetCarrierSteadyStateSynchronousResponseAtASpeed._Cast_PlanetCarrierSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3529.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3529,
            )

            return self._parent._cast(
                _3529.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "PlanetCarrierSteadyStateSynchronousResponseAtASpeed._Cast_PlanetCarrierSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3583.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(_3583.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "PlanetCarrierSteadyStateSynchronousResponseAtASpeed._Cast_PlanetCarrierSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetCarrierSteadyStateSynchronousResponseAtASpeed._Cast_PlanetCarrierSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetCarrierSteadyStateSynchronousResponseAtASpeed._Cast_PlanetCarrierSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetCarrierSteadyStateSynchronousResponseAtASpeed._Cast_PlanetCarrierSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierSteadyStateSynchronousResponseAtASpeed._Cast_PlanetCarrierSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planet_carrier_steady_state_synchronous_response_at_a_speed(
            self: "PlanetCarrierSteadyStateSynchronousResponseAtASpeed._Cast_PlanetCarrierSteadyStateSynchronousResponseAtASpeed",
        ) -> "PlanetCarrierSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierSteadyStateSynchronousResponseAtASpeed._Cast_PlanetCarrierSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "PlanetCarrierSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2469.PlanetCarrier":
        """mastapy.system_model.part_model.PlanetCarrier

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6936.PlanetCarrierLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase

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
    ) -> "PlanetCarrierSteadyStateSynchronousResponseAtASpeed._Cast_PlanetCarrierSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_PlanetCarrierSteadyStateSynchronousResponseAtASpeed(self)
