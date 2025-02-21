"""ClutchHalfCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4482,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "ClutchHalfCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2579
    from mastapy.system_model.analyses_and_results.static_loads import _6834
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4318
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4520,
        _4468,
        _4522,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalfCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="ClutchHalfCompoundParametricStudyTool")


class ClutchHalfCompoundParametricStudyTool(
    _4482.CouplingHalfCompoundParametricStudyTool
):
    """ClutchHalfCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ClutchHalfCompoundParametricStudyTool"
    )

    class _Cast_ClutchHalfCompoundParametricStudyTool:
        """Special nested class for casting ClutchHalfCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "ClutchHalfCompoundParametricStudyTool._Cast_ClutchHalfCompoundParametricStudyTool",
            parent: "ClutchHalfCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "ClutchHalfCompoundParametricStudyTool._Cast_ClutchHalfCompoundParametricStudyTool",
        ) -> "_4482.CouplingHalfCompoundParametricStudyTool":
            return self._parent._cast(_4482.CouplingHalfCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "ClutchHalfCompoundParametricStudyTool._Cast_ClutchHalfCompoundParametricStudyTool",
        ) -> "_4520.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4520,
            )

            return self._parent._cast(
                _4520.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "ClutchHalfCompoundParametricStudyTool._Cast_ClutchHalfCompoundParametricStudyTool",
        ) -> "_4468.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "ClutchHalfCompoundParametricStudyTool._Cast_ClutchHalfCompoundParametricStudyTool",
        ) -> "_4522.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "ClutchHalfCompoundParametricStudyTool._Cast_ClutchHalfCompoundParametricStudyTool",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchHalfCompoundParametricStudyTool._Cast_ClutchHalfCompoundParametricStudyTool",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHalfCompoundParametricStudyTool._Cast_ClutchHalfCompoundParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_half_compound_parametric_study_tool(
            self: "ClutchHalfCompoundParametricStudyTool._Cast_ClutchHalfCompoundParametricStudyTool",
        ) -> "ClutchHalfCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ClutchHalfCompoundParametricStudyTool._Cast_ClutchHalfCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "ClutchHalfCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2579.ClutchHalf":
        """mastapy.system_model.part_model.couplings.ClutchHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(self: Self) -> "_6834.ClutchHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase

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
    ) -> "List[_4318.ClutchHalfParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ClutchHalfParametricStudyTool]

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
    ) -> "List[_4318.ClutchHalfParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ClutchHalfParametricStudyTool]

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
    ) -> "ClutchHalfCompoundParametricStudyTool._Cast_ClutchHalfCompoundParametricStudyTool":
        return self._Cast_ClutchHalfCompoundParametricStudyTool(self)
