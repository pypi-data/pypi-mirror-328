"""AbstractShaftHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5680
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "AbstractShaftHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2435
    from mastapy.system_model.analyses_and_results.system_deflections import _2687
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5724,
        _5805,
        _5704,
        _5787,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftHarmonicAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftHarmonicAnalysis")


class AbstractShaftHarmonicAnalysis(_5680.AbstractShaftOrHousingHarmonicAnalysis):
    """AbstractShaftHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftHarmonicAnalysis")

    class _Cast_AbstractShaftHarmonicAnalysis:
        """Special nested class for casting AbstractShaftHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
            parent: "AbstractShaftHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_harmonic_analysis(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ) -> "_5680.AbstractShaftOrHousingHarmonicAnalysis":
            return self._parent._cast(_5680.AbstractShaftOrHousingHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ) -> "_5704.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5704,
            )

            return self._parent._cast(_5704.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ) -> "_5787.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5787,
            )

            return self._parent._cast(_5787.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ) -> "_5724.CycloidalDiscHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5724,
            )

            return self._parent._cast(_5724.CycloidalDiscHarmonicAnalysis)

        @property
        def shaft_harmonic_analysis(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ) -> "_5805.ShaftHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5805,
            )

            return self._parent._cast(_5805.ShaftHarmonicAnalysis)

        @property
        def abstract_shaft_harmonic_analysis(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ) -> "AbstractShaftHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftHarmonicAnalysis.TYPE"):
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
    def system_deflection_results(self: Self) -> "_2687.AbstractShaftSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis":
        return self._Cast_AbstractShaftHarmonicAnalysis(self)
