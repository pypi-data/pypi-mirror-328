"""PulleyCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3155,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "PulleyCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2590
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3072,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3158,
        _3193,
        _3141,
        _3195,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("PulleyCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="PulleyCompoundSteadyStateSynchronousResponse")


class PulleyCompoundSteadyStateSynchronousResponse(
    _3155.CouplingHalfCompoundSteadyStateSynchronousResponse
):
    """PulleyCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _PULLEY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PulleyCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_PulleyCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting PulleyCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "PulleyCompoundSteadyStateSynchronousResponse._Cast_PulleyCompoundSteadyStateSynchronousResponse",
            parent: "PulleyCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_steady_state_synchronous_response(
            self: "PulleyCompoundSteadyStateSynchronousResponse._Cast_PulleyCompoundSteadyStateSynchronousResponse",
        ) -> "_3155.CouplingHalfCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3155.CouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "PulleyCompoundSteadyStateSynchronousResponse._Cast_PulleyCompoundSteadyStateSynchronousResponse",
        ) -> "_3193.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(
                _3193.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "PulleyCompoundSteadyStateSynchronousResponse._Cast_PulleyCompoundSteadyStateSynchronousResponse",
        ) -> "_3141.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3141,
            )

            return self._parent._cast(
                _3141.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "PulleyCompoundSteadyStateSynchronousResponse._Cast_PulleyCompoundSteadyStateSynchronousResponse",
        ) -> "_3195.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3195,
            )

            return self._parent._cast(_3195.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "PulleyCompoundSteadyStateSynchronousResponse._Cast_PulleyCompoundSteadyStateSynchronousResponse",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PulleyCompoundSteadyStateSynchronousResponse._Cast_PulleyCompoundSteadyStateSynchronousResponse",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleyCompoundSteadyStateSynchronousResponse._Cast_PulleyCompoundSteadyStateSynchronousResponse",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_steady_state_synchronous_response(
            self: "PulleyCompoundSteadyStateSynchronousResponse._Cast_PulleyCompoundSteadyStateSynchronousResponse",
        ) -> "_3158.CVTPulleyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3158,
            )

            return self._parent._cast(
                _3158.CVTPulleyCompoundSteadyStateSynchronousResponse
            )

        @property
        def pulley_compound_steady_state_synchronous_response(
            self: "PulleyCompoundSteadyStateSynchronousResponse._Cast_PulleyCompoundSteadyStateSynchronousResponse",
        ) -> "PulleyCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "PulleyCompoundSteadyStateSynchronousResponse._Cast_PulleyCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "PulleyCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2590.Pulley":
        """mastapy.system_model.part_model.couplings.Pulley

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
    ) -> "List[_3072.PulleySteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.PulleySteadyStateSynchronousResponse]

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
    ) -> "List[_3072.PulleySteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.PulleySteadyStateSynchronousResponse]

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
    ) -> "PulleyCompoundSteadyStateSynchronousResponse._Cast_PulleyCompoundSteadyStateSynchronousResponse":
        return self._Cast_PulleyCompoundSteadyStateSynchronousResponse(self)
