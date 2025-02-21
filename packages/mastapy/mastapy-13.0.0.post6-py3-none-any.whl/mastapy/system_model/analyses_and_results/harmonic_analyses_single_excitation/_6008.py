"""AbstractShaftHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6009,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "AbstractShaftHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2435
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6052,
        _6104,
        _6032,
        _6088,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="AbstractShaftHarmonicAnalysisOfSingleExcitation")


class AbstractShaftHarmonicAnalysisOfSingleExcitation(
    _6009.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation
):
    """AbstractShaftHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting AbstractShaftHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
            parent: "AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_6009.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6009.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_6032.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6032,
            )

            return self._parent._cast(_6032.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_6088.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6088,
            )

            return self._parent._cast(_6088.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_6052.CycloidalDiscHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6052,
            )

            return self._parent._cast(
                _6052.CycloidalDiscHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_6104.ShaftHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6104,
            )

            return self._parent._cast(_6104.ShaftHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_shaft_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "AbstractShaftHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "AbstractShaftHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2435.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

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
    ) -> "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation":
        return self._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation(self)
