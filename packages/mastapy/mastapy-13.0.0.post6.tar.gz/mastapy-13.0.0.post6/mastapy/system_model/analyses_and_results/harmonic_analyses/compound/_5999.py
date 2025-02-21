"""UnbalancedMassCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _6000
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "UnbalancedMassCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2477
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5835
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5955,
        _5903,
        _5957,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="UnbalancedMassCompoundHarmonicAnalysis")


class UnbalancedMassCompoundHarmonicAnalysis(
    _6000.VirtualComponentCompoundHarmonicAnalysis
):
    """UnbalancedMassCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_UnbalancedMassCompoundHarmonicAnalysis"
    )

    class _Cast_UnbalancedMassCompoundHarmonicAnalysis:
        """Special nested class for casting UnbalancedMassCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "UnbalancedMassCompoundHarmonicAnalysis._Cast_UnbalancedMassCompoundHarmonicAnalysis",
            parent: "UnbalancedMassCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_harmonic_analysis(
            self: "UnbalancedMassCompoundHarmonicAnalysis._Cast_UnbalancedMassCompoundHarmonicAnalysis",
        ) -> "_6000.VirtualComponentCompoundHarmonicAnalysis":
            return self._parent._cast(_6000.VirtualComponentCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "UnbalancedMassCompoundHarmonicAnalysis._Cast_UnbalancedMassCompoundHarmonicAnalysis",
        ) -> "_5955.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5955,
            )

            return self._parent._cast(_5955.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "UnbalancedMassCompoundHarmonicAnalysis._Cast_UnbalancedMassCompoundHarmonicAnalysis",
        ) -> "_5903.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5903,
            )

            return self._parent._cast(_5903.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "UnbalancedMassCompoundHarmonicAnalysis._Cast_UnbalancedMassCompoundHarmonicAnalysis",
        ) -> "_5957.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5957,
            )

            return self._parent._cast(_5957.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "UnbalancedMassCompoundHarmonicAnalysis._Cast_UnbalancedMassCompoundHarmonicAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "UnbalancedMassCompoundHarmonicAnalysis._Cast_UnbalancedMassCompoundHarmonicAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassCompoundHarmonicAnalysis._Cast_UnbalancedMassCompoundHarmonicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def unbalanced_mass_compound_harmonic_analysis(
            self: "UnbalancedMassCompoundHarmonicAnalysis._Cast_UnbalancedMassCompoundHarmonicAnalysis",
        ) -> "UnbalancedMassCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassCompoundHarmonicAnalysis._Cast_UnbalancedMassCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "UnbalancedMassCompoundHarmonicAnalysis.TYPE"
    ):
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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5835.UnbalancedMassHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.UnbalancedMassHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5835.UnbalancedMassHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.UnbalancedMassHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "UnbalancedMassCompoundHarmonicAnalysis._Cast_UnbalancedMassCompoundHarmonicAnalysis":
        return self._Cast_UnbalancedMassCompoundHarmonicAnalysis(self)
