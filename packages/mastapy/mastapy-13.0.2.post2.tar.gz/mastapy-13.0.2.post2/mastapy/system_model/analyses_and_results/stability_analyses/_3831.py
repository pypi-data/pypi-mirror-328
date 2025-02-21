"""GearMeshStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3838
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "GearMeshStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2320
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3775,
        _3782,
        _3787,
        _3800,
        _3803,
        _3819,
        _3826,
        _3835,
        _3839,
        _3842,
        _3845,
        _3872,
        _3881,
        _3884,
        _3899,
        _3902,
        _3806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshStabilityAnalysis",)


Self = TypeVar("Self", bound="GearMeshStabilityAnalysis")


class GearMeshStabilityAnalysis(
    _3838.InterMountableComponentConnectionStabilityAnalysis
):
    """GearMeshStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshStabilityAnalysis")

    class _Cast_GearMeshStabilityAnalysis:
        """Special nested class for casting GearMeshStabilityAnalysis to subclasses."""

        def __init__(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
            parent: "GearMeshStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3838.InterMountableComponentConnectionStabilityAnalysis":
            return self._parent._cast(
                _3838.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3806.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3806,
            )

            return self._parent._cast(_3806.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3775.AGMAGleasonConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3775,
            )

            return self._parent._cast(_3775.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def bevel_differential_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3782.BevelDifferentialGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3782,
            )

            return self._parent._cast(_3782.BevelDifferentialGearMeshStabilityAnalysis)

        @property
        def bevel_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3787.BevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3787,
            )

            return self._parent._cast(_3787.BevelGearMeshStabilityAnalysis)

        @property
        def concept_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3800.ConceptGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3800,
            )

            return self._parent._cast(_3800.ConceptGearMeshStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3803.ConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3803,
            )

            return self._parent._cast(_3803.ConicalGearMeshStabilityAnalysis)

        @property
        def cylindrical_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3819.CylindricalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.CylindricalGearMeshStabilityAnalysis)

        @property
        def face_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3826.FaceGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3826,
            )

            return self._parent._cast(_3826.FaceGearMeshStabilityAnalysis)

        @property
        def hypoid_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3835.HypoidGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3835,
            )

            return self._parent._cast(_3835.HypoidGearMeshStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3839.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(
                _3839.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3842.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(
                _3842.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3845.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3845,
            )

            return self._parent._cast(
                _3845.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3872.SpiralBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3872,
            )

            return self._parent._cast(_3872.SpiralBevelGearMeshStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3881.StraightBevelDiffGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3881,
            )

            return self._parent._cast(_3881.StraightBevelDiffGearMeshStabilityAnalysis)

        @property
        def straight_bevel_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3884.StraightBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3884,
            )

            return self._parent._cast(_3884.StraightBevelGearMeshStabilityAnalysis)

        @property
        def worm_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3899.WormGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3899,
            )

            return self._parent._cast(_3899.WormGearMeshStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3902.ZerolBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3902,
            )

            return self._parent._cast(_3902.ZerolBevelGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "GearMeshStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2320.GearMesh":
        """mastapy.system_model.connections_and_sockets.gears.GearMesh

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
    ) -> "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis":
        return self._Cast_GearMeshStabilityAnalysis(self)
