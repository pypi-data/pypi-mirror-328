"""ConnectorHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5807
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ConnectorHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2467
    from mastapy.system_model.analyses_and_results.system_deflections import _2749
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5708,
        _5808,
        _5828,
        _5726,
        _5809,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConnectorHarmonicAnalysis")


class ConnectorHarmonicAnalysis(_5807.MountableComponentHarmonicAnalysis):
    """ConnectorHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorHarmonicAnalysis")

    class _Cast_ConnectorHarmonicAnalysis:
        """Special nested class for casting ConnectorHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
            parent: "ConnectorHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_5807.MountableComponentHarmonicAnalysis":
            return self._parent._cast(_5807.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_5726.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(_5726.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_5809.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(_5809.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bearing_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_5708.BearingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5708,
            )

            return self._parent._cast(_5708.BearingHarmonicAnalysis)

        @property
        def oil_seal_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_5808.OilSealHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5808,
            )

            return self._parent._cast(_5808.OilSealHarmonicAnalysis)

        @property
        def shaft_hub_connection_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_5828.ShaftHubConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5828,
            )

            return self._parent._cast(_5828.ShaftHubConnectionHarmonicAnalysis)

        @property
        def connector_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "ConnectorHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2467.Connector":
        """mastapy.system_model.part_model.Connector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2749.ConnectorSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConnectorSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis":
        return self._Cast_ConnectorHarmonicAnalysis(self)
