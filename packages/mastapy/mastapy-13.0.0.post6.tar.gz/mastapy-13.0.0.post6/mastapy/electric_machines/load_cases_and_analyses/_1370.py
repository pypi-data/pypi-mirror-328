"""SlotDetailForAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SLOT_DETAIL_FOR_ANALYSIS = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "SlotDetailForAnalysis"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1297


__docformat__ = "restructuredtext en"
__all__ = ("SlotDetailForAnalysis",)


Self = TypeVar("Self", bound="SlotDetailForAnalysis")


class SlotDetailForAnalysis(_0.APIBase):
    """SlotDetailForAnalysis

    This is a mastapy class.
    """

    TYPE = _SLOT_DETAIL_FOR_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SlotDetailForAnalysis")

    class _Cast_SlotDetailForAnalysis:
        """Special nested class for casting SlotDetailForAnalysis to subclasses."""

        def __init__(
            self: "SlotDetailForAnalysis._Cast_SlotDetailForAnalysis",
            parent: "SlotDetailForAnalysis",
        ):
            self._parent = parent

        @property
        def slot_detail_for_analysis(
            self: "SlotDetailForAnalysis._Cast_SlotDetailForAnalysis",
        ) -> "SlotDetailForAnalysis":
            return self._parent

        def __getattr__(
            self: "SlotDetailForAnalysis._Cast_SlotDetailForAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SlotDetailForAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def d_axis_current_density_conductors(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DAxisCurrentDensityConductors

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_current_density_slot(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DAxisCurrentDensitySlot

        if temp is None:
            return 0.0

        return temp

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
    def peak_current_density_conductors(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakCurrentDensityConductors

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_current_density_slot(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakCurrentDensitySlot

        if temp is None:
            return 0.0

        return temp

    @property
    def q_axis_current_density_conductors(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.QAxisCurrentDensityConductors

        if temp is None:
            return 0.0

        return temp

    @property
    def q_axis_current_density_slot(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.QAxisCurrentDensitySlot

        if temp is None:
            return 0.0

        return temp

    @property
    def rms_current_density_conductors(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RMSCurrentDensityConductors

        if temp is None:
            return 0.0

        return temp

    @property
    def rms_current_density_slot(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RMSCurrentDensitySlot

        if temp is None:
            return 0.0

        return temp

    @property
    def slot_section_details(self: Self) -> "_1297.SlotSectionDetail":
        """mastapy.electric_machines.SlotSectionDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlotSectionDetails

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
    def cast_to(self: Self) -> "SlotDetailForAnalysis._Cast_SlotDetailForAnalysis":
        return self._Cast_SlotDetailForAnalysis(self)
