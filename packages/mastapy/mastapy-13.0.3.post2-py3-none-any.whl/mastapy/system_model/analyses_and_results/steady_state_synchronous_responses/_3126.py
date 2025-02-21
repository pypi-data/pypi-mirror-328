"""TorqueConverterPumpSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3042,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "TorqueConverterPumpSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2629
    from mastapy.system_model.analyses_and_results.static_loads import _6996
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3082,
        _3029,
        _3084,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="TorqueConverterPumpSteadyStateSynchronousResponse")


class TorqueConverterPumpSteadyStateSynchronousResponse(
    _3042.CouplingHalfSteadyStateSynchronousResponse
):
    """TorqueConverterPumpSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterPumpSteadyStateSynchronousResponse"
    )

    class _Cast_TorqueConverterPumpSteadyStateSynchronousResponse:
        """Special nested class for casting TorqueConverterPumpSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "TorqueConverterPumpSteadyStateSynchronousResponse._Cast_TorqueConverterPumpSteadyStateSynchronousResponse",
            parent: "TorqueConverterPumpSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "TorqueConverterPumpSteadyStateSynchronousResponse._Cast_TorqueConverterPumpSteadyStateSynchronousResponse",
        ) -> "_3042.CouplingHalfSteadyStateSynchronousResponse":
            return self._parent._cast(_3042.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "TorqueConverterPumpSteadyStateSynchronousResponse._Cast_TorqueConverterPumpSteadyStateSynchronousResponse",
        ) -> "_3082.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3082,
            )

            return self._parent._cast(
                _3082.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "TorqueConverterPumpSteadyStateSynchronousResponse._Cast_TorqueConverterPumpSteadyStateSynchronousResponse",
        ) -> "_3029.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3029,
            )

            return self._parent._cast(_3029.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "TorqueConverterPumpSteadyStateSynchronousResponse._Cast_TorqueConverterPumpSteadyStateSynchronousResponse",
        ) -> "_3084.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(_3084.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterPumpSteadyStateSynchronousResponse._Cast_TorqueConverterPumpSteadyStateSynchronousResponse",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterPumpSteadyStateSynchronousResponse._Cast_TorqueConverterPumpSteadyStateSynchronousResponse",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterPumpSteadyStateSynchronousResponse._Cast_TorqueConverterPumpSteadyStateSynchronousResponse",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterPumpSteadyStateSynchronousResponse._Cast_TorqueConverterPumpSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpSteadyStateSynchronousResponse._Cast_TorqueConverterPumpSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def torque_converter_pump_steady_state_synchronous_response(
            self: "TorqueConverterPumpSteadyStateSynchronousResponse._Cast_TorqueConverterPumpSteadyStateSynchronousResponse",
        ) -> "TorqueConverterPumpSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpSteadyStateSynchronousResponse._Cast_TorqueConverterPumpSteadyStateSynchronousResponse",
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
        instance_to_wrap: "TorqueConverterPumpSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2629.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6996.TorqueConverterPumpLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase

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
    ) -> "TorqueConverterPumpSteadyStateSynchronousResponse._Cast_TorqueConverterPumpSteadyStateSynchronousResponse":
        return self._Cast_TorqueConverterPumpSteadyStateSynchronousResponse(self)
