"""OilSealSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3540,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "OilSealSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.static_loads import _6927
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3581,
        _3529,
        _3583,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("OilSealSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="OilSealSteadyStateSynchronousResponseAtASpeed")


class OilSealSteadyStateSynchronousResponseAtASpeed(
    _3540.ConnectorSteadyStateSynchronousResponseAtASpeed
):
    """OilSealSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_OilSealSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_OilSealSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting OilSealSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "OilSealSteadyStateSynchronousResponseAtASpeed._Cast_OilSealSteadyStateSynchronousResponseAtASpeed",
            parent: "OilSealSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def connector_steady_state_synchronous_response_at_a_speed(
            self: "OilSealSteadyStateSynchronousResponseAtASpeed._Cast_OilSealSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3540.ConnectorSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3540.ConnectorSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "OilSealSteadyStateSynchronousResponseAtASpeed._Cast_OilSealSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3581.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3581,
            )

            return self._parent._cast(
                _3581.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "OilSealSteadyStateSynchronousResponseAtASpeed._Cast_OilSealSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3529.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3529,
            )

            return self._parent._cast(
                _3529.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "OilSealSteadyStateSynchronousResponseAtASpeed._Cast_OilSealSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3583.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(_3583.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "OilSealSteadyStateSynchronousResponseAtASpeed._Cast_OilSealSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "OilSealSteadyStateSynchronousResponseAtASpeed._Cast_OilSealSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "OilSealSteadyStateSynchronousResponseAtASpeed._Cast_OilSealSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "OilSealSteadyStateSynchronousResponseAtASpeed._Cast_OilSealSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealSteadyStateSynchronousResponseAtASpeed._Cast_OilSealSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def oil_seal_steady_state_synchronous_response_at_a_speed(
            self: "OilSealSteadyStateSynchronousResponseAtASpeed._Cast_OilSealSteadyStateSynchronousResponseAtASpeed",
        ) -> "OilSealSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "OilSealSteadyStateSynchronousResponseAtASpeed._Cast_OilSealSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "OilSealSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2466.OilSeal":
        """mastapy.system_model.part_model.OilSeal

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6927.OilSealLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase

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
    ) -> "OilSealSteadyStateSynchronousResponseAtASpeed._Cast_OilSealSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_OilSealSteadyStateSynchronousResponseAtASpeed(self)
