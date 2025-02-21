"""PlanetaryConnectionCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4263
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "PlanetaryConnectionCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2287
    from mastapy.system_model.analyses_and_results.power_flows import _4117
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4169,
        _4201,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionCompoundPowerFlow",)


Self = TypeVar("Self", bound="PlanetaryConnectionCompoundPowerFlow")


class PlanetaryConnectionCompoundPowerFlow(
    _4263.ShaftToMountableComponentConnectionCompoundPowerFlow
):
    """PlanetaryConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryConnectionCompoundPowerFlow")

    class _Cast_PlanetaryConnectionCompoundPowerFlow:
        """Special nested class for casting PlanetaryConnectionCompoundPowerFlow to subclasses."""

        def __init__(
            self: "PlanetaryConnectionCompoundPowerFlow._Cast_PlanetaryConnectionCompoundPowerFlow",
            parent: "PlanetaryConnectionCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_power_flow(
            self: "PlanetaryConnectionCompoundPowerFlow._Cast_PlanetaryConnectionCompoundPowerFlow",
        ) -> "_4263.ShaftToMountableComponentConnectionCompoundPowerFlow":
            return self._parent._cast(
                _4263.ShaftToMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_power_flow(
            self: "PlanetaryConnectionCompoundPowerFlow._Cast_PlanetaryConnectionCompoundPowerFlow",
        ) -> "_4169.AbstractShaftToMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4169,
            )

            return self._parent._cast(
                _4169.AbstractShaftToMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "PlanetaryConnectionCompoundPowerFlow._Cast_PlanetaryConnectionCompoundPowerFlow",
        ) -> "_4201.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "PlanetaryConnectionCompoundPowerFlow._Cast_PlanetaryConnectionCompoundPowerFlow",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryConnectionCompoundPowerFlow._Cast_PlanetaryConnectionCompoundPowerFlow",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionCompoundPowerFlow._Cast_PlanetaryConnectionCompoundPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_connection_compound_power_flow(
            self: "PlanetaryConnectionCompoundPowerFlow._Cast_PlanetaryConnectionCompoundPowerFlow",
        ) -> "PlanetaryConnectionCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionCompoundPowerFlow._Cast_PlanetaryConnectionCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "PlanetaryConnectionCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2287.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4117.PlanetaryConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PlanetaryConnectionPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4117.PlanetaryConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PlanetaryConnectionPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryConnectionCompoundPowerFlow._Cast_PlanetaryConnectionCompoundPowerFlow":
        return self._Cast_PlanetaryConnectionCompoundPowerFlow(self)
