"""WormGearCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6205,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "WormGearCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2558
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6141,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6224,
        _6172,
        _6226,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("WormGearCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="WormGearCompoundHarmonicAnalysisOfSingleExcitation")


class WormGearCompoundHarmonicAnalysisOfSingleExcitation(
    _6205.GearCompoundHarmonicAnalysisOfSingleExcitation
):
    """WormGearCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_WormGearCompoundHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_WormGearCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting WormGearCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "WormGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_WormGearCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "WormGearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def gear_compound_harmonic_analysis_of_single_excitation(
            self: "WormGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_WormGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6205.GearCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6205.GearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "WormGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_WormGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6224.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6224,
            )

            return self._parent._cast(
                _6224.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "WormGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_WormGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6172.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6172,
            )

            return self._parent._cast(
                _6172.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "WormGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_WormGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6226.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6226,
            )

            return self._parent._cast(
                _6226.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "WormGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_WormGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "WormGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_WormGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_WormGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def worm_gear_compound_harmonic_analysis_of_single_excitation(
            self: "WormGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_WormGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "WormGearCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "WormGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_WormGearCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "WormGearCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2558.WormGear":
        """mastapy.system_model.part_model.gears.WormGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6141.WormGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.WormGearHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6141.WormGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.WormGearHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "WormGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_WormGearCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_WormGearCompoundHarmonicAnalysisOfSingleExcitation(self)
