"""BeltConnectionHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6095,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "BeltConnectionHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2288
    from mastapy.system_model.analyses_and_results.static_loads import _6842
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6069,
        _6064,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="BeltConnectionHarmonicAnalysisOfSingleExcitation")


class BeltConnectionHarmonicAnalysisOfSingleExcitation(
    _6095.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
):
    """BeltConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltConnectionHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_BeltConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting BeltConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "BeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionHarmonicAnalysisOfSingleExcitation",
            parent: "BeltConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "BeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6095.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"
        ):
            return self._parent._cast(
                _6095.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "BeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6064.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6064,
            )

            return self._parent._cast(
                _6064.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "BeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_harmonic_analysis_of_single_excitation(
            self: "BeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6069.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6069,
            )

            return self._parent._cast(
                _6069.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_connection_harmonic_analysis_of_single_excitation(
            self: "BeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "BeltConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "BeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "BeltConnectionHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2288.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6842.BeltConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionHarmonicAnalysisOfSingleExcitation":
        return self._Cast_BeltConnectionHarmonicAnalysisOfSingleExcitation(self)
