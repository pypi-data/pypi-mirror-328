"""MassDiscSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3130,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "MassDiscSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2482
    from mastapy.system_model.analyses_and_results.static_loads import _6943
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3082,
        _3029,
        _3084,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="MassDiscSteadyStateSynchronousResponse")


class MassDiscSteadyStateSynchronousResponse(
    _3130.VirtualComponentSteadyStateSynchronousResponse
):
    """MassDiscSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MassDiscSteadyStateSynchronousResponse"
    )

    class _Cast_MassDiscSteadyStateSynchronousResponse:
        """Special nested class for casting MassDiscSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
            parent: "MassDiscSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def virtual_component_steady_state_synchronous_response(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
        ) -> "_3130.VirtualComponentSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3130.VirtualComponentSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
        ) -> "_3082.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3082,
            )

            return self._parent._cast(
                _3082.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
        ) -> "_3029.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3029,
            )

            return self._parent._cast(_3029.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
        ) -> "_3084.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(_3084.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def mass_disc_steady_state_synchronous_response(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
        ) -> "MassDiscSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "MassDiscSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2482.MassDisc":
        """mastapy.system_model.part_model.MassDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6943.MassDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[MassDiscSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.MassDiscSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "MassDiscSteadyStateSynchronousResponse._Cast_MassDiscSteadyStateSynchronousResponse":
        return self._Cast_MassDiscSteadyStateSynchronousResponse(self)
