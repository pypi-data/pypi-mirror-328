"""CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6280
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2338
    from mastapy.system_model.analyses_and_results.static_loads import _6861
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7540,
        _7541,
        _7538,
    )
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis")


class CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis(
    _6280.AbstractShaftToMountableComponentConnectionDynamicAnalysis
):
    """CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis",
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis",
            parent: "CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_dynamic_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis",
        ) -> "_6280.AbstractShaftToMountableComponentConnectionDynamicAnalysis":
            return self._parent._cast(
                _6280.AbstractShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis",
        ) -> "_6312.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis",
        ) -> "_7540.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_dynamic_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis",
        ) -> "CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2338.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6861.CycloidalDiscPlanetaryBearingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase

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
    ) -> "CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis":
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis(self)
