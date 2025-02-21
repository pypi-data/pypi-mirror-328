"""ConnectorCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4244
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ConnectorCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4068
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4175,
        _4245,
        _4263,
        _4192,
        _4246,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorCompoundPowerFlow",)


Self = TypeVar("Self", bound="ConnectorCompoundPowerFlow")


class ConnectorCompoundPowerFlow(_4244.MountableComponentCompoundPowerFlow):
    """ConnectorCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorCompoundPowerFlow")

    class _Cast_ConnectorCompoundPowerFlow:
        """Special nested class for casting ConnectorCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
            parent: "ConnectorCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_power_flow(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
        ) -> "_4244.MountableComponentCompoundPowerFlow":
            return self._parent._cast(_4244.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
        ) -> "_4192.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
        ) -> "_4246.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bearing_compound_power_flow(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
        ) -> "_4175.BearingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4175,
            )

            return self._parent._cast(_4175.BearingCompoundPowerFlow)

        @property
        def oil_seal_compound_power_flow(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
        ) -> "_4245.OilSealCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4245,
            )

            return self._parent._cast(_4245.OilSealCompoundPowerFlow)

        @property
        def shaft_hub_connection_compound_power_flow(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
        ) -> "_4263.ShaftHubConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4263,
            )

            return self._parent._cast(_4263.ShaftHubConnectionCompoundPowerFlow)

        @property
        def connector_compound_power_flow(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
        ) -> "ConnectorCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4068.ConnectorPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConnectorPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4068.ConnectorPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConnectorPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow":
        return self._Cast_ConnectorCompoundPowerFlow(self)
