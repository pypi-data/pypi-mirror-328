"""HypoidGearParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4301
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "HypoidGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534
    from mastapy.system_model.analyses_and_results.static_loads import _6906
    from mastapy.system_model.analyses_and_results.system_deflections import _2765
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4329,
        _4362,
        _4381,
        _4321,
        _4393,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearParametricStudyTool",)


Self = TypeVar("Self", bound="HypoidGearParametricStudyTool")


class HypoidGearParametricStudyTool(_4301.AGMAGleasonConicalGearParametricStudyTool):
    """HypoidGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearParametricStudyTool")

    class _Cast_HypoidGearParametricStudyTool:
        """Special nested class for casting HypoidGearParametricStudyTool to subclasses."""

        def __init__(
            self: "HypoidGearParametricStudyTool._Cast_HypoidGearParametricStudyTool",
            parent: "HypoidGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "HypoidGearParametricStudyTool._Cast_HypoidGearParametricStudyTool",
        ) -> "_4301.AGMAGleasonConicalGearParametricStudyTool":
            return self._parent._cast(_4301.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "HypoidGearParametricStudyTool._Cast_HypoidGearParametricStudyTool",
        ) -> "_4329.ConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.ConicalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "HypoidGearParametricStudyTool._Cast_HypoidGearParametricStudyTool",
        ) -> "_4362.GearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4362,
            )

            return self._parent._cast(_4362.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "HypoidGearParametricStudyTool._Cast_HypoidGearParametricStudyTool",
        ) -> "_4381.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(_4381.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "HypoidGearParametricStudyTool._Cast_HypoidGearParametricStudyTool",
        ) -> "_4321.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4321,
            )

            return self._parent._cast(_4321.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "HypoidGearParametricStudyTool._Cast_HypoidGearParametricStudyTool",
        ) -> "_4393.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4393,
            )

            return self._parent._cast(_4393.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "HypoidGearParametricStudyTool._Cast_HypoidGearParametricStudyTool",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearParametricStudyTool._Cast_HypoidGearParametricStudyTool",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearParametricStudyTool._Cast_HypoidGearParametricStudyTool",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearParametricStudyTool._Cast_HypoidGearParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def hypoid_gear_parametric_study_tool(
            self: "HypoidGearParametricStudyTool._Cast_HypoidGearParametricStudyTool",
        ) -> "HypoidGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "HypoidGearParametricStudyTool._Cast_HypoidGearParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2534.HypoidGear":
        """mastapy.system_model.part_model.gears.HypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6906.HypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2765.HypoidGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearParametricStudyTool._Cast_HypoidGearParametricStudyTool":
        return self._Cast_HypoidGearParametricStudyTool(self)
