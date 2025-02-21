"""BevelDifferentialSunGearParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4316
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "BevelDifferentialSunGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2525
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4321,
        _4309,
        _4337,
        _4370,
        _4389,
        _4329,
        _4401,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearParametricStudyTool",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearParametricStudyTool")


class BevelDifferentialSunGearParametricStudyTool(
    _4316.BevelDifferentialGearParametricStudyTool
):
    """BevelDifferentialSunGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearParametricStudyTool"
    )

    class _Cast_BevelDifferentialSunGearParametricStudyTool:
        """Special nested class for casting BevelDifferentialSunGearParametricStudyTool to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
            parent: "BevelDifferentialSunGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ) -> "_4316.BevelDifferentialGearParametricStudyTool":
            return self._parent._cast(_4316.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ) -> "_4321.BevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4321,
            )

            return self._parent._cast(_4321.BevelGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ) -> "_4309.AGMAGleasonConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4309,
            )

            return self._parent._cast(_4309.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ) -> "_4337.ConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4337,
            )

            return self._parent._cast(_4337.ConicalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ) -> "_4370.GearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4370,
            )

            return self._parent._cast(_4370.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ) -> "_4389.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4389,
            )

            return self._parent._cast(_4389.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ) -> "_4329.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ) -> "_4401.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_parametric_study_tool(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ) -> "BevelDifferentialSunGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
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
        self: Self, instance_to_wrap: "BevelDifferentialSunGearParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2525.BevelDifferentialSunGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialSunGear

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
    ) -> "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool":
        return self._Cast_BevelDifferentialSunGearParametricStudyTool(self)
