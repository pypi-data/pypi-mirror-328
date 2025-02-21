"""PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6046,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
        "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2589
    from mastapy.system_model.analyses_and_results.static_loads import _6931
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6087,
        _6033,
        _6089,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation"
)


class PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation(
    _6046.CouplingHalfHarmonicAnalysisOfSingleExcitation
):
    """PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
            parent: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6046.CouplingHalfHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6046.CouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6087.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6087,
            )

            return self._parent._cast(
                _6087.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6033.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6033,
            )

            return self._parent._cast(_6033.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6089.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(_6089.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2589.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6931.PartToPartShearCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase

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
    ) -> "PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation":
        return self._Cast_PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation(
            self
        )
