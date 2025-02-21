"""SpiralBevelGearMeshStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3787
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "SpiralBevelGearMeshStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2330
    from mastapy.system_model.analyses_and_results.static_loads import _6963
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3775,
        _3803,
        _3831,
        _3838,
        _3806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshStabilityAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshStabilityAnalysis")


class SpiralBevelGearMeshStabilityAnalysis(_3787.BevelGearMeshStabilityAnalysis):
    """SpiralBevelGearMeshStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearMeshStabilityAnalysis")

    class _Cast_SpiralBevelGearMeshStabilityAnalysis:
        """Special nested class for casting SpiralBevelGearMeshStabilityAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
            parent: "SpiralBevelGearMeshStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_stability_analysis(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ) -> "_3787.BevelGearMeshStabilityAnalysis":
            return self._parent._cast(_3787.BevelGearMeshStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ) -> "_3775.AGMAGleasonConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3775,
            )

            return self._parent._cast(_3775.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ) -> "_3803.ConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3803,
            )

            return self._parent._cast(_3803.ConicalGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ) -> "_3831.GearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3831,
            )

            return self._parent._cast(_3831.GearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ) -> "_3838.InterMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3838,
            )

            return self._parent._cast(
                _3838.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ) -> "_3806.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3806,
            )

            return self._parent._cast(_3806.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_stability_analysis(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ) -> "SpiralBevelGearMeshStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
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
        self: Self, instance_to_wrap: "SpiralBevelGearMeshStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2330.SpiralBevelGearMesh":
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
    def connection_load_case(self: Self) -> "_6963.SpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase

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
    ) -> "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis":
        return self._Cast_SpiralBevelGearMeshStabilityAnalysis(self)
