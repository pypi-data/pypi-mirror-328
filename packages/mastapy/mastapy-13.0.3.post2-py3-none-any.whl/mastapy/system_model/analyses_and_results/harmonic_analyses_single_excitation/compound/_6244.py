"""PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6209,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6115,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6220,
        _6258,
        _6160,
        _6239,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation"
)


class PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation(
    _6209.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation
):
    """PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6209.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6209.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6220.GearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6220,
            )

            return self._parent._cast(
                _6220.GearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6258.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6258,
            )

            return self._parent._cast(
                _6258.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6160.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6160,
            )

            return self._parent._cast(
                _6160.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6239.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6239,
            )

            return self._parent._cast(
                _6239.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6115.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6115.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation]

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
    ) -> "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
