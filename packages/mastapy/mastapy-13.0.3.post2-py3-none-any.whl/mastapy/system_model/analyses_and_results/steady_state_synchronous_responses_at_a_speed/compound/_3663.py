"""BearingCompoundSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3691,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "BearingCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2459
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3533,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3732,
        _3680,
        _3734,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BearingCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="BearingCompoundSteadyStateSynchronousResponseAtASpeed")


class BearingCompoundSteadyStateSynchronousResponseAtASpeed(
    _3691.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed
):
    """BearingCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEARING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BearingCompoundSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_BearingCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting BearingCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "BearingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BearingCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "BearingCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def connector_compound_steady_state_synchronous_response_at_a_speed(
            self: "BearingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BearingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3691.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3691.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "BearingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BearingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3732.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3732,
            )

            return self._parent._cast(
                _3732.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "BearingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BearingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3680.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3680,
            )

            return self._parent._cast(
                _3680.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "BearingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BearingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3734.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3734,
            )

            return self._parent._cast(
                _3734.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "BearingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BearingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BearingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BearingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BearingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BearingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bearing_compound_steady_state_synchronous_response_at_a_speed(
            self: "BearingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BearingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "BearingCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "BearingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BearingCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "BearingCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2459.Bearing":
        """mastapy.system_model.part_model.Bearing

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
    ) -> "List[_3533.BearingSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.BearingSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[BearingCompoundSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound.BearingCompoundSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3533.BearingSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.BearingSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "BearingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BearingCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_BearingCompoundSteadyStateSynchronousResponseAtASpeed(self)
