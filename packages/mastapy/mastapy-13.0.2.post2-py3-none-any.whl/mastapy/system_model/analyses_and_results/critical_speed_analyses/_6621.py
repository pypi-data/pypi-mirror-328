"""KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6584
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
        "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6624,
        _6627,
        _6613,
        _6619,
        _6586,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis"
)


class KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis(
    _6584.ConicalGearMeshCriticalSpeedAnalysis
):
    """KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6584.ConicalGearMeshCriticalSpeedAnalysis":
            return self._parent._cast(_6584.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6613.GearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6613,
            )

            return self._parent._cast(_6613.GearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6619.InterMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(
                _6619.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6586.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6586,
            )

            return self._parent._cast(_6586.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6624.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(
                _6624.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
        ) -> "_6627.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(
                _6627.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2325.KlingelnbergCycloPalloidConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis(
            self
        )
