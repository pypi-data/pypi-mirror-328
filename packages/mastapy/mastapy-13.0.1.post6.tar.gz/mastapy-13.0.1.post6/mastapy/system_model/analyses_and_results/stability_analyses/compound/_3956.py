"""GearMeshCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3962
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "GearMeshCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3823
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3902,
        _3909,
        _3914,
        _3927,
        _3930,
        _3945,
        _3951,
        _3960,
        _3964,
        _3967,
        _3970,
        _3997,
        _4003,
        _4006,
        _4021,
        _4024,
        _3932,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="GearMeshCompoundStabilityAnalysis")


class GearMeshCompoundStabilityAnalysis(
    _3962.InterMountableComponentConnectionCompoundStabilityAnalysis
):
    """GearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshCompoundStabilityAnalysis")

    class _Cast_GearMeshCompoundStabilityAnalysis:
        """Special nested class for casting GearMeshCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
            parent: "GearMeshCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3962.InterMountableComponentConnectionCompoundStabilityAnalysis":
            return self._parent._cast(
                _3962.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3932.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3932,
            )

            return self._parent._cast(_3932.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3902.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3902,
            )

            return self._parent._cast(
                _3902.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3909.BevelDifferentialGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3909,
            )

            return self._parent._cast(
                _3909.BevelDifferentialGearMeshCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3914.BevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3914,
            )

            return self._parent._cast(_3914.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def concept_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3927.ConceptGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3927,
            )

            return self._parent._cast(_3927.ConceptGearMeshCompoundStabilityAnalysis)

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3930.ConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3945.CylindricalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3945,
            )

            return self._parent._cast(
                _3945.CylindricalGearMeshCompoundStabilityAnalysis
            )

        @property
        def face_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3951.FaceGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3951,
            )

            return self._parent._cast(_3951.FaceGearMeshCompoundStabilityAnalysis)

        @property
        def hypoid_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3960.HypoidGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3960,
            )

            return self._parent._cast(_3960.HypoidGearMeshCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3964.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3964,
            )

            return self._parent._cast(
                _3964.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3967.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3967,
            )

            return self._parent._cast(
                _3967.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> (
            "_3970.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3970,
            )

            return self._parent._cast(
                _3970.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3997.SpiralBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(
                _3997.SpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_4003.StraightBevelDiffGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4003,
            )

            return self._parent._cast(
                _4003.StraightBevelDiffGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_4006.StraightBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(
                _4006.StraightBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def worm_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_4021.WormGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4021,
            )

            return self._parent._cast(_4021.WormGearMeshCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_4024.ZerolBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4024,
            )

            return self._parent._cast(_4024.ZerolBevelGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "GearMeshCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "GearMeshCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3823.GearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.GearMeshStabilityAnalysis]

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
    ) -> "List[_3823.GearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.GearMeshStabilityAnalysis]

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
    ) -> "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis":
        return self._Cast_GearMeshCompoundStabilityAnalysis(self)
