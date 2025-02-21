"""BevelDifferentialGearMeshCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6424
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "BevelDifferentialGearMeshCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2301
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6288
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6412,
        _6440,
        _6466,
        _6472,
        _6442,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMeshCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearMeshCompoundDynamicAnalysis")


class BevelDifferentialGearMeshCompoundDynamicAnalysis(
    _6424.BevelGearMeshCompoundDynamicAnalysis
):
    """BevelDifferentialGearMeshCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearMeshCompoundDynamicAnalysis"
    )

    class _Cast_BevelDifferentialGearMeshCompoundDynamicAnalysis:
        """Special nested class for casting BevelDifferentialGearMeshCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshCompoundDynamicAnalysis._Cast_BevelDifferentialGearMeshCompoundDynamicAnalysis",
            parent: "BevelDifferentialGearMeshCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_dynamic_analysis(
            self: "BevelDifferentialGearMeshCompoundDynamicAnalysis._Cast_BevelDifferentialGearMeshCompoundDynamicAnalysis",
        ) -> "_6424.BevelGearMeshCompoundDynamicAnalysis":
            return self._parent._cast(_6424.BevelGearMeshCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(
            self: "BevelDifferentialGearMeshCompoundDynamicAnalysis._Cast_BevelDifferentialGearMeshCompoundDynamicAnalysis",
        ) -> "_6412.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6412,
            )

            return self._parent._cast(
                _6412.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def conical_gear_mesh_compound_dynamic_analysis(
            self: "BevelDifferentialGearMeshCompoundDynamicAnalysis._Cast_BevelDifferentialGearMeshCompoundDynamicAnalysis",
        ) -> "_6440.ConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6440,
            )

            return self._parent._cast(_6440.ConicalGearMeshCompoundDynamicAnalysis)

        @property
        def gear_mesh_compound_dynamic_analysis(
            self: "BevelDifferentialGearMeshCompoundDynamicAnalysis._Cast_BevelDifferentialGearMeshCompoundDynamicAnalysis",
        ) -> "_6466.GearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6466,
            )

            return self._parent._cast(_6466.GearMeshCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "BevelDifferentialGearMeshCompoundDynamicAnalysis._Cast_BevelDifferentialGearMeshCompoundDynamicAnalysis",
        ) -> "_6472.InterMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6472,
            )

            return self._parent._cast(
                _6472.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "BevelDifferentialGearMeshCompoundDynamicAnalysis._Cast_BevelDifferentialGearMeshCompoundDynamicAnalysis",
        ) -> "_6442.ConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6442,
            )

            return self._parent._cast(_6442.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "BevelDifferentialGearMeshCompoundDynamicAnalysis._Cast_BevelDifferentialGearMeshCompoundDynamicAnalysis",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearMeshCompoundDynamicAnalysis._Cast_BevelDifferentialGearMeshCompoundDynamicAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshCompoundDynamicAnalysis._Cast_BevelDifferentialGearMeshCompoundDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_dynamic_analysis(
            self: "BevelDifferentialGearMeshCompoundDynamicAnalysis._Cast_BevelDifferentialGearMeshCompoundDynamicAnalysis",
        ) -> "BevelDifferentialGearMeshCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshCompoundDynamicAnalysis._Cast_BevelDifferentialGearMeshCompoundDynamicAnalysis",
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
        instance_to_wrap: "BevelDifferentialGearMeshCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2301.BevelDifferentialGearMesh":
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
    def connection_design(self: Self) -> "_2301.BevelDifferentialGearMesh":
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
    ) -> "List[_6288.BevelDifferentialGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialGearMeshDynamicAnalysis]

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
    ) -> "List[_6288.BevelDifferentialGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialGearMeshDynamicAnalysis]

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
    ) -> "BevelDifferentialGearMeshCompoundDynamicAnalysis._Cast_BevelDifferentialGearMeshCompoundDynamicAnalysis":
        return self._Cast_BevelDifferentialGearMeshCompoundDynamicAnalysis(self)
