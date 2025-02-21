"""RingPinsHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5807
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "RingPinsHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2590
    from mastapy.system_model.analyses_and_results.static_loads import _6965
    from mastapy.system_model.analyses_and_results.system_deflections import _2815
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5726, _5809
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsHarmonicAnalysis",)


Self = TypeVar("Self", bound="RingPinsHarmonicAnalysis")


class RingPinsHarmonicAnalysis(_5807.MountableComponentHarmonicAnalysis):
    """RingPinsHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsHarmonicAnalysis")

    class _Cast_RingPinsHarmonicAnalysis:
        """Special nested class for casting RingPinsHarmonicAnalysis to subclasses."""

        def __init__(
            self: "RingPinsHarmonicAnalysis._Cast_RingPinsHarmonicAnalysis",
            parent: "RingPinsHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis(
            self: "RingPinsHarmonicAnalysis._Cast_RingPinsHarmonicAnalysis",
        ) -> "_5807.MountableComponentHarmonicAnalysis":
            return self._parent._cast(_5807.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "RingPinsHarmonicAnalysis._Cast_RingPinsHarmonicAnalysis",
        ) -> "_5726.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(_5726.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "RingPinsHarmonicAnalysis._Cast_RingPinsHarmonicAnalysis",
        ) -> "_5809.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(_5809.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RingPinsHarmonicAnalysis._Cast_RingPinsHarmonicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RingPinsHarmonicAnalysis._Cast_RingPinsHarmonicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RingPinsHarmonicAnalysis._Cast_RingPinsHarmonicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsHarmonicAnalysis._Cast_RingPinsHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsHarmonicAnalysis._Cast_RingPinsHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def ring_pins_harmonic_analysis(
            self: "RingPinsHarmonicAnalysis._Cast_RingPinsHarmonicAnalysis",
        ) -> "RingPinsHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "RingPinsHarmonicAnalysis._Cast_RingPinsHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinsHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2590.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6965.RingPinsLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2815.RingPinsSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.RingPinsSystemDeflection

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
    ) -> "RingPinsHarmonicAnalysis._Cast_RingPinsHarmonicAnalysis":
        return self._Cast_RingPinsHarmonicAnalysis(self)
