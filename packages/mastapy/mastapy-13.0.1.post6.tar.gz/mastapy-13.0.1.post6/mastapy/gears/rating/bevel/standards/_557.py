"""AGMASpiralBevelGearSingleFlankRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.bevel.standards import _561
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_SPIRAL_BEVEL_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Bevel.Standards", "AGMASpiralBevelGearSingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.conical import _543
    from mastapy.gears.rating import _364


__docformat__ = "restructuredtext en"
__all__ = ("AGMASpiralBevelGearSingleFlankRating",)


Self = TypeVar("Self", bound="AGMASpiralBevelGearSingleFlankRating")


class AGMASpiralBevelGearSingleFlankRating(_561.SpiralBevelGearSingleFlankRating):
    """AGMASpiralBevelGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _AGMA_SPIRAL_BEVEL_GEAR_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMASpiralBevelGearSingleFlankRating")

    class _Cast_AGMASpiralBevelGearSingleFlankRating:
        """Special nested class for casting AGMASpiralBevelGearSingleFlankRating to subclasses."""

        def __init__(
            self: "AGMASpiralBevelGearSingleFlankRating._Cast_AGMASpiralBevelGearSingleFlankRating",
            parent: "AGMASpiralBevelGearSingleFlankRating",
        ):
            self._parent = parent

        @property
        def spiral_bevel_gear_single_flank_rating(
            self: "AGMASpiralBevelGearSingleFlankRating._Cast_AGMASpiralBevelGearSingleFlankRating",
        ) -> "_561.SpiralBevelGearSingleFlankRating":
            return self._parent._cast(_561.SpiralBevelGearSingleFlankRating)

        @property
        def conical_gear_single_flank_rating(
            self: "AGMASpiralBevelGearSingleFlankRating._Cast_AGMASpiralBevelGearSingleFlankRating",
        ) -> "_543.ConicalGearSingleFlankRating":
            from mastapy.gears.rating.conical import _543

            return self._parent._cast(_543.ConicalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(
            self: "AGMASpiralBevelGearSingleFlankRating._Cast_AGMASpiralBevelGearSingleFlankRating",
        ) -> "_364.GearSingleFlankRating":
            from mastapy.gears.rating import _364

            return self._parent._cast(_364.GearSingleFlankRating)

        @property
        def agma_spiral_bevel_gear_single_flank_rating(
            self: "AGMASpiralBevelGearSingleFlankRating._Cast_AGMASpiralBevelGearSingleFlankRating",
        ) -> "AGMASpiralBevelGearSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "AGMASpiralBevelGearSingleFlankRating._Cast_AGMASpiralBevelGearSingleFlankRating",
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
        self: Self, instance_to_wrap: "AGMASpiralBevelGearSingleFlankRating.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def hardness_ratio_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HardnessRatioFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_cycle_factor_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressCycleFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_cycle_factor_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressCycleFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "AGMASpiralBevelGearSingleFlankRating._Cast_AGMASpiralBevelGearSingleFlankRating":
        return self._Cast_AGMASpiralBevelGearSingleFlankRating(self)
