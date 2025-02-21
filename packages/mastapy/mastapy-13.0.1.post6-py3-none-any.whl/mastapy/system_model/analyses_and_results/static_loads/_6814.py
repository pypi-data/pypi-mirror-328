"""AGMAGleasonConicalGearLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6845
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AGMAGleasonConicalGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2513
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6823,
        _6826,
        _6827,
        _6828,
        _6906,
        _6954,
        _6960,
        _6963,
        _6966,
        _6967,
        _6986,
        _6891,
        _6925,
        _6838,
        _6929,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearLoadCase",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearLoadCase")


class AGMAGleasonConicalGearLoadCase(_6845.ConicalGearLoadCase):
    """AGMAGleasonConicalGearLoadCase

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearLoadCase")

    class _Cast_AGMAGleasonConicalGearLoadCase:
        """Special nested class for casting AGMAGleasonConicalGearLoadCase to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
            parent: "AGMAGleasonConicalGearLoadCase",
        ):
            self._parent = parent

        @property
        def conical_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6845.ConicalGearLoadCase":
            return self._parent._cast(_6845.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6891.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6891

            return self._parent._cast(_6891.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6925.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(_6925.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6838.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6838

            return self._parent._cast(_6838.ComponentLoadCase)

        @property
        def part_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6929.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(_6929.PartLoadCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6823.BevelDifferentialGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6823

            return self._parent._cast(_6823.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6826.BevelDifferentialPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6826

            return self._parent._cast(_6826.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6827.BevelDifferentialSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6827

            return self._parent._cast(_6827.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6828.BevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6828

            return self._parent._cast(_6828.BevelGearLoadCase)

        @property
        def hypoid_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6906.HypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6906

            return self._parent._cast(_6906.HypoidGearLoadCase)

        @property
        def spiral_bevel_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6954.SpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6954

            return self._parent._cast(_6954.SpiralBevelGearLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6960.StraightBevelDiffGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6960

            return self._parent._cast(_6960.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6963.StraightBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6963

            return self._parent._cast(_6963.StraightBevelGearLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6966.StraightBevelPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6966

            return self._parent._cast(_6966.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6967.StraightBevelSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6967

            return self._parent._cast(_6967.StraightBevelSunGearLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6986.ZerolBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6986

            return self._parent._cast(_6986.ZerolBevelGearLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "AGMAGleasonConicalGearLoadCase":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2513.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

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
    ) -> "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase":
        return self._Cast_AGMAGleasonConicalGearLoadCase(self)
