"""ConceptGearMeshParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4382
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ConceptGearMeshParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.static_loads import _6864
    from mastapy.system_model.analyses_and_results.system_deflections import _2741
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4389,
        _4352,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearMeshParametricStudyTool",)


Self = TypeVar("Self", bound="ConceptGearMeshParametricStudyTool")


class ConceptGearMeshParametricStudyTool(_4382.GearMeshParametricStudyTool):
    """ConceptGearMeshParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearMeshParametricStudyTool")

    class _Cast_ConceptGearMeshParametricStudyTool:
        """Special nested class for casting ConceptGearMeshParametricStudyTool to subclasses."""

        def __init__(
            self: "ConceptGearMeshParametricStudyTool._Cast_ConceptGearMeshParametricStudyTool",
            parent: "ConceptGearMeshParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_mesh_parametric_study_tool(
            self: "ConceptGearMeshParametricStudyTool._Cast_ConceptGearMeshParametricStudyTool",
        ) -> "_4382.GearMeshParametricStudyTool":
            return self._parent._cast(_4382.GearMeshParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "ConceptGearMeshParametricStudyTool._Cast_ConceptGearMeshParametricStudyTool",
        ) -> "_4389.InterMountableComponentConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4389,
            )

            return self._parent._cast(
                _4389.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "ConceptGearMeshParametricStudyTool._Cast_ConceptGearMeshParametricStudyTool",
        ) -> "_4352.ConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4352,
            )

            return self._parent._cast(_4352.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "ConceptGearMeshParametricStudyTool._Cast_ConceptGearMeshParametricStudyTool",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptGearMeshParametricStudyTool._Cast_ConceptGearMeshParametricStudyTool",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearMeshParametricStudyTool._Cast_ConceptGearMeshParametricStudyTool",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearMeshParametricStudyTool._Cast_ConceptGearMeshParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def concept_gear_mesh_parametric_study_tool(
            self: "ConceptGearMeshParametricStudyTool._Cast_ConceptGearMeshParametricStudyTool",
        ) -> "ConceptGearMeshParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ConceptGearMeshParametricStudyTool._Cast_ConceptGearMeshParametricStudyTool",
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
        self: Self, instance_to_wrap: "ConceptGearMeshParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2325.ConceptGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6864.ConceptGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2741.ConceptGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConceptGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptGearMeshParametricStudyTool._Cast_ConceptGearMeshParametricStudyTool":
        return self._Cast_ConceptGearMeshParametricStudyTool(self)
