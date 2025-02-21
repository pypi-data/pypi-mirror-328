"""BevelDifferentialGearMeshCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4481,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "BevelDifferentialGearMeshCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2321
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4328
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4469,
        _4497,
        _4523,
        _4529,
        _4499,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMeshCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="BevelDifferentialGearMeshCompoundParametricStudyTool")


class BevelDifferentialGearMeshCompoundParametricStudyTool(
    _4481.BevelGearMeshCompoundParametricStudyTool
):
    """BevelDifferentialGearMeshCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearMeshCompoundParametricStudyTool"
    )

    class _Cast_BevelDifferentialGearMeshCompoundParametricStudyTool:
        """Special nested class for casting BevelDifferentialGearMeshCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshCompoundParametricStudyTool._Cast_BevelDifferentialGearMeshCompoundParametricStudyTool",
            parent: "BevelDifferentialGearMeshCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_parametric_study_tool(
            self: "BevelDifferentialGearMeshCompoundParametricStudyTool._Cast_BevelDifferentialGearMeshCompoundParametricStudyTool",
        ) -> "_4481.BevelGearMeshCompoundParametricStudyTool":
            return self._parent._cast(_4481.BevelGearMeshCompoundParametricStudyTool)

        @property
        def agma_gleason_conical_gear_mesh_compound_parametric_study_tool(
            self: "BevelDifferentialGearMeshCompoundParametricStudyTool._Cast_BevelDifferentialGearMeshCompoundParametricStudyTool",
        ) -> "_4469.AGMAGleasonConicalGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4469,
            )

            return self._parent._cast(
                _4469.AGMAGleasonConicalGearMeshCompoundParametricStudyTool
            )

        @property
        def conical_gear_mesh_compound_parametric_study_tool(
            self: "BevelDifferentialGearMeshCompoundParametricStudyTool._Cast_BevelDifferentialGearMeshCompoundParametricStudyTool",
        ) -> "_4497.ConicalGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4497,
            )

            return self._parent._cast(_4497.ConicalGearMeshCompoundParametricStudyTool)

        @property
        def gear_mesh_compound_parametric_study_tool(
            self: "BevelDifferentialGearMeshCompoundParametricStudyTool._Cast_BevelDifferentialGearMeshCompoundParametricStudyTool",
        ) -> "_4523.GearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4523,
            )

            return self._parent._cast(_4523.GearMeshCompoundParametricStudyTool)

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "BevelDifferentialGearMeshCompoundParametricStudyTool._Cast_BevelDifferentialGearMeshCompoundParametricStudyTool",
        ) -> "_4529.InterMountableComponentConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4529,
            )

            return self._parent._cast(
                _4529.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "BevelDifferentialGearMeshCompoundParametricStudyTool._Cast_BevelDifferentialGearMeshCompoundParametricStudyTool",
        ) -> "_4499.ConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4499,
            )

            return self._parent._cast(_4499.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "BevelDifferentialGearMeshCompoundParametricStudyTool._Cast_BevelDifferentialGearMeshCompoundParametricStudyTool",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearMeshCompoundParametricStudyTool._Cast_BevelDifferentialGearMeshCompoundParametricStudyTool",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshCompoundParametricStudyTool._Cast_BevelDifferentialGearMeshCompoundParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_parametric_study_tool(
            self: "BevelDifferentialGearMeshCompoundParametricStudyTool._Cast_BevelDifferentialGearMeshCompoundParametricStudyTool",
        ) -> "BevelDifferentialGearMeshCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshCompoundParametricStudyTool._Cast_BevelDifferentialGearMeshCompoundParametricStudyTool",
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
        self: Self,
        instance_to_wrap: "BevelDifferentialGearMeshCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2321.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2321.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4328.BevelDifferentialGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4328.BevelDifferentialGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearMeshCompoundParametricStudyTool._Cast_BevelDifferentialGearMeshCompoundParametricStudyTool":
        return self._Cast_BevelDifferentialGearMeshCompoundParametricStudyTool(self)
