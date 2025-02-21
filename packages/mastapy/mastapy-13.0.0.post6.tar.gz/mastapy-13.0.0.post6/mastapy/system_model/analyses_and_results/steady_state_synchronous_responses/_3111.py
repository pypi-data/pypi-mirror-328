"""WormGearSetSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3043,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "WormGearSetSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2552
    from mastapy.system_model.analyses_and_results.static_loads import _6984
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3112,
        _3110,
        _3082,
        _2983,
        _3063,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="WormGearSetSteadyStateSynchronousResponse")


class WormGearSetSteadyStateSynchronousResponse(
    _3043.GearSetSteadyStateSynchronousResponse
):
    """WormGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_WormGearSetSteadyStateSynchronousResponse"
    )

    class _Cast_WormGearSetSteadyStateSynchronousResponse:
        """Special nested class for casting WormGearSetSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "WormGearSetSteadyStateSynchronousResponse._Cast_WormGearSetSteadyStateSynchronousResponse",
            parent: "WormGearSetSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def gear_set_steady_state_synchronous_response(
            self: "WormGearSetSteadyStateSynchronousResponse._Cast_WormGearSetSteadyStateSynchronousResponse",
        ) -> "_3043.GearSetSteadyStateSynchronousResponse":
            return self._parent._cast(_3043.GearSetSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "WormGearSetSteadyStateSynchronousResponse._Cast_WormGearSetSteadyStateSynchronousResponse",
        ) -> "_3082.SpecialisedAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3082,
            )

            return self._parent._cast(
                _3082.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "WormGearSetSteadyStateSynchronousResponse._Cast_WormGearSetSteadyStateSynchronousResponse",
        ) -> "_2983.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2983,
            )

            return self._parent._cast(
                _2983.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "WormGearSetSteadyStateSynchronousResponse._Cast_WormGearSetSteadyStateSynchronousResponse",
        ) -> "_3063.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3063,
            )

            return self._parent._cast(_3063.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "WormGearSetSteadyStateSynchronousResponse._Cast_WormGearSetSteadyStateSynchronousResponse",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "WormGearSetSteadyStateSynchronousResponse._Cast_WormGearSetSteadyStateSynchronousResponse",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "WormGearSetSteadyStateSynchronousResponse._Cast_WormGearSetSteadyStateSynchronousResponse",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearSetSteadyStateSynchronousResponse._Cast_WormGearSetSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearSetSteadyStateSynchronousResponse._Cast_WormGearSetSteadyStateSynchronousResponse",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def worm_gear_set_steady_state_synchronous_response(
            self: "WormGearSetSteadyStateSynchronousResponse._Cast_WormGearSetSteadyStateSynchronousResponse",
        ) -> "WormGearSetSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "WormGearSetSteadyStateSynchronousResponse._Cast_WormGearSetSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "WormGearSetSteadyStateSynchronousResponse.TYPE"
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
    def worm_gears_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3112.WormGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.WormGearSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearsSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_meshes_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3110.WormGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.WormGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshesSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "WormGearSetSteadyStateSynchronousResponse._Cast_WormGearSetSteadyStateSynchronousResponse":
        return self._Cast_WormGearSetSteadyStateSynchronousResponse(self)
