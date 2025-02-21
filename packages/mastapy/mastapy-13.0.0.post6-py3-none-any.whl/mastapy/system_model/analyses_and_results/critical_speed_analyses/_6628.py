"""PlanetaryConnectionCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6642
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "PlanetaryConnectionCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2287
    from mastapy.system_model.analyses_and_results.static_loads import _6932
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6545,
        _6577,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7540, _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="PlanetaryConnectionCriticalSpeedAnalysis")


class PlanetaryConnectionCriticalSpeedAnalysis(
    _6642.ShaftToMountableComponentConnectionCriticalSpeedAnalysis
):
    """PlanetaryConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryConnectionCriticalSpeedAnalysis"
    )

    class _Cast_PlanetaryConnectionCriticalSpeedAnalysis:
        """Special nested class for casting PlanetaryConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
            parent: "PlanetaryConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
        ) -> "_6642.ShaftToMountableComponentConnectionCriticalSpeedAnalysis":
            return self._parent._cast(
                _6642.ShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
        ) -> "_6545.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6545,
            )

            return self._parent._cast(
                _6545.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
        ) -> "_6577.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6577,
            )

            return self._parent._cast(_6577.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
        ) -> "_7540.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_connection_critical_speed_analysis(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
        ) -> "PlanetaryConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryConnectionCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2287.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6932.PlanetaryConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase

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
    ) -> "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis":
        return self._Cast_PlanetaryConnectionCriticalSpeedAnalysis(self)
