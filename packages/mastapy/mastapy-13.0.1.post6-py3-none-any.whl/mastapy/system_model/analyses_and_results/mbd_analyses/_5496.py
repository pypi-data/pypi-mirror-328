"""StraightBevelDiffGearMeshMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5394
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "StraightBevelDiffGearMeshMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.static_loads import _6961
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
__all__ = ("StraightBevelDiffGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearMeshMultibodyDynamicsAnalysis")


class StraightBevelDiffGearMeshMultibodyDynamicsAnalysis(
    _5394.BevelGearMeshMultibodyDynamicsAnalysis
):
    """StraightBevelDiffGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearMeshMultibodyDynamicsAnalysis"
    )

    class _Cast_StraightBevelDiffGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting StraightBevelDiffGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshMultibodyDynamicsAnalysis",
            parent: "StraightBevelDiffGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5394.BevelGearMeshMultibodyDynamicsAnalysis":
            return self._parent._cast(_5394.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5380.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5380

            return self._parent._cast(
                _5380.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5411.ConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5411

            return self._parent._cast(_5411.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5437.GearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437

            return self._parent._cast(_5437.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5449.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5449

            return self._parent._cast(
                _5449.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5414.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414

            return self._parent._cast(_5414.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "StraightBevelDiffGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7542.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelDiffGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelDiffGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshMultibodyDynamicsAnalysis",
        ) -> "StraightBevelDiffGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "StraightBevelDiffGearMeshMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2325.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6961.StraightBevelDiffGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase

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
    ) -> "StraightBevelDiffGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshMultibodyDynamicsAnalysis":
        return self._Cast_StraightBevelDiffGearMeshMultibodyDynamicsAnalysis(self)
