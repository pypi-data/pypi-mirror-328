"""AbstractShaftToMountableComponentConnectionPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4088
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "AbstractShaftToMountableComponentConnectionPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2285
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4077,
        _4097,
        _4098,
        _4139,
        _4155,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionPowerFlow",)


Self = TypeVar("Self", bound="AbstractShaftToMountableComponentConnectionPowerFlow")


class AbstractShaftToMountableComponentConnectionPowerFlow(_4088.ConnectionPowerFlow):
    """AbstractShaftToMountableComponentConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftToMountableComponentConnectionPowerFlow"
    )

    class _Cast_AbstractShaftToMountableComponentConnectionPowerFlow:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionPowerFlow to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionPowerFlow._Cast_AbstractShaftToMountableComponentConnectionPowerFlow",
            parent: "AbstractShaftToMountableComponentConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def connection_power_flow(
            self: "AbstractShaftToMountableComponentConnectionPowerFlow._Cast_AbstractShaftToMountableComponentConnectionPowerFlow",
        ) -> "_4088.ConnectionPowerFlow":
            return self._parent._cast(_4088.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionPowerFlow._Cast_AbstractShaftToMountableComponentConnectionPowerFlow",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionPowerFlow._Cast_AbstractShaftToMountableComponentConnectionPowerFlow",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionPowerFlow._Cast_AbstractShaftToMountableComponentConnectionPowerFlow",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionPowerFlow._Cast_AbstractShaftToMountableComponentConnectionPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionPowerFlow._Cast_AbstractShaftToMountableComponentConnectionPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_power_flow(
            self: "AbstractShaftToMountableComponentConnectionPowerFlow._Cast_AbstractShaftToMountableComponentConnectionPowerFlow",
        ) -> "_4077.CoaxialConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4077

            return self._parent._cast(_4077.CoaxialConnectionPowerFlow)

        @property
        def cycloidal_disc_central_bearing_connection_power_flow(
            self: "AbstractShaftToMountableComponentConnectionPowerFlow._Cast_AbstractShaftToMountableComponentConnectionPowerFlow",
        ) -> "_4097.CycloidalDiscCentralBearingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4097

            return self._parent._cast(
                _4097.CycloidalDiscCentralBearingConnectionPowerFlow
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_power_flow(
            self: "AbstractShaftToMountableComponentConnectionPowerFlow._Cast_AbstractShaftToMountableComponentConnectionPowerFlow",
        ) -> "_4098.CycloidalDiscPlanetaryBearingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4098

            return self._parent._cast(
                _4098.CycloidalDiscPlanetaryBearingConnectionPowerFlow
            )

        @property
        def planetary_connection_power_flow(
            self: "AbstractShaftToMountableComponentConnectionPowerFlow._Cast_AbstractShaftToMountableComponentConnectionPowerFlow",
        ) -> "_4139.PlanetaryConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4139

            return self._parent._cast(_4139.PlanetaryConnectionPowerFlow)

        @property
        def shaft_to_mountable_component_connection_power_flow(
            self: "AbstractShaftToMountableComponentConnectionPowerFlow._Cast_AbstractShaftToMountableComponentConnectionPowerFlow",
        ) -> "_4155.ShaftToMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4155

            return self._parent._cast(
                _4155.ShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def abstract_shaft_to_mountable_component_connection_power_flow(
            self: "AbstractShaftToMountableComponentConnectionPowerFlow._Cast_AbstractShaftToMountableComponentConnectionPowerFlow",
        ) -> "AbstractShaftToMountableComponentConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionPowerFlow._Cast_AbstractShaftToMountableComponentConnectionPowerFlow",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2285.AbstractShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

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
    ) -> "AbstractShaftToMountableComponentConnectionPowerFlow._Cast_AbstractShaftToMountableComponentConnectionPowerFlow":
        return self._Cast_AbstractShaftToMountableComponentConnectionPowerFlow(self)
