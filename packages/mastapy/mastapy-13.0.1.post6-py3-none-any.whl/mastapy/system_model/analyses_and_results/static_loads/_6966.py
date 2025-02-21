"""StraightBevelPlanetGearLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6960
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelPlanetGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2549
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6828,
        _6814,
        _6845,
        _6891,
        _6925,
        _6838,
        _6929,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearLoadCase",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearLoadCase")


class StraightBevelPlanetGearLoadCase(_6960.StraightBevelDiffGearLoadCase):
    """StraightBevelPlanetGearLoadCase

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelPlanetGearLoadCase")

    class _Cast_StraightBevelPlanetGearLoadCase:
        """Special nested class for casting StraightBevelPlanetGearLoadCase to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
            parent: "StraightBevelPlanetGearLoadCase",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_load_case(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ) -> "_6960.StraightBevelDiffGearLoadCase":
            return self._parent._cast(_6960.StraightBevelDiffGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ) -> "_6828.BevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6828

            return self._parent._cast(_6828.BevelGearLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ) -> "_6814.AGMAGleasonConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6814

            return self._parent._cast(_6814.AGMAGleasonConicalGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ) -> "_6845.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6845

            return self._parent._cast(_6845.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ) -> "_6891.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6891

            return self._parent._cast(_6891.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ) -> "_6925.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(_6925.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ) -> "_6838.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6838

            return self._parent._cast(_6838.ComponentLoadCase)

        @property
        def part_load_case(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ) -> "_6929.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(_6929.PartLoadCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ) -> "StraightBevelPlanetGearLoadCase":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelPlanetGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2549.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase":
        return self._Cast_StraightBevelPlanetGearLoadCase(self)
