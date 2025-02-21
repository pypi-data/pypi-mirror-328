"""MeasurementComponentHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6140,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "MeasurementComponentHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2470
    from mastapy.system_model.analyses_and_results.static_loads import _6931
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6095,
        _6041,
        _6097,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="MeasurementComponentHarmonicAnalysisOfSingleExcitation")


class MeasurementComponentHarmonicAnalysisOfSingleExcitation(
    _6140.VirtualComponentHarmonicAnalysisOfSingleExcitation
):
    """MeasurementComponentHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MeasurementComponentHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_MeasurementComponentHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting MeasurementComponentHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "MeasurementComponentHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentHarmonicAnalysisOfSingleExcitation",
            parent: "MeasurementComponentHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(
            self: "MeasurementComponentHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6140.VirtualComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6140.VirtualComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "MeasurementComponentHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6095.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6095,
            )

            return self._parent._cast(
                _6095.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "MeasurementComponentHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6041.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6041,
            )

            return self._parent._cast(_6041.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "MeasurementComponentHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6097.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(_6097.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "MeasurementComponentHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MeasurementComponentHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MeasurementComponentHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MeasurementComponentHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def measurement_component_harmonic_analysis_of_single_excitation(
            self: "MeasurementComponentHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "MeasurementComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "MeasurementComponentHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2470.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6931.MeasurementComponentLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase

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
    ) -> "MeasurementComponentHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentHarmonicAnalysisOfSingleExcitation":
        return self._Cast_MeasurementComponentHarmonicAnalysisOfSingleExcitation(self)
