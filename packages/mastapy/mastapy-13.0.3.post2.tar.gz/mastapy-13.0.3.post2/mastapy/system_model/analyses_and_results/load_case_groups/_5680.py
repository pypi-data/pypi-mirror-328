"""AbstractLoadCaseGroup"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_LOAD_CASE_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups",
    "AbstractLoadCaseGroup",
)

if TYPE_CHECKING:
    from mastapy.system_model import _2220
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4410
    from mastapy.system_model.analyses_and_results.static_loads import _6970, _6825
    from mastapy import _7580
    from mastapy.system_model.analyses_and_results.load_case_groups import (
        _5679,
        _5681,
        _5684,
        _5685,
        _5688,
        _5692,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractLoadCaseGroup",)


Self = TypeVar("Self", bound="AbstractLoadCaseGroup")


class AbstractLoadCaseGroup(_0.APIBase):
    """AbstractLoadCaseGroup

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_LOAD_CASE_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractLoadCaseGroup")

    class _Cast_AbstractLoadCaseGroup:
        """Special nested class for casting AbstractLoadCaseGroup to subclasses."""

        def __init__(
            self: "AbstractLoadCaseGroup._Cast_AbstractLoadCaseGroup",
            parent: "AbstractLoadCaseGroup",
        ):
            self._parent = parent

        @property
        def abstract_design_state_load_case_group(
            self: "AbstractLoadCaseGroup._Cast_AbstractLoadCaseGroup",
        ) -> "_5679.AbstractDesignStateLoadCaseGroup":
            from mastapy.system_model.analyses_and_results.load_case_groups import _5679

            return self._parent._cast(_5679.AbstractDesignStateLoadCaseGroup)

        @property
        def abstract_static_load_case_group(
            self: "AbstractLoadCaseGroup._Cast_AbstractLoadCaseGroup",
        ) -> "_5681.AbstractStaticLoadCaseGroup":
            from mastapy.system_model.analyses_and_results.load_case_groups import _5681

            return self._parent._cast(_5681.AbstractStaticLoadCaseGroup)

        @property
        def design_state(
            self: "AbstractLoadCaseGroup._Cast_AbstractLoadCaseGroup",
        ) -> "_5684.DesignState":
            from mastapy.system_model.analyses_and_results.load_case_groups import _5684

            return self._parent._cast(_5684.DesignState)

        @property
        def duty_cycle(
            self: "AbstractLoadCaseGroup._Cast_AbstractLoadCaseGroup",
        ) -> "_5685.DutyCycle":
            from mastapy.system_model.analyses_and_results.load_case_groups import _5685

            return self._parent._cast(_5685.DutyCycle)

        @property
        def sub_group_in_single_design_state(
            self: "AbstractLoadCaseGroup._Cast_AbstractLoadCaseGroup",
        ) -> "_5688.SubGroupInSingleDesignState":
            from mastapy.system_model.analyses_and_results.load_case_groups import _5688

            return self._parent._cast(_5688.SubGroupInSingleDesignState)

        @property
        def time_series_load_case_group(
            self: "AbstractLoadCaseGroup._Cast_AbstractLoadCaseGroup",
        ) -> "_5692.TimeSeriesLoadCaseGroup":
            from mastapy.system_model.analyses_and_results.load_case_groups import _5692

            return self._parent._cast(_5692.TimeSeriesLoadCaseGroup)

        @property
        def abstract_load_case_group(
            self: "AbstractLoadCaseGroup._Cast_AbstractLoadCaseGroup",
        ) -> "AbstractLoadCaseGroup":
            return self._parent

        def __getattr__(
            self: "AbstractLoadCaseGroup._Cast_AbstractLoadCaseGroup", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractLoadCaseGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def number_of_load_cases(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfLoadCases

        if temp is None:
            return 0.0

        return temp

    @property
    def total_duration(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TotalDuration

        if temp is None:
            return 0.0

        return temp

    @total_duration.setter
    @enforce_parameter_types
    def total_duration(self: Self, value: "float"):
        self.wrapped.TotalDuration = float(value) if value is not None else 0.0

    @property
    def model(self: Self) -> "_2220.Design":
        """mastapy.system_model.Design

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Model

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def parametric_analysis_options(self: Self) -> "_4410.ParametricStudyToolOptions":
        """mastapy.system_model.analyses_and_results.parametric_study_tools.ParametricStudyToolOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParametricAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def load_case_root_assemblies(self: Self) -> "List[_6970.RootAssemblyLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCaseRootAssemblies

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
    def create_load_cases(
        self: Self, number_of_load_cases: "int", token: "_7580.TaskProgress"
    ) -> "List[_6825.LoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.LoadCase]

        Args:
            number_of_load_cases (int)
            token (mastapy.TaskProgress)
        """
        number_of_load_cases = int(number_of_load_cases)
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.CreateLoadCases(
                number_of_load_cases if number_of_load_cases else 0,
                token.wrapped if token else None,
            )
        )

    def perform_pst(self: Self):
        """Method does not return."""
        self.wrapped.PerformPst()

    @enforce_parameter_types
    def perform_pst_with_progress(self: Self, progress: "_7580.TaskProgress"):
        """Method does not return.

        Args:
            progress (mastapy.TaskProgress)
        """
        self.wrapped.PerformPstWithProgress(progress.wrapped if progress else None)

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
    def cast_to(self: Self) -> "AbstractLoadCaseGroup._Cast_AbstractLoadCaseGroup":
        return self._Cast_AbstractLoadCaseGroup(self)
