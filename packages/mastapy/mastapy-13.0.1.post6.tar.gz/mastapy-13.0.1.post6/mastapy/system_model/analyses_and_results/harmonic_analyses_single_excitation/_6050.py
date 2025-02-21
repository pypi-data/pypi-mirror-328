"""CVTPulleyHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6098,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "CVTPulleyHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2587
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6046,
        _6087,
        _6033,
        _6089,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="CVTPulleyHarmonicAnalysisOfSingleExcitation")


class CVTPulleyHarmonicAnalysisOfSingleExcitation(
    _6098.PulleyHarmonicAnalysisOfSingleExcitation
):
    """CVTPulleyHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTPulleyHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_CVTPulleyHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CVTPulleyHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CVTPulleyHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyHarmonicAnalysisOfSingleExcitation",
            parent: "CVTPulleyHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def pulley_harmonic_analysis_of_single_excitation(
            self: "CVTPulleyHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6098.PulleyHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6098.PulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "CVTPulleyHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6046.CouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6046,
            )

            return self._parent._cast(
                _6046.CouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "CVTPulleyHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6087.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6087,
            )

            return self._parent._cast(
                _6087.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "CVTPulleyHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6033.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6033,
            )

            return self._parent._cast(_6033.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "CVTPulleyHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6089.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(_6089.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleyHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyHarmonicAnalysisOfSingleExcitation",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyHarmonicAnalysisOfSingleExcitation",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_pulley_harmonic_analysis_of_single_excitation(
            self: "CVTPulleyHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyHarmonicAnalysisOfSingleExcitation",
        ) -> "CVTPulleyHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CVTPulleyHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "CVTPulleyHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2587.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTPulleyHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CVTPulleyHarmonicAnalysisOfSingleExcitation(self)
