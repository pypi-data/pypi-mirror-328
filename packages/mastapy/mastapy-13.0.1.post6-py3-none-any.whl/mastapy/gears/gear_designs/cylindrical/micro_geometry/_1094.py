"""CylindricalGearCommonFlankMicroGeometry"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_COMMON_FLANK_MICRO_GEOMETRY = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "CylindricalGearCommonFlankMicroGeometry",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1025


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearCommonFlankMicroGeometry",)


Self = TypeVar("Self", bound="CylindricalGearCommonFlankMicroGeometry")


class CylindricalGearCommonFlankMicroGeometry(_0.APIBase):
    """CylindricalGearCommonFlankMicroGeometry

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_COMMON_FLANK_MICRO_GEOMETRY
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearCommonFlankMicroGeometry"
    )

    class _Cast_CylindricalGearCommonFlankMicroGeometry:
        """Special nested class for casting CylindricalGearCommonFlankMicroGeometry to subclasses."""

        def __init__(
            self: "CylindricalGearCommonFlankMicroGeometry._Cast_CylindricalGearCommonFlankMicroGeometry",
            parent: "CylindricalGearCommonFlankMicroGeometry",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_common_flank_micro_geometry(
            self: "CylindricalGearCommonFlankMicroGeometry._Cast_CylindricalGearCommonFlankMicroGeometry",
        ) -> "CylindricalGearCommonFlankMicroGeometry":
            return self._parent

        def __getattr__(
            self: "CylindricalGearCommonFlankMicroGeometry._Cast_CylindricalGearCommonFlankMicroGeometry",
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
        self: Self, instance_to_wrap: "CylindricalGearCommonFlankMicroGeometry.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def profile_factor_for_0_bias_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileFactorFor0BiasRelief

        if temp is None:
            return 0.0

        return temp

    @profile_factor_for_0_bias_relief.setter
    @enforce_parameter_types
    def profile_factor_for_0_bias_relief(self: Self, value: "float"):
        self.wrapped.ProfileFactorFor0BiasRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def read_micro_geometry_from_an_external_file_using_file_name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.ReadMicroGeometryFromAnExternalFileUsingFileName

        if temp is None:
            return ""

        return temp

    @read_micro_geometry_from_an_external_file_using_file_name.setter
    @enforce_parameter_types
    def read_micro_geometry_from_an_external_file_using_file_name(
        self: Self, value: "str"
    ):
        self.wrapped.ReadMicroGeometryFromAnExternalFileUsingFileName = (
            str(value) if value is not None else ""
        )

    @property
    def use_measured_map_data(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseMeasuredMapData

        if temp is None:
            return False

        return temp

    @use_measured_map_data.setter
    @enforce_parameter_types
    def use_measured_map_data(self: Self, value: "bool"):
        self.wrapped.UseMeasuredMapData = bool(value) if value is not None else False

    @property
    def zero_bias_relief(self: Self) -> "_1025.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZeroBiasRelief

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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

    def read_micro_geometry_from_an_external_file(self: Self):
        """Method does not return."""
        self.wrapped.ReadMicroGeometryFromAnExternalFile()

    def switch_measured_data_direction_with_respect_to_face_width(self: Self):
        """Method does not return."""
        self.wrapped.SwitchMeasuredDataDirectionWithRespectToFaceWidth()

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
    def cast_to(
        self: Self,
    ) -> "CylindricalGearCommonFlankMicroGeometry._Cast_CylindricalGearCommonFlankMicroGeometry":
        return self._Cast_CylindricalGearCommonFlankMicroGeometry(self)
