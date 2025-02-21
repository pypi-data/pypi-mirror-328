"""MeshedCylindricalGearMicroGeometry"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MESHED_CYLINDRICAL_GEAR_MICRO_GEOMETRY = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "MeshedCylindricalGearMicroGeometry",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1120


__docformat__ = "restructuredtext en"
__all__ = ("MeshedCylindricalGearMicroGeometry",)


Self = TypeVar("Self", bound="MeshedCylindricalGearMicroGeometry")


class MeshedCylindricalGearMicroGeometry(_0.APIBase):
    """MeshedCylindricalGearMicroGeometry

    This is a mastapy class.
    """

    TYPE = _MESHED_CYLINDRICAL_GEAR_MICRO_GEOMETRY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MeshedCylindricalGearMicroGeometry")

    class _Cast_MeshedCylindricalGearMicroGeometry:
        """Special nested class for casting MeshedCylindricalGearMicroGeometry to subclasses."""

        def __init__(
            self: "MeshedCylindricalGearMicroGeometry._Cast_MeshedCylindricalGearMicroGeometry",
            parent: "MeshedCylindricalGearMicroGeometry",
        ):
            self._parent = parent

        @property
        def meshed_cylindrical_gear_micro_geometry(
            self: "MeshedCylindricalGearMicroGeometry._Cast_MeshedCylindricalGearMicroGeometry",
        ) -> "MeshedCylindricalGearMicroGeometry":
            return self._parent

        def __getattr__(
            self: "MeshedCylindricalGearMicroGeometry._Cast_MeshedCylindricalGearMicroGeometry",
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
        self: Self, instance_to_wrap: "MeshedCylindricalGearMicroGeometry.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def flanks(self: Self) -> "List[_1120.MeshedCylindricalGearFlankMicroGeometry]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.MeshedCylindricalGearFlankMicroGeometry]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Flanks

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
    def cast_to(
        self: Self,
    ) -> "MeshedCylindricalGearMicroGeometry._Cast_MeshedCylindricalGearMicroGeometry":
        return self._Cast_MeshedCylindricalGearMicroGeometry(self)
