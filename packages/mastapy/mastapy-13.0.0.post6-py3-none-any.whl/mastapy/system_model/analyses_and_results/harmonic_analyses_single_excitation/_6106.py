"""ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6010,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
        "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2295
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6031,
        _6051,
        _6092,
        _6042,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7540, _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self",
    bound="ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
)


class ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation(
    _6010.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
):
    """ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = (
        _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
            parent: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6010.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6010.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6042.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6042,
            )

            return self._parent._cast(
                _6042.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7540.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def coaxial_connection_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6031.CoaxialConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6031,
            )

            return self._parent._cast(
                _6031.CoaxialConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6051.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6051,
            )

            return self._parent._cast(
                _6051.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_connection_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6092.PlanetaryConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6092,
            )

            return self._parent._cast(
                _6092.PlanetaryConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2295.ShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation(
            self
        )
