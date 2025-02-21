"""ShaftCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4444,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "ShaftCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2482
    from mastapy.system_model.analyses_and_results.static_loads import _6951
    from mastapy.shafts import _19
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4410
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4445,
        _4468,
        _4522,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ShaftCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="ShaftCompoundParametricStudyTool")


class ShaftCompoundParametricStudyTool(_4444.AbstractShaftCompoundParametricStudyTool):
    """ShaftCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SHAFT_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftCompoundParametricStudyTool")

    class _Cast_ShaftCompoundParametricStudyTool:
        """Special nested class for casting ShaftCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "ShaftCompoundParametricStudyTool._Cast_ShaftCompoundParametricStudyTool",
            parent: "ShaftCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_parametric_study_tool(
            self: "ShaftCompoundParametricStudyTool._Cast_ShaftCompoundParametricStudyTool",
        ) -> "_4444.AbstractShaftCompoundParametricStudyTool":
            return self._parent._cast(_4444.AbstractShaftCompoundParametricStudyTool)

        @property
        def abstract_shaft_or_housing_compound_parametric_study_tool(
            self: "ShaftCompoundParametricStudyTool._Cast_ShaftCompoundParametricStudyTool",
        ) -> "_4445.AbstractShaftOrHousingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4445,
            )

            return self._parent._cast(
                _4445.AbstractShaftOrHousingCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "ShaftCompoundParametricStudyTool._Cast_ShaftCompoundParametricStudyTool",
        ) -> "_4468.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "ShaftCompoundParametricStudyTool._Cast_ShaftCompoundParametricStudyTool",
        ) -> "_4522.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "ShaftCompoundParametricStudyTool._Cast_ShaftCompoundParametricStudyTool",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftCompoundParametricStudyTool._Cast_ShaftCompoundParametricStudyTool",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftCompoundParametricStudyTool._Cast_ShaftCompoundParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def shaft_compound_parametric_study_tool(
            self: "ShaftCompoundParametricStudyTool._Cast_ShaftCompoundParametricStudyTool",
        ) -> "ShaftCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ShaftCompoundParametricStudyTool._Cast_ShaftCompoundParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftCompoundParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2482.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(self: Self) -> "_6951.ShaftLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft_duty_cycle_results(self: Self) -> "_19.ShaftDamageResults":
        """mastapy.shafts.ShaftDamageResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftDutyCycleResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4410.ShaftParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ShaftParametricStudyTool]

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
    def planetaries(self: Self) -> "List[ShaftCompoundParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ShaftCompoundParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(self: Self) -> "List[_4410.ShaftParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ShaftParametricStudyTool]

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
    ) -> "ShaftCompoundParametricStudyTool._Cast_ShaftCompoundParametricStudyTool":
        return self._Cast_ShaftCompoundParametricStudyTool(self)
