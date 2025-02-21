"""PlanetaryGearSet"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2546
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "PlanetaryGearSet"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545, _2547, _2552
    from mastapy.system_model.part_model import _2496, _2454, _2488
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSet",)


Self = TypeVar("Self", bound="PlanetaryGearSet")


class PlanetaryGearSet(_2546.CylindricalGearSet):
    """PlanetaryGearSet

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryGearSet")

    class _Cast_PlanetaryGearSet:
        """Special nested class for casting PlanetaryGearSet to subclasses."""

        def __init__(
            self: "PlanetaryGearSet._Cast_PlanetaryGearSet", parent: "PlanetaryGearSet"
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set(
            self: "PlanetaryGearSet._Cast_PlanetaryGearSet",
        ) -> "_2546.CylindricalGearSet":
            return self._parent._cast(_2546.CylindricalGearSet)

        @property
        def gear_set(
            self: "PlanetaryGearSet._Cast_PlanetaryGearSet",
        ) -> "_2552.GearSet":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.GearSet)

        @property
        def specialised_assembly(
            self: "PlanetaryGearSet._Cast_PlanetaryGearSet",
        ) -> "_2496.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2496

            return self._parent._cast(_2496.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "PlanetaryGearSet._Cast_PlanetaryGearSet",
        ) -> "_2454.AbstractAssembly":
            from mastapy.system_model.part_model import _2454

            return self._parent._cast(_2454.AbstractAssembly)

        @property
        def part(self: "PlanetaryGearSet._Cast_PlanetaryGearSet") -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(
            self: "PlanetaryGearSet._Cast_PlanetaryGearSet",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def planetary_gear_set(
            self: "PlanetaryGearSet._Cast_PlanetaryGearSet",
        ) -> "PlanetaryGearSet":
            return self._parent

        def __getattr__(self: "PlanetaryGearSet._Cast_PlanetaryGearSet", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetaryGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def annuluses(self: Self) -> "List[_2545.CylindricalGear]":
        """List[mastapy.system_model.part_model.gears.CylindricalGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Annuluses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planets(self: Self) -> "List[_2547.CylindricalPlanetGear]":
        """List[mastapy.system_model.part_model.gears.CylindricalPlanetGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def suns(self: Self) -> "List[_2545.CylindricalGear]":
        """List[mastapy.system_model.part_model.gears.CylindricalGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Suns

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def add_annulus(self: Self) -> "_2545.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear"""
        method_result = self.wrapped.AddAnnulus()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def add_planet(self: Self) -> "_2545.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear"""
        method_result = self.wrapped.AddPlanet()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def add_sun(self: Self) -> "_2545.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear"""
        method_result = self.wrapped.AddSun()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def set_number_of_planets(self: Self, amount: "int"):
        """Method does not return.

        Args:
            amount (int)
        """
        amount = int(amount)
        self.wrapped.SetNumberOfPlanets(amount if amount else 0)

    @property
    def cast_to(self: Self) -> "PlanetaryGearSet._Cast_PlanetaryGearSet":
        return self._Cast_PlanetaryGearSet(self)
