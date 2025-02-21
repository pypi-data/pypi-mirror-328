"""MassDiscHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6131,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "MassDiscHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.static_loads import _6921
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6086,
        _6032,
        _6088,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="MassDiscHarmonicAnalysisOfSingleExcitation")


class MassDiscHarmonicAnalysisOfSingleExcitation(
    _6131.VirtualComponentHarmonicAnalysisOfSingleExcitation
):
    """MassDiscHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MassDiscHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_MassDiscHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting MassDiscHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "MassDiscHarmonicAnalysisOfSingleExcitation._Cast_MassDiscHarmonicAnalysisOfSingleExcitation",
            parent: "MassDiscHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(
            self: "MassDiscHarmonicAnalysisOfSingleExcitation._Cast_MassDiscHarmonicAnalysisOfSingleExcitation",
        ) -> "_6131.VirtualComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6131.VirtualComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "MassDiscHarmonicAnalysisOfSingleExcitation._Cast_MassDiscHarmonicAnalysisOfSingleExcitation",
        ) -> "_6086.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(
                _6086.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "MassDiscHarmonicAnalysisOfSingleExcitation._Cast_MassDiscHarmonicAnalysisOfSingleExcitation",
        ) -> "_6032.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6032,
            )

            return self._parent._cast(_6032.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "MassDiscHarmonicAnalysisOfSingleExcitation._Cast_MassDiscHarmonicAnalysisOfSingleExcitation",
        ) -> "_6088.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6088,
            )

            return self._parent._cast(_6088.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "MassDiscHarmonicAnalysisOfSingleExcitation._Cast_MassDiscHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MassDiscHarmonicAnalysisOfSingleExcitation._Cast_MassDiscHarmonicAnalysisOfSingleExcitation",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MassDiscHarmonicAnalysisOfSingleExcitation._Cast_MassDiscHarmonicAnalysisOfSingleExcitation",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MassDiscHarmonicAnalysisOfSingleExcitation._Cast_MassDiscHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscHarmonicAnalysisOfSingleExcitation._Cast_MassDiscHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def mass_disc_harmonic_analysis_of_single_excitation(
            self: "MassDiscHarmonicAnalysisOfSingleExcitation._Cast_MassDiscHarmonicAnalysisOfSingleExcitation",
        ) -> "MassDiscHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "MassDiscHarmonicAnalysisOfSingleExcitation._Cast_MassDiscHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "MassDiscHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2462.MassDisc":
        """mastapy.system_model.part_model.MassDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6921.MassDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[MassDiscHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.MassDiscHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "MassDiscHarmonicAnalysisOfSingleExcitation._Cast_MassDiscHarmonicAnalysisOfSingleExcitation":
        return self._Cast_MassDiscHarmonicAnalysisOfSingleExcitation(self)
