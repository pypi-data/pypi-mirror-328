"""CustomGraphic"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.report import _1760
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_GRAPHIC = python_net_import("SMT.MastaAPI.Utility.Report", "CustomGraphic")

if TYPE_CHECKING:
    from mastapy.utility.report import _1750, _1751, _1753, _1771, _1763
    from mastapy.bearings.bearing_results import _1947


__docformat__ = "restructuredtext en"
__all__ = ("CustomGraphic",)


Self = TypeVar("Self", bound="CustomGraphic")


class CustomGraphic(_1760.CustomReportDefinitionItem):
    """CustomGraphic

    This is a mastapy class.
    """

    TYPE = _CUSTOM_GRAPHIC
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomGraphic")

    class _Cast_CustomGraphic:
        """Special nested class for casting CustomGraphic to subclasses."""

        def __init__(
            self: "CustomGraphic._Cast_CustomGraphic", parent: "CustomGraphic"
        ):
            self._parent = parent

        @property
        def custom_report_definition_item(
            self: "CustomGraphic._Cast_CustomGraphic",
        ) -> "_1760.CustomReportDefinitionItem":
            return self._parent._cast(_1760.CustomReportDefinitionItem)

        @property
        def custom_report_nameable_item(
            self: "CustomGraphic._Cast_CustomGraphic",
        ) -> "_1771.CustomReportNameableItem":
            from mastapy.utility.report import _1771

            return self._parent._cast(_1771.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomGraphic._Cast_CustomGraphic",
        ) -> "_1763.CustomReportItem":
            from mastapy.utility.report import _1763

            return self._parent._cast(_1763.CustomReportItem)

        @property
        def custom_chart(
            self: "CustomGraphic._Cast_CustomGraphic",
        ) -> "_1750.CustomChart":
            from mastapy.utility.report import _1750

            return self._parent._cast(_1750.CustomChart)

        @property
        def custom_drawing(
            self: "CustomGraphic._Cast_CustomGraphic",
        ) -> "_1751.CustomDrawing":
            from mastapy.utility.report import _1751

            return self._parent._cast(_1751.CustomDrawing)

        @property
        def custom_image(
            self: "CustomGraphic._Cast_CustomGraphic",
        ) -> "_1753.CustomImage":
            from mastapy.utility.report import _1753

            return self._parent._cast(_1753.CustomImage)

        @property
        def loaded_bearing_chart_reporter(
            self: "CustomGraphic._Cast_CustomGraphic",
        ) -> "_1947.LoadedBearingChartReporter":
            from mastapy.bearings.bearing_results import _1947

            return self._parent._cast(_1947.LoadedBearingChartReporter)

        @property
        def custom_graphic(
            self: "CustomGraphic._Cast_CustomGraphic",
        ) -> "CustomGraphic":
            return self._parent

        def __getattr__(self: "CustomGraphic._Cast_CustomGraphic", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomGraphic.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def height(self: Self) -> "int":
        """int"""
        temp = self.wrapped.Height

        if temp is None:
            return 0

        return temp

    @height.setter
    @enforce_parameter_types
    def height(self: Self, value: "int"):
        self.wrapped.Height = int(value) if value is not None else 0

    @property
    def height_for_cad(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HeightForCAD

        if temp is None:
            return 0.0

        return temp

    @height_for_cad.setter
    @enforce_parameter_types
    def height_for_cad(self: Self, value: "float"):
        self.wrapped.HeightForCAD = float(value) if value is not None else 0.0

    @property
    def transposed(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.Transposed

        if temp is None:
            return False

        return temp

    @transposed.setter
    @enforce_parameter_types
    def transposed(self: Self, value: "bool"):
        self.wrapped.Transposed = bool(value) if value is not None else False

    @property
    def width(self: Self) -> "int":
        """int"""
        temp = self.wrapped.Width

        if temp is None:
            return 0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "int"):
        self.wrapped.Width = int(value) if value is not None else 0

    @property
    def width_for_cad(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WidthForCAD

        if temp is None:
            return 0.0

        return temp

    @width_for_cad.setter
    @enforce_parameter_types
    def width_for_cad(self: Self, value: "float"):
        self.wrapped.WidthForCAD = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "CustomGraphic._Cast_CustomGraphic":
        return self._Cast_CustomGraphic(self)
