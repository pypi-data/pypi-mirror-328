"""GearMeshCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6739,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "GearMeshCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6604
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6679,
        _6686,
        _6691,
        _6704,
        _6707,
        _6722,
        _6728,
        _6737,
        _6741,
        _6744,
        _6747,
        _6774,
        _6780,
        _6783,
        _6798,
        _6801,
        _6709,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="GearMeshCompoundCriticalSpeedAnalysis")


class GearMeshCompoundCriticalSpeedAnalysis(
    _6739.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
):
    """GearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearMeshCompoundCriticalSpeedAnalysis"
    )

    class _Cast_GearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting GearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
            parent: "GearMeshCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6739.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6739.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6709.ConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6709,
            )

            return self._parent._cast(_6709.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6679.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6679,
            )

            return self._parent._cast(
                _6679.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6686.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6686,
            )

            return self._parent._cast(
                _6686.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6691.BevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6691,
            )

            return self._parent._cast(_6691.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def concept_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6704.ConceptGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6704,
            )

            return self._parent._cast(
                _6704.ConceptGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6707.ConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6707,
            )

            return self._parent._cast(
                _6707.ConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6722.CylindricalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6722,
            )

            return self._parent._cast(
                _6722.CylindricalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6728.FaceGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6728,
            )

            return self._parent._cast(_6728.FaceGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6737.HypoidGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6737,
            )

            return self._parent._cast(_6737.HypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> (
            "_6741.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6741,
            )

            return self._parent._cast(
                _6741.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> (
            "_6744.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6744,
            )

            return self._parent._cast(
                _6744.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6747.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6747,
            )

            return self._parent._cast(
                _6747.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6774.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6774,
            )

            return self._parent._cast(
                _6774.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6780.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(
                _6780.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6783.StraightBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6783,
            )

            return self._parent._cast(
                _6783.StraightBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6798.WormGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6798,
            )

            return self._parent._cast(_6798.WormGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6801.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6801,
            )

            return self._parent._cast(
                _6801.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "GearMeshCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "GearMeshCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6604.GearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.GearMeshCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6604.GearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.GearMeshCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis":
        return self._Cast_GearMeshCompoundCriticalSpeedAnalysis(self)
