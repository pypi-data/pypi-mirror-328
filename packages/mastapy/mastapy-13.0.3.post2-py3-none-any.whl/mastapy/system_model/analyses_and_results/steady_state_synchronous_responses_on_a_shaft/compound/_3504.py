"""StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3412,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2567
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3377,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3400,
        _3428,
        _3454,
        _3473,
        _3421,
        _3475,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"
)


class StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft(
    _3412.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
):
    """StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3412.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3412.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3400.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3400,
            )

            return self._parent._cast(
                _3400.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3428.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3428,
            )

            return self._parent._cast(
                _3428.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3454.GearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3454,
            )

            return self._parent._cast(
                _3454.GearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3473.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3473,
            )

            return self._parent._cast(
                _3473.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3421.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3421,
            )

            return self._parent._cast(
                _3421.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3475.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3475,
            )

            return self._parent._cast(
                _3475.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2567.StraightBevelGear":
        """mastapy.system_model.part_model.gears.StraightBevelGear

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
    ) -> "List[_3377.StraightBevelGearSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.StraightBevelGearSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3377.StraightBevelGearSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.StraightBevelGearSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
        return (
            self._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )
