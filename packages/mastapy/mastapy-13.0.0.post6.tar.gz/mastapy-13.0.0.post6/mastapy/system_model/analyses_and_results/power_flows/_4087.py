"""FaceGearPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4093
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "FaceGearPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2528
    from mastapy.gears.rating.face import _448
    from mastapy.system_model.analyses_and_results.static_loads import _6884
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4111,
        _4057,
        _4113,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearPowerFlow",)


Self = TypeVar("Self", bound="FaceGearPowerFlow")


class FaceGearPowerFlow(_4093.GearPowerFlow):
    """FaceGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearPowerFlow")

    class _Cast_FaceGearPowerFlow:
        """Special nested class for casting FaceGearPowerFlow to subclasses."""

        def __init__(
            self: "FaceGearPowerFlow._Cast_FaceGearPowerFlow",
            parent: "FaceGearPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_power_flow(
            self: "FaceGearPowerFlow._Cast_FaceGearPowerFlow",
        ) -> "_4093.GearPowerFlow":
            return self._parent._cast(_4093.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "FaceGearPowerFlow._Cast_FaceGearPowerFlow",
        ) -> "_4111.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "FaceGearPowerFlow._Cast_FaceGearPowerFlow",
        ) -> "_4057.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "FaceGearPowerFlow._Cast_FaceGearPowerFlow",
        ) -> "_4113.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearPowerFlow._Cast_FaceGearPowerFlow",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearPowerFlow._Cast_FaceGearPowerFlow",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearPowerFlow._Cast_FaceGearPowerFlow",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearPowerFlow._Cast_FaceGearPowerFlow",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearPowerFlow._Cast_FaceGearPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def face_gear_power_flow(
            self: "FaceGearPowerFlow._Cast_FaceGearPowerFlow",
        ) -> "FaceGearPowerFlow":
            return self._parent

        def __getattr__(self: "FaceGearPowerFlow._Cast_FaceGearPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2528.FaceGear":
        """mastapy.system_model.part_model.gears.FaceGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_448.FaceGearRating":
        """mastapy.gears.rating.face.FaceGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6884.FaceGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "FaceGearPowerFlow._Cast_FaceGearPowerFlow":
        return self._Cast_FaceGearPowerFlow(self)
