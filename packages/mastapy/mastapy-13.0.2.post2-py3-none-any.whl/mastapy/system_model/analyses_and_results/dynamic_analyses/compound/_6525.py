"""StraightBevelGearMeshCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6433
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "StraightBevelGearMeshCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2334
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6396
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6421,
        _6449,
        _6475,
        _6481,
        _6451,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelGearMeshCompoundDynamicAnalysis")


class StraightBevelGearMeshCompoundDynamicAnalysis(
    _6433.BevelGearMeshCompoundDynamicAnalysis
):
    """StraightBevelGearMeshCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearMeshCompoundDynamicAnalysis"
    )

    class _Cast_StraightBevelGearMeshCompoundDynamicAnalysis:
        """Special nested class for casting StraightBevelGearMeshCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshCompoundDynamicAnalysis._Cast_StraightBevelGearMeshCompoundDynamicAnalysis",
            parent: "StraightBevelGearMeshCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_dynamic_analysis(
            self: "StraightBevelGearMeshCompoundDynamicAnalysis._Cast_StraightBevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6433.BevelGearMeshCompoundDynamicAnalysis":
            return self._parent._cast(_6433.BevelGearMeshCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(
            self: "StraightBevelGearMeshCompoundDynamicAnalysis._Cast_StraightBevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6421.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6421,
            )

            return self._parent._cast(
                _6421.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def conical_gear_mesh_compound_dynamic_analysis(
            self: "StraightBevelGearMeshCompoundDynamicAnalysis._Cast_StraightBevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6449.ConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6449,
            )

            return self._parent._cast(_6449.ConicalGearMeshCompoundDynamicAnalysis)

        @property
        def gear_mesh_compound_dynamic_analysis(
            self: "StraightBevelGearMeshCompoundDynamicAnalysis._Cast_StraightBevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6475.GearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6475,
            )

            return self._parent._cast(_6475.GearMeshCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "StraightBevelGearMeshCompoundDynamicAnalysis._Cast_StraightBevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6481.InterMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6481,
            )

            return self._parent._cast(
                _6481.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "StraightBevelGearMeshCompoundDynamicAnalysis._Cast_StraightBevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6451.ConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6451,
            )

            return self._parent._cast(_6451.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "StraightBevelGearMeshCompoundDynamicAnalysis._Cast_StraightBevelGearMeshCompoundDynamicAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearMeshCompoundDynamicAnalysis._Cast_StraightBevelGearMeshCompoundDynamicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshCompoundDynamicAnalysis._Cast_StraightBevelGearMeshCompoundDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_dynamic_analysis(
            self: "StraightBevelGearMeshCompoundDynamicAnalysis._Cast_StraightBevelGearMeshCompoundDynamicAnalysis",
        ) -> "StraightBevelGearMeshCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshCompoundDynamicAnalysis._Cast_StraightBevelGearMeshCompoundDynamicAnalysis",
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
        instance_to_wrap: "StraightBevelGearMeshCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2334.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2334.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

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
    ) -> "List[_6396.StraightBevelGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelGearMeshDynamicAnalysis]

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
    ) -> "List[_6396.StraightBevelGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelGearMeshDynamicAnalysis]

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
    ) -> "StraightBevelGearMeshCompoundDynamicAnalysis._Cast_StraightBevelGearMeshCompoundDynamicAnalysis":
        return self._Cast_StraightBevelGearMeshCompoundDynamicAnalysis(self)
