"""LeadReliefWithDeviation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1145
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LEAD_RELIEF_WITH_DEVIATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "LeadReliefWithDeviation",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import (
        _1126,
        _1128,
        _1130,
        _1147,
    )


__docformat__ = "restructuredtext en"
__all__ = ("LeadReliefWithDeviation",)


Self = TypeVar("Self", bound="LeadReliefWithDeviation")


class LeadReliefWithDeviation(_1145.ReliefWithDeviation):
    """LeadReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _LEAD_RELIEF_WITH_DEVIATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LeadReliefWithDeviation")

    class _Cast_LeadReliefWithDeviation:
        """Special nested class for casting LeadReliefWithDeviation to subclasses."""

        def __init__(
            self: "LeadReliefWithDeviation._Cast_LeadReliefWithDeviation",
            parent: "LeadReliefWithDeviation",
        ):
            self._parent = parent

        @property
        def relief_with_deviation(
            self: "LeadReliefWithDeviation._Cast_LeadReliefWithDeviation",
        ) -> "_1145.ReliefWithDeviation":
            return self._parent._cast(_1145.ReliefWithDeviation)

        @property
        def lead_form_relief_with_deviation(
            self: "LeadReliefWithDeviation._Cast_LeadReliefWithDeviation",
        ) -> "_1126.LeadFormReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1126

            return self._parent._cast(_1126.LeadFormReliefWithDeviation)

        @property
        def lead_relief_specification_for_customer_102(
            self: "LeadReliefWithDeviation._Cast_LeadReliefWithDeviation",
        ) -> "_1128.LeadReliefSpecificationForCustomer102":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1128

            return self._parent._cast(_1128.LeadReliefSpecificationForCustomer102)

        @property
        def lead_slope_relief_with_deviation(
            self: "LeadReliefWithDeviation._Cast_LeadReliefWithDeviation",
        ) -> "_1130.LeadSlopeReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1130

            return self._parent._cast(_1130.LeadSlopeReliefWithDeviation)

        @property
        def total_lead_relief_with_deviation(
            self: "LeadReliefWithDeviation._Cast_LeadReliefWithDeviation",
        ) -> "_1147.TotalLeadReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1147

            return self._parent._cast(_1147.TotalLeadReliefWithDeviation)

        @property
        def lead_relief_with_deviation(
            self: "LeadReliefWithDeviation._Cast_LeadReliefWithDeviation",
        ) -> "LeadReliefWithDeviation":
            return self._parent

        def __getattr__(
            self: "LeadReliefWithDeviation._Cast_LeadReliefWithDeviation", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LeadReliefWithDeviation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def distance_along_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DistanceAlongFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def lead_relief(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadRelief

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "LeadReliefWithDeviation._Cast_LeadReliefWithDeviation":
        return self._Cast_LeadReliefWithDeviation(self)
