"""BevelDifferentialPlanetGearLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6822
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialPlanetGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2517
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6827,
        _6813,
        _6844,
        _6890,
        _6924,
        _6837,
        _6928,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearLoadCase",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearLoadCase")


class BevelDifferentialPlanetGearLoadCase(_6822.BevelDifferentialGearLoadCase):
    """BevelDifferentialPlanetGearLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialPlanetGearLoadCase")

    class _Cast_BevelDifferentialPlanetGearLoadCase:
        """Special nested class for casting BevelDifferentialPlanetGearLoadCase to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearLoadCase._Cast_BevelDifferentialPlanetGearLoadCase",
            parent: "BevelDifferentialPlanetGearLoadCase",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_load_case(
            self: "BevelDifferentialPlanetGearLoadCase._Cast_BevelDifferentialPlanetGearLoadCase",
        ) -> "_6822.BevelDifferentialGearLoadCase":
            return self._parent._cast(_6822.BevelDifferentialGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "BevelDifferentialPlanetGearLoadCase._Cast_BevelDifferentialPlanetGearLoadCase",
        ) -> "_6827.BevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6827

            return self._parent._cast(_6827.BevelGearLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "BevelDifferentialPlanetGearLoadCase._Cast_BevelDifferentialPlanetGearLoadCase",
        ) -> "_6813.AGMAGleasonConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6813

            return self._parent._cast(_6813.AGMAGleasonConicalGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "BevelDifferentialPlanetGearLoadCase._Cast_BevelDifferentialPlanetGearLoadCase",
        ) -> "_6844.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6844

            return self._parent._cast(_6844.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "BevelDifferentialPlanetGearLoadCase._Cast_BevelDifferentialPlanetGearLoadCase",
        ) -> "_6890.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6890

            return self._parent._cast(_6890.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "BevelDifferentialPlanetGearLoadCase._Cast_BevelDifferentialPlanetGearLoadCase",
        ) -> "_6924.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6924

            return self._parent._cast(_6924.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "BevelDifferentialPlanetGearLoadCase._Cast_BevelDifferentialPlanetGearLoadCase",
        ) -> "_6837.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.ComponentLoadCase)

        @property
        def part_load_case(
            self: "BevelDifferentialPlanetGearLoadCase._Cast_BevelDifferentialPlanetGearLoadCase",
        ) -> "_6928.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(
            self: "BevelDifferentialPlanetGearLoadCase._Cast_BevelDifferentialPlanetGearLoadCase",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialPlanetGearLoadCase._Cast_BevelDifferentialPlanetGearLoadCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearLoadCase._Cast_BevelDifferentialPlanetGearLoadCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "BevelDifferentialPlanetGearLoadCase._Cast_BevelDifferentialPlanetGearLoadCase",
        ) -> "BevelDifferentialPlanetGearLoadCase":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearLoadCase._Cast_BevelDifferentialPlanetGearLoadCase",
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
        self: Self, instance_to_wrap: "BevelDifferentialPlanetGearLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2517.BevelDifferentialPlanetGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear

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
    ) -> (
        "BevelDifferentialPlanetGearLoadCase._Cast_BevelDifferentialPlanetGearLoadCase"
    ):
        return self._Cast_BevelDifferentialPlanetGearLoadCase(self)
