"""KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5450
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
        "KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2320
    from mastapy.system_model.analyses_and_results.static_loads import _6920
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5411,
        _5437,
        _5449,
        _5414,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7542, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis"
)


class KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis(
    _5450.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis
):
    """KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = (
        _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5450.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5450.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5411.ConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5411

            return self._parent._cast(_5411.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5437.GearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437

            return self._parent._cast(_5437.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5449.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5449

            return self._parent._cast(
                _5449.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5414.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414

            return self._parent._cast(_5414.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7542.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2320.KlingelnbergCycloPalloidSpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6920.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis(
            self
        )
