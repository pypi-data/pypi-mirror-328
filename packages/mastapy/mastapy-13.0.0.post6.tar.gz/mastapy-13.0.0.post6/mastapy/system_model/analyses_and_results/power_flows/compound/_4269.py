"""SpringDamperConnectionCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4204
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "SpringDamperConnectionCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2350
    from mastapy.system_model.analyses_and_results.power_flows import _4138
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4231,
        _4201,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionCompoundPowerFlow",)


Self = TypeVar("Self", bound="SpringDamperConnectionCompoundPowerFlow")


class SpringDamperConnectionCompoundPowerFlow(
    _4204.CouplingConnectionCompoundPowerFlow
):
    """SpringDamperConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperConnectionCompoundPowerFlow"
    )

    class _Cast_SpringDamperConnectionCompoundPowerFlow:
        """Special nested class for casting SpringDamperConnectionCompoundPowerFlow to subclasses."""

        def __init__(
            self: "SpringDamperConnectionCompoundPowerFlow._Cast_SpringDamperConnectionCompoundPowerFlow",
            parent: "SpringDamperConnectionCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_power_flow(
            self: "SpringDamperConnectionCompoundPowerFlow._Cast_SpringDamperConnectionCompoundPowerFlow",
        ) -> "_4204.CouplingConnectionCompoundPowerFlow":
            return self._parent._cast(_4204.CouplingConnectionCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "SpringDamperConnectionCompoundPowerFlow._Cast_SpringDamperConnectionCompoundPowerFlow",
        ) -> "_4231.InterMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4231,
            )

            return self._parent._cast(
                _4231.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "SpringDamperConnectionCompoundPowerFlow._Cast_SpringDamperConnectionCompoundPowerFlow",
        ) -> "_4201.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "SpringDamperConnectionCompoundPowerFlow._Cast_SpringDamperConnectionCompoundPowerFlow",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperConnectionCompoundPowerFlow._Cast_SpringDamperConnectionCompoundPowerFlow",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionCompoundPowerFlow._Cast_SpringDamperConnectionCompoundPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spring_damper_connection_compound_power_flow(
            self: "SpringDamperConnectionCompoundPowerFlow._Cast_SpringDamperConnectionCompoundPowerFlow",
        ) -> "SpringDamperConnectionCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionCompoundPowerFlow._Cast_SpringDamperConnectionCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "SpringDamperConnectionCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2350.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2350.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

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
    ) -> "List[_4138.SpringDamperConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpringDamperConnectionPowerFlow]

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
    ) -> "List[_4138.SpringDamperConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpringDamperConnectionPowerFlow]

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
    ) -> "SpringDamperConnectionCompoundPowerFlow._Cast_SpringDamperConnectionCompoundPowerFlow":
        return self._Cast_SpringDamperConnectionCompoundPowerFlow(self)
