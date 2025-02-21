"""SynchroniserPartParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4333
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "SynchroniserPartParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4426,
        _4429,
        _4380,
        _4320,
        _4392,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartParametricStudyTool",)


Self = TypeVar("Self", bound="SynchroniserPartParametricStudyTool")


class SynchroniserPartParametricStudyTool(_4333.CouplingHalfParametricStudyTool):
    """SynchroniserPartParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserPartParametricStudyTool")

    class _Cast_SynchroniserPartParametricStudyTool:
        """Special nested class for casting SynchroniserPartParametricStudyTool to subclasses."""

        def __init__(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
            parent: "SynchroniserPartParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_half_parametric_study_tool(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ) -> "_4333.CouplingHalfParametricStudyTool":
            return self._parent._cast(_4333.CouplingHalfParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ) -> "_4380.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4380,
            )

            return self._parent._cast(_4380.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ) -> "_4320.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4320,
            )

            return self._parent._cast(_4320.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ) -> "_4392.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(_4392.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_half_parametric_study_tool(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ) -> "_4426.SynchroniserHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4426,
            )

            return self._parent._cast(_4426.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ) -> "_4429.SynchroniserSleeveParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4429,
            )

            return self._parent._cast(_4429.SynchroniserSleeveParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ) -> "SynchroniserPartParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
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
        self: Self, instance_to_wrap: "SynchroniserPartParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2605.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

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
    ) -> (
        "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool"
    ):
        return self._Cast_SynchroniserPartParametricStudyTool(self)
