"""KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5449
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
        "KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2319
    from mastapy.system_model.analyses_and_results.static_loads import _6916
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5410,
        _5436,
        _5448,
        _5413,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis"
)


class KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis(
    _5449.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5449.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5449.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5410.ConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410

            return self._parent._cast(_5410.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5436.GearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(_5436.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5448.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5448

            return self._parent._cast(
                _5448.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5413.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5413

            return self._parent._cast(_5413.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7541.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2319.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

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
    ) -> "_6916.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase

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
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis(
                self
            )
        )
