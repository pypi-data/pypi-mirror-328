"""KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6075,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
        "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2538
    from mastapy.system_model.analyses_and_results.static_loads import _6916
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6040,
        _6066,
        _6087,
        _6033,
        _6089,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation"
)


class KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation(
    _6075.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation
):
    """KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = (
        _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation",
            parent: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6075.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6075.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6040.ConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6040,
            )

            return self._parent._cast(
                _6040.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6066.GearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6066,
            )

            return self._parent._cast(_6066.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6087.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6087,
            )

            return self._parent._cast(
                _6087.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6033.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6033,
            )

            return self._parent._cast(_6033.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6089.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(_6089.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2538.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6916.KlingelnbergCycloPalloidHypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase

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
    ) -> "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation(
            self
        )
