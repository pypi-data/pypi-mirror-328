"""BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3666,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3540,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3671,
        _3659,
        _3687,
        _3713,
        _3732,
        _3680,
        _3734,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self",
    bound="BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
)


class BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed(
    _3666.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed
):
    """BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3666.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            return self._parent._cast(
                _3666.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3671.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3671,
            )

            return self._parent._cast(
                _3671.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3659.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3659,
            )

            return self._parent._cast(
                _3659.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3687.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3687,
            )

            return self._parent._cast(
                _3687.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3713.GearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3713,
            )

            return self._parent._cast(
                _3713.GearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3732.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3732,
            )

            return self._parent._cast(
                _3732.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3680.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3680,
            )

            return self._parent._cast(
                _3680.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3734.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3734,
            )

            return self._parent._cast(
                _3734.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3540.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3540.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
