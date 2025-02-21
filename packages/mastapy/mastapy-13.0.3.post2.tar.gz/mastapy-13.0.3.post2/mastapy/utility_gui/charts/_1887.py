"""TwoDChartDefinition"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.utility_gui.charts import _1879
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TWO_D_CHART_DEFINITION = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Charts", "TwoDChartDefinition"
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1873, _1883, _1872, _1877, _1880, _1882
    from mastapy.utility.report import _1766


__docformat__ = "restructuredtext en"
__all__ = ("TwoDChartDefinition",)


Self = TypeVar("Self", bound="TwoDChartDefinition")


class TwoDChartDefinition(_1879.NDChartDefinition):
    """TwoDChartDefinition

    This is a mastapy class.
    """

    TYPE = _TWO_D_CHART_DEFINITION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TwoDChartDefinition")

    class _Cast_TwoDChartDefinition:
        """Special nested class for casting TwoDChartDefinition to subclasses."""

        def __init__(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
            parent: "TwoDChartDefinition",
        ):
            self._parent = parent

        @property
        def nd_chart_definition(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
        ) -> "_1879.NDChartDefinition":
            return self._parent._cast(_1879.NDChartDefinition)

        @property
        def chart_definition(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
        ) -> "_1766.ChartDefinition":
            from mastapy.utility.report import _1766

            return self._parent._cast(_1766.ChartDefinition)

        @property
        def bubble_chart_definition(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
        ) -> "_1872.BubbleChartDefinition":
            from mastapy.utility_gui.charts import _1872

            return self._parent._cast(_1872.BubbleChartDefinition)

        @property
        def matrix_visualisation_definition(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
        ) -> "_1877.MatrixVisualisationDefinition":
            from mastapy.utility_gui.charts import _1877

            return self._parent._cast(_1877.MatrixVisualisationDefinition)

        @property
        def parallel_coordinates_chart_definition(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
        ) -> "_1880.ParallelCoordinatesChartDefinition":
            from mastapy.utility_gui.charts import _1880

            return self._parent._cast(_1880.ParallelCoordinatesChartDefinition)

        @property
        def scatter_chart_definition(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
        ) -> "_1882.ScatterChartDefinition":
            from mastapy.utility_gui.charts import _1882

            return self._parent._cast(_1882.ScatterChartDefinition)

        @property
        def two_d_chart_definition(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition",
        ) -> "TwoDChartDefinition":
            return self._parent

        def __getattr__(
            self: "TwoDChartDefinition._Cast_TwoDChartDefinition", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TwoDChartDefinition.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def const_lines(self: Self) -> "List[_1873.ConstantLine]":
        """List[mastapy.utility_gui.charts.ConstantLine]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConstLines

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def series_list(self: Self) -> "List[_1883.Series2D]":
        """List[mastapy.utility_gui.charts.Series2D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SeriesList

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "TwoDChartDefinition._Cast_TwoDChartDefinition":
        return self._Cast_TwoDChartDefinition(self)
