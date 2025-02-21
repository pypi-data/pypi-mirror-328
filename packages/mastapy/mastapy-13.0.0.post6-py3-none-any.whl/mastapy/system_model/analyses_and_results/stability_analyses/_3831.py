"""KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3795
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2318
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3834,
        _3837,
        _3823,
        _3830,
        _3798,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7540, _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis")


class KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis(
    _3795.ConicalGearMeshStabilityAnalysis
):
    """KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
        ) -> "_3795.ConicalGearMeshStabilityAnalysis":
            return self._parent._cast(_3795.ConicalGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
        ) -> "_3823.GearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3823,
            )

            return self._parent._cast(_3823.GearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
        ) -> "_3830.InterMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3830,
            )

            return self._parent._cast(
                _3830.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
        ) -> "_3798.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3798,
            )

            return self._parent._cast(_3798.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
        ) -> "_7540.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
        ) -> "_3834.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3834,
            )

            return self._parent._cast(
                _3834.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
        ) -> "_3837.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3837,
            )

            return self._parent._cast(
                _3837.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis.TYPE",
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
    ) -> "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis(self)
