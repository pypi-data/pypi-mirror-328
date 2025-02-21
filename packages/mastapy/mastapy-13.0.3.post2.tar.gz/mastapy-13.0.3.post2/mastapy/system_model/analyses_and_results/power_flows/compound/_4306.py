"""TorqueConverterConnectionCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4226
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "TorqueConverterConnectionCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2372
    from mastapy.system_model.analyses_and_results.power_flows import _4176
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4253,
        _4223,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionCompoundPowerFlow",)


Self = TypeVar("Self", bound="TorqueConverterConnectionCompoundPowerFlow")


class TorqueConverterConnectionCompoundPowerFlow(
    _4226.CouplingConnectionCompoundPowerFlow
):
    """TorqueConverterConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterConnectionCompoundPowerFlow"
    )

    class _Cast_TorqueConverterConnectionCompoundPowerFlow:
        """Special nested class for casting TorqueConverterConnectionCompoundPowerFlow to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionCompoundPowerFlow._Cast_TorqueConverterConnectionCompoundPowerFlow",
            parent: "TorqueConverterConnectionCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_power_flow(
            self: "TorqueConverterConnectionCompoundPowerFlow._Cast_TorqueConverterConnectionCompoundPowerFlow",
        ) -> "_4226.CouplingConnectionCompoundPowerFlow":
            return self._parent._cast(_4226.CouplingConnectionCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "TorqueConverterConnectionCompoundPowerFlow._Cast_TorqueConverterConnectionCompoundPowerFlow",
        ) -> "_4253.InterMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4253,
            )

            return self._parent._cast(
                _4253.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "TorqueConverterConnectionCompoundPowerFlow._Cast_TorqueConverterConnectionCompoundPowerFlow",
        ) -> "_4223.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4223,
            )

            return self._parent._cast(_4223.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "TorqueConverterConnectionCompoundPowerFlow._Cast_TorqueConverterConnectionCompoundPowerFlow",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterConnectionCompoundPowerFlow._Cast_TorqueConverterConnectionCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionCompoundPowerFlow._Cast_TorqueConverterConnectionCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def torque_converter_connection_compound_power_flow(
            self: "TorqueConverterConnectionCompoundPowerFlow._Cast_TorqueConverterConnectionCompoundPowerFlow",
        ) -> "TorqueConverterConnectionCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionCompoundPowerFlow._Cast_TorqueConverterConnectionCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "TorqueConverterConnectionCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2372.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2372.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

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
    ) -> "List[_4176.TorqueConverterConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.TorqueConverterConnectionPowerFlow]

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
    ) -> "List[_4176.TorqueConverterConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.TorqueConverterConnectionPowerFlow]

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
    ) -> "TorqueConverterConnectionCompoundPowerFlow._Cast_TorqueConverterConnectionCompoundPowerFlow":
        return self._Cast_TorqueConverterConnectionCompoundPowerFlow(self)
