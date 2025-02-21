"""SynchroniserHalfPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4172
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "SynchroniserHalfPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4074,
        _4091,
        _4133,
        _4078,
        _4135,
    )
    from mastapy.system_model.part_model.couplings import _2625
    from mastapy.system_model.analyses_and_results.static_loads import _6989
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfPowerFlow",)


Self = TypeVar("Self", bound="SynchroniserHalfPowerFlow")


class SynchroniserHalfPowerFlow(_4172.SynchroniserPartPowerFlow):
    """SynchroniserHalfPowerFlow

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserHalfPowerFlow")

    class _Cast_SynchroniserHalfPowerFlow:
        """Special nested class for casting SynchroniserHalfPowerFlow to subclasses."""

        def __init__(
            self: "SynchroniserHalfPowerFlow._Cast_SynchroniserHalfPowerFlow",
            parent: "SynchroniserHalfPowerFlow",
        ):
            self._parent = parent

        @property
        def synchroniser_part_power_flow(
            self: "SynchroniserHalfPowerFlow._Cast_SynchroniserHalfPowerFlow",
        ) -> "_4172.SynchroniserPartPowerFlow":
            return self._parent._cast(_4172.SynchroniserPartPowerFlow)

        @property
        def coupling_half_power_flow(
            self: "SynchroniserHalfPowerFlow._Cast_SynchroniserHalfPowerFlow",
        ) -> "_4091.CouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4091

            return self._parent._cast(_4091.CouplingHalfPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "SynchroniserHalfPowerFlow._Cast_SynchroniserHalfPowerFlow",
        ) -> "_4133.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "SynchroniserHalfPowerFlow._Cast_SynchroniserHalfPowerFlow",
        ) -> "_4078.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "SynchroniserHalfPowerFlow._Cast_SynchroniserHalfPowerFlow",
        ) -> "_4135.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserHalfPowerFlow._Cast_SynchroniserHalfPowerFlow",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserHalfPowerFlow._Cast_SynchroniserHalfPowerFlow",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserHalfPowerFlow._Cast_SynchroniserHalfPowerFlow",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserHalfPowerFlow._Cast_SynchroniserHalfPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfPowerFlow._Cast_SynchroniserHalfPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def synchroniser_half_power_flow(
            self: "SynchroniserHalfPowerFlow._Cast_SynchroniserHalfPowerFlow",
        ) -> "SynchroniserHalfPowerFlow":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfPowerFlow._Cast_SynchroniserHalfPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserHalfPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clutch_connection(self: Self) -> "_4074.ClutchConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ClutchConnectionPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClutchConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_design(self: Self) -> "_2625.SynchroniserHalf":
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
    def component_load_case(self: Self) -> "_6989.SynchroniserHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserHalfPowerFlow._Cast_SynchroniserHalfPowerFlow":
        return self._Cast_SynchroniserHalfPowerFlow(self)
