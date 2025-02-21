"""RingPinsToDiscConnectionPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4100
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "RingPinsToDiscConnectionPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2341
    from mastapy.system_model.analyses_and_results.static_loads import _6945
    from mastapy.system_model.analyses_and_results.power_flows import _4067
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionPowerFlow",)


Self = TypeVar("Self", bound="RingPinsToDiscConnectionPowerFlow")


class RingPinsToDiscConnectionPowerFlow(
    _4100.InterMountableComponentConnectionPowerFlow
):
    """RingPinsToDiscConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsToDiscConnectionPowerFlow")

    class _Cast_RingPinsToDiscConnectionPowerFlow:
        """Special nested class for casting RingPinsToDiscConnectionPowerFlow to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow",
            parent: "RingPinsToDiscConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_power_flow(
            self: "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow",
        ) -> "_4100.InterMountableComponentConnectionPowerFlow":
            return self._parent._cast(_4100.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow",
        ) -> "_4067.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_power_flow(
            self: "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow",
        ) -> "RingPinsToDiscConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow",
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
        self: Self, instance_to_wrap: "RingPinsToDiscConnectionPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2341.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6945.RingPinsToDiscConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsToDiscConnectionLoadCase

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
    ) -> "RingPinsToDiscConnectionPowerFlow._Cast_RingPinsToDiscConnectionPowerFlow":
        return self._Cast_RingPinsToDiscConnectionPowerFlow(self)
