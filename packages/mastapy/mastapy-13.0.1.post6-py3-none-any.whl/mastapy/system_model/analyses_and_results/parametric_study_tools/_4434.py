"""TorqueConverterTurbineParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4334
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "TorqueConverterTurbineParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.static_loads import _6976
    from mastapy.system_model.analyses_and_results.system_deflections import _2831
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4381,
        _4321,
        _4393,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineParametricStudyTool",)


Self = TypeVar("Self", bound="TorqueConverterTurbineParametricStudyTool")


class TorqueConverterTurbineParametricStudyTool(_4334.CouplingHalfParametricStudyTool):
    """TorqueConverterTurbineParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineParametricStudyTool"
    )

    class _Cast_TorqueConverterTurbineParametricStudyTool:
        """Special nested class for casting TorqueConverterTurbineParametricStudyTool to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
            parent: "TorqueConverterTurbineParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_half_parametric_study_tool(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
        ) -> "_4334.CouplingHalfParametricStudyTool":
            return self._parent._cast(_4334.CouplingHalfParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
        ) -> "_4381.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(_4381.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
        ) -> "_4321.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4321,
            )

            return self._parent._cast(_4321.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
        ) -> "_4393.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4393,
            )

            return self._parent._cast(_4393.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_parametric_study_tool(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
        ) -> "TorqueConverterTurbineParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool",
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
        self: Self, instance_to_wrap: "TorqueConverterTurbineParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2610.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6976.TorqueConverterTurbineLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase

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
    ) -> "List[_2831.TorqueConverterTurbineSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterTurbineSystemDeflection]

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
    ) -> "TorqueConverterTurbineParametricStudyTool._Cast_TorqueConverterTurbineParametricStudyTool":
        return self._Cast_TorqueConverterTurbineParametricStudyTool(self)
