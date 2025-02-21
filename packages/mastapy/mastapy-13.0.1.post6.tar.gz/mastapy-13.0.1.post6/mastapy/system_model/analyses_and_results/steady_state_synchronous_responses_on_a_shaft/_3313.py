"""KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3279,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2536
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3316,
        _3319,
        _3305,
        _3322,
        _3270,
        _3324,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft",
)


class KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft(
    _3279.ConicalGearSteadyStateSynchronousResponseOnAShaft
):
    """KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft",
            parent: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3279.ConicalGearSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3279.ConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3305.GearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3305,
            )

            return self._parent._cast(_3305.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3322.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(
                _3322.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3270.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3270,
            )

            return self._parent._cast(
                _3270.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3324.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(_3324.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3316.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3316,
            )

            return self._parent._cast(
                _3316.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3319.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3319,
            )

            return self._parent._cast(
                _3319.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft"
        ):
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2536.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

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
    ) -> "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft(
            self
        )
