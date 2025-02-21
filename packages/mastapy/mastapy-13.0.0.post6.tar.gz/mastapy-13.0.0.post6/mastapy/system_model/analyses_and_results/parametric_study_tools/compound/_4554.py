"""StraightBevelSunGearCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4547,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "StraightBevelSunGearCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6966
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4425
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4458,
        _4446,
        _4474,
        _4500,
        _4519,
        _4467,
        _4521,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="StraightBevelSunGearCompoundParametricStudyTool")


class StraightBevelSunGearCompoundParametricStudyTool(
    _4547.StraightBevelDiffGearCompoundParametricStudyTool
):
    """StraightBevelSunGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelSunGearCompoundParametricStudyTool"
    )

    class _Cast_StraightBevelSunGearCompoundParametricStudyTool:
        """Special nested class for casting StraightBevelSunGearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "StraightBevelSunGearCompoundParametricStudyTool._Cast_StraightBevelSunGearCompoundParametricStudyTool",
            parent: "StraightBevelSunGearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "StraightBevelSunGearCompoundParametricStudyTool._Cast_StraightBevelSunGearCompoundParametricStudyTool",
        ) -> "_4547.StraightBevelDiffGearCompoundParametricStudyTool":
            return self._parent._cast(
                _4547.StraightBevelDiffGearCompoundParametricStudyTool
            )

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "StraightBevelSunGearCompoundParametricStudyTool._Cast_StraightBevelSunGearCompoundParametricStudyTool",
        ) -> "_4458.BevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4458,
            )

            return self._parent._cast(_4458.BevelGearCompoundParametricStudyTool)

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "StraightBevelSunGearCompoundParametricStudyTool._Cast_StraightBevelSunGearCompoundParametricStudyTool",
        ) -> "_4446.AGMAGleasonConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4446,
            )

            return self._parent._cast(
                _4446.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "StraightBevelSunGearCompoundParametricStudyTool._Cast_StraightBevelSunGearCompoundParametricStudyTool",
        ) -> "_4474.ConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4474,
            )

            return self._parent._cast(_4474.ConicalGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "StraightBevelSunGearCompoundParametricStudyTool._Cast_StraightBevelSunGearCompoundParametricStudyTool",
        ) -> "_4500.GearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4500,
            )

            return self._parent._cast(_4500.GearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "StraightBevelSunGearCompoundParametricStudyTool._Cast_StraightBevelSunGearCompoundParametricStudyTool",
        ) -> "_4519.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(
                _4519.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "StraightBevelSunGearCompoundParametricStudyTool._Cast_StraightBevelSunGearCompoundParametricStudyTool",
        ) -> "_4467.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4467,
            )

            return self._parent._cast(_4467.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "StraightBevelSunGearCompoundParametricStudyTool._Cast_StraightBevelSunGearCompoundParametricStudyTool",
        ) -> "_4521.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4521,
            )

            return self._parent._cast(_4521.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "StraightBevelSunGearCompoundParametricStudyTool._Cast_StraightBevelSunGearCompoundParametricStudyTool",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelSunGearCompoundParametricStudyTool._Cast_StraightBevelSunGearCompoundParametricStudyTool",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearCompoundParametricStudyTool._Cast_StraightBevelSunGearCompoundParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(
            self: "StraightBevelSunGearCompoundParametricStudyTool._Cast_StraightBevelSunGearCompoundParametricStudyTool",
        ) -> "StraightBevelSunGearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearCompoundParametricStudyTool._Cast_StraightBevelSunGearCompoundParametricStudyTool",
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
        instance_to_wrap: "StraightBevelSunGearCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def properties_changing_all_load_cases(
        self: Self,
    ) -> "_6966.StraightBevelSunGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase

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
    ) -> "List[_4425.StraightBevelSunGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelSunGearParametricStudyTool]

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
    ) -> "List[_4425.StraightBevelSunGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelSunGearParametricStudyTool]

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
    ) -> "StraightBevelSunGearCompoundParametricStudyTool._Cast_StraightBevelSunGearCompoundParametricStudyTool":
        return self._Cast_StraightBevelSunGearCompoundParametricStudyTool(self)
