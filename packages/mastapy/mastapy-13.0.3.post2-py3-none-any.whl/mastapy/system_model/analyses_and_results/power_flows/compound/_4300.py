"""StraightBevelSunGearCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4293
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "StraightBevelSunGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4170
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4204,
        _4192,
        _4220,
        _4246,
        _4265,
        _4213,
        _4267,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="StraightBevelSunGearCompoundPowerFlow")


class StraightBevelSunGearCompoundPowerFlow(
    _4293.StraightBevelDiffGearCompoundPowerFlow
):
    """StraightBevelSunGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelSunGearCompoundPowerFlow"
    )

    class _Cast_StraightBevelSunGearCompoundPowerFlow:
        """Special nested class for casting StraightBevelSunGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "StraightBevelSunGearCompoundPowerFlow._Cast_StraightBevelSunGearCompoundPowerFlow",
            parent: "StraightBevelSunGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "StraightBevelSunGearCompoundPowerFlow._Cast_StraightBevelSunGearCompoundPowerFlow",
        ) -> "_4293.StraightBevelDiffGearCompoundPowerFlow":
            return self._parent._cast(_4293.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "StraightBevelSunGearCompoundPowerFlow._Cast_StraightBevelSunGearCompoundPowerFlow",
        ) -> "_4204.BevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4204,
            )

            return self._parent._cast(_4204.BevelGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "StraightBevelSunGearCompoundPowerFlow._Cast_StraightBevelSunGearCompoundPowerFlow",
        ) -> "_4192.AGMAGleasonConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "StraightBevelSunGearCompoundPowerFlow._Cast_StraightBevelSunGearCompoundPowerFlow",
        ) -> "_4220.ConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4220,
            )

            return self._parent._cast(_4220.ConicalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "StraightBevelSunGearCompoundPowerFlow._Cast_StraightBevelSunGearCompoundPowerFlow",
        ) -> "_4246.GearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "StraightBevelSunGearCompoundPowerFlow._Cast_StraightBevelSunGearCompoundPowerFlow",
        ) -> "_4265.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "StraightBevelSunGearCompoundPowerFlow._Cast_StraightBevelSunGearCompoundPowerFlow",
        ) -> "_4213.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4213,
            )

            return self._parent._cast(_4213.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "StraightBevelSunGearCompoundPowerFlow._Cast_StraightBevelSunGearCompoundPowerFlow",
        ) -> "_4267.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "StraightBevelSunGearCompoundPowerFlow._Cast_StraightBevelSunGearCompoundPowerFlow",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelSunGearCompoundPowerFlow._Cast_StraightBevelSunGearCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearCompoundPowerFlow._Cast_StraightBevelSunGearCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "StraightBevelSunGearCompoundPowerFlow._Cast_StraightBevelSunGearCompoundPowerFlow",
        ) -> "StraightBevelSunGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearCompoundPowerFlow._Cast_StraightBevelSunGearCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "StraightBevelSunGearCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4170.StraightBevelSunGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelSunGearPowerFlow]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4170.StraightBevelSunGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelSunGearPowerFlow]

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
    ) -> "StraightBevelSunGearCompoundPowerFlow._Cast_StraightBevelSunGearCompoundPowerFlow":
        return self._Cast_StraightBevelSunGearCompoundPowerFlow(self)
