"""TorqueConverterConnectionCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5917
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "TorqueConverterConnectionCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2352
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5831
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5944,
        _5914,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterConnectionCompoundHarmonicAnalysis")


class TorqueConverterConnectionCompoundHarmonicAnalysis(
    _5917.CouplingConnectionCompoundHarmonicAnalysis
):
    """TorqueConverterConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterConnectionCompoundHarmonicAnalysis"
    )

    class _Cast_TorqueConverterConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting TorqueConverterConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionCompoundHarmonicAnalysis._Cast_TorqueConverterConnectionCompoundHarmonicAnalysis",
            parent: "TorqueConverterConnectionCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_harmonic_analysis(
            self: "TorqueConverterConnectionCompoundHarmonicAnalysis._Cast_TorqueConverterConnectionCompoundHarmonicAnalysis",
        ) -> "_5917.CouplingConnectionCompoundHarmonicAnalysis":
            return self._parent._cast(_5917.CouplingConnectionCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "TorqueConverterConnectionCompoundHarmonicAnalysis._Cast_TorqueConverterConnectionCompoundHarmonicAnalysis",
        ) -> "_5944.InterMountableComponentConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5944,
            )

            return self._parent._cast(
                _5944.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "TorqueConverterConnectionCompoundHarmonicAnalysis._Cast_TorqueConverterConnectionCompoundHarmonicAnalysis",
        ) -> "_5914.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5914,
            )

            return self._parent._cast(_5914.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "TorqueConverterConnectionCompoundHarmonicAnalysis._Cast_TorqueConverterConnectionCompoundHarmonicAnalysis",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterConnectionCompoundHarmonicAnalysis._Cast_TorqueConverterConnectionCompoundHarmonicAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionCompoundHarmonicAnalysis._Cast_TorqueConverterConnectionCompoundHarmonicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_connection_compound_harmonic_analysis(
            self: "TorqueConverterConnectionCompoundHarmonicAnalysis._Cast_TorqueConverterConnectionCompoundHarmonicAnalysis",
        ) -> "TorqueConverterConnectionCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionCompoundHarmonicAnalysis._Cast_TorqueConverterConnectionCompoundHarmonicAnalysis",
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
        instance_to_wrap: "TorqueConverterConnectionCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2352.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2352.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

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
    ) -> "List[_5831.TorqueConverterConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.TorqueConverterConnectionHarmonicAnalysis]

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
    ) -> "List[_5831.TorqueConverterConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.TorqueConverterConnectionHarmonicAnalysis]

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
    ) -> "TorqueConverterConnectionCompoundHarmonicAnalysis._Cast_TorqueConverterConnectionCompoundHarmonicAnalysis":
        return self._Cast_TorqueConverterConnectionCompoundHarmonicAnalysis(self)
