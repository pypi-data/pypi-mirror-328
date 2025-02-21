"""SpringDamperCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6453
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "SpringDamperCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6514,
        _6416,
        _6495,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="SpringDamperCompoundDynamicAnalysis")


class SpringDamperCompoundDynamicAnalysis(_6453.CouplingCompoundDynamicAnalysis):
    """SpringDamperCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperCompoundDynamicAnalysis")

    class _Cast_SpringDamperCompoundDynamicAnalysis:
        """Special nested class for casting SpringDamperCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperCompoundDynamicAnalysis._Cast_SpringDamperCompoundDynamicAnalysis",
            parent: "SpringDamperCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_compound_dynamic_analysis(
            self: "SpringDamperCompoundDynamicAnalysis._Cast_SpringDamperCompoundDynamicAnalysis",
        ) -> "_6453.CouplingCompoundDynamicAnalysis":
            return self._parent._cast(_6453.CouplingCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "SpringDamperCompoundDynamicAnalysis._Cast_SpringDamperCompoundDynamicAnalysis",
        ) -> "_6514.SpecialisedAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6514,
            )

            return self._parent._cast(_6514.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "SpringDamperCompoundDynamicAnalysis._Cast_SpringDamperCompoundDynamicAnalysis",
        ) -> "_6416.AbstractAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6416,
            )

            return self._parent._cast(_6416.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "SpringDamperCompoundDynamicAnalysis._Cast_SpringDamperCompoundDynamicAnalysis",
        ) -> "_6495.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(_6495.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "SpringDamperCompoundDynamicAnalysis._Cast_SpringDamperCompoundDynamicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperCompoundDynamicAnalysis._Cast_SpringDamperCompoundDynamicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperCompoundDynamicAnalysis._Cast_SpringDamperCompoundDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spring_damper_compound_dynamic_analysis(
            self: "SpringDamperCompoundDynamicAnalysis._Cast_SpringDamperCompoundDynamicAnalysis",
        ) -> "SpringDamperCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperCompoundDynamicAnalysis._Cast_SpringDamperCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "SpringDamperCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.SpringDamper":
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
    def assembly_design(self: Self) -> "_2608.SpringDamper":
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
    ) -> "List[_6390.SpringDamperDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SpringDamperDynamicAnalysis]

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
    ) -> "List[_6390.SpringDamperDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SpringDamperDynamicAnalysis]

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
    ) -> (
        "SpringDamperCompoundDynamicAnalysis._Cast_SpringDamperCompoundDynamicAnalysis"
    ):
        return self._Cast_SpringDamperCompoundDynamicAnalysis(self)
