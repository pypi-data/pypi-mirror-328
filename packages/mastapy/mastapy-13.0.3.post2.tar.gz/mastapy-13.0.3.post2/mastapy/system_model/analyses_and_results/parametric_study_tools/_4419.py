"""PlanetaryGearSetParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4366
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "PlanetaryGearSetParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2562
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4384,
        _4433,
        _4317,
        _4414,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetParametricStudyTool",)


Self = TypeVar("Self", bound="PlanetaryGearSetParametricStudyTool")


class PlanetaryGearSetParametricStudyTool(_4366.CylindricalGearSetParametricStudyTool):
    """PlanetaryGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryGearSetParametricStudyTool")

    class _Cast_PlanetaryGearSetParametricStudyTool:
        """Special nested class for casting PlanetaryGearSetParametricStudyTool to subclasses."""

        def __init__(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
            parent: "PlanetaryGearSetParametricStudyTool",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_parametric_study_tool(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
        ) -> "_4366.CylindricalGearSetParametricStudyTool":
            return self._parent._cast(_4366.CylindricalGearSetParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
        ) -> "_4384.GearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4384,
            )

            return self._parent._cast(_4384.GearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
        ) -> "_4433.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4433,
            )

            return self._parent._cast(_4433.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
        ) -> "_4317.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4317,
            )

            return self._parent._cast(_4317.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
        ) -> "_4414.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_gear_set_parametric_study_tool(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
        ) -> "PlanetaryGearSetParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2562.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "PlanetaryGearSetParametricStudyTool._Cast_PlanetaryGearSetParametricStudyTool"
    ):
        return self._Cast_PlanetaryGearSetParametricStudyTool(self)
