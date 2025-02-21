"""ShaftToMountableComponentConnectionDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6280
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "ShaftToMountableComponentConnectionDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2295
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6301,
        _6321,
        _6362,
        _6312,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7540,
        _7541,
        _7538,
    )
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionDynamicAnalysis",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnectionDynamicAnalysis")


class ShaftToMountableComponentConnectionDynamicAnalysis(
    _6280.AbstractShaftToMountableComponentConnectionDynamicAnalysis
):
    """ShaftToMountableComponentConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftToMountableComponentConnectionDynamicAnalysis"
    )

    class _Cast_ShaftToMountableComponentConnectionDynamicAnalysis:
        """Special nested class for casting ShaftToMountableComponentConnectionDynamicAnalysis to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionDynamicAnalysis._Cast_ShaftToMountableComponentConnectionDynamicAnalysis",
            parent: "ShaftToMountableComponentConnectionDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_dynamic_analysis(
            self: "ShaftToMountableComponentConnectionDynamicAnalysis._Cast_ShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_6280.AbstractShaftToMountableComponentConnectionDynamicAnalysis":
            return self._parent._cast(
                _6280.AbstractShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "ShaftToMountableComponentConnectionDynamicAnalysis._Cast_ShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_6312.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "ShaftToMountableComponentConnectionDynamicAnalysis._Cast_ShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_7540.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ShaftToMountableComponentConnectionDynamicAnalysis._Cast_ShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionDynamicAnalysis._Cast_ShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionDynamicAnalysis._Cast_ShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionDynamicAnalysis._Cast_ShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionDynamicAnalysis._Cast_ShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def coaxial_connection_dynamic_analysis(
            self: "ShaftToMountableComponentConnectionDynamicAnalysis._Cast_ShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_6301.CoaxialConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301

            return self._parent._cast(_6301.CoaxialConnectionDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_dynamic_analysis(
            self: "ShaftToMountableComponentConnectionDynamicAnalysis._Cast_ShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_6321.CycloidalDiscCentralBearingConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321

            return self._parent._cast(
                _6321.CycloidalDiscCentralBearingConnectionDynamicAnalysis
            )

        @property
        def planetary_connection_dynamic_analysis(
            self: "ShaftToMountableComponentConnectionDynamicAnalysis._Cast_ShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_6362.PlanetaryConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362

            return self._parent._cast(_6362.PlanetaryConnectionDynamicAnalysis)

        @property
        def shaft_to_mountable_component_connection_dynamic_analysis(
            self: "ShaftToMountableComponentConnectionDynamicAnalysis._Cast_ShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "ShaftToMountableComponentConnectionDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionDynamicAnalysis._Cast_ShaftToMountableComponentConnectionDynamicAnalysis",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionDynamicAnalysis.TYPE",
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
    ) -> "ShaftToMountableComponentConnectionDynamicAnalysis._Cast_ShaftToMountableComponentConnectionDynamicAnalysis":
        return self._Cast_ShaftToMountableComponentConnectionDynamicAnalysis(self)
