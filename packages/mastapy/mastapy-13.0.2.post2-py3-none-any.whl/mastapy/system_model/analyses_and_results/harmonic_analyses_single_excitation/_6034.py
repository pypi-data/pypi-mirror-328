"""BevelGearSetHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6022,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "BevelGearSetHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6029,
        _6119,
        _6125,
        _6128,
        _6146,
        _6050,
        _6076,
        _6116,
        _6016,
        _6097,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="BevelGearSetHarmonicAnalysisOfSingleExcitation")


class BevelGearSetHarmonicAnalysisOfSingleExcitation(
    _6022.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
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
        ) -> "_6022.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6022.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6050.ConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6050,
            )

            return self._parent._cast(
                _6050.ConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6076.GearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6076,
            )

            return self._parent._cast(_6076.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6116.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6116,
            )

            return self._parent._cast(
                _6116.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6016.AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6016,
            )

            return self._parent._cast(
                _6016.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6097.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(_6097.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6029.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6029,
            )

            return self._parent._cast(
                _6029.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6119.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6119,
            )

            return self._parent._cast(
                _6119.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6125.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6125,
            )

            return self._parent._cast(
                _6125.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6128.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6128,
            )

            return self._parent._cast(
                _6128.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6146.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6146,
            )

            return self._parent._cast(
                _6146.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation
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
    def assembly_design(self: Self) -> "_2527.BevelGearSet":
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
