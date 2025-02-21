"""SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3770,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2627
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3641,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3694,
        _3732,
        _3680,
        _3734,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed"
)


class SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed(
    _3770.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
):
    """SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3770.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3770.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3694.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3694,
            )

            return self._parent._cast(
                _3694.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3732.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3732,
            )

            return self._parent._cast(
                _3732.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3680.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3680,
            )

            return self._parent._cast(
                _3680.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3734.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3734,
            )

            return self._parent._cast(
                _3734.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2627.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

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
    ) -> "List[_3641.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3641.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed":
        return (
            self._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed(
                self
            )
        )
