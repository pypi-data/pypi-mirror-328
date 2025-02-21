"""AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6032,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2436
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6008,
        _6052,
        _6063,
        _6104,
        _6088,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation")


class AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation(
    _6032.ComponentHarmonicAnalysisOfSingleExcitation
):
    """AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
            parent: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ) -> "_6032.ComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6032.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ) -> "_6088.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6088,
            )

            return self._parent._cast(_6088.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ) -> "_6008.AbstractShaftHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6008,
            )

            return self._parent._cast(
                _6008.AbstractShaftHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ) -> "_6052.CycloidalDiscHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6052,
            )

            return self._parent._cast(
                _6052.CycloidalDiscHarmonicAnalysisOfSingleExcitation
            )

        @property
        def fe_part_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ) -> "_6063.FEPartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6063,
            )

            return self._parent._cast(_6063.FEPartHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ) -> "_6104.ShaftHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6104,
            )

            return self._parent._cast(_6104.ShaftHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_shaft_or_housing_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ) -> "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2436.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

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
    ) -> "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation":
        return self._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation(self)
