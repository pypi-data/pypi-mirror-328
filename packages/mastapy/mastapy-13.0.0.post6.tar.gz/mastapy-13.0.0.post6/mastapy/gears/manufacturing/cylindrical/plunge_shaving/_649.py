"""PlungeShaverGeneration"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLUNGE_SHAVER_GENERATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving",
    "PlungeShaverGeneration",
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1488
    from mastapy.gears.gear_designs.cylindrical import _1004
    from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _642, _656


__docformat__ = "restructuredtext en"
__all__ = ("PlungeShaverGeneration",)


Self = TypeVar("Self", bound="PlungeShaverGeneration")


class PlungeShaverGeneration(_0.APIBase):
    """PlungeShaverGeneration

    This is a mastapy class.
    """

    TYPE = _PLUNGE_SHAVER_GENERATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlungeShaverGeneration")

    class _Cast_PlungeShaverGeneration:
        """Special nested class for casting PlungeShaverGeneration to subclasses."""

        def __init__(
            self: "PlungeShaverGeneration._Cast_PlungeShaverGeneration",
            parent: "PlungeShaverGeneration",
        ):
            self._parent = parent

        @property
        def plunge_shaver_generation(
            self: "PlungeShaverGeneration._Cast_PlungeShaverGeneration",
        ) -> "PlungeShaverGeneration":
            return self._parent

        def __getattr__(
            self: "PlungeShaverGeneration._Cast_PlungeShaverGeneration", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlungeShaverGeneration.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def calculated_conjugate_face_width(self: Self) -> "_1488.Range":
        """mastapy.math_utility.Range

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedConjugateFaceWidth

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_start_of_active_profile_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearStartOfActiveProfileDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def manufactured_end_of_active_profile_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ManufacturedEndOfActiveProfileDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def manufactured_start_of_active_profile_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ManufacturedStartOfActiveProfileDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def shaft_angle_unsigned(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftAngleUnsigned

        if temp is None:
            return 0.0

        return temp

    @property
    def crossed_axis_calculation_details(
        self: Self,
    ) -> "_1004.CrossedAxisCylindricalGearPairLineContact":
        """mastapy.gears.gear_designs.cylindrical.CrossedAxisCylindricalGearPairLineContact

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CrossedAxisCalculationDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def calculation_errors(self: Self) -> "List[_642.CalculationError]":
        """List[mastapy.gears.manufacturing.cylindrical.plunge_shaving.CalculationError]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculationErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def points_of_interest_on_the_shaver(
        self: Self,
    ) -> "List[_656.ShaverPointOfInterest]":
        """List[mastapy.gears.manufacturing.cylindrical.plunge_shaving.ShaverPointOfInterest]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PointsOfInterestOnTheShaver

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "PlungeShaverGeneration._Cast_PlungeShaverGeneration":
        return self._Cast_PlungeShaverGeneration(self)
