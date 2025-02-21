"""PowerLoadSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3389,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "PowerLoadSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2492
    from mastapy.system_model.analyses_and_results.static_loads import _6961
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3343,
        _3291,
        _3345,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="PowerLoadSteadyStateSynchronousResponseOnAShaft")


class PowerLoadSteadyStateSynchronousResponseOnAShaft(
    _3389.VirtualComponentSteadyStateSynchronousResponseOnAShaft
):
    """PowerLoadSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PowerLoadSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_PowerLoadSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting PowerLoadSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "PowerLoadSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadSteadyStateSynchronousResponseOnAShaft",
            parent: "PowerLoadSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def virtual_component_steady_state_synchronous_response_on_a_shaft(
            self: "PowerLoadSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3389.VirtualComponentSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3389.VirtualComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "PowerLoadSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3343.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3343,
            )

            return self._parent._cast(
                _3343.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "PowerLoadSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3291.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3291,
            )

            return self._parent._cast(
                _3291.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "PowerLoadSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3345.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(_3345.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "PowerLoadSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PowerLoadSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PowerLoadSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PowerLoadSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def power_load_steady_state_synchronous_response_on_a_shaft(
            self: "PowerLoadSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadSteadyStateSynchronousResponseOnAShaft",
        ) -> "PowerLoadSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "PowerLoadSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "PowerLoadSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2492.PowerLoad":
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
    def component_load_case(self: Self) -> "_6961.PowerLoadLoadCase":
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
    ) -> "PowerLoadSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_PowerLoadSteadyStateSynchronousResponseOnAShaft(self)
