"""CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5903
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
        "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5724
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5976,
        _5882,
        _5914,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis"
)


class CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis(
    _5903.CoaxialConnectionCompoundHarmonicAnalysis
):
    """CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
            parent: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_harmonic_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "_5903.CoaxialConnectionCompoundHarmonicAnalysis":
            return self._parent._cast(_5903.CoaxialConnectionCompoundHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "_5976.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5976,
            )

            return self._parent._cast(
                _5976.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> (
            "_5882.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5882,
            )

            return self._parent._cast(
                _5882.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "_5914.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5914,
            )

            return self._parent._cast(_5914.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5724.CycloidalDiscCentralBearingConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscCentralBearingConnectionHarmonicAnalysis]

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
    ) -> "List[_5724.CycloidalDiscCentralBearingConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscCentralBearingConnectionHarmonicAnalysis]

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
    ) -> "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis":
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis(
            self
        )
