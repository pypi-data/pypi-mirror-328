"""AGMAGleasonConicalGearMeshRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy.gears.rating.conical import _539
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.AGMAGleasonConical", "AGMAGleasonConicalGearMeshRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1169
    from mastapy.gears.rating.zerol_bevel import _369
    from mastapy.gears.rating.straight_bevel import _395
    from mastapy.gears.rating.spiral_bevel import _402
    from mastapy.gears.rating.hypoid import _438
    from mastapy.gears.rating.bevel import _554
    from mastapy.gears.rating import _360, _353
    from mastapy.gears.analysis import _1216


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshRating",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshRating")


class AGMAGleasonConicalGearMeshRating(_539.ConicalGearMeshRating):
    """AGMAGleasonConicalGearMeshRating

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshRating")

    class _Cast_AGMAGleasonConicalGearMeshRating:
        """Special nested class for casting AGMAGleasonConicalGearMeshRating to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
            parent: "AGMAGleasonConicalGearMeshRating",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_rating(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
        ) -> "_539.ConicalGearMeshRating":
            return self._parent._cast(_539.ConicalGearMeshRating)

        @property
        def gear_mesh_rating(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
        ) -> "_360.GearMeshRating":
            from mastapy.gears.rating import _360

            return self._parent._cast(_360.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
        ) -> "_353.AbstractGearMeshRating":
            from mastapy.gears.rating import _353

            return self._parent._cast(_353.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
        ) -> "_1216.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1216

            return self._parent._cast(_1216.AbstractGearMeshAnalysis)

        @property
        def zerol_bevel_gear_mesh_rating(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
        ) -> "_369.ZerolBevelGearMeshRating":
            from mastapy.gears.rating.zerol_bevel import _369

            return self._parent._cast(_369.ZerolBevelGearMeshRating)

        @property
        def straight_bevel_gear_mesh_rating(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
        ) -> "_395.StraightBevelGearMeshRating":
            from mastapy.gears.rating.straight_bevel import _395

            return self._parent._cast(_395.StraightBevelGearMeshRating)

        @property
        def spiral_bevel_gear_mesh_rating(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
        ) -> "_402.SpiralBevelGearMeshRating":
            from mastapy.gears.rating.spiral_bevel import _402

            return self._parent._cast(_402.SpiralBevelGearMeshRating)

        @property
        def hypoid_gear_mesh_rating(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
        ) -> "_438.HypoidGearMeshRating":
            from mastapy.gears.rating.hypoid import _438

            return self._parent._cast(_438.HypoidGearMeshRating)

        @property
        def bevel_gear_mesh_rating(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
        ) -> "_554.BevelGearMeshRating":
            from mastapy.gears.rating.bevel import _554

            return self._parent._cast(_554.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
        ) -> "AGMAGleasonConicalGearMeshRating":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearMeshRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_distribution_factor_method(
        self: Self,
    ) -> "_1169.LoadDistributionFactorMethods":
        """mastapy.gears.gear_designs.conical.LoadDistributionFactorMethods

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadDistributionFactorMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Conical.LoadDistributionFactorMethods"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.conical._1169", "LoadDistributionFactorMethods"
        )(value)

    @property
    def maximum_relative_displacement(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumRelativeDisplacement

        if temp is None:
            return 0.0

        return temp

    @property
    def overload_factor_bending(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverloadFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def overload_factor_contact(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverloadFactorContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating":
        return self._Cast_AGMAGleasonConicalGearMeshRating(self)
