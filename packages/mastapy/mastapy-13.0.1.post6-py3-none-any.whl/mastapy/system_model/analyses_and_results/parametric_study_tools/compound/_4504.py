"""GuideDxfModelCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4468,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "GuideDxfModelCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455
    from mastapy.system_model.analyses_and_results.static_loads import _6897
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4364
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4522,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="GuideDxfModelCompoundParametricStudyTool")


class GuideDxfModelCompoundParametricStudyTool(
    _4468.ComponentCompoundParametricStudyTool
):
    """GuideDxfModelCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GuideDxfModelCompoundParametricStudyTool"
    )

    class _Cast_GuideDxfModelCompoundParametricStudyTool:
        """Special nested class for casting GuideDxfModelCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "GuideDxfModelCompoundParametricStudyTool._Cast_GuideDxfModelCompoundParametricStudyTool",
            parent: "GuideDxfModelCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def component_compound_parametric_study_tool(
            self: "GuideDxfModelCompoundParametricStudyTool._Cast_GuideDxfModelCompoundParametricStudyTool",
        ) -> "_4468.ComponentCompoundParametricStudyTool":
            return self._parent._cast(_4468.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "GuideDxfModelCompoundParametricStudyTool._Cast_GuideDxfModelCompoundParametricStudyTool",
        ) -> "_4522.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "GuideDxfModelCompoundParametricStudyTool._Cast_GuideDxfModelCompoundParametricStudyTool",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GuideDxfModelCompoundParametricStudyTool._Cast_GuideDxfModelCompoundParametricStudyTool",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelCompoundParametricStudyTool._Cast_GuideDxfModelCompoundParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def guide_dxf_model_compound_parametric_study_tool(
            self: "GuideDxfModelCompoundParametricStudyTool._Cast_GuideDxfModelCompoundParametricStudyTool",
        ) -> "GuideDxfModelCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelCompoundParametricStudyTool._Cast_GuideDxfModelCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "GuideDxfModelCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2455.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(self: Self) -> "_6897.GuideDxfModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4364.GuideDxfModelParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.GuideDxfModelParametricStudyTool]

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
    ) -> "List[_4364.GuideDxfModelParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.GuideDxfModelParametricStudyTool]

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
    ) -> "GuideDxfModelCompoundParametricStudyTool._Cast_GuideDxfModelCompoundParametricStudyTool":
        return self._Cast_GuideDxfModelCompoundParametricStudyTool(self)
