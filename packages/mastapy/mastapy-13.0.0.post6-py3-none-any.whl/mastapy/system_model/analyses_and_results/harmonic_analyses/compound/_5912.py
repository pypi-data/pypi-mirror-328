"""ConicalGearSetCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5938
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "ConicalGearSetCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5713
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5884,
        _5891,
        _5896,
        _5942,
        _5946,
        _5949,
        _5952,
        _5979,
        _5985,
        _5988,
        _6006,
        _5976,
        _5878,
        _5957,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearSetCompoundHarmonicAnalysis")


class ConicalGearSetCompoundHarmonicAnalysis(_5938.GearSetCompoundHarmonicAnalysis):
    """ConicalGearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetCompoundHarmonicAnalysis"
    )

    class _Cast_ConicalGearSetCompoundHarmonicAnalysis:
        """Special nested class for casting ConicalGearSetCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
            parent: "ConicalGearSetCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5938.GearSetCompoundHarmonicAnalysis":
            return self._parent._cast(_5938.GearSetCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5976.SpecialisedAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5976,
            )

            return self._parent._cast(_5976.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5878.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5878,
            )

            return self._parent._cast(_5878.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5957.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5957,
            )

            return self._parent._cast(_5957.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5884.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5884,
            )

            return self._parent._cast(
                _5884.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5891.BevelDifferentialGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5891,
            )

            return self._parent._cast(
                _5891.BevelDifferentialGearSetCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5896.BevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5896,
            )

            return self._parent._cast(_5896.BevelGearSetCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5942.HypoidGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5942,
            )

            return self._parent._cast(_5942.HypoidGearSetCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5946.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5946,
            )

            return self._parent._cast(
                _5946.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5949.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5949,
            )

            return self._parent._cast(
                _5949.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5952.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5952,
            )

            return self._parent._cast(
                _5952.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5979.SpiralBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(_5979.SpiralBevelGearSetCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5985.StraightBevelDiffGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5985,
            )

            return self._parent._cast(
                _5985.StraightBevelDiffGearSetCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5988.StraightBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5988,
            )

            return self._parent._cast(
                _5988.StraightBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_6006.ZerolBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6006,
            )

            return self._parent._cast(_6006.ZerolBevelGearSetCompoundHarmonicAnalysis)

        @property
        def conical_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ) -> "ConicalGearSetCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearSetCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5713.ConicalGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearSetHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5713.ConicalGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearSetHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis":
        return self._Cast_ConicalGearSetCompoundHarmonicAnalysis(self)
