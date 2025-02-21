"""CylindricalGearMeshParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4360
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CylindricalGearMeshParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2309
    from mastapy.system_model.analyses_and_results.static_loads import _6863
    from mastapy.system_model.analyses_and_results.system_deflections import _2739
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4367,
        _4330,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshParametricStudyTool",)


Self = TypeVar("Self", bound="CylindricalGearMeshParametricStudyTool")


class CylindricalGearMeshParametricStudyTool(_4360.GearMeshParametricStudyTool):
    """CylindricalGearMeshParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearMeshParametricStudyTool"
    )

    class _Cast_CylindricalGearMeshParametricStudyTool:
        """Special nested class for casting CylindricalGearMeshParametricStudyTool to subclasses."""

        def __init__(
            self: "CylindricalGearMeshParametricStudyTool._Cast_CylindricalGearMeshParametricStudyTool",
            parent: "CylindricalGearMeshParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_mesh_parametric_study_tool(
            self: "CylindricalGearMeshParametricStudyTool._Cast_CylindricalGearMeshParametricStudyTool",
        ) -> "_4360.GearMeshParametricStudyTool":
            return self._parent._cast(_4360.GearMeshParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "CylindricalGearMeshParametricStudyTool._Cast_CylindricalGearMeshParametricStudyTool",
        ) -> "_4367.InterMountableComponentConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4367,
            )

            return self._parent._cast(
                _4367.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "CylindricalGearMeshParametricStudyTool._Cast_CylindricalGearMeshParametricStudyTool",
        ) -> "_4330.ConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4330,
            )

            return self._parent._cast(_4330.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "CylindricalGearMeshParametricStudyTool._Cast_CylindricalGearMeshParametricStudyTool",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CylindricalGearMeshParametricStudyTool._Cast_CylindricalGearMeshParametricStudyTool",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearMeshParametricStudyTool._Cast_CylindricalGearMeshParametricStudyTool",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMeshParametricStudyTool._Cast_CylindricalGearMeshParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_gear_mesh_parametric_study_tool(
            self: "CylindricalGearMeshParametricStudyTool._Cast_CylindricalGearMeshParametricStudyTool",
        ) -> "CylindricalGearMeshParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshParametricStudyTool._Cast_CylindricalGearMeshParametricStudyTool",
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
        self: Self, instance_to_wrap: "CylindricalGearMeshParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2309.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6863.CylindricalGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase

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
    ) -> "List[_2739.CylindricalGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearMeshSystemDeflection]

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
    def planetaries(self: Self) -> "List[CylindricalGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CylindricalGearMeshParametricStudyTool]

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
    ) -> "CylindricalGearMeshParametricStudyTool._Cast_CylindricalGearMeshParametricStudyTool":
        return self._Cast_CylindricalGearMeshParametricStudyTool(self)
