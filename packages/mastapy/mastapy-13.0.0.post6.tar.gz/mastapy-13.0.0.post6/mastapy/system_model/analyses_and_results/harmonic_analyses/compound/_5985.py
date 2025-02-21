"""StraightBevelDiffGearSetCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5896
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "StraightBevelDiffGearSetCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5820
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5983,
        _5984,
        _5884,
        _5912,
        _5938,
        _5976,
        _5878,
        _5957,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetCompoundHarmonicAnalysis")


class StraightBevelDiffGearSetCompoundHarmonicAnalysis(
    _5896.BevelGearSetCompoundHarmonicAnalysis
):
    """StraightBevelDiffGearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysis"
    )

    class _Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysis:
        """Special nested class for casting StraightBevelDiffGearSetCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysis",
            parent: "StraightBevelDiffGearSetCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_harmonic_analysis(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysis",
        ) -> "_5896.BevelGearSetCompoundHarmonicAnalysis":
            return self._parent._cast(_5896.BevelGearSetCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysis",
        ) -> "_5884.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5884,
            )

            return self._parent._cast(
                _5884.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def conical_gear_set_compound_harmonic_analysis(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysis",
        ) -> "_5912.ConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(_5912.ConicalGearSetCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysis",
        ) -> "_5938.GearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5938,
            )

            return self._parent._cast(_5938.GearSetCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysis",
        ) -> "_5976.SpecialisedAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5976,
            )

            return self._parent._cast(_5976.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysis",
        ) -> "_5878.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5878,
            )

            return self._parent._cast(_5878.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysis",
        ) -> "_5957.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5957,
            )

            return self._parent._cast(_5957.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysis",
        ) -> "StraightBevelDiffGearSetCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysis",
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
        instance_to_wrap: "StraightBevelDiffGearSetCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2546.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2546.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

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
    ) -> "List[_5820.StraightBevelDiffGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelDiffGearSetHarmonicAnalysis]

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
    def straight_bevel_diff_gears_compound_harmonic_analysis(
        self: Self,
    ) -> "List[_5983.StraightBevelDiffGearCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.StraightBevelDiffGearCompoundHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsCompoundHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_compound_harmonic_analysis(
        self: Self,
    ) -> "List[_5984.StraightBevelDiffGearMeshCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.StraightBevelDiffGearMeshCompoundHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesCompoundHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5820.StraightBevelDiffGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelDiffGearSetHarmonicAnalysis]

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
    ) -> "StraightBevelDiffGearSetCompoundHarmonicAnalysis._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysis":
        return self._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysis(self)
