"""SynchroniserHalfCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4282
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "SynchroniserHalfCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2604
    from mastapy.system_model.analyses_and_results.power_flows import _4150
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4206,
        _4244,
        _4192,
        _4246,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfCompoundPowerFlow",)


Self = TypeVar("Self", bound="SynchroniserHalfCompoundPowerFlow")


class SynchroniserHalfCompoundPowerFlow(_4282.SynchroniserPartCompoundPowerFlow):
    """SynchroniserHalfCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserHalfCompoundPowerFlow")

    class _Cast_SynchroniserHalfCompoundPowerFlow:
        """Special nested class for casting SynchroniserHalfCompoundPowerFlow to subclasses."""

        def __init__(
            self: "SynchroniserHalfCompoundPowerFlow._Cast_SynchroniserHalfCompoundPowerFlow",
            parent: "SynchroniserHalfCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_power_flow(
            self: "SynchroniserHalfCompoundPowerFlow._Cast_SynchroniserHalfCompoundPowerFlow",
        ) -> "_4282.SynchroniserPartCompoundPowerFlow":
            return self._parent._cast(_4282.SynchroniserPartCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(
            self: "SynchroniserHalfCompoundPowerFlow._Cast_SynchroniserHalfCompoundPowerFlow",
        ) -> "_4206.CouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4206,
            )

            return self._parent._cast(_4206.CouplingHalfCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "SynchroniserHalfCompoundPowerFlow._Cast_SynchroniserHalfCompoundPowerFlow",
        ) -> "_4244.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(_4244.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "SynchroniserHalfCompoundPowerFlow._Cast_SynchroniserHalfCompoundPowerFlow",
        ) -> "_4192.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "SynchroniserHalfCompoundPowerFlow._Cast_SynchroniserHalfCompoundPowerFlow",
        ) -> "_4246.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "SynchroniserHalfCompoundPowerFlow._Cast_SynchroniserHalfCompoundPowerFlow",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserHalfCompoundPowerFlow._Cast_SynchroniserHalfCompoundPowerFlow",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfCompoundPowerFlow._Cast_SynchroniserHalfCompoundPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_power_flow(
            self: "SynchroniserHalfCompoundPowerFlow._Cast_SynchroniserHalfCompoundPowerFlow",
        ) -> "SynchroniserHalfCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfCompoundPowerFlow._Cast_SynchroniserHalfCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "SynchroniserHalfCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2604.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4150.SynchroniserHalfPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SynchroniserHalfPowerFlow]

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
    def component_analysis_cases(self: Self) -> "List[_4150.SynchroniserHalfPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SynchroniserHalfPowerFlow]

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
    ) -> "SynchroniserHalfCompoundPowerFlow._Cast_SynchroniserHalfCompoundPowerFlow":
        return self._Cast_SynchroniserHalfCompoundPowerFlow(self)
