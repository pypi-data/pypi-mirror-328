"""HypoidGearSetParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4301
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "HypoidGearSetParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2535
    from mastapy.system_model.analyses_and_results.static_loads import _6907
    from mastapy.system_model.analyses_and_results.system_deflections import _2764
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4365,
        _4364,
        _4329,
        _4362,
        _4411,
        _4295,
        _4392,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetParametricStudyTool",)


Self = TypeVar("Self", bound="HypoidGearSetParametricStudyTool")


class HypoidGearSetParametricStudyTool(
    _4301.AGMAGleasonConicalGearSetParametricStudyTool
):
    """HypoidGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearSetParametricStudyTool")

    class _Cast_HypoidGearSetParametricStudyTool:
        """Special nested class for casting HypoidGearSetParametricStudyTool to subclasses."""

        def __init__(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
            parent: "HypoidGearSetParametricStudyTool",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "_4301.AGMAGleasonConicalGearSetParametricStudyTool":
            return self._parent._cast(
                _4301.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def conical_gear_set_parametric_study_tool(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "_4329.ConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.ConicalGearSetParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "_4362.GearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4362,
            )

            return self._parent._cast(_4362.GearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "_4411.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4411,
            )

            return self._parent._cast(_4411.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "_4295.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4295,
            )

            return self._parent._cast(_4295.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "_4392.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(_4392.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_parametric_study_tool(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
        ) -> "HypoidGearSetParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearSetParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2535.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6907.HypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase

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
    ) -> "List[_2764.HypoidGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSetSystemDeflection]

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
    def hypoid_gears_parametric_study_tool(
        self: Self,
    ) -> "List[_4365.HypoidGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.HypoidGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_parametric_study_tool(
        self: Self,
    ) -> "List[_4364.HypoidGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.HypoidGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearSetParametricStudyTool._Cast_HypoidGearSetParametricStudyTool":
        return self._Cast_HypoidGearSetParametricStudyTool(self)
