"""BevelGearLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BevelGearLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6844,
        _6847,
        _6848,
        _6975,
        _6981,
        _6984,
        _6987,
        _6988,
        _7007,
        _6866,
        _6912,
        _6946,
        _6859,
        _6950,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearLoadCase",)


Self = TypeVar("Self", bound="BevelGearLoadCase")


class BevelGearLoadCase(_6835.AGMAGleasonConicalGearLoadCase):
    """BevelGearLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearLoadCase")

    class _Cast_BevelGearLoadCase:
        """Special nested class for casting BevelGearLoadCase to subclasses."""

        def __init__(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
            parent: "BevelGearLoadCase",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6835.AGMAGleasonConicalGearLoadCase":
            return self._parent._cast(_6835.AGMAGleasonConicalGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6866.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6866

            return self._parent._cast(_6866.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6912.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6912

            return self._parent._cast(_6912.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6946.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6946

            return self._parent._cast(_6946.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6859.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(_6859.ComponentLoadCase)

        @property
        def part_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6950.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.PartLoadCase)

        @property
        def part_analysis(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6844.BevelDifferentialGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6844

            return self._parent._cast(_6844.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6847.BevelDifferentialPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6847

            return self._parent._cast(_6847.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6848.BevelDifferentialSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6848

            return self._parent._cast(_6848.BevelDifferentialSunGearLoadCase)

        @property
        def spiral_bevel_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6975.SpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6975

            return self._parent._cast(_6975.SpiralBevelGearLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6981.StraightBevelDiffGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6981

            return self._parent._cast(_6981.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6984.StraightBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6984

            return self._parent._cast(_6984.StraightBevelGearLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6987.StraightBevelPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6987

            return self._parent._cast(_6987.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6988.StraightBevelSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6988

            return self._parent._cast(_6988.StraightBevelSunGearLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_7007.ZerolBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7007

            return self._parent._cast(_7007.ZerolBevelGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "BevelGearLoadCase":
            return self._parent

        def __getattr__(self: "BevelGearLoadCase._Cast_BevelGearLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2539.BevelGear":
        """mastapy.system_model.part_model.gears.BevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BevelGearLoadCase._Cast_BevelGearLoadCase":
        return self._Cast_BevelGearLoadCase(self)
