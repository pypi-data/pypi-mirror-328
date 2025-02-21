"""ReducedCylindricalGearSetDutyCycleRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.cylindrical import _463
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_REDUCED_CYLINDRICAL_GEAR_SET_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "ReducedCylindricalGearSetDutyCycleRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _362, _355
    from mastapy.gears.analysis import _1217


__docformat__ = "restructuredtext en"
__all__ = ("ReducedCylindricalGearSetDutyCycleRating",)


Self = TypeVar("Self", bound="ReducedCylindricalGearSetDutyCycleRating")


class ReducedCylindricalGearSetDutyCycleRating(_463.CylindricalGearSetDutyCycleRating):
    """ReducedCylindricalGearSetDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _REDUCED_CYLINDRICAL_GEAR_SET_DUTY_CYCLE_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ReducedCylindricalGearSetDutyCycleRating"
    )

    class _Cast_ReducedCylindricalGearSetDutyCycleRating:
        """Special nested class for casting ReducedCylindricalGearSetDutyCycleRating to subclasses."""

        def __init__(
            self: "ReducedCylindricalGearSetDutyCycleRating._Cast_ReducedCylindricalGearSetDutyCycleRating",
            parent: "ReducedCylindricalGearSetDutyCycleRating",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_duty_cycle_rating(
            self: "ReducedCylindricalGearSetDutyCycleRating._Cast_ReducedCylindricalGearSetDutyCycleRating",
        ) -> "_463.CylindricalGearSetDutyCycleRating":
            return self._parent._cast(_463.CylindricalGearSetDutyCycleRating)

        @property
        def gear_set_duty_cycle_rating(
            self: "ReducedCylindricalGearSetDutyCycleRating._Cast_ReducedCylindricalGearSetDutyCycleRating",
        ) -> "_362.GearSetDutyCycleRating":
            from mastapy.gears.rating import _362

            return self._parent._cast(_362.GearSetDutyCycleRating)

        @property
        def abstract_gear_set_rating(
            self: "ReducedCylindricalGearSetDutyCycleRating._Cast_ReducedCylindricalGearSetDutyCycleRating",
        ) -> "_355.AbstractGearSetRating":
            from mastapy.gears.rating import _355

            return self._parent._cast(_355.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "ReducedCylindricalGearSetDutyCycleRating._Cast_ReducedCylindricalGearSetDutyCycleRating",
        ) -> "_1217.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1217

            return self._parent._cast(_1217.AbstractGearSetAnalysis)

        @property
        def reduced_cylindrical_gear_set_duty_cycle_rating(
            self: "ReducedCylindricalGearSetDutyCycleRating._Cast_ReducedCylindricalGearSetDutyCycleRating",
        ) -> "ReducedCylindricalGearSetDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "ReducedCylindricalGearSetDutyCycleRating._Cast_ReducedCylindricalGearSetDutyCycleRating",
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
        self: Self, instance_to_wrap: "ReducedCylindricalGearSetDutyCycleRating.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ReducedCylindricalGearSetDutyCycleRating._Cast_ReducedCylindricalGearSetDutyCycleRating":
        return self._Cast_ReducedCylindricalGearSetDutyCycleRating(self)
