"""ParetoOptimisationStrategyBars"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_OPTIMISATION_STRATEGY_BARS = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "ParetoOptimisationStrategyBars"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_set_pareto_optimiser import _902


__docformat__ = "restructuredtext en"
__all__ = ("ParetoOptimisationStrategyBars",)


Self = TypeVar("Self", bound="ParetoOptimisationStrategyBars")


class ParetoOptimisationStrategyBars(_0.APIBase):
    """ParetoOptimisationStrategyBars

    This is a mastapy class.
    """

    TYPE = _PARETO_OPTIMISATION_STRATEGY_BARS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ParetoOptimisationStrategyBars")

    class _Cast_ParetoOptimisationStrategyBars:
        """Special nested class for casting ParetoOptimisationStrategyBars to subclasses."""

        def __init__(
            self: "ParetoOptimisationStrategyBars._Cast_ParetoOptimisationStrategyBars",
            parent: "ParetoOptimisationStrategyBars",
        ):
            self._parent = parent

        @property
        def bar_for_pareto(
            self: "ParetoOptimisationStrategyBars._Cast_ParetoOptimisationStrategyBars",
        ) -> "_902.BarForPareto":
            from mastapy.gears.gear_set_pareto_optimiser import _902

            return self._parent._cast(_902.BarForPareto)

        @property
        def pareto_optimisation_strategy_bars(
            self: "ParetoOptimisationStrategyBars._Cast_ParetoOptimisationStrategyBars",
        ) -> "ParetoOptimisationStrategyBars":
            return self._parent

        def __getattr__(
            self: "ParetoOptimisationStrategyBars._Cast_ParetoOptimisationStrategyBars",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ParetoOptimisationStrategyBars.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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

    def remove_bar(self: Self):
        """Method does not return."""
        self.wrapped.RemoveBar()

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
    ) -> "ParetoOptimisationStrategyBars._Cast_ParetoOptimisationStrategyBars":
        return self._Cast_ParetoOptimisationStrategyBars(self)
