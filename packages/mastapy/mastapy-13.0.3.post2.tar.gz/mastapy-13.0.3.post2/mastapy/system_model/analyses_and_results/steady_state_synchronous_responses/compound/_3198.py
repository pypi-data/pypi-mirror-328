"""GuideDxfModelCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3162,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "GuideDxfModelCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2475
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3066,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3216,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="GuideDxfModelCompoundSteadyStateSynchronousResponse")


class GuideDxfModelCompoundSteadyStateSynchronousResponse(
    _3162.ComponentCompoundSteadyStateSynchronousResponse
):
    """GuideDxfModelCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GuideDxfModelCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_GuideDxfModelCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting GuideDxfModelCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "GuideDxfModelCompoundSteadyStateSynchronousResponse._Cast_GuideDxfModelCompoundSteadyStateSynchronousResponse",
            parent: "GuideDxfModelCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def component_compound_steady_state_synchronous_response(
            self: "GuideDxfModelCompoundSteadyStateSynchronousResponse._Cast_GuideDxfModelCompoundSteadyStateSynchronousResponse",
        ) -> "_3162.ComponentCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3162.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "GuideDxfModelCompoundSteadyStateSynchronousResponse._Cast_GuideDxfModelCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(_3216.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "GuideDxfModelCompoundSteadyStateSynchronousResponse._Cast_GuideDxfModelCompoundSteadyStateSynchronousResponse",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GuideDxfModelCompoundSteadyStateSynchronousResponse._Cast_GuideDxfModelCompoundSteadyStateSynchronousResponse",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelCompoundSteadyStateSynchronousResponse._Cast_GuideDxfModelCompoundSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response(
            self: "GuideDxfModelCompoundSteadyStateSynchronousResponse._Cast_GuideDxfModelCompoundSteadyStateSynchronousResponse",
        ) -> "GuideDxfModelCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelCompoundSteadyStateSynchronousResponse._Cast_GuideDxfModelCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "GuideDxfModelCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2475.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

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
    ) -> "List[_3066.GuideDxfModelSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.GuideDxfModelSteadyStateSynchronousResponse]

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
    ) -> "List[_3066.GuideDxfModelSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.GuideDxfModelSteadyStateSynchronousResponse]

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
    ) -> "GuideDxfModelCompoundSteadyStateSynchronousResponse._Cast_GuideDxfModelCompoundSteadyStateSynchronousResponse":
        return self._Cast_GuideDxfModelCompoundSteadyStateSynchronousResponse(self)
