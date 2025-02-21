"""SpiralBevelGearMeshCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6691,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6645
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6679,
        _6707,
        _6733,
        _6739,
        _6709,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshCompoundCriticalSpeedAnalysis")


class SpiralBevelGearMeshCompoundCriticalSpeedAnalysis(
    _6691.BevelGearMeshCompoundCriticalSpeedAnalysis
):
    """SpiralBevelGearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis"
    )

    class _Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting SpiralBevelGearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
            parent: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6691.BevelGearMeshCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6691.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6679.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6679,
            )

            return self._parent._cast(
                _6679.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6707.ConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6707,
            )

            return self._parent._cast(
                _6707.ConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6733.GearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6733,
            )

            return self._parent._cast(_6733.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6739.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6739,
            )

            return self._parent._cast(
                _6739.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6709.ConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6709,
            )

            return self._parent._cast(_6709.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2323.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2323.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

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
    ) -> "List[_6645.SpiralBevelGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.SpiralBevelGearMeshCriticalSpeedAnalysis]

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
    ) -> "List[_6645.SpiralBevelGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.SpiralBevelGearMeshCriticalSpeedAnalysis]

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
    ) -> "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
        return self._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis(self)
