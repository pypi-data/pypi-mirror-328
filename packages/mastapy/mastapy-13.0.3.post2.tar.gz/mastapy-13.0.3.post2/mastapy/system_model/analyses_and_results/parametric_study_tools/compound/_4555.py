"""RollingRingAssemblyCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4562,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "RollingRingAssemblyCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2618
    from mastapy.system_model.analyses_and_results.static_loads import _6967
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4426
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4464,
        _4543,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="RollingRingAssemblyCompoundParametricStudyTool")


class RollingRingAssemblyCompoundParametricStudyTool(
    _4562.SpecialisedAssemblyCompoundParametricStudyTool
):
    """RollingRingAssemblyCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingAssemblyCompoundParametricStudyTool"
    )

    class _Cast_RollingRingAssemblyCompoundParametricStudyTool:
        """Special nested class for casting RollingRingAssemblyCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "RollingRingAssemblyCompoundParametricStudyTool._Cast_RollingRingAssemblyCompoundParametricStudyTool",
            parent: "RollingRingAssemblyCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "RollingRingAssemblyCompoundParametricStudyTool._Cast_RollingRingAssemblyCompoundParametricStudyTool",
        ) -> "_4562.SpecialisedAssemblyCompoundParametricStudyTool":
            return self._parent._cast(
                _4562.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "RollingRingAssemblyCompoundParametricStudyTool._Cast_RollingRingAssemblyCompoundParametricStudyTool",
        ) -> "_4464.AbstractAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4464,
            )

            return self._parent._cast(_4464.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "RollingRingAssemblyCompoundParametricStudyTool._Cast_RollingRingAssemblyCompoundParametricStudyTool",
        ) -> "_4543.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(_4543.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "RollingRingAssemblyCompoundParametricStudyTool._Cast_RollingRingAssemblyCompoundParametricStudyTool",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingAssemblyCompoundParametricStudyTool._Cast_RollingRingAssemblyCompoundParametricStudyTool",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyCompoundParametricStudyTool._Cast_RollingRingAssemblyCompoundParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_compound_parametric_study_tool(
            self: "RollingRingAssemblyCompoundParametricStudyTool._Cast_RollingRingAssemblyCompoundParametricStudyTool",
        ) -> "RollingRingAssemblyCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyCompoundParametricStudyTool._Cast_RollingRingAssemblyCompoundParametricStudyTool",
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
        instance_to_wrap: "RollingRingAssemblyCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2618.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2618.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(
        self: Self,
    ) -> "_6967.RollingRingAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4426.RollingRingAssemblyParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.RollingRingAssemblyParametricStudyTool]

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
    ) -> "List[_4426.RollingRingAssemblyParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.RollingRingAssemblyParametricStudyTool]

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
    ) -> "RollingRingAssemblyCompoundParametricStudyTool._Cast_RollingRingAssemblyCompoundParametricStudyTool":
        return self._Cast_RollingRingAssemblyCompoundParametricStudyTool(self)
