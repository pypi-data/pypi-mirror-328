"""ConceptCouplingSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3284,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "ConceptCouplingSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581
    from mastapy.system_model.analyses_and_results.static_loads import _6841
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3343,
        _3245,
        _3324,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="ConceptCouplingSteadyStateSynchronousResponseOnAShaft")


class ConceptCouplingSteadyStateSynchronousResponseOnAShaft(
    _3284.CouplingSteadyStateSynchronousResponseOnAShaft
):
    """ConceptCouplingSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_ConceptCouplingSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ConceptCouplingSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ConceptCouplingSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingSteadyStateSynchronousResponseOnAShaft",
            parent: "ConceptCouplingSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def coupling_steady_state_synchronous_response_on_a_shaft(
            self: "ConceptCouplingSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3284.CouplingSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3284.CouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "ConceptCouplingSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3343.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3343,
            )

            return self._parent._cast(
                _3343.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "ConceptCouplingSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3245.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3245,
            )

            return self._parent._cast(
                _3245.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "ConceptCouplingSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3324.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(_3324.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "ConceptCouplingSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "ConceptCouplingSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ConceptCouplingSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2581.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6841.ConceptCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ConceptCouplingSteadyStateSynchronousResponseOnAShaft(self)
