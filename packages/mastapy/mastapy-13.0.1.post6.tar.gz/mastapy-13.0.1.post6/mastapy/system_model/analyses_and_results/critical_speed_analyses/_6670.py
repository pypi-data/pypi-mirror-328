"""WormGearMeshCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6605
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "WormGearMeshCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2329
    from mastapy.system_model.analyses_and_results.static_loads import _6984
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6611,
        _6578,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="WormGearMeshCriticalSpeedAnalysis")


class WormGearMeshCriticalSpeedAnalysis(_6605.GearMeshCriticalSpeedAnalysis):
    """WormGearMeshCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearMeshCriticalSpeedAnalysis")

    class _Cast_WormGearMeshCriticalSpeedAnalysis:
        """Special nested class for casting WormGearMeshCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "WormGearMeshCriticalSpeedAnalysis._Cast_WormGearMeshCriticalSpeedAnalysis",
            parent: "WormGearMeshCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_critical_speed_analysis(
            self: "WormGearMeshCriticalSpeedAnalysis._Cast_WormGearMeshCriticalSpeedAnalysis",
        ) -> "_6605.GearMeshCriticalSpeedAnalysis":
            return self._parent._cast(_6605.GearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "WormGearMeshCriticalSpeedAnalysis._Cast_WormGearMeshCriticalSpeedAnalysis",
        ) -> "_6611.InterMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6611,
            )

            return self._parent._cast(
                _6611.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "WormGearMeshCriticalSpeedAnalysis._Cast_WormGearMeshCriticalSpeedAnalysis",
        ) -> "_6578.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6578,
            )

            return self._parent._cast(_6578.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "WormGearMeshCriticalSpeedAnalysis._Cast_WormGearMeshCriticalSpeedAnalysis",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "WormGearMeshCriticalSpeedAnalysis._Cast_WormGearMeshCriticalSpeedAnalysis",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "WormGearMeshCriticalSpeedAnalysis._Cast_WormGearMeshCriticalSpeedAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearMeshCriticalSpeedAnalysis._Cast_WormGearMeshCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshCriticalSpeedAnalysis._Cast_WormGearMeshCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_critical_speed_analysis(
            self: "WormGearMeshCriticalSpeedAnalysis._Cast_WormGearMeshCriticalSpeedAnalysis",
        ) -> "WormGearMeshCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearMeshCriticalSpeedAnalysis._Cast_WormGearMeshCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "WormGearMeshCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2329.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6984.WormGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase

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
    ) -> "WormGearMeshCriticalSpeedAnalysis._Cast_WormGearMeshCriticalSpeedAnalysis":
        return self._Cast_WormGearMeshCriticalSpeedAnalysis(self)
