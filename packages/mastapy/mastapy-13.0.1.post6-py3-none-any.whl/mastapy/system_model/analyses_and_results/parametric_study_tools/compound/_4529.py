"""PointLoadCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4565,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "PointLoadCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.static_loads import _6939
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4400
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4520,
        _4468,
        _4522,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="PointLoadCompoundParametricStudyTool")


class PointLoadCompoundParametricStudyTool(
    _4565.VirtualComponentCompoundParametricStudyTool
):
    """PointLoadCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointLoadCompoundParametricStudyTool")

    class _Cast_PointLoadCompoundParametricStudyTool:
        """Special nested class for casting PointLoadCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool",
            parent: "PointLoadCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_parametric_study_tool(
            self: "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool",
        ) -> "_4565.VirtualComponentCompoundParametricStudyTool":
            return self._parent._cast(_4565.VirtualComponentCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool",
        ) -> "_4520.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4520,
            )

            return self._parent._cast(
                _4520.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool",
        ) -> "_4468.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool",
        ) -> "_4522.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def point_load_compound_parametric_study_tool(
            self: "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool",
        ) -> "PointLoadCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "PointLoadCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2471.PointLoad":
        """mastapy.system_model.part_model.PointLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(self: Self) -> "_6939.PointLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase

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
    ) -> "List[_4400.PointLoadParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PointLoadParametricStudyTool]

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
    ) -> "List[_4400.PointLoadParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PointLoadParametricStudyTool]

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
    ) -> "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool":
        return self._Cast_PointLoadCompoundParametricStudyTool(self)
