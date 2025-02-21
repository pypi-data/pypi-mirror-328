"""CycloidalDiscCentralBearingConnectionStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3808
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CycloidalDiscCentralBearingConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2355
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3883,
        _3787,
        _3819,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscCentralBearingConnectionStabilityAnalysis")


class CycloidalDiscCentralBearingConnectionStabilityAnalysis(
    _3808.CoaxialConnectionStabilityAnalysis
):
    """CycloidalDiscCentralBearingConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
            parent: "CycloidalDiscCentralBearingConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coaxial_connection_stability_analysis(
            self: "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
        ) -> "_3808.CoaxialConnectionStabilityAnalysis":
            return self._parent._cast(_3808.CoaxialConnectionStabilityAnalysis)

        @property
        def shaft_to_mountable_component_connection_stability_analysis(
            self: "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
        ) -> "_3883.ShaftToMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3883,
            )

            return self._parent._cast(
                _3883.ShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_stability_analysis(
            self: "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
        ) -> "_3787.AbstractShaftToMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3787,
            )

            return self._parent._cast(
                _3787.AbstractShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
        ) -> "_3819.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_stability_analysis(
            self: "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
        ) -> "CycloidalDiscCentralBearingConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2355.CycloidalDiscCentralBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection

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
    ) -> "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis":
        return self._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis(self)
