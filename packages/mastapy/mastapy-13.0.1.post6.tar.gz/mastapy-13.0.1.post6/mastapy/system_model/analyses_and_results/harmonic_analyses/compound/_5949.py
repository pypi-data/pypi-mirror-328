"""KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5946
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
        "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2319
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5779
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5912,
        _5938,
        _5944,
        _5914,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis"
)


class KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis(
    _5946.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",
        ) -> "_5946.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis":
            return self._parent._cast(
                _5946.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def conical_gear_mesh_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",
        ) -> "_5912.ConicalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(_5912.ConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def gear_mesh_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",
        ) -> "_5938.GearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5938,
            )

            return self._parent._cast(_5938.GearMeshCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",
        ) -> "_5944.InterMountableComponentConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5944,
            )

            return self._parent._cast(
                _5944.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",
        ) -> "_5914.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5914,
            )

            return self._parent._cast(_5914.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2319.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2319.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

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
    ) -> "List[_5779.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis]

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
    ) -> "List[_5779.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis]

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
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis(
                self
            )
        )
