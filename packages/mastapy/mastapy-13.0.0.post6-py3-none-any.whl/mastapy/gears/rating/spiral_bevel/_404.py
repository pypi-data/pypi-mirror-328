"""SpiralBevelGearSetRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.bevel import _556
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.SpiralBevel", "SpiralBevelGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.spiral_bevel import _971
    from mastapy.gears.rating.spiral_bevel import _403, _402
    from mastapy.gears.rating.agma_gleason_conical import _567
    from mastapy.gears.rating.conical import _542
    from mastapy.gears.rating import _363, _355
    from mastapy.gears.analysis import _1217


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetRating",)


Self = TypeVar("Self", bound="SpiralBevelGearSetRating")


class SpiralBevelGearSetRating(_556.BevelGearSetRating):
    """SpiralBevelGearSetRating

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearSetRating")

    class _Cast_SpiralBevelGearSetRating:
        """Special nested class for casting SpiralBevelGearSetRating to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetRating._Cast_SpiralBevelGearSetRating",
            parent: "SpiralBevelGearSetRating",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_rating(
            self: "SpiralBevelGearSetRating._Cast_SpiralBevelGearSetRating",
        ) -> "_556.BevelGearSetRating":
            return self._parent._cast(_556.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "SpiralBevelGearSetRating._Cast_SpiralBevelGearSetRating",
        ) -> "_567.AGMAGleasonConicalGearSetRating":
            from mastapy.gears.rating.agma_gleason_conical import _567

            return self._parent._cast(_567.AGMAGleasonConicalGearSetRating)

        @property
        def conical_gear_set_rating(
            self: "SpiralBevelGearSetRating._Cast_SpiralBevelGearSetRating",
        ) -> "_542.ConicalGearSetRating":
            from mastapy.gears.rating.conical import _542

            return self._parent._cast(_542.ConicalGearSetRating)

        @property
        def gear_set_rating(
            self: "SpiralBevelGearSetRating._Cast_SpiralBevelGearSetRating",
        ) -> "_363.GearSetRating":
            from mastapy.gears.rating import _363

            return self._parent._cast(_363.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "SpiralBevelGearSetRating._Cast_SpiralBevelGearSetRating",
        ) -> "_355.AbstractGearSetRating":
            from mastapy.gears.rating import _355

            return self._parent._cast(_355.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "SpiralBevelGearSetRating._Cast_SpiralBevelGearSetRating",
        ) -> "_1217.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1217

            return self._parent._cast(_1217.AbstractGearSetAnalysis)

        @property
        def spiral_bevel_gear_set_rating(
            self: "SpiralBevelGearSetRating._Cast_SpiralBevelGearSetRating",
        ) -> "SpiralBevelGearSetRating":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetRating._Cast_SpiralBevelGearSetRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearSetRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def spiral_bevel_gear_set(self: Self) -> "_971.SpiralBevelGearSetDesign":
        """mastapy.gears.gear_designs.spiral_bevel.SpiralBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def spiral_bevel_gear_ratings(self: Self) -> "List[_403.SpiralBevelGearRating]":
        """List[mastapy.gears.rating.spiral_bevel.SpiralBevelGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_mesh_ratings(self: Self) -> "List[_402.SpiralBevelGearMeshRating]":
        """List[mastapy.gears.rating.spiral_bevel.SpiralBevelGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearSetRating._Cast_SpiralBevelGearSetRating":
        return self._Cast_SpiralBevelGearSetRating(self)
