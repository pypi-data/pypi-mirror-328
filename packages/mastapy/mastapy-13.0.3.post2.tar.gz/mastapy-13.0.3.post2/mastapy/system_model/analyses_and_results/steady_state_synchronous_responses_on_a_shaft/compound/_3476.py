"""PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3433,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2609
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3348,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3494,
        _3396,
        _3475,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self",
    bound="PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
)


class PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft(
    _3433.CouplingCompoundSteadyStateSynchronousResponseOnAShaft
):
    """PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def coupling_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3433.CouplingCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3433.CouplingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3494.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3494,
            )

            return self._parent._cast(
                _3494.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3396.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3396,
            )

            return self._parent._cast(
                _3396.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3475.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3475,
            )

            return self._parent._cast(
                _3475.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2609.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2609.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3348.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3348.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
