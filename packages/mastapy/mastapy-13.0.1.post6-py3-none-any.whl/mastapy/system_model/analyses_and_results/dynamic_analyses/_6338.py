"""GearMeshDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "GearMeshDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2313
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6282,
        _6289,
        _6294,
        _6307,
        _6310,
        _6325,
        _6333,
        _6342,
        _6346,
        _6349,
        _6352,
        _6379,
        _6385,
        _6388,
        _6403,
        _6406,
        _6312,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7540,
        _7541,
        _7538,
    )
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshDynamicAnalysis",)


Self = TypeVar("Self", bound="GearMeshDynamicAnalysis")


class GearMeshDynamicAnalysis(_6344.InterMountableComponentConnectionDynamicAnalysis):
    """GearMeshDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshDynamicAnalysis")

    class _Cast_GearMeshDynamicAnalysis:
        """Special nested class for casting GearMeshDynamicAnalysis to subclasses."""

        def __init__(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
            parent: "GearMeshDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6344.InterMountableComponentConnectionDynamicAnalysis":
            return self._parent._cast(
                _6344.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6312.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_7540.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6282.AGMAGleasonConicalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6282

            return self._parent._cast(_6282.AGMAGleasonConicalGearMeshDynamicAnalysis)

        @property
        def bevel_differential_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6289.BevelDifferentialGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6289

            return self._parent._cast(_6289.BevelDifferentialGearMeshDynamicAnalysis)

        @property
        def bevel_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6294.BevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6294

            return self._parent._cast(_6294.BevelGearMeshDynamicAnalysis)

        @property
        def concept_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6307.ConceptGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.ConceptGearMeshDynamicAnalysis)

        @property
        def conical_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6310.ConicalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.ConicalGearMeshDynamicAnalysis)

        @property
        def cylindrical_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6325.CylindricalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6325

            return self._parent._cast(_6325.CylindricalGearMeshDynamicAnalysis)

        @property
        def face_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6333.FaceGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6333

            return self._parent._cast(_6333.FaceGearMeshDynamicAnalysis)

        @property
        def hypoid_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6342.HypoidGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342

            return self._parent._cast(_6342.HypoidGearMeshDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6346.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346

            return self._parent._cast(
                _6346.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6349.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6349

            return self._parent._cast(
                _6349.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6352.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(
                _6352.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6379.SpiralBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.SpiralBevelGearMeshDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6385.StraightBevelDiffGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.StraightBevelDiffGearMeshDynamicAnalysis)

        @property
        def straight_bevel_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6388.StraightBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6388

            return self._parent._cast(_6388.StraightBevelGearMeshDynamicAnalysis)

        @property
        def worm_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6403.WormGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403

            return self._parent._cast(_6403.WormGearMeshDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6406.ZerolBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6406

            return self._parent._cast(_6406.ZerolBevelGearMeshDynamicAnalysis)

        @property
        def gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "GearMeshDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2313.GearMesh":
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
    def cast_to(self: Self) -> "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis":
        return self._Cast_GearMeshDynamicAnalysis(self)
