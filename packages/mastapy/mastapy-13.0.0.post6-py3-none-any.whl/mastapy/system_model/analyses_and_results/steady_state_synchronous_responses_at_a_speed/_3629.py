"""WormGearSetSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3563,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "WormGearSetSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2552
    from mastapy.system_model.analyses_and_results.static_loads import _6984
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3630,
        _3628,
        _3602,
        _3504,
        _3583,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="WormGearSetSteadyStateSynchronousResponseAtASpeed")


class WormGearSetSteadyStateSynchronousResponseAtASpeed(
    _3563.GearSetSteadyStateSynchronousResponseAtASpeed
):
    """WormGearSetSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_WormGearSetSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_WormGearSetSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting WormGearSetSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "WormGearSetSteadyStateSynchronousResponseAtASpeed._Cast_WormGearSetSteadyStateSynchronousResponseAtASpeed",
            parent: "WormGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(
            self: "WormGearSetSteadyStateSynchronousResponseAtASpeed._Cast_WormGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3563.GearSetSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3563.GearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "WormGearSetSteadyStateSynchronousResponseAtASpeed._Cast_WormGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3602.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3602,
            )

            return self._parent._cast(
                _3602.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "WormGearSetSteadyStateSynchronousResponseAtASpeed._Cast_WormGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3504.AbstractAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3504,
            )

            return self._parent._cast(
                _3504.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "WormGearSetSteadyStateSynchronousResponseAtASpeed._Cast_WormGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3583.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(_3583.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "WormGearSetSteadyStateSynchronousResponseAtASpeed._Cast_WormGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "WormGearSetSteadyStateSynchronousResponseAtASpeed._Cast_WormGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "WormGearSetSteadyStateSynchronousResponseAtASpeed._Cast_WormGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearSetSteadyStateSynchronousResponseAtASpeed._Cast_WormGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearSetSteadyStateSynchronousResponseAtASpeed._Cast_WormGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def worm_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "WormGearSetSteadyStateSynchronousResponseAtASpeed._Cast_WormGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "WormGearSetSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "WormGearSetSteadyStateSynchronousResponseAtASpeed._Cast_WormGearSetSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "WormGearSetSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2552.WormGearSet":
        """mastapy.system_model.part_model.gears.WormGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6984.WormGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm_gears_steady_state_synchronous_response_at_a_speed(
        self: Self,
    ) -> "List[_3630.WormGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.WormGearSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearsSteadyStateSynchronousResponseAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_meshes_steady_state_synchronous_response_at_a_speed(
        self: Self,
    ) -> "List[_3628.WormGearMeshSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.WormGearMeshSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshesSteadyStateSynchronousResponseAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "WormGearSetSteadyStateSynchronousResponseAtASpeed._Cast_WormGearSetSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_WormGearSetSteadyStateSynchronousResponseAtASpeed(self)
