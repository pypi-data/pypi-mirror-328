"""BevelDifferentialGearSetCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5905
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "BevelDifferentialGearSetCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2523
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5700
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5898,
        _5899,
        _5893,
        _5921,
        _5947,
        _5985,
        _5887,
        _5966,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearSetCompoundHarmonicAnalysis")


class BevelDifferentialGearSetCompoundHarmonicAnalysis(
    _5905.BevelGearSetCompoundHarmonicAnalysis
):
    """BevelDifferentialGearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis"
    )

    class _Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis:
        """Special nested class for casting BevelDifferentialGearSetCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
            parent: "BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_harmonic_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "_5905.BevelGearSetCompoundHarmonicAnalysis":
            return self._parent._cast(_5905.BevelGearSetCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "_5893.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5893,
            )

            return self._parent._cast(
                _5893.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def conical_gear_set_compound_harmonic_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "_5921.ConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5921,
            )

            return self._parent._cast(_5921.ConicalGearSetCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "_5947.GearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5947,
            )

            return self._parent._cast(_5947.GearSetCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "_5985.SpecialisedAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5985,
            )

            return self._parent._cast(_5985.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "_5887.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5887,
            )

            return self._parent._cast(_5887.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "_5966.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "BevelDifferentialGearSetCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
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
        instance_to_wrap: "BevelDifferentialGearSetCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2523.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2523.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

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
    ) -> "List[_5700.BevelDifferentialGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialGearSetHarmonicAnalysis]

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
    def bevel_differential_gears_compound_harmonic_analysis(
        self: Self,
    ) -> "List[_5898.BevelDifferentialGearCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.BevelDifferentialGearCompoundHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsCompoundHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_compound_harmonic_analysis(
        self: Self,
    ) -> "List[_5899.BevelDifferentialGearMeshCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.BevelDifferentialGearMeshCompoundHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialMeshesCompoundHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5700.BevelDifferentialGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialGearSetHarmonicAnalysis]

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
    ) -> "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis":
        return self._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis(self)
