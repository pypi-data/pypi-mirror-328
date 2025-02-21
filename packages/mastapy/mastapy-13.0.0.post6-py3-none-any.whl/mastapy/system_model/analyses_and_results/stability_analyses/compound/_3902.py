"""AGMAGleasonConicalGearMeshCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3930
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3767
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3909,
        _3914,
        _3960,
        _3997,
        _4003,
        _4006,
        _4024,
        _3956,
        _3962,
        _3932,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshCompoundStabilityAnalysis")


class AGMAGleasonConicalGearMeshCompoundStabilityAnalysis(
    _3930.ConicalGearMeshCompoundStabilityAnalysis
):
    """AGMAGleasonConicalGearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
            parent: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_3930.ConicalGearMeshCompoundStabilityAnalysis":
            return self._parent._cast(_3930.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_3956.GearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3956,
            )

            return self._parent._cast(_3956.GearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_3962.InterMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3962,
            )

            return self._parent._cast(
                _3962.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_3932.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3932,
            )

            return self._parent._cast(_3932.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_3909.BevelDifferentialGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3909,
            )

            return self._parent._cast(
                _3909.BevelDifferentialGearMeshCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_mesh_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_3914.BevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3914,
            )

            return self._parent._cast(_3914.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def hypoid_gear_mesh_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_3960.HypoidGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3960,
            )

            return self._parent._cast(_3960.HypoidGearMeshCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_3997.SpiralBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(
                _3997.SpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_4003.StraightBevelDiffGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4003,
            )

            return self._parent._cast(
                _4003.StraightBevelDiffGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_4006.StraightBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(
                _4006.StraightBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_4024.ZerolBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4024,
            )

            return self._parent._cast(_4024.ZerolBevelGearMeshCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ) -> "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3767.AGMAGleasonConicalGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AGMAGleasonConicalGearMeshStabilityAnalysis]

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
    ) -> "List[_3767.AGMAGleasonConicalGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AGMAGleasonConicalGearMeshStabilityAnalysis]

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
    ) -> "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis":
        return self._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis(self)
