"""AGMAGleasonConicalGearSet"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.gears import _2524
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGearSet"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import (
        _2516,
        _2520,
        _2535,
        _2544,
        _2546,
        _2548,
        _2554,
        _2532,
    )
    from mastapy.system_model.part_model import _2476, _2434, _2468
    from mastapy.system_model import _2203


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSet",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSet")


class AGMAGleasonConicalGearSet(_2524.ConicalGearSet):
    """AGMAGleasonConicalGearSet

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearSet")

    class _Cast_AGMAGleasonConicalGearSet:
        """Special nested class for casting AGMAGleasonConicalGearSet to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
            parent: "AGMAGleasonConicalGearSet",
        ):
            self._parent = parent

        @property
        def conical_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2524.ConicalGearSet":
            return self._parent._cast(_2524.ConicalGearSet)

        @property
        def gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2532.GearSet":
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.GearSet)

        @property
        def specialised_assembly(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2476.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2476

            return self._parent._cast(_2476.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2434.AbstractAssembly":
            from mastapy.system_model.part_model import _2434

            return self._parent._cast(_2434.AbstractAssembly)

        @property
        def part(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2468.Part":
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2203.DesignEntity":
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def bevel_differential_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2516.BevelDifferentialGearSet":
            from mastapy.system_model.part_model.gears import _2516

            return self._parent._cast(_2516.BevelDifferentialGearSet)

        @property
        def bevel_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2520.BevelGearSet":
            from mastapy.system_model.part_model.gears import _2520

            return self._parent._cast(_2520.BevelGearSet)

        @property
        def hypoid_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2535.HypoidGearSet":
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.HypoidGearSet)

        @property
        def spiral_bevel_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2544.SpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2546.StraightBevelDiffGearSet":
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2548.StraightBevelGearSet":
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.StraightBevelGearSet)

        @property
        def zerol_bevel_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2554.ZerolBevelGearSet":
            from mastapy.system_model.part_model.gears import _2554

            return self._parent._cast(_2554.ZerolBevelGearSet)

        @property
        def agma_gleason_conical_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "AGMAGleasonConicalGearSet":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet":
        return self._Cast_AGMAGleasonConicalGearSet(self)
