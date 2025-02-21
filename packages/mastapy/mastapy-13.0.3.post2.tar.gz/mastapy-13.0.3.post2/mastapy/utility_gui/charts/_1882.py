"""ScatterChartDefinition"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.utility_gui.charts import _1887
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SCATTER_CHART_DEFINITION = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Charts", "ScatterChartDefinition"
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1872, _1879
    from mastapy.utility.report import _1766


__docformat__ = "restructuredtext en"
__all__ = ("ScatterChartDefinition",)


Self = TypeVar("Self", bound="ScatterChartDefinition")


class ScatterChartDefinition(_1887.TwoDChartDefinition):
    """ScatterChartDefinition

    This is a mastapy class.
    """

    TYPE = _SCATTER_CHART_DEFINITION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ScatterChartDefinition")

    class _Cast_ScatterChartDefinition:
        """Special nested class for casting ScatterChartDefinition to subclasses."""

        def __init__(
            self: "ScatterChartDefinition._Cast_ScatterChartDefinition",
            parent: "ScatterChartDefinition",
        ):
            self._parent = parent

        @property
        def two_d_chart_definition(
            self: "ScatterChartDefinition._Cast_ScatterChartDefinition",
        ) -> "_1887.TwoDChartDefinition":
            return self._parent._cast(_1887.TwoDChartDefinition)

        @property
        def nd_chart_definition(
            self: "ScatterChartDefinition._Cast_ScatterChartDefinition",
        ) -> "_1879.NDChartDefinition":
            from mastapy.utility_gui.charts import _1879

            return self._parent._cast(_1879.NDChartDefinition)

        @property
        def chart_definition(
            self: "ScatterChartDefinition._Cast_ScatterChartDefinition",
        ) -> "_1766.ChartDefinition":
            from mastapy.utility.report import _1766

            return self._parent._cast(_1766.ChartDefinition)

        @property
        def bubble_chart_definition(
            self: "ScatterChartDefinition._Cast_ScatterChartDefinition",
        ) -> "_1872.BubbleChartDefinition":
            from mastapy.utility_gui.charts import _1872

            return self._parent._cast(_1872.BubbleChartDefinition)

        @property
        def scatter_chart_definition(
            self: "ScatterChartDefinition._Cast_ScatterChartDefinition",
        ) -> "ScatterChartDefinition":
            return self._parent

        def __getattr__(
            self: "ScatterChartDefinition._Cast_ScatterChartDefinition", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ScatterChartDefinition.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def x_values(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.XValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def y_values(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def z_axis_title(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZAxisTitle

        if temp is None:
            return ""

        return temp

    @property
    def z_values(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ScatterChartDefinition._Cast_ScatterChartDefinition":
        return self._Cast_ScatterChartDefinition(self)
