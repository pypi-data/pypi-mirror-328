"""NodeBoundaryConditionStaticAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODE_BOUNDARY_CONDITION_STATIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "NodeBoundaryConditionStaticAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe import _2371, _2372


__docformat__ = "restructuredtext en"
__all__ = ("NodeBoundaryConditionStaticAnalysis",)


Self = TypeVar("Self", bound="NodeBoundaryConditionStaticAnalysis")


class NodeBoundaryConditionStaticAnalysis(_0.APIBase):
    """NodeBoundaryConditionStaticAnalysis

    This is a mastapy class.
    """

    TYPE = _NODE_BOUNDARY_CONDITION_STATIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NodeBoundaryConditionStaticAnalysis")

    class _Cast_NodeBoundaryConditionStaticAnalysis:
        """Special nested class for casting NodeBoundaryConditionStaticAnalysis to subclasses."""

        def __init__(
            self: "NodeBoundaryConditionStaticAnalysis._Cast_NodeBoundaryConditionStaticAnalysis",
            parent: "NodeBoundaryConditionStaticAnalysis",
        ):
            self._parent = parent

        @property
        def node_boundary_condition_static_analysis(
            self: "NodeBoundaryConditionStaticAnalysis._Cast_NodeBoundaryConditionStaticAnalysis",
        ) -> "NodeBoundaryConditionStaticAnalysis":
            return self._parent

        def __getattr__(
            self: "NodeBoundaryConditionStaticAnalysis._Cast_NodeBoundaryConditionStaticAnalysis",
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
        self: Self, instance_to_wrap: "NodeBoundaryConditionStaticAnalysis.TYPE"
    ):
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
    def boundary_conditions_angular(
        self: Self,
    ) -> "List[_2371.DegreeOfFreedomBoundaryConditionAngular]":
        """List[mastapy.system_model.fe.DegreeOfFreedomBoundaryConditionAngular]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BoundaryConditionsAngular

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def boundary_conditions_linear(
        self: Self,
    ) -> "List[_2372.DegreeOfFreedomBoundaryConditionLinear]":
        """List[mastapy.system_model.fe.DegreeOfFreedomBoundaryConditionLinear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BoundaryConditionsLinear

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

    def ground_all_degrees_of_freedom(self: Self):
        """Method does not return."""
        self.wrapped.GroundAllDegreesOfFreedom()

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
    ) -> (
        "NodeBoundaryConditionStaticAnalysis._Cast_NodeBoundaryConditionStaticAnalysis"
    ):
        return self._Cast_NodeBoundaryConditionStaticAnalysis(self)
