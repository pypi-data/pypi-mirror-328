"""BevelGearSetHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6014,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "BevelGearSetHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2520
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6021,
        _6111,
        _6117,
        _6120,
        _6138,
        _6042,
        _6068,
        _6108,
        _6008,
        _6089,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="BevelGearSetHarmonicAnalysisOfSingleExcitation")


class BevelGearSetHarmonicAnalysisOfSingleExcitation(
    _6014.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
):
    """BevelGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting BevelGearSetHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
            parent: "BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6014.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6014.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6042.ConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6042,
            )

            return self._parent._cast(
                _6042.ConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6068.GearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6068,
            )

            return self._parent._cast(_6068.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6108.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6108,
            )

            return self._parent._cast(
                _6108.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6008.AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6008,
            )

            return self._parent._cast(
                _6008.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6089.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(_6089.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6021.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6021,
            )

            return self._parent._cast(
                _6021.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6111.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6111,
            )

            return self._parent._cast(
                _6111.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6117.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6117,
            )

            return self._parent._cast(
                _6117.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6120.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6120,
            )

            return self._parent._cast(
                _6120.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6138.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6138,
            )

            return self._parent._cast(
                _6138.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "BevelGearSetHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "BevelGearSetHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2520.BevelGearSet":
        """mastapy.system_model.part_model.gears.BevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation":
        return self._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation(self)
