"""ConceptGearSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3065,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ConceptGearSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.static_loads import _6863
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3082,
        _3029,
        _3084,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ConceptGearSteadyStateSynchronousResponse")


class ConceptGearSteadyStateSynchronousResponse(
    _3065.GearSteadyStateSynchronousResponse
):
    """ConceptGearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearSteadyStateSynchronousResponse"
    )

    class _Cast_ConceptGearSteadyStateSynchronousResponse:
        """Special nested class for casting ConceptGearSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
            parent: "ConceptGearSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def gear_steady_state_synchronous_response(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
        ) -> "_3065.GearSteadyStateSynchronousResponse":
            return self._parent._cast(_3065.GearSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
        ) -> "_3082.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3082,
            )

            return self._parent._cast(
                _3082.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
        ) -> "_3029.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3029,
            )

            return self._parent._cast(_3029.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
        ) -> "_3084.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(_3084.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def concept_gear_steady_state_synchronous_response(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
        ) -> "ConceptGearSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "ConceptGearSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2541.ConceptGear":
        """mastapy.system_model.part_model.gears.ConceptGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6863.ConceptGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase

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
    ) -> "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse":
        return self._Cast_ConceptGearSteadyStateSynchronousResponse(self)
