"""RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6204,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2292
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6102,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6174,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation"
)


class RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation(
    _6204.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
):
    """RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6204.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6204.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6174.ConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6174,
            )

            return self._parent._cast(
                _6174.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_analysis(
            self: "RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def rolling_ring_connection_compound_harmonic_analysis_of_single_excitation(
            self: "RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2292.RollingRingConnection":
        """mastapy.system_model.connections_and_sockets.RollingRingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2292.RollingRingConnection":
        """mastapy.system_model.connections_and_sockets.RollingRingConnection

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
    ) -> "List[_6102.RollingRingConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.RollingRingConnectionHarmonicAnalysisOfSingleExcitation]

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
    def planetaries(
        self: Self,
    ) -> "List[RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6102.RollingRingConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.RollingRingConnectionHarmonicAnalysisOfSingleExcitation]

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
    ) -> "RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation":
        return (
            self._Cast_RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation(
                self
            )
        )
