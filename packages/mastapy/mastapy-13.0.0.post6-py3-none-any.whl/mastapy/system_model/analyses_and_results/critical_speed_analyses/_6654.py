"""StraightBevelGearMeshCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6559
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "StraightBevelGearMeshCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2327
    from mastapy.system_model.analyses_and_results.static_loads import _6963
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6547,
        _6575,
        _6604,
        _6610,
        _6577,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7540, _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="StraightBevelGearMeshCriticalSpeedAnalysis")


class StraightBevelGearMeshCriticalSpeedAnalysis(
    _6559.BevelGearMeshCriticalSpeedAnalysis
):
    """StraightBevelGearMeshCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearMeshCriticalSpeedAnalysis"
    )

    class _Cast_StraightBevelGearMeshCriticalSpeedAnalysis:
        """Special nested class for casting StraightBevelGearMeshCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCriticalSpeedAnalysis",
            parent: "StraightBevelGearMeshCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_critical_speed_analysis(
            self: "StraightBevelGearMeshCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6559.BevelGearMeshCriticalSpeedAnalysis":
            return self._parent._cast(_6559.BevelGearMeshCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(
            self: "StraightBevelGearMeshCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6547.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6547,
            )

            return self._parent._cast(
                _6547.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_critical_speed_analysis(
            self: "StraightBevelGearMeshCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6575.ConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6575,
            )

            return self._parent._cast(_6575.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(
            self: "StraightBevelGearMeshCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6604.GearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6604,
            )

            return self._parent._cast(_6604.GearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "StraightBevelGearMeshCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6610.InterMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6610,
            )

            return self._parent._cast(
                _6610.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "StraightBevelGearMeshCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6577.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6577,
            )

            return self._parent._cast(_6577.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelGearMeshCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_7540.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelGearMeshCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelGearMeshCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearMeshCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_critical_speed_analysis(
            self: "StraightBevelGearMeshCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCriticalSpeedAnalysis",
        ) -> "StraightBevelGearMeshCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelGearMeshCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_load_case(self: Self) -> "_6963.StraightBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearMeshCriticalSpeedAnalysis._Cast_StraightBevelGearMeshCriticalSpeedAnalysis":
        return self._Cast_StraightBevelGearMeshCriticalSpeedAnalysis(self)
