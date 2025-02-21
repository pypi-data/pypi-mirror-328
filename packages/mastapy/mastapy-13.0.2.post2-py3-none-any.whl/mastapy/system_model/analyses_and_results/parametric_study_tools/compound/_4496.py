"""CycloidalDiscCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4452,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "CycloidalDiscCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2576
    from mastapy.system_model.analyses_and_results.static_loads import _6868
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4349
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4453,
        _4476,
        _4530,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="CycloidalDiscCompoundParametricStudyTool")


class CycloidalDiscCompoundParametricStudyTool(
    _4452.AbstractShaftCompoundParametricStudyTool
):
    """CycloidalDiscCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscCompoundParametricStudyTool"
    )

    class _Cast_CycloidalDiscCompoundParametricStudyTool:
        """Special nested class for casting CycloidalDiscCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool",
            parent: "CycloidalDiscCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_parametric_study_tool(
            self: "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool",
        ) -> "_4452.AbstractShaftCompoundParametricStudyTool":
            return self._parent._cast(_4452.AbstractShaftCompoundParametricStudyTool)

        @property
        def abstract_shaft_or_housing_compound_parametric_study_tool(
            self: "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool",
        ) -> "_4453.AbstractShaftOrHousingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4453,
            )

            return self._parent._cast(
                _4453.AbstractShaftOrHousingCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool",
        ) -> "_4476.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4476,
            )

            return self._parent._cast(_4476.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool",
        ) -> "_4530.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(_4530.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_parametric_study_tool(
            self: "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool",
        ) -> "CycloidalDiscCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "CycloidalDiscCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2576.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(self: Self) -> "_6868.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

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
    ) -> "List[_4349.CycloidalDiscParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CycloidalDiscParametricStudyTool]

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
    ) -> "List[_4349.CycloidalDiscParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CycloidalDiscParametricStudyTool]

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
    ) -> "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool":
        return self._Cast_CycloidalDiscCompoundParametricStudyTool(self)
