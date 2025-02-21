"""StraightBevelGearMeshMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5394
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "StraightBevelGearMeshMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2327
    from mastapy.system_model.analyses_and_results.static_loads import _6964
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5380,
        _5411,
        _5437,
        _5449,
        _5414,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7542, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="StraightBevelGearMeshMultibodyDynamicsAnalysis")


class StraightBevelGearMeshMultibodyDynamicsAnalysis(
    _5394.BevelGearMeshMultibodyDynamicsAnalysis
):
    """StraightBevelGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis"
    )

    class _Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting StraightBevelGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
            parent: "StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5394.BevelGearMeshMultibodyDynamicsAnalysis":
            return self._parent._cast(_5394.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5380.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5380

            return self._parent._cast(
                _5380.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5411.ConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5411

            return self._parent._cast(_5411.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5437.GearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437

            return self._parent._cast(_5437.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5449.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5449

            return self._parent._cast(
                _5449.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5414.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414

            return self._parent._cast(_5414.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7542.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "StraightBevelGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "StraightBevelGearMeshMultibodyDynamicsAnalysis.TYPE",
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
    def connection_load_case(self: Self) -> "_6964.StraightBevelGearMeshLoadCase":
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
    ) -> "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis":
        return self._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis(self)
