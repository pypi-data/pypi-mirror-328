"""RingPinsCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4244
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "RingPinsCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2570
    from mastapy.system_model.analyses_and_results.power_flows import _4126
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4192,
        _4246,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsCompoundPowerFlow",)


Self = TypeVar("Self", bound="RingPinsCompoundPowerFlow")


class RingPinsCompoundPowerFlow(_4244.MountableComponentCompoundPowerFlow):
    """RingPinsCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _RING_PINS_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsCompoundPowerFlow")

    class _Cast_RingPinsCompoundPowerFlow:
        """Special nested class for casting RingPinsCompoundPowerFlow to subclasses."""

        def __init__(
            self: "RingPinsCompoundPowerFlow._Cast_RingPinsCompoundPowerFlow",
            parent: "RingPinsCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_power_flow(
            self: "RingPinsCompoundPowerFlow._Cast_RingPinsCompoundPowerFlow",
        ) -> "_4244.MountableComponentCompoundPowerFlow":
            return self._parent._cast(_4244.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "RingPinsCompoundPowerFlow._Cast_RingPinsCompoundPowerFlow",
        ) -> "_4192.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "RingPinsCompoundPowerFlow._Cast_RingPinsCompoundPowerFlow",
        ) -> "_4246.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "RingPinsCompoundPowerFlow._Cast_RingPinsCompoundPowerFlow",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RingPinsCompoundPowerFlow._Cast_RingPinsCompoundPowerFlow",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsCompoundPowerFlow._Cast_RingPinsCompoundPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def ring_pins_compound_power_flow(
            self: "RingPinsCompoundPowerFlow._Cast_RingPinsCompoundPowerFlow",
        ) -> "RingPinsCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "RingPinsCompoundPowerFlow._Cast_RingPinsCompoundPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinsCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2570.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4126.RingPinsPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.RingPinsPowerFlow]

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
    def component_analysis_cases(self: Self) -> "List[_4126.RingPinsPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.RingPinsPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "RingPinsCompoundPowerFlow._Cast_RingPinsCompoundPowerFlow":
        return self._Cast_RingPinsCompoundPowerFlow(self)
