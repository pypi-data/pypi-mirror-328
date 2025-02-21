"""CylindricalGearSetRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _363
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.materials import _251
    from mastapy.gears.gear_designs.cylindrical import _1028
    from mastapy.gears.rating.cylindrical.optimisation import _501
    from mastapy.gears.rating.cylindrical import _454, _460, _458
    from mastapy.gears.rating.cylindrical.vdi import _489
    from mastapy.gears.rating import _355
    from mastapy.gears.analysis import _1217


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetRating",)


Self = TypeVar("Self", bound="CylindricalGearSetRating")


class CylindricalGearSetRating(_363.GearSetRating):
    """CylindricalGearSetRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearSetRating")

    class _Cast_CylindricalGearSetRating:
        """Special nested class for casting CylindricalGearSetRating to subclasses."""

        def __init__(
            self: "CylindricalGearSetRating._Cast_CylindricalGearSetRating",
            parent: "CylindricalGearSetRating",
        ):
            self._parent = parent

        @property
        def gear_set_rating(
            self: "CylindricalGearSetRating._Cast_CylindricalGearSetRating",
        ) -> "_363.GearSetRating":
            return self._parent._cast(_363.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "CylindricalGearSetRating._Cast_CylindricalGearSetRating",
        ) -> "_355.AbstractGearSetRating":
            from mastapy.gears.rating import _355

            return self._parent._cast(_355.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "CylindricalGearSetRating._Cast_CylindricalGearSetRating",
        ) -> "_1217.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1217

            return self._parent._cast(_1217.AbstractGearSetAnalysis)

        @property
        def cylindrical_gear_set_rating(
            self: "CylindricalGearSetRating._Cast_CylindricalGearSetRating",
        ) -> "CylindricalGearSetRating":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetRating._Cast_CylindricalGearSetRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearSetRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating_method(self: Self) -> "_251.CylindricalGearRatingMethods":
        """mastapy.materials.CylindricalGearRatingMethods

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.CylindricalGearRatingMethods"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.materials._251", "CylindricalGearRatingMethods"
        )(value)

    @property
    def rating_standard_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingStandardName

        if temp is None:
            return ""

        return temp

    @property
    def cylindrical_gear_set(self: Self) -> "_1028.CylindricalGearSetDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def optimisations(self: Self) -> "_501.CylindricalGearSetRatingOptimisationHelper":
        """mastapy.gears.rating.cylindrical.optimisation.CylindricalGearSetRatingOptimisationHelper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Optimisations

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating_settings(
        self: Self,
    ) -> "_454.CylindricalGearDesignAndRatingSettingsItem":
        """mastapy.gears.rating.cylindrical.CylindricalGearDesignAndRatingSettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_ratings(self: Self) -> "List[_460.CylindricalGearRating]":
        """List[mastapy.gears.rating.cylindrical.CylindricalGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_gear_ratings(self: Self) -> "List[_460.CylindricalGearRating]":
        """List[mastapy.gears.rating.cylindrical.CylindricalGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_mesh_ratings(self: Self) -> "List[_458.CylindricalGearMeshRating]":
        """List[mastapy.gears.rating.cylindrical.CylindricalGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_mesh_ratings(self: Self) -> "List[_458.CylindricalGearMeshRating]":
        """List[mastapy.gears.rating.cylindrical.CylindricalGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def vdi_cylindrical_gear_single_flank_ratings(
        self: Self,
    ) -> "List[_489.VDI2737InternalGearSingleFlankRating]":
        """List[mastapy.gears.rating.cylindrical.vdi.VDI2737InternalGearSingleFlankRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VDICylindricalGearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetRating._Cast_CylindricalGearSetRating":
        return self._Cast_CylindricalGearSetRating(self)
