"""ResultsForOrder"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESULTS_FOR_ORDER = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "ResultsForOrder",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5860,
        _5870,
        _5871,
        _5872,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ResultsForOrder",)


Self = TypeVar("Self", bound="ResultsForOrder")


class ResultsForOrder(_0.APIBase):
    """ResultsForOrder

    This is a mastapy class.
    """

    TYPE = _RESULTS_FOR_ORDER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ResultsForOrder")

    class _Cast_ResultsForOrder:
        """Special nested class for casting ResultsForOrder to subclasses."""

        def __init__(
            self: "ResultsForOrder._Cast_ResultsForOrder", parent: "ResultsForOrder"
        ):
            self._parent = parent

        @property
        def results_for_order_including_groups(
            self: "ResultsForOrder._Cast_ResultsForOrder",
        ) -> "_5870.ResultsForOrderIncludingGroups":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
                _5870,
            )

            return self._parent._cast(_5870.ResultsForOrderIncludingGroups)

        @property
        def results_for_order_including_nodes(
            self: "ResultsForOrder._Cast_ResultsForOrder",
        ) -> "_5871.ResultsForOrderIncludingNodes":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
                _5871,
            )

            return self._parent._cast(_5871.ResultsForOrderIncludingNodes)

        @property
        def results_for_order_including_surfaces(
            self: "ResultsForOrder._Cast_ResultsForOrder",
        ) -> "_5872.ResultsForOrderIncludingSurfaces":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
                _5872,
            )

            return self._parent._cast(_5872.ResultsForOrderIncludingSurfaces)

        @property
        def results_for_order(
            self: "ResultsForOrder._Cast_ResultsForOrder",
        ) -> "ResultsForOrder":
            return self._parent

        def __getattr__(self: "ResultsForOrder._Cast_ResultsForOrder", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ResultsForOrder.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitations_description(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcitationsDescription

        if temp is None:
            return ""

        return temp

    @property
    def harmonics(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Harmonics

        if temp is None:
            return ""

        return temp

    @property
    def order(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Order

        if temp is None:
            return ""

        return temp

    @property
    def component(
        self: Self,
    ) -> "_5860.HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Component

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
    def cast_to(self: Self) -> "ResultsForOrder._Cast_ResultsForOrder":
        return self._Cast_ResultsForOrder(self)
