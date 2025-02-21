"""CycloidalAssemblyHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6129,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "CycloidalAssemblyHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2588
    from mastapy.system_model.analyses_and_results.static_loads import _6879
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6029,
        _6110,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalAssemblyHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="CycloidalAssemblyHarmonicAnalysisOfSingleExcitation")


class CycloidalAssemblyHarmonicAnalysisOfSingleExcitation(
    _6129.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
):
    """CycloidalAssemblyHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalAssemblyHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_CycloidalAssemblyHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CycloidalAssemblyHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CycloidalAssemblyHarmonicAnalysisOfSingleExcitation._Cast_CycloidalAssemblyHarmonicAnalysisOfSingleExcitation",
            parent: "CycloidalAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "CycloidalAssemblyHarmonicAnalysisOfSingleExcitation._Cast_CycloidalAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6129.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6129.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "CycloidalAssemblyHarmonicAnalysisOfSingleExcitation._Cast_CycloidalAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6029.AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6029,
            )

            return self._parent._cast(
                _6029.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "CycloidalAssemblyHarmonicAnalysisOfSingleExcitation._Cast_CycloidalAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6110.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6110,
            )

            return self._parent._cast(_6110.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalAssemblyHarmonicAnalysisOfSingleExcitation._Cast_CycloidalAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalAssemblyHarmonicAnalysisOfSingleExcitation._Cast_CycloidalAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalAssemblyHarmonicAnalysisOfSingleExcitation._Cast_CycloidalAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalAssemblyHarmonicAnalysisOfSingleExcitation._Cast_CycloidalAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalAssemblyHarmonicAnalysisOfSingleExcitation._Cast_CycloidalAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_assembly_harmonic_analysis_of_single_excitation(
            self: "CycloidalAssemblyHarmonicAnalysisOfSingleExcitation._Cast_CycloidalAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "CycloidalAssemblyHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CycloidalAssemblyHarmonicAnalysisOfSingleExcitation._Cast_CycloidalAssemblyHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CycloidalAssemblyHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2588.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6879.CycloidalAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalAssemblyHarmonicAnalysisOfSingleExcitation._Cast_CycloidalAssemblyHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CycloidalAssemblyHarmonicAnalysisOfSingleExcitation(self)
