"""ProfileReliefWithDeviation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1145
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PROFILE_RELIEF_WITH_DEVIATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "ProfileReliefWithDeviation",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1035
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import (
        _1140,
        _1142,
        _1144,
        _1148,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ProfileReliefWithDeviation",)


Self = TypeVar("Self", bound="ProfileReliefWithDeviation")


class ProfileReliefWithDeviation(_1145.ReliefWithDeviation):
    """ProfileReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _PROFILE_RELIEF_WITH_DEVIATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ProfileReliefWithDeviation")

    class _Cast_ProfileReliefWithDeviation:
        """Special nested class for casting ProfileReliefWithDeviation to subclasses."""

        def __init__(
            self: "ProfileReliefWithDeviation._Cast_ProfileReliefWithDeviation",
            parent: "ProfileReliefWithDeviation",
        ):
            self._parent = parent

        @property
        def relief_with_deviation(
            self: "ProfileReliefWithDeviation._Cast_ProfileReliefWithDeviation",
        ) -> "_1145.ReliefWithDeviation":
            return self._parent._cast(_1145.ReliefWithDeviation)

        @property
        def profile_form_relief_with_deviation(
            self: "ProfileReliefWithDeviation._Cast_ProfileReliefWithDeviation",
        ) -> "_1140.ProfileFormReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1140

            return self._parent._cast(_1140.ProfileFormReliefWithDeviation)

        @property
        def profile_relief_specification_for_customer_102(
            self: "ProfileReliefWithDeviation._Cast_ProfileReliefWithDeviation",
        ) -> "_1142.ProfileReliefSpecificationForCustomer102":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1142

            return self._parent._cast(_1142.ProfileReliefSpecificationForCustomer102)

        @property
        def profile_slope_relief_with_deviation(
            self: "ProfileReliefWithDeviation._Cast_ProfileReliefWithDeviation",
        ) -> "_1144.ProfileSlopeReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1144

            return self._parent._cast(_1144.ProfileSlopeReliefWithDeviation)

        @property
        def total_profile_relief_with_deviation(
            self: "ProfileReliefWithDeviation._Cast_ProfileReliefWithDeviation",
        ) -> "_1148.TotalProfileReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1148

            return self._parent._cast(_1148.TotalProfileReliefWithDeviation)

        @property
        def profile_relief_with_deviation(
            self: "ProfileReliefWithDeviation._Cast_ProfileReliefWithDeviation",
        ) -> "ProfileReliefWithDeviation":
            return self._parent

        def __getattr__(
            self: "ProfileReliefWithDeviation._Cast_ProfileReliefWithDeviation",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ProfileReliefWithDeviation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def profile_relief(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileRelief

        if temp is None:
            return 0.0

        return temp

    @property
    def roll_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def position_on_profile(self: Self) -> "_1035.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PositionOnProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ProfileReliefWithDeviation._Cast_ProfileReliefWithDeviation":
        return self._Cast_ProfileReliefWithDeviation(self)
