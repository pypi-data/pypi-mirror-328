"""SpringDamperParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4356
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "SpringDamperParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2621
    from mastapy.system_model.analyses_and_results.static_loads import _6980
    from mastapy.system_model.analyses_and_results.system_deflections import _2833
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4433,
        _4317,
        _4414,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperParametricStudyTool",)


Self = TypeVar("Self", bound="SpringDamperParametricStudyTool")


class SpringDamperParametricStudyTool(_4356.CouplingParametricStudyTool):
    """SpringDamperParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperParametricStudyTool")

    class _Cast_SpringDamperParametricStudyTool:
        """Special nested class for casting SpringDamperParametricStudyTool to subclasses."""

        def __init__(
            self: "SpringDamperParametricStudyTool._Cast_SpringDamperParametricStudyTool",
            parent: "SpringDamperParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_parametric_study_tool(
            self: "SpringDamperParametricStudyTool._Cast_SpringDamperParametricStudyTool",
        ) -> "_4356.CouplingParametricStudyTool":
            return self._parent._cast(_4356.CouplingParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "SpringDamperParametricStudyTool._Cast_SpringDamperParametricStudyTool",
        ) -> "_4433.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4433,
            )

            return self._parent._cast(_4433.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "SpringDamperParametricStudyTool._Cast_SpringDamperParametricStudyTool",
        ) -> "_4317.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4317,
            )

            return self._parent._cast(_4317.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "SpringDamperParametricStudyTool._Cast_SpringDamperParametricStudyTool",
        ) -> "_4414.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "SpringDamperParametricStudyTool._Cast_SpringDamperParametricStudyTool",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperParametricStudyTool._Cast_SpringDamperParametricStudyTool",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperParametricStudyTool._Cast_SpringDamperParametricStudyTool",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperParametricStudyTool._Cast_SpringDamperParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def spring_damper_parametric_study_tool(
            self: "SpringDamperParametricStudyTool._Cast_SpringDamperParametricStudyTool",
        ) -> "SpringDamperParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SpringDamperParametricStudyTool._Cast_SpringDamperParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2621.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6980.SpringDamperLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_system_deflection_results(
        self: Self,
    ) -> "List[_2833.SpringDamperSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SpringDamperSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperParametricStudyTool._Cast_SpringDamperParametricStudyTool":
        return self._Cast_SpringDamperParametricStudyTool(self)
