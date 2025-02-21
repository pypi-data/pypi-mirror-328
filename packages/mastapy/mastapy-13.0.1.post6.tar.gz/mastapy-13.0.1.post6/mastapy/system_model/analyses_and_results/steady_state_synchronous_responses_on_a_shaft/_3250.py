"""AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3278,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2514
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3257,
        _3262,
        _3308,
        _3345,
        _3352,
        _3355,
        _3373,
        _3304,
        _3343,
        _3245,
        _3324,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft"
)


class AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft(
    _3278.ConicalGearSetSteadyStateSynchronousResponseOnAShaft
):
    """AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
            parent: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3278.ConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3278.ConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3304.GearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3304,
            )

            return self._parent._cast(
                _3304.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3343.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3343,
            )

            return self._parent._cast(
                _3343.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3245.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3245,
            )

            return self._parent._cast(
                _3245.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3324.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(_3324.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3257.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3257,
            )

            return self._parent._cast(
                _3257.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3262.BevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3262,
            )

            return self._parent._cast(
                _3262.BevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3308.HypoidGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3308,
            )

            return self._parent._cast(
                _3308.HypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3345.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(
                _3345.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3352.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3352,
            )

            return self._parent._cast(
                _3352.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3355.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3355,
            )

            return self._parent._cast(
                _3355.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3373.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3373,
            )

            return self._parent._cast(
                _3373.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2514.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft":
        return (
            self._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )
