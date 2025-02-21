"""SpringDamperCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5025,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "SpringDamperCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2600
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4963,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5086,
        _4988,
        _5067,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="SpringDamperCompoundModalAnalysisAtAStiffness")


class SpringDamperCompoundModalAnalysisAtAStiffness(
    _5025.CouplingCompoundModalAnalysisAtAStiffness
):
    """SpringDamperCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_SpringDamperCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting SpringDamperCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "SpringDamperCompoundModalAnalysisAtAStiffness._Cast_SpringDamperCompoundModalAnalysisAtAStiffness",
            parent: "SpringDamperCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_compound_modal_analysis_at_a_stiffness(
            self: "SpringDamperCompoundModalAnalysisAtAStiffness._Cast_SpringDamperCompoundModalAnalysisAtAStiffness",
        ) -> "_5025.CouplingCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(_5025.CouplingCompoundModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "SpringDamperCompoundModalAnalysisAtAStiffness._Cast_SpringDamperCompoundModalAnalysisAtAStiffness",
        ) -> "_5086.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5086,
            )

            return self._parent._cast(
                _5086.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "SpringDamperCompoundModalAnalysisAtAStiffness._Cast_SpringDamperCompoundModalAnalysisAtAStiffness",
        ) -> "_4988.AbstractAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4988,
            )

            return self._parent._cast(
                _4988.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "SpringDamperCompoundModalAnalysisAtAStiffness._Cast_SpringDamperCompoundModalAnalysisAtAStiffness",
        ) -> "_5067.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(_5067.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "SpringDamperCompoundModalAnalysisAtAStiffness._Cast_SpringDamperCompoundModalAnalysisAtAStiffness",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperCompoundModalAnalysisAtAStiffness._Cast_SpringDamperCompoundModalAnalysisAtAStiffness",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperCompoundModalAnalysisAtAStiffness._Cast_SpringDamperCompoundModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spring_damper_compound_modal_analysis_at_a_stiffness(
            self: "SpringDamperCompoundModalAnalysisAtAStiffness._Cast_SpringDamperCompoundModalAnalysisAtAStiffness",
        ) -> "SpringDamperCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "SpringDamperCompoundModalAnalysisAtAStiffness._Cast_SpringDamperCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "SpringDamperCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2600.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2600.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

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
    ) -> "List[_4963.SpringDamperModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.SpringDamperModalAnalysisAtAStiffness]

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
    ) -> "List[_4963.SpringDamperModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.SpringDamperModalAnalysisAtAStiffness]

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
    ) -> "SpringDamperCompoundModalAnalysisAtAStiffness._Cast_SpringDamperCompoundModalAnalysisAtAStiffness":
        return self._Cast_SpringDamperCompoundModalAnalysisAtAStiffness(self)
