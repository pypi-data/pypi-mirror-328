"""CylindricalGearParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4361
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CylindricalGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2525
    from mastapy.system_model.analyses_and_results.static_loads import _6861
    from mastapy.system_model.analyses_and_results.system_deflections import _2745
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4345,
        _4380,
        _4320,
        _4392,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearParametricStudyTool",)


Self = TypeVar("Self", bound="CylindricalGearParametricStudyTool")


class CylindricalGearParametricStudyTool(_4361.GearParametricStudyTool):
    """CylindricalGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearParametricStudyTool")

    class _Cast_CylindricalGearParametricStudyTool:
        """Special nested class for casting CylindricalGearParametricStudyTool to subclasses."""

        def __init__(
            self: "CylindricalGearParametricStudyTool._Cast_CylindricalGearParametricStudyTool",
            parent: "CylindricalGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_parametric_study_tool(
            self: "CylindricalGearParametricStudyTool._Cast_CylindricalGearParametricStudyTool",
        ) -> "_4361.GearParametricStudyTool":
            return self._parent._cast(_4361.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "CylindricalGearParametricStudyTool._Cast_CylindricalGearParametricStudyTool",
        ) -> "_4380.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4380,
            )

            return self._parent._cast(_4380.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "CylindricalGearParametricStudyTool._Cast_CylindricalGearParametricStudyTool",
        ) -> "_4320.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4320,
            )

            return self._parent._cast(_4320.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "CylindricalGearParametricStudyTool._Cast_CylindricalGearParametricStudyTool",
        ) -> "_4392.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(_4392.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "CylindricalGearParametricStudyTool._Cast_CylindricalGearParametricStudyTool",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearParametricStudyTool._Cast_CylindricalGearParametricStudyTool",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearParametricStudyTool._Cast_CylindricalGearParametricStudyTool",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearParametricStudyTool._Cast_CylindricalGearParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_parametric_study_tool(
            self: "CylindricalGearParametricStudyTool._Cast_CylindricalGearParametricStudyTool",
        ) -> "_4345.CylindricalPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4345,
            )

            return self._parent._cast(_4345.CylindricalPlanetGearParametricStudyTool)

        @property
        def cylindrical_gear_parametric_study_tool(
            self: "CylindricalGearParametricStudyTool._Cast_CylindricalGearParametricStudyTool",
        ) -> "CylindricalGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CylindricalGearParametricStudyTool._Cast_CylindricalGearParametricStudyTool",
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
        self: Self, instance_to_wrap: "CylindricalGearParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2525.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6861.CylindricalGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase

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
    ) -> "List[_2745.CylindricalGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSystemDeflection]

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
    def planetaries(self: Self) -> "List[CylindricalGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CylindricalGearParametricStudyTool]

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
    def cast_to(
        self: Self,
    ) -> "CylindricalGearParametricStudyTool._Cast_CylindricalGearParametricStudyTool":
        return self._Cast_CylindricalGearParametricStudyTool(self)
