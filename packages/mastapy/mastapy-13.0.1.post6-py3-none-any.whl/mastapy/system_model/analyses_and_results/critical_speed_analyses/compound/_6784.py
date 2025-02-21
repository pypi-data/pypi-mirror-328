"""StraightBevelGearMeshCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6692,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "StraightBevelGearMeshCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2327
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6655
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6680,
        _6708,
        _6734,
        _6740,
        _6710,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="StraightBevelGearMeshCompoundCriticalSpeedAnalysis")


class StraightBevelGearMeshCompoundCriticalSpeedAnalysis(
    _6692.BevelGearMeshCompoundCriticalSpeedAnalysis
):
    """StraightBevelGearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearMeshCompoundCriticalSpeedAnalysis"
    )

    class _Cast_StraightBevelGearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting StraightBevelGearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCompoundCriticalSpeedAnalysis",
            parent: "StraightBevelGearMeshCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(
            self: "StraightBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6692.BevelGearMeshCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6692.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(
            self: "StraightBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6680.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6680,
            )

            return self._parent._cast(
                _6680.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(
            self: "StraightBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6708.ConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(
                _6708.ConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "StraightBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6734.GearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6734,
            )

            return self._parent._cast(_6734.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "StraightBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6740.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6740,
            )

            return self._parent._cast(
                _6740.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "StraightBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6710.ConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6710,
            )

            return self._parent._cast(_6710.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "StraightBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "StraightBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "StraightBevelGearMeshCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "StraightBevelGearMeshCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2327.StraightBevelGearMesh":
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
    def connection_design(self: Self) -> "_2327.StraightBevelGearMesh":
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
    ) -> "List[_6655.StraightBevelGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.StraightBevelGearMeshCriticalSpeedAnalysis]

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
    ) -> "List[_6655.StraightBevelGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.StraightBevelGearMeshCriticalSpeedAnalysis]

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
    ) -> "StraightBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCompoundCriticalSpeedAnalysis":
        return self._Cast_StraightBevelGearMeshCompoundCriticalSpeedAnalysis(self)
