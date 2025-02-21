"""ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5378
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
        "ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2295
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5402,
        _5422,
        _5470,
        _5413,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis"
)


class ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis(
    _5378.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
):
    """ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
    )

    class _Cast_ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
            parent: "ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> (
            "_5378.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis"
        ):
            return self._parent._cast(
                _5378.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "_5413.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5413

            return self._parent._cast(_5413.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "_7541.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def coaxial_connection_multibody_dynamics_analysis(
            self: "ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "_5402.CoaxialConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5402

            return self._parent._cast(_5402.CoaxialConnectionMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_multibody_dynamics_analysis(
            self: "ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "_5422.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5422

            return self._parent._cast(
                _5422.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def planetary_connection_multibody_dynamics_analysis(
            self: "ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "_5470.PlanetaryConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5470

            return self._parent._cast(
                _5470.PlanetaryConnectionMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2295.ShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection

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
    ) -> "ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
        return self._Cast_ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis(
            self
        )
