"""HypoidGearMeshCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6548
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "HypoidGearMeshCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2315
    from mastapy.system_model.analyses_and_results.static_loads import _6907
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6576,
        _6605,
        _6611,
        _6578,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="HypoidGearMeshCriticalSpeedAnalysis")


class HypoidGearMeshCriticalSpeedAnalysis(
    _6548.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
):
    """HypoidGearMeshCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearMeshCriticalSpeedAnalysis")

    class _Cast_HypoidGearMeshCriticalSpeedAnalysis:
        """Special nested class for casting HypoidGearMeshCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearMeshCriticalSpeedAnalysis._Cast_HypoidGearMeshCriticalSpeedAnalysis",
            parent: "HypoidGearMeshCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(
            self: "HypoidGearMeshCriticalSpeedAnalysis._Cast_HypoidGearMeshCriticalSpeedAnalysis",
        ) -> "_6548.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis":
            return self._parent._cast(
                _6548.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_critical_speed_analysis(
            self: "HypoidGearMeshCriticalSpeedAnalysis._Cast_HypoidGearMeshCriticalSpeedAnalysis",
        ) -> "_6576.ConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6576,
            )

            return self._parent._cast(_6576.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(
            self: "HypoidGearMeshCriticalSpeedAnalysis._Cast_HypoidGearMeshCriticalSpeedAnalysis",
        ) -> "_6605.GearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6605,
            )

            return self._parent._cast(_6605.GearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "HypoidGearMeshCriticalSpeedAnalysis._Cast_HypoidGearMeshCriticalSpeedAnalysis",
        ) -> "_6611.InterMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6611,
            )

            return self._parent._cast(
                _6611.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "HypoidGearMeshCriticalSpeedAnalysis._Cast_HypoidGearMeshCriticalSpeedAnalysis",
        ) -> "_6578.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6578,
            )

            return self._parent._cast(_6578.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "HypoidGearMeshCriticalSpeedAnalysis._Cast_HypoidGearMeshCriticalSpeedAnalysis",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "HypoidGearMeshCriticalSpeedAnalysis._Cast_HypoidGearMeshCriticalSpeedAnalysis",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "HypoidGearMeshCriticalSpeedAnalysis._Cast_HypoidGearMeshCriticalSpeedAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearMeshCriticalSpeedAnalysis._Cast_HypoidGearMeshCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshCriticalSpeedAnalysis._Cast_HypoidGearMeshCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_critical_speed_analysis(
            self: "HypoidGearMeshCriticalSpeedAnalysis._Cast_HypoidGearMeshCriticalSpeedAnalysis",
        ) -> "HypoidGearMeshCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshCriticalSpeedAnalysis._Cast_HypoidGearMeshCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "HypoidGearMeshCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2315.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6907.HypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase

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
    ) -> (
        "HypoidGearMeshCriticalSpeedAnalysis._Cast_HypoidGearMeshCriticalSpeedAnalysis"
    ):
        return self._Cast_HypoidGearMeshCriticalSpeedAnalysis(self)
