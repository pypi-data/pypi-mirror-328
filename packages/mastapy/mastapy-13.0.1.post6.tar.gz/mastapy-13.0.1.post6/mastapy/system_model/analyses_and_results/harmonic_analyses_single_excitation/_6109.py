"""SpiralBevelGearHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6024,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "SpiralBevelGearHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.static_loads import _6954
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6012,
        _6040,
        _6066,
        _6087,
        _6033,
        _6089,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="SpiralBevelGearHarmonicAnalysisOfSingleExcitation")


class SpiralBevelGearHarmonicAnalysisOfSingleExcitation(
    _6024.BevelGearHarmonicAnalysisOfSingleExcitation
):
    """SpiralBevelGearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_SpiralBevelGearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting SpiralBevelGearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "SpiralBevelGearHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearHarmonicAnalysisOfSingleExcitation",
            parent: "SpiralBevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6024.BevelGearHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6024.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6012.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6012,
            )

            return self._parent._cast(
                _6012.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6040.ConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6040,
            )

            return self._parent._cast(
                _6040.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6066.GearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6066,
            )

            return self._parent._cast(_6066.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6087.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6087,
            )

            return self._parent._cast(
                _6087.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6033.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6033,
            )

            return self._parent._cast(_6033.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6089.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(_6089.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "SpiralBevelGearHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpiralBevelGearHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpiralBevelGearHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "SpiralBevelGearHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "SpiralBevelGearHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2543.SpiralBevelGear":
        """mastapy.system_model.part_model.gears.SpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6954.SpiralBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearHarmonicAnalysisOfSingleExcitation":
        return self._Cast_SpiralBevelGearHarmonicAnalysisOfSingleExcitation(self)
