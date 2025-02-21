"""StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3739,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3616,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3650,
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
__all__ = ("StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self",
    bound="StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
)


class StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed(
    _3739.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed
):
    """StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3739.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            return self._parent._cast(
                _3739.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3650.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3650,
            )

            return self._parent._cast(
                _3650.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
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
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3666.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3666,
            )

            return self._parent._cast(
                _3666.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3692.GearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3692,
            )

            return self._parent._cast(
                _3692.GearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3711.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3711,
            )

            return self._parent._cast(
                _3711.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3659.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3659,
            )

            return self._parent._cast(
                _3659.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3713.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3713,
            )

            return self._parent._cast(
                _3713.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3616.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3616.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
