"""KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3051,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
        "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.static_loads import _6918
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3055,
        _3053,
        _3016,
        _3043,
        _3082,
        _2983,
        _3063,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse"
)


class KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse(
    _3051.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse
):
    """KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
            parent: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> (
            "_3051.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse"
        ):
            return self._parent._cast(
                _3051.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "_3016.ConicalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(
                _3016.ConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def gear_set_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "_3043.GearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3043,
            )

            return self._parent._cast(_3043.GearSetSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "_3082.SpecialisedAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3082,
            )

            return self._parent._cast(
                _3082.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "_2983.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2983,
            )

            return self._parent._cast(
                _2983.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "_3063.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3063,
            )

            return self._parent._cast(_3063.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2539.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(
        self: Self,
    ) -> "_6918.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3055.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidHypoidGearsSteadyStateSynchronousResponse
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3053.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidHypoidMeshesSteadyStateSynchronousResponse
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse(
            self
        )
