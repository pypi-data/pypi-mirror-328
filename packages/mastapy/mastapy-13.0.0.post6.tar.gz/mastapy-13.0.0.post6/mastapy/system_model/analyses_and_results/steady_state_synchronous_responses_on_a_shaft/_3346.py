"""SpiralBevelGearSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3263,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.static_loads import _6953
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3251,
        _3279,
        _3305,
        _3322,
        _3270,
        _3324,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="SpiralBevelGearSteadyStateSynchronousResponseOnAShaft")


class SpiralBevelGearSteadyStateSynchronousResponseOnAShaft(
    _3263.BevelGearSteadyStateSynchronousResponseOnAShaft
):
    """SpiralBevelGearSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting SpiralBevelGearSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
            parent: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3263.BevelGearSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3263.BevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3251.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3251,
            )

            return self._parent._cast(
                _3251.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3279.ConicalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3279,
            )

            return self._parent._cast(
                _3279.ConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3305.GearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3305,
            )

            return self._parent._cast(_3305.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3322.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(
                _3322.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3270.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3270,
            )

            return self._parent._cast(
                _3270.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3324.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(_3324.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2543.SpiralBevelGear":
        """mastapy.system_model.part_model.gears.SpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6953.SpiralBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase

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
    ) -> "SpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_SpiralBevelGearSteadyStateSynchronousResponseOnAShaft(self)
