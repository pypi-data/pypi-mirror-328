"""SynchroniserHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5831
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "SynchroniserHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2623
    from mastapy.system_model.analyses_and_results.static_loads import _6990
    from mastapy.system_model.analyses_and_results.system_deflections import _2845
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5699, _5809
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHarmonicAnalysis",)


Self = TypeVar("Self", bound="SynchroniserHarmonicAnalysis")


class SynchroniserHarmonicAnalysis(_5831.SpecialisedAssemblyHarmonicAnalysis):
    """SynchroniserHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserHarmonicAnalysis")

    class _Cast_SynchroniserHarmonicAnalysis:
        """Special nested class for casting SynchroniserHarmonicAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserHarmonicAnalysis._Cast_SynchroniserHarmonicAnalysis",
            parent: "SynchroniserHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis(
            self: "SynchroniserHarmonicAnalysis._Cast_SynchroniserHarmonicAnalysis",
        ) -> "_5831.SpecialisedAssemblyHarmonicAnalysis":
            return self._parent._cast(_5831.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "SynchroniserHarmonicAnalysis._Cast_SynchroniserHarmonicAnalysis",
        ) -> "_5699.AbstractAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5699,
            )

            return self._parent._cast(_5699.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "SynchroniserHarmonicAnalysis._Cast_SynchroniserHarmonicAnalysis",
        ) -> "_5809.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(_5809.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserHarmonicAnalysis._Cast_SynchroniserHarmonicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserHarmonicAnalysis._Cast_SynchroniserHarmonicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserHarmonicAnalysis._Cast_SynchroniserHarmonicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserHarmonicAnalysis._Cast_SynchroniserHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHarmonicAnalysis._Cast_SynchroniserHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def synchroniser_harmonic_analysis(
            self: "SynchroniserHarmonicAnalysis._Cast_SynchroniserHarmonicAnalysis",
        ) -> "SynchroniserHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserHarmonicAnalysis._Cast_SynchroniserHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2623.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6990.SynchroniserLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2845.SynchroniserSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSystemDeflection

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
    ) -> "SynchroniserHarmonicAnalysis._Cast_SynchroniserHarmonicAnalysis":
        return self._Cast_SynchroniserHarmonicAnalysis(self)
