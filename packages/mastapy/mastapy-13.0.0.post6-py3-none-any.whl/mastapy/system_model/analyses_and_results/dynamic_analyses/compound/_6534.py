"""ZerolBevelGearMeshCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6424
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ZerolBevelGearMeshCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2331
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6405
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
__all__ = ("ZerolBevelGearMeshCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearMeshCompoundDynamicAnalysis")


class ZerolBevelGearMeshCompoundDynamicAnalysis(
    _6424.BevelGearMeshCompoundDynamicAnalysis
):
    """ZerolBevelGearMeshCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearMeshCompoundDynamicAnalysis"
    )

    class _Cast_ZerolBevelGearMeshCompoundDynamicAnalysis:
        """Special nested class for casting ZerolBevelGearMeshCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshCompoundDynamicAnalysis._Cast_ZerolBevelGearMeshCompoundDynamicAnalysis",
            parent: "ZerolBevelGearMeshCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_dynamic_analysis(
            self: "ZerolBevelGearMeshCompoundDynamicAnalysis._Cast_ZerolBevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6424.BevelGearMeshCompoundDynamicAnalysis":
            return self._parent._cast(_6424.BevelGearMeshCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(
            self: "ZerolBevelGearMeshCompoundDynamicAnalysis._Cast_ZerolBevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6412.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6412,
            )

            return self._parent._cast(
                _6412.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def conical_gear_mesh_compound_dynamic_analysis(
            self: "ZerolBevelGearMeshCompoundDynamicAnalysis._Cast_ZerolBevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6440.ConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6440,
            )

            return self._parent._cast(_6440.ConicalGearMeshCompoundDynamicAnalysis)

        @property
        def gear_mesh_compound_dynamic_analysis(
            self: "ZerolBevelGearMeshCompoundDynamicAnalysis._Cast_ZerolBevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6466.GearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6466,
            )

            return self._parent._cast(_6466.GearMeshCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "ZerolBevelGearMeshCompoundDynamicAnalysis._Cast_ZerolBevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6472.InterMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6472,
            )

            return self._parent._cast(
                _6472.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "ZerolBevelGearMeshCompoundDynamicAnalysis._Cast_ZerolBevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6442.ConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6442,
            )

            return self._parent._cast(_6442.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "ZerolBevelGearMeshCompoundDynamicAnalysis._Cast_ZerolBevelGearMeshCompoundDynamicAnalysis",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearMeshCompoundDynamicAnalysis._Cast_ZerolBevelGearMeshCompoundDynamicAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearMeshCompoundDynamicAnalysis._Cast_ZerolBevelGearMeshCompoundDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ZerolBevelGearMeshCompoundDynamicAnalysis._Cast_ZerolBevelGearMeshCompoundDynamicAnalysis",
        ) -> "ZerolBevelGearMeshCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshCompoundDynamicAnalysis._Cast_ZerolBevelGearMeshCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "ZerolBevelGearMeshCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2331.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2331.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

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
    ) -> "List[_6405.ZerolBevelGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ZerolBevelGearMeshDynamicAnalysis]

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
    ) -> "List[_6405.ZerolBevelGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ZerolBevelGearMeshDynamicAnalysis]

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
    ) -> "ZerolBevelGearMeshCompoundDynamicAnalysis._Cast_ZerolBevelGearMeshCompoundDynamicAnalysis":
        return self._Cast_ZerolBevelGearMeshCompoundDynamicAnalysis(self)
