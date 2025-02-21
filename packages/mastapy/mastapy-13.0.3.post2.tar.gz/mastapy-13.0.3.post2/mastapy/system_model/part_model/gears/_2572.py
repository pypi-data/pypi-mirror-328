"""WormGearSet"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2552
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "WormGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.worm import _963
    from mastapy.system_model.part_model.gears import _2571
    from mastapy.system_model.connections_and_sockets.gears import _2349
    from mastapy.system_model.part_model import _2496, _2454, _2488
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSet",)


Self = TypeVar("Self", bound="WormGearSet")


class WormGearSet(_2552.GearSet):
    """WormGearSet

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearSet")

    class _Cast_WormGearSet:
        """Special nested class for casting WormGearSet to subclasses."""

        def __init__(self: "WormGearSet._Cast_WormGearSet", parent: "WormGearSet"):
            self._parent = parent

        @property
        def gear_set(self: "WormGearSet._Cast_WormGearSet") -> "_2552.GearSet":
            return self._parent._cast(_2552.GearSet)

        @property
        def specialised_assembly(
            self: "WormGearSet._Cast_WormGearSet",
        ) -> "_2496.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2496

            return self._parent._cast(_2496.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "WormGearSet._Cast_WormGearSet",
        ) -> "_2454.AbstractAssembly":
            from mastapy.system_model.part_model import _2454

            return self._parent._cast(_2454.AbstractAssembly)

        @property
        def part(self: "WormGearSet._Cast_WormGearSet") -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(
            self: "WormGearSet._Cast_WormGearSet",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def worm_gear_set(self: "WormGearSet._Cast_WormGearSet") -> "WormGearSet":
            return self._parent

        def __getattr__(self: "WormGearSet._Cast_WormGearSet", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_set_design(self: Self) -> "_963.WormGearSetDesign":
        """mastapy.gears.gear_designs.worm.WormGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm_gear_set_design(self: Self) -> "_963.WormGearSetDesign":
        """mastapy.gears.gear_designs.worm.WormGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm_gears(self: Self) -> "List[_2571.WormGear]":
        """List[mastapy.system_model.part_model.gears.WormGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_meshes(self: Self) -> "List[_2349.WormGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.WormGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "WormGearSet._Cast_WormGearSet":
        return self._Cast_WormGearSet(self)
