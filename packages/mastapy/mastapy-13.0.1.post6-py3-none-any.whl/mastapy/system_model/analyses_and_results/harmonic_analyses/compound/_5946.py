"""KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5912
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
        "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5776
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5949,
        _5952,
        _5938,
        _5944,
        _5914,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis"
)


class KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis(
    _5912.ConicalGearMeshCompoundHarmonicAnalysis
):
    """KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5912.ConicalGearMeshCompoundHarmonicAnalysis":
            return self._parent._cast(_5912.ConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def gear_mesh_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5938.GearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5938,
            )

            return self._parent._cast(_5938.GearMeshCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5944.InterMountableComponentConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5944,
            )

            return self._parent._cast(
                _5944.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5914.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5914,
            )

            return self._parent._cast(_5914.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5949.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5949,
            )

            return self._parent._cast(
                _5949.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ) -> (
            "_5952.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5952,
            )

            return self._parent._cast(
                _5952.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5776.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis]

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
    ) -> "List[_5776.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis]

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
    ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis(
                self
            )
        )
