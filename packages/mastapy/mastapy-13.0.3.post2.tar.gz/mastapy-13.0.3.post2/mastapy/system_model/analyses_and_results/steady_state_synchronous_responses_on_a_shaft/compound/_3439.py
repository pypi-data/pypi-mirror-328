"""CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3494,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2588
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3309,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3396,
        _3475,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"
)


class CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft(
    _3494.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
):
    """CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3494.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3494.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3396.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3396,
            )

            return self._parent._cast(
                _3396.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3475.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3475,
            )

            return self._parent._cast(
                _3475.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2588.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2588.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

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
    ) -> "List[_3309.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3309.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft]

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
    ) -> "CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
        return (
            self._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )
