"""HypoidGearMeshStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3775
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "HypoidGearMeshStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2322
    from mastapy.system_model.analyses_and_results.static_loads import _6915
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3803,
        _3831,
        _3838,
        _3806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshStabilityAnalysis",)


Self = TypeVar("Self", bound="HypoidGearMeshStabilityAnalysis")


class HypoidGearMeshStabilityAnalysis(
    _3775.AGMAGleasonConicalGearMeshStabilityAnalysis
):
    """HypoidGearMeshStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearMeshStabilityAnalysis")

    class _Cast_HypoidGearMeshStabilityAnalysis:
        """Special nested class for casting HypoidGearMeshStabilityAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearMeshStabilityAnalysis._Cast_HypoidGearMeshStabilityAnalysis",
            parent: "HypoidGearMeshStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(
            self: "HypoidGearMeshStabilityAnalysis._Cast_HypoidGearMeshStabilityAnalysis",
        ) -> "_3775.AGMAGleasonConicalGearMeshStabilityAnalysis":
            return self._parent._cast(_3775.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(
            self: "HypoidGearMeshStabilityAnalysis._Cast_HypoidGearMeshStabilityAnalysis",
        ) -> "_3803.ConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3803,
            )

            return self._parent._cast(_3803.ConicalGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "HypoidGearMeshStabilityAnalysis._Cast_HypoidGearMeshStabilityAnalysis",
        ) -> "_3831.GearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3831,
            )

            return self._parent._cast(_3831.GearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "HypoidGearMeshStabilityAnalysis._Cast_HypoidGearMeshStabilityAnalysis",
        ) -> "_3838.InterMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3838,
            )

            return self._parent._cast(
                _3838.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "HypoidGearMeshStabilityAnalysis._Cast_HypoidGearMeshStabilityAnalysis",
        ) -> "_3806.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3806,
            )

            return self._parent._cast(_3806.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "HypoidGearMeshStabilityAnalysis._Cast_HypoidGearMeshStabilityAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "HypoidGearMeshStabilityAnalysis._Cast_HypoidGearMeshStabilityAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "HypoidGearMeshStabilityAnalysis._Cast_HypoidGearMeshStabilityAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearMeshStabilityAnalysis._Cast_HypoidGearMeshStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshStabilityAnalysis._Cast_HypoidGearMeshStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_stability_analysis(
            self: "HypoidGearMeshStabilityAnalysis._Cast_HypoidGearMeshStabilityAnalysis",
        ) -> "HypoidGearMeshStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshStabilityAnalysis._Cast_HypoidGearMeshStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearMeshStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2322.HypoidGearMesh":
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
    def connection_load_case(self: Self) -> "_6915.HypoidGearMeshLoadCase":
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
    ) -> "HypoidGearMeshStabilityAnalysis._Cast_HypoidGearMeshStabilityAnalysis":
        return self._Cast_HypoidGearMeshStabilityAnalysis(self)
