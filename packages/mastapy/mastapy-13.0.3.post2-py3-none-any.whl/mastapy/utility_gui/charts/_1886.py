"""ThreeDVectorChartDefinition"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility_gui.charts import _1879
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_THREE_D_VECTOR_CHART_DEFINITION = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Charts", "ThreeDVectorChartDefinition"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1766


__docformat__ = "restructuredtext en"
__all__ = ("ThreeDVectorChartDefinition",)


Self = TypeVar("Self", bound="ThreeDVectorChartDefinition")


class ThreeDVectorChartDefinition(_1879.NDChartDefinition):
    """ThreeDVectorChartDefinition

    This is a mastapy class.
    """

    TYPE = _THREE_D_VECTOR_CHART_DEFINITION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ThreeDVectorChartDefinition")

    class _Cast_ThreeDVectorChartDefinition:
        """Special nested class for casting ThreeDVectorChartDefinition to subclasses."""

        def __init__(
            self: "ThreeDVectorChartDefinition._Cast_ThreeDVectorChartDefinition",
            parent: "ThreeDVectorChartDefinition",
        ):
            self._parent = parent

        @property
        def nd_chart_definition(
            self: "ThreeDVectorChartDefinition._Cast_ThreeDVectorChartDefinition",
        ) -> "_1879.NDChartDefinition":
            return self._parent._cast(_1879.NDChartDefinition)

        @property
        def chart_definition(
            self: "ThreeDVectorChartDefinition._Cast_ThreeDVectorChartDefinition",
        ) -> "_1766.ChartDefinition":
            from mastapy.utility.report import _1766

            return self._parent._cast(_1766.ChartDefinition)

        @property
        def three_d_vector_chart_definition(
            self: "ThreeDVectorChartDefinition._Cast_ThreeDVectorChartDefinition",
        ) -> "ThreeDVectorChartDefinition":
            return self._parent

        def __getattr__(
            self: "ThreeDVectorChartDefinition._Cast_ThreeDVectorChartDefinition",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ThreeDVectorChartDefinition.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ThreeDVectorChartDefinition._Cast_ThreeDVectorChartDefinition":
        return self._Cast_ThreeDVectorChartDefinition(self)
