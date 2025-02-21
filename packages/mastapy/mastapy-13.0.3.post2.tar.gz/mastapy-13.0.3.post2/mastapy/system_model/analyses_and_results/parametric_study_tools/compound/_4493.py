"""ConceptGearCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4522,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "ConceptGearCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.static_loads import _6863
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4347
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4541,
        _4489,
        _4543,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="ConceptGearCompoundParametricStudyTool")


class ConceptGearCompoundParametricStudyTool(_4522.GearCompoundParametricStudyTool):
    """ConceptGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearCompoundParametricStudyTool"
    )

    class _Cast_ConceptGearCompoundParametricStudyTool:
        """Special nested class for casting ConceptGearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "ConceptGearCompoundParametricStudyTool._Cast_ConceptGearCompoundParametricStudyTool",
            parent: "ConceptGearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_compound_parametric_study_tool(
            self: "ConceptGearCompoundParametricStudyTool._Cast_ConceptGearCompoundParametricStudyTool",
        ) -> "_4522.GearCompoundParametricStudyTool":
            return self._parent._cast(_4522.GearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "ConceptGearCompoundParametricStudyTool._Cast_ConceptGearCompoundParametricStudyTool",
        ) -> "_4541.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4541,
            )

            return self._parent._cast(
                _4541.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "ConceptGearCompoundParametricStudyTool._Cast_ConceptGearCompoundParametricStudyTool",
        ) -> "_4489.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4489,
            )

            return self._parent._cast(_4489.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "ConceptGearCompoundParametricStudyTool._Cast_ConceptGearCompoundParametricStudyTool",
        ) -> "_4543.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(_4543.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "ConceptGearCompoundParametricStudyTool._Cast_ConceptGearCompoundParametricStudyTool",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptGearCompoundParametricStudyTool._Cast_ConceptGearCompoundParametricStudyTool",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearCompoundParametricStudyTool._Cast_ConceptGearCompoundParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def concept_gear_compound_parametric_study_tool(
            self: "ConceptGearCompoundParametricStudyTool._Cast_ConceptGearCompoundParametricStudyTool",
        ) -> "ConceptGearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ConceptGearCompoundParametricStudyTool._Cast_ConceptGearCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "ConceptGearCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2541.ConceptGear":
        """mastapy.system_model.part_model.gears.ConceptGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(self: Self) -> "_6863.ConceptGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase

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
    ) -> "List[_4347.ConceptGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConceptGearParametricStudyTool]

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
    ) -> "List[_4347.ConceptGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConceptGearParametricStudyTool]

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
    ) -> "ConceptGearCompoundParametricStudyTool._Cast_ConceptGearCompoundParametricStudyTool":
        return self._Cast_ConceptGearCompoundParametricStudyTool(self)
