"""RingPinsToDiscConnectionCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5943
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "RingPinsToDiscConnectionCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2341
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5800
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5913,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="RingPinsToDiscConnectionCompoundHarmonicAnalysis")


class RingPinsToDiscConnectionCompoundHarmonicAnalysis(
    _5943.InterMountableComponentConnectionCompoundHarmonicAnalysis
):
    """RingPinsToDiscConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysis"
    )

    class _Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting RingPinsToDiscConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionCompoundHarmonicAnalysis._Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysis",
            parent: "RingPinsToDiscConnectionCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "RingPinsToDiscConnectionCompoundHarmonicAnalysis._Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysis",
        ) -> "_5943.InterMountableComponentConnectionCompoundHarmonicAnalysis":
            return self._parent._cast(
                _5943.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "RingPinsToDiscConnectionCompoundHarmonicAnalysis._Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysis",
        ) -> "_5913.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5913,
            )

            return self._parent._cast(_5913.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "RingPinsToDiscConnectionCompoundHarmonicAnalysis._Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysis",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RingPinsToDiscConnectionCompoundHarmonicAnalysis._Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionCompoundHarmonicAnalysis._Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_harmonic_analysis(
            self: "RingPinsToDiscConnectionCompoundHarmonicAnalysis._Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysis",
        ) -> "RingPinsToDiscConnectionCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionCompoundHarmonicAnalysis._Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysis",
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
        instance_to_wrap: "RingPinsToDiscConnectionCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2341.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2341.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5800.RingPinsToDiscConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.RingPinsToDiscConnectionHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5800.RingPinsToDiscConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.RingPinsToDiscConnectionHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RingPinsToDiscConnectionCompoundHarmonicAnalysis._Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysis":
        return self._Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysis(self)
