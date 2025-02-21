"""DegreeOfFreedomBoundaryCondition"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DEGREE_OF_FREEDOM_BOUNDARY_CONDITION = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "DegreeOfFreedomBoundaryCondition"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe import _2371, _2372


__docformat__ = "restructuredtext en"
__all__ = ("DegreeOfFreedomBoundaryCondition",)


Self = TypeVar("Self", bound="DegreeOfFreedomBoundaryCondition")


class DegreeOfFreedomBoundaryCondition(_0.APIBase):
    """DegreeOfFreedomBoundaryCondition

    This is a mastapy class.
    """

    TYPE = _DEGREE_OF_FREEDOM_BOUNDARY_CONDITION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DegreeOfFreedomBoundaryCondition")

    class _Cast_DegreeOfFreedomBoundaryCondition:
        """Special nested class for casting DegreeOfFreedomBoundaryCondition to subclasses."""

        def __init__(
            self: "DegreeOfFreedomBoundaryCondition._Cast_DegreeOfFreedomBoundaryCondition",
            parent: "DegreeOfFreedomBoundaryCondition",
        ):
            self._parent = parent

        @property
        def degree_of_freedom_boundary_condition_angular(
            self: "DegreeOfFreedomBoundaryCondition._Cast_DegreeOfFreedomBoundaryCondition",
        ) -> "_2371.DegreeOfFreedomBoundaryConditionAngular":
            from mastapy.system_model.fe import _2371

            return self._parent._cast(_2371.DegreeOfFreedomBoundaryConditionAngular)

        @property
        def degree_of_freedom_boundary_condition_linear(
            self: "DegreeOfFreedomBoundaryCondition._Cast_DegreeOfFreedomBoundaryCondition",
        ) -> "_2372.DegreeOfFreedomBoundaryConditionLinear":
            from mastapy.system_model.fe import _2372

            return self._parent._cast(_2372.DegreeOfFreedomBoundaryConditionLinear)

        @property
        def degree_of_freedom_boundary_condition(
            self: "DegreeOfFreedomBoundaryCondition._Cast_DegreeOfFreedomBoundaryCondition",
        ) -> "DegreeOfFreedomBoundaryCondition":
            return self._parent

        def __getattr__(
            self: "DegreeOfFreedomBoundaryCondition._Cast_DegreeOfFreedomBoundaryCondition",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DegreeOfFreedomBoundaryCondition.TYPE"):
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
    def phase(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Phase

        if temp is None:
            return 0.0

        return temp

    @phase.setter
    @enforce_parameter_types
    def phase(self: Self, value: "float"):
        self.wrapped.Phase = float(value) if value is not None else 0.0

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
    ) -> "DegreeOfFreedomBoundaryCondition._Cast_DegreeOfFreedomBoundaryCondition":
        return self._Cast_DegreeOfFreedomBoundaryCondition(self)
