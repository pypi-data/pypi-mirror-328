"""CycloidalDiscCentralBearingConnectionStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3787
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CycloidalDiscCentralBearingConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2335
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3862,
        _3766,
        _3798,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7540, _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscCentralBearingConnectionStabilityAnalysis")


class CycloidalDiscCentralBearingConnectionStabilityAnalysis(
    _3787.CoaxialConnectionStabilityAnalysis
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
        ) -> "_3787.CoaxialConnectionStabilityAnalysis":
            return self._parent._cast(_3787.CoaxialConnectionStabilityAnalysis)

        @property
        def shaft_to_mountable_component_connection_stability_analysis(
            self: "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
        ) -> "_3862.ShaftToMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3862,
            )

            return self._parent._cast(
                _3862.ShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_stability_analysis(
            self: "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
        ) -> "_3766.AbstractShaftToMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3766,
            )

            return self._parent._cast(
                _3766.AbstractShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
        ) -> "_3798.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3798,
            )

            return self._parent._cast(_3798.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
        ) -> "_7540.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionStabilityAnalysis._Cast_CycloidalDiscCentralBearingConnectionStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

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
    def connection_design(self: Self) -> "_2335.CycloidalDiscCentralBearingConnection":
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
