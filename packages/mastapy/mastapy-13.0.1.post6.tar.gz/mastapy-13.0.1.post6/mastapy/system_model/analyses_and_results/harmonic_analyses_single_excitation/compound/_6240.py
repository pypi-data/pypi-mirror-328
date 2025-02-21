"""SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6157,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6111,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6238,
        _6239,
        _6145,
        _6173,
        _6199,
        _6237,
        _6139,
        _6218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation"
)


class SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation(
    _6157.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
):
    """SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6157.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6157.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6145.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6145,
            )

            return self._parent._cast(
                _6145.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6173.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6173,
            )

            return self._parent._cast(
                _6173.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6199.GearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6199,
            )

            return self._parent._cast(
                _6199.GearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6237.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6237,
            )

            return self._parent._cast(
                _6237.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6139.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6139,
            )

            return self._parent._cast(
                _6139.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6218.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6218,
            )

            return self._parent._cast(
                _6218.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2544.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2544.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6111.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation]

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
    def spiral_bevel_gears_compound_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6238.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearsCompoundHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes_compound_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6239.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshesCompoundHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6111.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation]

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
    ) -> "SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
