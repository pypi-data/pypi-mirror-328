"""MassDiscCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3259,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "MassDiscCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2482
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3080,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3214,
        _3162,
        _3216,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="MassDiscCompoundSteadyStateSynchronousResponse")


class MassDiscCompoundSteadyStateSynchronousResponse(
    _3259.VirtualComponentCompoundSteadyStateSynchronousResponse
):
    """MassDiscCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MassDiscCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_MassDiscCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting MassDiscCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "MassDiscCompoundSteadyStateSynchronousResponse._Cast_MassDiscCompoundSteadyStateSynchronousResponse",
            parent: "MassDiscCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_steady_state_synchronous_response(
            self: "MassDiscCompoundSteadyStateSynchronousResponse._Cast_MassDiscCompoundSteadyStateSynchronousResponse",
        ) -> "_3259.VirtualComponentCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3259.VirtualComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "MassDiscCompoundSteadyStateSynchronousResponse._Cast_MassDiscCompoundSteadyStateSynchronousResponse",
        ) -> "_3214.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3214,
            )

            return self._parent._cast(
                _3214.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "MassDiscCompoundSteadyStateSynchronousResponse._Cast_MassDiscCompoundSteadyStateSynchronousResponse",
        ) -> "_3162.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3162,
            )

            return self._parent._cast(
                _3162.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "MassDiscCompoundSteadyStateSynchronousResponse._Cast_MassDiscCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(_3216.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "MassDiscCompoundSteadyStateSynchronousResponse._Cast_MassDiscCompoundSteadyStateSynchronousResponse",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MassDiscCompoundSteadyStateSynchronousResponse._Cast_MassDiscCompoundSteadyStateSynchronousResponse",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscCompoundSteadyStateSynchronousResponse._Cast_MassDiscCompoundSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def mass_disc_compound_steady_state_synchronous_response(
            self: "MassDiscCompoundSteadyStateSynchronousResponse._Cast_MassDiscCompoundSteadyStateSynchronousResponse",
        ) -> "MassDiscCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "MassDiscCompoundSteadyStateSynchronousResponse._Cast_MassDiscCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "MassDiscCompoundSteadyStateSynchronousResponse.TYPE",
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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3080.MassDiscSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.MassDiscSteadyStateSynchronousResponse]

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
    def planetaries(
        self: Self,
    ) -> "List[MassDiscCompoundSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound.MassDiscCompoundSteadyStateSynchronousResponse]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3080.MassDiscSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.MassDiscSteadyStateSynchronousResponse]

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
    ) -> "MassDiscCompoundSteadyStateSynchronousResponse._Cast_MassDiscCompoundSteadyStateSynchronousResponse":
        return self._Cast_MassDiscCompoundSteadyStateSynchronousResponse(self)
