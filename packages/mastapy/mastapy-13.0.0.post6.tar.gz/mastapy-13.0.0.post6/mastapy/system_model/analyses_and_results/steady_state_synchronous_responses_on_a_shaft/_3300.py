"""FaceGearSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3305,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "FaceGearSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2528
    from mastapy.system_model.analyses_and_results.static_loads import _6884
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3322,
        _3270,
        _3324,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="FaceGearSteadyStateSynchronousResponseOnAShaft")


class FaceGearSteadyStateSynchronousResponseOnAShaft(
    _3305.GearSteadyStateSynchronousResponseOnAShaft
):
    """FaceGearSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_FaceGearSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting FaceGearSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "FaceGearSteadyStateSynchronousResponseOnAShaft._Cast_FaceGearSteadyStateSynchronousResponseOnAShaft",
            parent: "FaceGearSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(
            self: "FaceGearSteadyStateSynchronousResponseOnAShaft._Cast_FaceGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3305.GearSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(_3305.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "FaceGearSteadyStateSynchronousResponseOnAShaft._Cast_FaceGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3322.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(
                _3322.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "FaceGearSteadyStateSynchronousResponseOnAShaft._Cast_FaceGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3270.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3270,
            )

            return self._parent._cast(
                _3270.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "FaceGearSteadyStateSynchronousResponseOnAShaft._Cast_FaceGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3324.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(_3324.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearSteadyStateSynchronousResponseOnAShaft._Cast_FaceGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearSteadyStateSynchronousResponseOnAShaft._Cast_FaceGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearSteadyStateSynchronousResponseOnAShaft._Cast_FaceGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearSteadyStateSynchronousResponseOnAShaft._Cast_FaceGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSteadyStateSynchronousResponseOnAShaft._Cast_FaceGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def face_gear_steady_state_synchronous_response_on_a_shaft(
            self: "FaceGearSteadyStateSynchronousResponseOnAShaft._Cast_FaceGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "FaceGearSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "FaceGearSteadyStateSynchronousResponseOnAShaft._Cast_FaceGearSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "FaceGearSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2528.FaceGear":
        """mastapy.system_model.part_model.gears.FaceGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6884.FaceGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSteadyStateSynchronousResponseOnAShaft._Cast_FaceGearSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_FaceGearSteadyStateSynchronousResponseOnAShaft(self)
