"""PlanetaryGearSetCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5928
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "PlanetaryGearSetCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5794
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5939,
        _5977,
        _5879,
        _5958,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundHarmonicAnalysis")


class PlanetaryGearSetCompoundHarmonicAnalysis(
    _5928.CylindricalGearSetCompoundHarmonicAnalysis
):
    """PlanetaryGearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetCompoundHarmonicAnalysis"
    )

    class _Cast_PlanetaryGearSetCompoundHarmonicAnalysis:
        """Special nested class for casting PlanetaryGearSetCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
            parent: "PlanetaryGearSetCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_harmonic_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
        ) -> "_5928.CylindricalGearSetCompoundHarmonicAnalysis":
            return self._parent._cast(_5928.CylindricalGearSetCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
        ) -> "_5939.GearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5939,
            )

            return self._parent._cast(_5939.GearSetCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
        ) -> "_5977.SpecialisedAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5977,
            )

            return self._parent._cast(_5977.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
        ) -> "_5879.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5879,
            )

            return self._parent._cast(_5879.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
        ) -> "_5958.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_harmonic_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
        ) -> "PlanetaryGearSetCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5794.PlanetaryGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.PlanetaryGearSetHarmonicAnalysis]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5794.PlanetaryGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.PlanetaryGearSetHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis":
        return self._Cast_PlanetaryGearSetCompoundHarmonicAnalysis(self)
