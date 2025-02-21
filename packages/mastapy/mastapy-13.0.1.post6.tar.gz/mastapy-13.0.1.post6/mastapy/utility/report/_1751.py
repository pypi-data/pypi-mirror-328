"""CustomDrawing"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.report import _1752
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_DRAWING = python_net_import("SMT.MastaAPI.Utility.Report", "CustomDrawing")

if TYPE_CHECKING:
    from mastapy.utility.report import _1760, _1771, _1763


__docformat__ = "restructuredtext en"
__all__ = ("CustomDrawing",)


Self = TypeVar("Self", bound="CustomDrawing")


class CustomDrawing(_1752.CustomGraphic):
    """CustomDrawing

    This is a mastapy class.
    """

    TYPE = _CUSTOM_DRAWING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomDrawing")

    class _Cast_CustomDrawing:
        """Special nested class for casting CustomDrawing to subclasses."""

        def __init__(
            self: "CustomDrawing._Cast_CustomDrawing", parent: "CustomDrawing"
        ):
            self._parent = parent

        @property
        def custom_graphic(
            self: "CustomDrawing._Cast_CustomDrawing",
        ) -> "_1752.CustomGraphic":
            return self._parent._cast(_1752.CustomGraphic)

        @property
        def custom_report_definition_item(
            self: "CustomDrawing._Cast_CustomDrawing",
        ) -> "_1760.CustomReportDefinitionItem":
            from mastapy.utility.report import _1760

            return self._parent._cast(_1760.CustomReportDefinitionItem)

        @property
        def custom_report_nameable_item(
            self: "CustomDrawing._Cast_CustomDrawing",
        ) -> "_1771.CustomReportNameableItem":
            from mastapy.utility.report import _1771

            return self._parent._cast(_1771.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomDrawing._Cast_CustomDrawing",
        ) -> "_1763.CustomReportItem":
            from mastapy.utility.report import _1763

            return self._parent._cast(_1763.CustomReportItem)

        @property
        def custom_drawing(
            self: "CustomDrawing._Cast_CustomDrawing",
        ) -> "CustomDrawing":
            return self._parent

        def __getattr__(self: "CustomDrawing._Cast_CustomDrawing", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomDrawing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def show_editor(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowEditor

        if temp is None:
            return False

        return temp

    @show_editor.setter
    @enforce_parameter_types
    def show_editor(self: Self, value: "bool"):
        self.wrapped.ShowEditor = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "CustomDrawing._Cast_CustomDrawing":
        return self._Cast_CustomDrawing(self)
