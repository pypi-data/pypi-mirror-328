"""ConicalGearSetHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6068,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "ConicalGearSetHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2524
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6014,
        _6021,
        _6026,
        _6073,
        _6077,
        _6080,
        _6083,
        _6111,
        _6117,
        _6120,
        _6138,
        _6108,
        _6008,
        _6089,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="ConicalGearSetHarmonicAnalysisOfSingleExcitation")


class ConicalGearSetHarmonicAnalysisOfSingleExcitation(
    _6068.GearSetHarmonicAnalysisOfSingleExcitation
):
    """ConicalGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ConicalGearSetHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
            parent: "ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6068.GearSetHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6068.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6108.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6108,
            )

            return self._parent._cast(
                _6108.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6008.AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6008,
            )

            return self._parent._cast(
                _6008.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6089.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(_6089.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6014.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6014,
            )

            return self._parent._cast(
                _6014.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6021.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6021,
            )

            return self._parent._cast(
                _6021.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6026.BevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6026,
            )

            return self._parent._cast(
                _6026.BevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6073.HypoidGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6073,
            )

            return self._parent._cast(
                _6073.HypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6077.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6077,
            )

            return self._parent._cast(
                _6077.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6080.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6080,
            )

            return self._parent._cast(
                _6080.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6083.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6083,
            )

            return self._parent._cast(
                _6083.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6111.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6111,
            )

            return self._parent._cast(
                _6111.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6117.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6117,
            )

            return self._parent._cast(
                _6117.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6120.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6120,
            )

            return self._parent._cast(
                _6120.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6138.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6138,
            )

            return self._parent._cast(
                _6138.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "ConicalGearSetHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ConicalGearSetHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2524.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

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
    ) -> "ConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ConicalGearSetHarmonicAnalysisOfSingleExcitation(self)
