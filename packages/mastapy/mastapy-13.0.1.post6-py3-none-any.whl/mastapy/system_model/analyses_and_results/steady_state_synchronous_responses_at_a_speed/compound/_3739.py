"""StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3650,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3612,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3745,
        _3746,
        _3638,
        _3666,
        _3692,
        _3711,
        _3659,
        _3713,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed"
)


class StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed(
    _3650.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
):
    """StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = (
        _STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3650.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3650.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3638.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3638,
            )

            return self._parent._cast(
                _3638.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3666.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3666,
            )

            return self._parent._cast(
                _3666.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3692.GearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3692,
            )

            return self._parent._cast(
                _3692.GearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3711.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3711,
            )

            return self._parent._cast(
                _3711.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3659.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3659,
            )

            return self._parent._cast(
                _3659.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3713.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3713,
            )

            return self._parent._cast(
                _3713.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3745.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3745,
            )

            return self._parent._cast(
                _3745.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3746.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3746,
            )

            return self._parent._cast(
                _3746.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2545.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

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
    ) -> "List[_3612.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3612.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
