"""KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6750,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
        "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2327
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6627
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6716,
        _6742,
        _6748,
        _6718,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
)


class KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis(
    _6750.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis
):
    """KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> (
            "_6750.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis"
        ):
            return self._parent._cast(
                _6750.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6716.ConicalGearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6716,
            )

            return self._parent._cast(
                _6716.ConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6742.GearMeshCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6742,
            )

            return self._parent._cast(_6742.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6748.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6748,
            )

            return self._parent._cast(
                _6748.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_6718.ConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6718,
            )

            return self._parent._cast(_6718.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(
        self: Self,
    ) -> "_2327.KlingelnbergCycloPalloidSpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(
        self: Self,
    ) -> "_2327.KlingelnbergCycloPalloidSpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6627.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6627.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis(
            self
        )
