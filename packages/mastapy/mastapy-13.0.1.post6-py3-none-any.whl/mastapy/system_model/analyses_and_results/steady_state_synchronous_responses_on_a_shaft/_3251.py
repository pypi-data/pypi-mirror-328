"""AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3279,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2513
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3258,
        _3259,
        _3260,
        _3263,
        _3309,
        _3346,
        _3353,
        _3356,
        _3357,
        _3358,
        _3374,
        _3305,
        _3322,
        _3270,
        _3324,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft"
)


class AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft(
    _3279.ConicalGearSteadyStateSynchronousResponseOnAShaft
):
    """AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
            parent: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3279.ConicalGearSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3279.ConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3305.GearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3305,
            )

            return self._parent._cast(_3305.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3322.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(
                _3322.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3270.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3270,
            )

            return self._parent._cast(
                _3270.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3324.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(_3324.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3258.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3258,
            )

            return self._parent._cast(
                _3258.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3259.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3259,
            )

            return self._parent._cast(
                _3259.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3260.BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3260,
            )

            return self._parent._cast(
                _3260.BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3263.BevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3263,
            )

            return self._parent._cast(
                _3263.BevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3309.HypoidGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3309,
            )

            return self._parent._cast(
                _3309.HypoidGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3346.SpiralBevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3346,
            )

            return self._parent._cast(
                _3346.SpiralBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3353.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3353,
            )

            return self._parent._cast(
                _3353.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3356.StraightBevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3356,
            )

            return self._parent._cast(
                _3356.StraightBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3357.StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3357,
            )

            return self._parent._cast(
                _3357.StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3358.StraightBevelSunGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3358,
            )

            return self._parent._cast(
                _3358.StraightBevelSunGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3374.ZerolBevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3374,
            )

            return self._parent._cast(
                _3374.ZerolBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2513.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft(
            self
        )
