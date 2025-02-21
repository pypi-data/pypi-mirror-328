"""AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3559,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3538,
        _3539,
        _3540,
        _3543,
        _3589,
        _3626,
        _3633,
        _3636,
        _3637,
        _3638,
        _3654,
        _3585,
        _3602,
        _3550,
        _3604,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed"
)


class AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed(
    _3559.ConicalGearSteadyStateSynchronousResponseAtASpeed
):
    """AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
            parent: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3559.ConicalGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3559.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3585.GearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3585,
            )

            return self._parent._cast(_3585.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3602.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3602,
            )

            return self._parent._cast(
                _3602.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3550.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3550,
            )

            return self._parent._cast(
                _3550.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3604.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(_3604.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3538.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3538,
            )

            return self._parent._cast(
                _3538.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3539.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3539,
            )

            return self._parent._cast(
                _3539.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3540.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3540,
            )

            return self._parent._cast(
                _3540.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3543.BevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3543,
            )

            return self._parent._cast(
                _3543.BevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3589.HypoidGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3589,
            )

            return self._parent._cast(
                _3589.HypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3626.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3626,
            )

            return self._parent._cast(
                _3626.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3633.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3633,
            )

            return self._parent._cast(
                _3633.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3636.StraightBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3636,
            )

            return self._parent._cast(
                _3636.StraightBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3637.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3637,
            )

            return self._parent._cast(
                _3637.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3638.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3638,
            )

            return self._parent._cast(
                _3638.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3654.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3654,
            )

            return self._parent._cast(
                _3654.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.AGMAGleasonConicalGear":
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
    ) -> "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed(
            self
        )
