"""BevelDifferentialGear"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2539
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialGear"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.bevel import _1198
    from mastapy.system_model.part_model.gears import _2537, _2538, _2533, _2543, _2550
    from mastapy.system_model.part_model import _2484, _2464, _2488
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGear",)


Self = TypeVar("Self", bound="BevelDifferentialGear")


class BevelDifferentialGear(_2539.BevelGear):
    """BevelDifferentialGear

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialGear")

    class _Cast_BevelDifferentialGear:
        """Special nested class for casting BevelDifferentialGear to subclasses."""

        def __init__(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
            parent: "BevelDifferentialGear",
        ):
            self._parent = parent

        @property
        def bevel_gear(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "_2539.BevelGear":
            return self._parent._cast(_2539.BevelGear)

        @property
        def agma_gleason_conical_gear(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "_2533.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.AGMAGleasonConicalGear)

        @property
        def conical_gear(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "_2543.ConicalGear":
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.ConicalGear)

        @property
        def gear(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "_2550.Gear":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.Gear)

        @property
        def mountable_component(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "_2484.MountableComponent":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.MountableComponent)

        @property
        def component(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "_2464.Component":
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.Component)

        @property
        def part(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def bevel_differential_planet_gear(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "_2537.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "_2538.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.BevelDifferentialSunGear)

        @property
        def bevel_differential_gear(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "BevelDifferentialGear":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelDifferentialGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_design(self: Self) -> "_1198.BevelGearDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BevelDifferentialGear._Cast_BevelDifferentialGear":
        return self._Cast_BevelDifferentialGear(self)
