"""KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2318
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6348,
        _6351,
        _6337,
        _6343,
        _6311,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7539,
        _7540,
        _7537,
    )
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis")


class KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis(
    _6309.ConicalGearMeshDynamicAnalysis
):
    """KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis",
        ) -> "_6309.ConicalGearMeshDynamicAnalysis":
            return self._parent._cast(_6309.ConicalGearMeshDynamicAnalysis)

        @property
        def gear_mesh_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis",
        ) -> "_6337.GearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.GearMeshDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis",
        ) -> "_6343.InterMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6343

            return self._parent._cast(
                _6343.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis",
        ) -> "_6311.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311

            return self._parent._cast(_6311.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis",
        ) -> "_7539.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis",
        ) -> "_7540.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis",
        ) -> "_6348.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6348

            return self._parent._cast(
                _6348.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis",
        ) -> "_6351.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351

            return self._parent._cast(
                _6351.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2318.KlingelnbergCycloPalloidConicalGearMesh":
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
    ) -> "KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis(self)
