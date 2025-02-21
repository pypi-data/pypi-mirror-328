"""OrderForTE"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ORDER_FOR_TE = python_net_import(
    "SMT.MastaAPI.Utility.ModalAnalysis.Gears", "OrderForTE"
)

if TYPE_CHECKING:
    from mastapy.utility.modal_analysis.gears import (
        _1815,
        _1816,
        _1818,
        _1819,
        _1821,
        _1822,
        _1823,
        _1824,
        _1825,
    )


__docformat__ = "restructuredtext en"
__all__ = ("OrderForTE",)


Self = TypeVar("Self", bound="OrderForTE")


class OrderForTE(_0.APIBase):
    """OrderForTE

    This is a mastapy class.
    """

    TYPE = _ORDER_FOR_TE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OrderForTE")

    class _Cast_OrderForTE:
        """Special nested class for casting OrderForTE to subclasses."""

        def __init__(self: "OrderForTE._Cast_OrderForTE", parent: "OrderForTE"):
            self._parent = parent

        @property
        def gear_mesh_for_te(
            self: "OrderForTE._Cast_OrderForTE",
        ) -> "_1815.GearMeshForTE":
            from mastapy.utility.modal_analysis.gears import _1815

            return self._parent._cast(_1815.GearMeshForTE)

        @property
        def gear_order_for_te(
            self: "OrderForTE._Cast_OrderForTE",
        ) -> "_1816.GearOrderForTE":
            from mastapy.utility.modal_analysis.gears import _1816

            return self._parent._cast(_1816.GearOrderForTE)

        @property
        def harmonic_order_for_te(
            self: "OrderForTE._Cast_OrderForTE",
        ) -> "_1818.HarmonicOrderForTE":
            from mastapy.utility.modal_analysis.gears import _1818

            return self._parent._cast(_1818.HarmonicOrderForTE)

        @property
        def label_only_order(
            self: "OrderForTE._Cast_OrderForTE",
        ) -> "_1819.LabelOnlyOrder":
            from mastapy.utility.modal_analysis.gears import _1819

            return self._parent._cast(_1819.LabelOnlyOrder)

        @property
        def order_selector(
            self: "OrderForTE._Cast_OrderForTE",
        ) -> "_1821.OrderSelector":
            from mastapy.utility.modal_analysis.gears import _1821

            return self._parent._cast(_1821.OrderSelector)

        @property
        def order_with_radius(
            self: "OrderForTE._Cast_OrderForTE",
        ) -> "_1822.OrderWithRadius":
            from mastapy.utility.modal_analysis.gears import _1822

            return self._parent._cast(_1822.OrderWithRadius)

        @property
        def rolling_bearing_order(
            self: "OrderForTE._Cast_OrderForTE",
        ) -> "_1823.RollingBearingOrder":
            from mastapy.utility.modal_analysis.gears import _1823

            return self._parent._cast(_1823.RollingBearingOrder)

        @property
        def shaft_order_for_te(
            self: "OrderForTE._Cast_OrderForTE",
        ) -> "_1824.ShaftOrderForTE":
            from mastapy.utility.modal_analysis.gears import _1824

            return self._parent._cast(_1824.ShaftOrderForTE)

        @property
        def user_defined_order_for_te(
            self: "OrderForTE._Cast_OrderForTE",
        ) -> "_1825.UserDefinedOrderForTE":
            from mastapy.utility.modal_analysis.gears import _1825

            return self._parent._cast(_1825.UserDefinedOrderForTE)

        @property
        def order_for_te(self: "OrderForTE._Cast_OrderForTE") -> "OrderForTE":
            return self._parent

        def __getattr__(self: "OrderForTE._Cast_OrderForTE", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OrderForTE.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def frequency_offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FrequencyOffset

        if temp is None:
            return 0.0

        return temp

    @frequency_offset.setter
    @enforce_parameter_types
    def frequency_offset(self: Self, value: "float"):
        self.wrapped.FrequencyOffset = float(value) if value is not None else 0.0

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
    def order(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Order

        if temp is None:
            return 0.0

        return temp

    @property
    def children(self: Self) -> "List[OrderForTE]":
        """List[mastapy.utility.modal_analysis.gears.OrderForTE]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Children

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
    def cast_to(self: Self) -> "OrderForTE._Cast_OrderForTE":
        return self._Cast_OrderForTE(self)
