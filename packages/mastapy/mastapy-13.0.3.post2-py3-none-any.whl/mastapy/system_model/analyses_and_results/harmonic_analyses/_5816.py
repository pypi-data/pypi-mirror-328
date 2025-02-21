"""PlanetCarrierHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5807
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "PlanetCarrierHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2489
    from mastapy.system_model.analyses_and_results.static_loads import _6957
    from mastapy.system_model.analyses_and_results.system_deflections import _2811
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5726, _5809
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierHarmonicAnalysis",)


Self = TypeVar("Self", bound="PlanetCarrierHarmonicAnalysis")


class PlanetCarrierHarmonicAnalysis(_5807.MountableComponentHarmonicAnalysis):
    """PlanetCarrierHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetCarrierHarmonicAnalysis")

    class _Cast_PlanetCarrierHarmonicAnalysis:
        """Special nested class for casting PlanetCarrierHarmonicAnalysis to subclasses."""

        def __init__(
            self: "PlanetCarrierHarmonicAnalysis._Cast_PlanetCarrierHarmonicAnalysis",
            parent: "PlanetCarrierHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis(
            self: "PlanetCarrierHarmonicAnalysis._Cast_PlanetCarrierHarmonicAnalysis",
        ) -> "_5807.MountableComponentHarmonicAnalysis":
            return self._parent._cast(_5807.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "PlanetCarrierHarmonicAnalysis._Cast_PlanetCarrierHarmonicAnalysis",
        ) -> "_5726.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(_5726.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "PlanetCarrierHarmonicAnalysis._Cast_PlanetCarrierHarmonicAnalysis",
        ) -> "_5809.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(_5809.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PlanetCarrierHarmonicAnalysis._Cast_PlanetCarrierHarmonicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetCarrierHarmonicAnalysis._Cast_PlanetCarrierHarmonicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetCarrierHarmonicAnalysis._Cast_PlanetCarrierHarmonicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetCarrierHarmonicAnalysis._Cast_PlanetCarrierHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierHarmonicAnalysis._Cast_PlanetCarrierHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planet_carrier_harmonic_analysis(
            self: "PlanetCarrierHarmonicAnalysis._Cast_PlanetCarrierHarmonicAnalysis",
        ) -> "PlanetCarrierHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierHarmonicAnalysis._Cast_PlanetCarrierHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetCarrierHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2489.PlanetCarrier":
        """mastapy.system_model.part_model.PlanetCarrier

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6957.PlanetCarrierLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2811.PlanetCarrierSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PlanetCarrierSystemDeflection

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
    ) -> "PlanetCarrierHarmonicAnalysis._Cast_PlanetCarrierHarmonicAnalysis":
        return self._Cast_PlanetCarrierHarmonicAnalysis(self)
