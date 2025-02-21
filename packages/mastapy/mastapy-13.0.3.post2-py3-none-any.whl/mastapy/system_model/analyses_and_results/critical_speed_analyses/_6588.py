"""CoaxialConnectionCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6664
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "CoaxialConnectionCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2289
    from mastapy.system_model.analyses_and_results.static_loads import _6858
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6611,
        _6567,
        _6599,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CoaxialConnectionCriticalSpeedAnalysis")


class CoaxialConnectionCriticalSpeedAnalysis(
    _6664.ShaftToMountableComponentConnectionCriticalSpeedAnalysis
):
    """CoaxialConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CoaxialConnectionCriticalSpeedAnalysis"
    )

    class _Cast_CoaxialConnectionCriticalSpeedAnalysis:
        """Special nested class for casting CoaxialConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CoaxialConnectionCriticalSpeedAnalysis._Cast_CoaxialConnectionCriticalSpeedAnalysis",
            parent: "CoaxialConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "CoaxialConnectionCriticalSpeedAnalysis._Cast_CoaxialConnectionCriticalSpeedAnalysis",
        ) -> "_6664.ShaftToMountableComponentConnectionCriticalSpeedAnalysis":
            return self._parent._cast(
                _6664.ShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "CoaxialConnectionCriticalSpeedAnalysis._Cast_CoaxialConnectionCriticalSpeedAnalysis",
        ) -> "_6567.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6567,
            )

            return self._parent._cast(
                _6567.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "CoaxialConnectionCriticalSpeedAnalysis._Cast_CoaxialConnectionCriticalSpeedAnalysis",
        ) -> "_6599.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6599,
            )

            return self._parent._cast(_6599.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CoaxialConnectionCriticalSpeedAnalysis._Cast_CoaxialConnectionCriticalSpeedAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CoaxialConnectionCriticalSpeedAnalysis._Cast_CoaxialConnectionCriticalSpeedAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionCriticalSpeedAnalysis._Cast_CoaxialConnectionCriticalSpeedAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionCriticalSpeedAnalysis._Cast_CoaxialConnectionCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionCriticalSpeedAnalysis._Cast_CoaxialConnectionCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_critical_speed_analysis(
            self: "CoaxialConnectionCriticalSpeedAnalysis._Cast_CoaxialConnectionCriticalSpeedAnalysis",
        ) -> "_6611.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6611,
            )

            return self._parent._cast(
                _6611.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis
            )

        @property
        def coaxial_connection_critical_speed_analysis(
            self: "CoaxialConnectionCriticalSpeedAnalysis._Cast_CoaxialConnectionCriticalSpeedAnalysis",
        ) -> "CoaxialConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionCriticalSpeedAnalysis._Cast_CoaxialConnectionCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "CoaxialConnectionCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2289.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6858.CoaxialConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase

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
    ) -> "CoaxialConnectionCriticalSpeedAnalysis._Cast_CoaxialConnectionCriticalSpeedAnalysis":
        return self._Cast_CoaxialConnectionCriticalSpeedAnalysis(self)
