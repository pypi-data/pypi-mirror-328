"""RootAssemblyCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4450,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "RootAssemblyCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.load_case_groups import _5659
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4389,
        _4390,
        _4408,
    )
    from mastapy.system_model.analyses_and_results.static_loads import _6949
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2903,
    )
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4443,
        _4522,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="RootAssemblyCompoundParametricStudyTool")


class RootAssemblyCompoundParametricStudyTool(
    _4450.AssemblyCompoundParametricStudyTool
):
    """RootAssemblyCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RootAssemblyCompoundParametricStudyTool"
    )

    class _Cast_RootAssemblyCompoundParametricStudyTool:
        """Special nested class for casting RootAssemblyCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "RootAssemblyCompoundParametricStudyTool._Cast_RootAssemblyCompoundParametricStudyTool",
            parent: "RootAssemblyCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def assembly_compound_parametric_study_tool(
            self: "RootAssemblyCompoundParametricStudyTool._Cast_RootAssemblyCompoundParametricStudyTool",
        ) -> "_4450.AssemblyCompoundParametricStudyTool":
            return self._parent._cast(_4450.AssemblyCompoundParametricStudyTool)

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "RootAssemblyCompoundParametricStudyTool._Cast_RootAssemblyCompoundParametricStudyTool",
        ) -> "_4443.AbstractAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4443,
            )

            return self._parent._cast(_4443.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "RootAssemblyCompoundParametricStudyTool._Cast_RootAssemblyCompoundParametricStudyTool",
        ) -> "_4522.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "RootAssemblyCompoundParametricStudyTool._Cast_RootAssemblyCompoundParametricStudyTool",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RootAssemblyCompoundParametricStudyTool._Cast_RootAssemblyCompoundParametricStudyTool",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyCompoundParametricStudyTool._Cast_RootAssemblyCompoundParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def root_assembly_compound_parametric_study_tool(
            self: "RootAssemblyCompoundParametricStudyTool._Cast_RootAssemblyCompoundParametricStudyTool",
        ) -> "RootAssemblyCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "RootAssemblyCompoundParametricStudyTool._Cast_RootAssemblyCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "RootAssemblyCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def compound_load_case(self: Self) -> "_5659.AbstractLoadCaseGroup":
        """mastapy.system_model.analyses_and_results.load_case_groups.AbstractLoadCaseGroup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def parametric_analysis_options(self: Self) -> "_4389.ParametricStudyToolOptions":
        """mastapy.system_model.analyses_and_results.parametric_study_tools.ParametricStudyToolOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParametricAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(self: Self) -> "_6949.RootAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def results_for_reporting(
        self: Self,
    ) -> "_4390.ParametricStudyToolResultsForReporting":
        """mastapy.system_model.analyses_and_results.parametric_study_tools.ParametricStudyToolResultsForReporting

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsForReporting

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def root_assembly_duty_cycle_results(
        self: Self,
    ) -> "_2903.DutyCycleEfficiencyResults":
        """mastapy.system_model.analyses_and_results.system_deflections.compound.DutyCycleEfficiencyResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootAssemblyDutyCycleResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4408.RootAssemblyParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.RootAssemblyParametricStudyTool]

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
    ) -> "List[_4408.RootAssemblyParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.RootAssemblyParametricStudyTool]

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
    ) -> "RootAssemblyCompoundParametricStudyTool._Cast_RootAssemblyCompoundParametricStudyTool":
        return self._Cast_RootAssemblyCompoundParametricStudyTool(self)
