"""UnbalancedMassHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "UnbalancedMassHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2477
    from mastapy.system_model.analyses_and_results.static_loads import _6980
    from mastapy.system_model.analyses_and_results.system_deflections import _2834
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5785,
        _5704,
        _5787,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassHarmonicAnalysis",)


Self = TypeVar("Self", bound="UnbalancedMassHarmonicAnalysis")


class UnbalancedMassHarmonicAnalysis(_5836.VirtualComponentHarmonicAnalysis):
    """UnbalancedMassHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_UnbalancedMassHarmonicAnalysis")

    class _Cast_UnbalancedMassHarmonicAnalysis:
        """Special nested class for casting UnbalancedMassHarmonicAnalysis to subclasses."""

        def __init__(
            self: "UnbalancedMassHarmonicAnalysis._Cast_UnbalancedMassHarmonicAnalysis",
            parent: "UnbalancedMassHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_harmonic_analysis(
            self: "UnbalancedMassHarmonicAnalysis._Cast_UnbalancedMassHarmonicAnalysis",
        ) -> "_5836.VirtualComponentHarmonicAnalysis":
            return self._parent._cast(_5836.VirtualComponentHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "UnbalancedMassHarmonicAnalysis._Cast_UnbalancedMassHarmonicAnalysis",
        ) -> "_5785.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(_5785.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "UnbalancedMassHarmonicAnalysis._Cast_UnbalancedMassHarmonicAnalysis",
        ) -> "_5704.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5704,
            )

            return self._parent._cast(_5704.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "UnbalancedMassHarmonicAnalysis._Cast_UnbalancedMassHarmonicAnalysis",
        ) -> "_5787.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5787,
            )

            return self._parent._cast(_5787.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "UnbalancedMassHarmonicAnalysis._Cast_UnbalancedMassHarmonicAnalysis",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "UnbalancedMassHarmonicAnalysis._Cast_UnbalancedMassHarmonicAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "UnbalancedMassHarmonicAnalysis._Cast_UnbalancedMassHarmonicAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "UnbalancedMassHarmonicAnalysis._Cast_UnbalancedMassHarmonicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassHarmonicAnalysis._Cast_UnbalancedMassHarmonicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def unbalanced_mass_harmonic_analysis(
            self: "UnbalancedMassHarmonicAnalysis._Cast_UnbalancedMassHarmonicAnalysis",
        ) -> "UnbalancedMassHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassHarmonicAnalysis._Cast_UnbalancedMassHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "UnbalancedMassHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2477.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6980.UnbalancedMassLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2834.UnbalancedMassSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.UnbalancedMassSystemDeflection

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
    ) -> "UnbalancedMassHarmonicAnalysis._Cast_UnbalancedMassHarmonicAnalysis":
        return self._Cast_UnbalancedMassHarmonicAnalysis(self)
