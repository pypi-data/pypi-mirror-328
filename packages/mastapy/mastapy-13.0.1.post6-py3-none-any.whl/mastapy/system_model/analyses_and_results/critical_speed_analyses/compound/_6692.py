"""BevelGearMeshCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6680,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "BevelGearMeshCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6560
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6687,
        _6775,
        _6781,
        _6784,
        _6802,
        _6708,
        _6734,
        _6740,
        _6710,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelGearMeshCompoundCriticalSpeedAnalysis")


class BevelGearMeshCompoundCriticalSpeedAnalysis(
    _6680.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
):
    """BevelGearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshCompoundCriticalSpeedAnalysis"
    )

    class _Cast_BevelGearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting BevelGearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
            parent: "BevelGearMeshCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6680.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6680.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6708.ConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(
                _6708.ConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6734.GearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6734,
            )

            return self._parent._cast(_6734.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6740.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6740,
            )

            return self._parent._cast(
                _6740.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6710.ConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6710,
            )

            return self._parent._cast(_6710.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6687.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6687,
            )

            return self._parent._cast(
                _6687.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6775.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(
                _6775.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6781.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6781,
            )

            return self._parent._cast(
                _6781.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6784.StraightBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6784,
            )

            return self._parent._cast(
                _6784.StraightBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6802.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6802,
            )

            return self._parent._cast(
                _6802.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "BevelGearMeshCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearMeshCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6560.BevelGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelGearMeshCriticalSpeedAnalysis]

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
    ) -> "List[_6560.BevelGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelGearMeshCriticalSpeedAnalysis]

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
    ) -> "BevelGearMeshCompoundCriticalSpeedAnalysis._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis":
        return self._Cast_BevelGearMeshCompoundCriticalSpeedAnalysis(self)
