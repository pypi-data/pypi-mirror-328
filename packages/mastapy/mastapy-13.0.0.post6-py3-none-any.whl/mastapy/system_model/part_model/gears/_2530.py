"""Gear"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Optional

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2464
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "Gear")

if TYPE_CHECKING:
    from mastapy.gears.gear_designs import _947
    from mastapy.system_model.part_model.gears import (
        _2532,
        _2513,
        _2515,
        _2517,
        _2518,
        _2519,
        _2521,
        _2523,
        _2525,
        _2527,
        _2528,
        _2534,
        _2536,
        _2538,
        _2540,
        _2543,
        _2545,
        _2547,
        _2549,
        _2550,
        _2551,
        _2553,
    )
    from mastapy.system_model.part_model.shaft_model import _2482
    from mastapy.system_model.part_model import _2444, _2468
    from mastapy.system_model import _2203


__docformat__ = "restructuredtext en"
__all__ = ("Gear",)


Self = TypeVar("Self", bound="Gear")


class Gear(_2464.MountableComponent):
    """Gear

    This is a mastapy class.
    """

    TYPE = _GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Gear")

    class _Cast_Gear:
        """Special nested class for casting Gear to subclasses."""

        def __init__(self: "Gear._Cast_Gear", parent: "Gear"):
            self._parent = parent

        @property
        def mountable_component(self: "Gear._Cast_Gear") -> "_2464.MountableComponent":
            return self._parent._cast(_2464.MountableComponent)

        @property
        def component(self: "Gear._Cast_Gear") -> "_2444.Component":
            from mastapy.system_model.part_model import _2444

            return self._parent._cast(_2444.Component)

        @property
        def part(self: "Gear._Cast_Gear") -> "_2468.Part":
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(self: "Gear._Cast_Gear") -> "_2203.DesignEntity":
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def agma_gleason_conical_gear(
            self: "Gear._Cast_Gear",
        ) -> "_2513.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2513

            return self._parent._cast(_2513.AGMAGleasonConicalGear)

        @property
        def bevel_differential_gear(
            self: "Gear._Cast_Gear",
        ) -> "_2515.BevelDifferentialGear":
            from mastapy.system_model.part_model.gears import _2515

            return self._parent._cast(_2515.BevelDifferentialGear)

        @property
        def bevel_differential_planet_gear(
            self: "Gear._Cast_Gear",
        ) -> "_2517.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2517

            return self._parent._cast(_2517.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "Gear._Cast_Gear",
        ) -> "_2518.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2518

            return self._parent._cast(_2518.BevelDifferentialSunGear)

        @property
        def bevel_gear(self: "Gear._Cast_Gear") -> "_2519.BevelGear":
            from mastapy.system_model.part_model.gears import _2519

            return self._parent._cast(_2519.BevelGear)

        @property
        def concept_gear(self: "Gear._Cast_Gear") -> "_2521.ConceptGear":
            from mastapy.system_model.part_model.gears import _2521

            return self._parent._cast(_2521.ConceptGear)

        @property
        def conical_gear(self: "Gear._Cast_Gear") -> "_2523.ConicalGear":
            from mastapy.system_model.part_model.gears import _2523

            return self._parent._cast(_2523.ConicalGear)

        @property
        def cylindrical_gear(self: "Gear._Cast_Gear") -> "_2525.CylindricalGear":
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.CylindricalGear)

        @property
        def cylindrical_planet_gear(
            self: "Gear._Cast_Gear",
        ) -> "_2527.CylindricalPlanetGear":
            from mastapy.system_model.part_model.gears import _2527

            return self._parent._cast(_2527.CylindricalPlanetGear)

        @property
        def face_gear(self: "Gear._Cast_Gear") -> "_2528.FaceGear":
            from mastapy.system_model.part_model.gears import _2528

            return self._parent._cast(_2528.FaceGear)

        @property
        def hypoid_gear(self: "Gear._Cast_Gear") -> "_2534.HypoidGear":
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.HypoidGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "Gear._Cast_Gear",
        ) -> "_2536.KlingelnbergCycloPalloidConicalGear":
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "Gear._Cast_Gear",
        ) -> "_2538.KlingelnbergCycloPalloidHypoidGear":
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "Gear._Cast_Gear",
        ) -> "_2540.KlingelnbergCycloPalloidSpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2540

            return self._parent._cast(_2540.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def spiral_bevel_gear(self: "Gear._Cast_Gear") -> "_2543.SpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(
            self: "Gear._Cast_Gear",
        ) -> "_2545.StraightBevelDiffGear":
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(self: "Gear._Cast_Gear") -> "_2547.StraightBevelGear":
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.StraightBevelGear)

        @property
        def straight_bevel_planet_gear(
            self: "Gear._Cast_Gear",
        ) -> "_2549.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2549

            return self._parent._cast(_2549.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "Gear._Cast_Gear",
        ) -> "_2550.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.StraightBevelSunGear)

        @property
        def worm_gear(self: "Gear._Cast_Gear") -> "_2551.WormGear":
            from mastapy.system_model.part_model.gears import _2551

            return self._parent._cast(_2551.WormGear)

        @property
        def zerol_bevel_gear(self: "Gear._Cast_Gear") -> "_2553.ZerolBevelGear":
            from mastapy.system_model.part_model.gears import _2553

            return self._parent._cast(_2553.ZerolBevelGear)

        @property
        def gear(self: "Gear._Cast_Gear") -> "Gear":
            return self._parent

        def __getattr__(self: "Gear._Cast_Gear", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Gear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cloned_from(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClonedFrom

        if temp is None:
            return ""

        return temp

    @property
    def even_number_of_teeth_required(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.EvenNumberOfTeethRequired

        if temp is None:
            return False

        return temp

    @even_number_of_teeth_required.setter
    @enforce_parameter_types
    def even_number_of_teeth_required(self: Self, value: "bool"):
        self.wrapped.EvenNumberOfTeethRequired = (
            bool(value) if value is not None else False
        )

    @property
    def is_clone_gear(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsCloneGear

        if temp is None:
            return False

        return temp

    @property
    def length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: Self, value: "float"):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def maximum_number_of_teeth(self: Self) -> "int":
        """int"""
        temp = self.wrapped.MaximumNumberOfTeeth

        if temp is None:
            return 0

        return temp

    @maximum_number_of_teeth.setter
    @enforce_parameter_types
    def maximum_number_of_teeth(self: Self, value: "int"):
        self.wrapped.MaximumNumberOfTeeth = int(value) if value is not None else 0

    @property
    def maximum_and_minimum_number_of_teeth_deviation(self: Self) -> "Optional[int]":
        """Optional[int]"""
        temp = self.wrapped.MaximumAndMinimumNumberOfTeethDeviation

        if temp is None:
            return None

        return temp

    @maximum_and_minimum_number_of_teeth_deviation.setter
    @enforce_parameter_types
    def maximum_and_minimum_number_of_teeth_deviation(
        self: Self, value: "Optional[int]"
    ):
        self.wrapped.MaximumAndMinimumNumberOfTeethDeviation = value

    @property
    def minimum_number_of_teeth(self: Self) -> "int":
        """int"""
        temp = self.wrapped.MinimumNumberOfTeeth

        if temp is None:
            return 0

        return temp

    @minimum_number_of_teeth.setter
    @enforce_parameter_types
    def minimum_number_of_teeth(self: Self, value: "int"):
        self.wrapped.MinimumNumberOfTeeth = int(value) if value is not None else 0

    @property
    def active_gear_design(self: Self) -> "_947.GearDesign":
        """mastapy.gears.gear_designs.GearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    @enforce_parameter_types
    def face_width(self: Self, value: "float"):
        self.wrapped.FaceWidth = float(value) if value is not None else 0.0

    @property
    def gear_set(self: Self) -> "_2532.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def number_of_teeth(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return 0

        return temp

    @number_of_teeth.setter
    @enforce_parameter_types
    def number_of_teeth(self: Self, value: "int"):
        self.wrapped.NumberOfTeeth = int(value) if value is not None else 0

    @property
    def shaft(self: Self) -> "_2482.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Shaft

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def connect_to(self: Self, other_gear: "Gear"):
        """Method does not return.

        Args:
            other_gear (mastapy.system_model.part_model.gears.Gear)
        """
        self.wrapped.ConnectTo(other_gear.wrapped if other_gear else None)

    @property
    def cast_to(self: Self) -> "Gear._Cast_Gear":
        return self._Cast_Gear(self)
