"""ClutchConnectionCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4205
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ClutchConnectionCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2342
    from mastapy.system_model.analyses_and_results.power_flows import _4053
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4232,
        _4202,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ClutchConnectionCompoundPowerFlow",)


Self = TypeVar("Self", bound="ClutchConnectionCompoundPowerFlow")


class ClutchConnectionCompoundPowerFlow(_4205.CouplingConnectionCompoundPowerFlow):
    """ClutchConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchConnectionCompoundPowerFlow")

    class _Cast_ClutchConnectionCompoundPowerFlow:
        """Special nested class for casting ClutchConnectionCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ClutchConnectionCompoundPowerFlow._Cast_ClutchConnectionCompoundPowerFlow",
            parent: "ClutchConnectionCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_power_flow(
            self: "ClutchConnectionCompoundPowerFlow._Cast_ClutchConnectionCompoundPowerFlow",
        ) -> "_4205.CouplingConnectionCompoundPowerFlow":
            return self._parent._cast(_4205.CouplingConnectionCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "ClutchConnectionCompoundPowerFlow._Cast_ClutchConnectionCompoundPowerFlow",
        ) -> "_4232.InterMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4232,
            )

            return self._parent._cast(
                _4232.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "ClutchConnectionCompoundPowerFlow._Cast_ClutchConnectionCompoundPowerFlow",
        ) -> "_4202.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4202,
            )

            return self._parent._cast(_4202.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "ClutchConnectionCompoundPowerFlow._Cast_ClutchConnectionCompoundPowerFlow",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchConnectionCompoundPowerFlow._Cast_ClutchConnectionCompoundPowerFlow",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchConnectionCompoundPowerFlow._Cast_ClutchConnectionCompoundPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_power_flow(
            self: "ClutchConnectionCompoundPowerFlow._Cast_ClutchConnectionCompoundPowerFlow",
        ) -> "ClutchConnectionCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ClutchConnectionCompoundPowerFlow._Cast_ClutchConnectionCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "ClutchConnectionCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2342.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2342.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

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
    ) -> "List[_4053.ClutchConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ClutchConnectionPowerFlow]

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
    ) -> "List[_4053.ClutchConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ClutchConnectionPowerFlow]

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
    ) -> "ClutchConnectionCompoundPowerFlow._Cast_ClutchConnectionCompoundPowerFlow":
        return self._Cast_ClutchConnectionCompoundPowerFlow(self)
