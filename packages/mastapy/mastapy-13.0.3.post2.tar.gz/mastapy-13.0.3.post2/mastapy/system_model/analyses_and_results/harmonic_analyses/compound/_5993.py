"""RollingRingConnectionCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5965
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "RollingRingConnectionCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2312
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5824
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5935,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingConnectionCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="RollingRingConnectionCompoundHarmonicAnalysis")


class RollingRingConnectionCompoundHarmonicAnalysis(
    _5965.InterMountableComponentConnectionCompoundHarmonicAnalysis
):
    """RollingRingConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingConnectionCompoundHarmonicAnalysis"
    )

    class _Cast_RollingRingConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting RollingRingConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "RollingRingConnectionCompoundHarmonicAnalysis._Cast_RollingRingConnectionCompoundHarmonicAnalysis",
            parent: "RollingRingConnectionCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "RollingRingConnectionCompoundHarmonicAnalysis._Cast_RollingRingConnectionCompoundHarmonicAnalysis",
        ) -> "_5965.InterMountableComponentConnectionCompoundHarmonicAnalysis":
            return self._parent._cast(
                _5965.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "RollingRingConnectionCompoundHarmonicAnalysis._Cast_RollingRingConnectionCompoundHarmonicAnalysis",
        ) -> "_5935.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5935,
            )

            return self._parent._cast(_5935.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "RollingRingConnectionCompoundHarmonicAnalysis._Cast_RollingRingConnectionCompoundHarmonicAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingConnectionCompoundHarmonicAnalysis._Cast_RollingRingConnectionCompoundHarmonicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingConnectionCompoundHarmonicAnalysis._Cast_RollingRingConnectionCompoundHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def rolling_ring_connection_compound_harmonic_analysis(
            self: "RollingRingConnectionCompoundHarmonicAnalysis._Cast_RollingRingConnectionCompoundHarmonicAnalysis",
        ) -> "RollingRingConnectionCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingConnectionCompoundHarmonicAnalysis._Cast_RollingRingConnectionCompoundHarmonicAnalysis",
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
        instance_to_wrap: "RollingRingConnectionCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2312.RollingRingConnection":
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
    def connection_design(self: Self) -> "_2312.RollingRingConnection":
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
    ) -> "List[_5824.RollingRingConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.RollingRingConnectionHarmonicAnalysis]

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
    ) -> "List[RollingRingConnectionCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.RollingRingConnectionCompoundHarmonicAnalysis]

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
    ) -> "List[_5824.RollingRingConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.RollingRingConnectionHarmonicAnalysis]

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
    ) -> "RollingRingConnectionCompoundHarmonicAnalysis._Cast_RollingRingConnectionCompoundHarmonicAnalysis":
        return self._Cast_RollingRingConnectionCompoundHarmonicAnalysis(self)
