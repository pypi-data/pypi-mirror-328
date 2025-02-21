"""CylindricalAccuracyGrader"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_ACCURACY_GRADER = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances",
    "CylindricalAccuracyGrader",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
        _1156,
        _1149,
        _1150,
        _1152,
        _1153,
        _1155,
        _1159,
        _1160,
        _1161,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalAccuracyGrader",)


Self = TypeVar("Self", bound="CylindricalAccuracyGrader")


class CylindricalAccuracyGrader(_0.APIBase):
    """CylindricalAccuracyGrader

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_ACCURACY_GRADER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalAccuracyGrader")

    class _Cast_CylindricalAccuracyGrader:
        """Special nested class for casting CylindricalAccuracyGrader to subclasses."""

        def __init__(
            self: "CylindricalAccuracyGrader._Cast_CylindricalAccuracyGrader",
            parent: "CylindricalAccuracyGrader",
        ):
            self._parent = parent

        @property
        def agma2000a88_accuracy_grader(
            self: "CylindricalAccuracyGrader._Cast_CylindricalAccuracyGrader",
        ) -> "_1149.AGMA2000A88AccuracyGrader":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1149,
            )

            return self._parent._cast(_1149.AGMA2000A88AccuracyGrader)

        @property
        def agma20151a01_accuracy_grader(
            self: "CylindricalAccuracyGrader._Cast_CylindricalAccuracyGrader",
        ) -> "_1150.AGMA20151A01AccuracyGrader":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1150,
            )

            return self._parent._cast(_1150.AGMA20151A01AccuracyGrader)

        @property
        def agmaiso13281b14_accuracy_grader(
            self: "CylindricalAccuracyGrader._Cast_CylindricalAccuracyGrader",
        ) -> "_1152.AGMAISO13281B14AccuracyGrader":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1152,
            )

            return self._parent._cast(_1152.AGMAISO13281B14AccuracyGrader)

        @property
        def customer_102agma2000_accuracy_grader(
            self: "CylindricalAccuracyGrader._Cast_CylindricalAccuracyGrader",
        ) -> "_1153.Customer102AGMA2000AccuracyGrader":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1153,
            )

            return self._parent._cast(_1153.Customer102AGMA2000AccuracyGrader)

        @property
        def cylindrical_accuracy_grader_with_profile_form_and_slope(
            self: "CylindricalAccuracyGrader._Cast_CylindricalAccuracyGrader",
        ) -> "_1155.CylindricalAccuracyGraderWithProfileFormAndSlope":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1155,
            )

            return self._parent._cast(
                _1155.CylindricalAccuracyGraderWithProfileFormAndSlope
            )

        @property
        def iso132811995_accuracy_grader(
            self: "CylindricalAccuracyGrader._Cast_CylindricalAccuracyGrader",
        ) -> "_1159.ISO132811995AccuracyGrader":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1159,
            )

            return self._parent._cast(_1159.ISO132811995AccuracyGrader)

        @property
        def iso132812013_accuracy_grader(
            self: "CylindricalAccuracyGrader._Cast_CylindricalAccuracyGrader",
        ) -> "_1160.ISO132812013AccuracyGrader":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1160,
            )

            return self._parent._cast(_1160.ISO132812013AccuracyGrader)

        @property
        def iso1328_accuracy_grader_common(
            self: "CylindricalAccuracyGrader._Cast_CylindricalAccuracyGrader",
        ) -> "_1161.ISO1328AccuracyGraderCommon":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1161,
            )

            return self._parent._cast(_1161.ISO1328AccuracyGraderCommon)

        @property
        def cylindrical_accuracy_grader(
            self: "CylindricalAccuracyGrader._Cast_CylindricalAccuracyGrader",
        ) -> "CylindricalAccuracyGrader":
            return self._parent

        def __getattr__(
            self: "CylindricalAccuracyGrader._Cast_CylindricalAccuracyGrader", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalAccuracyGrader.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def tolerance_standard(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToleranceStandard

        if temp is None:
            return ""

        return temp

    @property
    def accuracy_grades(self: Self) -> "_1156.CylindricalAccuracyGrades":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.CylindricalAccuracyGrades

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AccuracyGrades

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalAccuracyGrader._Cast_CylindricalAccuracyGrader":
        return self._Cast_CylindricalAccuracyGrader(self)
