"""CylindricalPlanetGearParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4344
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CylindricalPlanetGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4362,
        _4381,
        _4321,
        _4393,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearParametricStudyTool",)


Self = TypeVar("Self", bound="CylindricalPlanetGearParametricStudyTool")


class CylindricalPlanetGearParametricStudyTool(
    _4344.CylindricalGearParametricStudyTool
):
    """CylindricalPlanetGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearParametricStudyTool"
    )

    class _Cast_CylindricalPlanetGearParametricStudyTool:
        """Special nested class for casting CylindricalPlanetGearParametricStudyTool to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
            parent: "CylindricalPlanetGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_parametric_study_tool(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "_4344.CylindricalGearParametricStudyTool":
            return self._parent._cast(_4344.CylindricalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "_4362.GearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4362,
            )

            return self._parent._cast(_4362.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "_4381.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(_4381.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "_4321.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4321,
            )

            return self._parent._cast(_4321.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "_4393.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4393,
            )

            return self._parent._cast(_4393.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_parametric_study_tool(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
        ) -> "CylindricalPlanetGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool",
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
        self: Self, instance_to_wrap: "CylindricalPlanetGearParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2527.CylindricalPlanetGear":
        """mastapy.system_model.part_model.gears.CylindricalPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearParametricStudyTool._Cast_CylindricalPlanetGearParametricStudyTool":
        return self._Cast_CylindricalPlanetGearParametricStudyTool(self)
