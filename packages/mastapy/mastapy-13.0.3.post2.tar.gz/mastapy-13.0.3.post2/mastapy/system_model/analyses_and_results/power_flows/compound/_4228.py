"""CVTBeltConnectionCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4197
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "CVTBeltConnectionCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4093
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4253,
        _4223,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionCompoundPowerFlow",)


Self = TypeVar("Self", bound="CVTBeltConnectionCompoundPowerFlow")


class CVTBeltConnectionCompoundPowerFlow(_4197.BeltConnectionCompoundPowerFlow):
    """CVTBeltConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTBeltConnectionCompoundPowerFlow")

    class _Cast_CVTBeltConnectionCompoundPowerFlow:
        """Special nested class for casting CVTBeltConnectionCompoundPowerFlow to subclasses."""

        def __init__(
            self: "CVTBeltConnectionCompoundPowerFlow._Cast_CVTBeltConnectionCompoundPowerFlow",
            parent: "CVTBeltConnectionCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def belt_connection_compound_power_flow(
            self: "CVTBeltConnectionCompoundPowerFlow._Cast_CVTBeltConnectionCompoundPowerFlow",
        ) -> "_4197.BeltConnectionCompoundPowerFlow":
            return self._parent._cast(_4197.BeltConnectionCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "CVTBeltConnectionCompoundPowerFlow._Cast_CVTBeltConnectionCompoundPowerFlow",
        ) -> "_4253.InterMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4253,
            )

            return self._parent._cast(
                _4253.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "CVTBeltConnectionCompoundPowerFlow._Cast_CVTBeltConnectionCompoundPowerFlow",
        ) -> "_4223.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4223,
            )

            return self._parent._cast(_4223.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "CVTBeltConnectionCompoundPowerFlow._Cast_CVTBeltConnectionCompoundPowerFlow",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTBeltConnectionCompoundPowerFlow._Cast_CVTBeltConnectionCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionCompoundPowerFlow._Cast_CVTBeltConnectionCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_power_flow(
            self: "CVTBeltConnectionCompoundPowerFlow._Cast_CVTBeltConnectionCompoundPowerFlow",
        ) -> "CVTBeltConnectionCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionCompoundPowerFlow._Cast_CVTBeltConnectionCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "CVTBeltConnectionCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4093.CVTBeltConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CVTBeltConnectionPowerFlow]

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
    ) -> "List[_4093.CVTBeltConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CVTBeltConnectionPowerFlow]

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
    ) -> "CVTBeltConnectionCompoundPowerFlow._Cast_CVTBeltConnectionCompoundPowerFlow":
        return self._Cast_CVTBeltConnectionCompoundPowerFlow(self)
