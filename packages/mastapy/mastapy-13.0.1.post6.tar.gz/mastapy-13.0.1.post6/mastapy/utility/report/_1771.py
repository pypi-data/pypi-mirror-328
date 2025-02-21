"""CustomReportNameableItem"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.report import _1763
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_NAMEABLE_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportNameableItem"
)

if TYPE_CHECKING:
    from mastapy.shafts import _20
    from mastapy.gears.gear_designs.cylindrical import _1035
    from mastapy.utility.report import (
        _1742,
        _1750,
        _1751,
        _1752,
        _1753,
        _1755,
        _1756,
        _1760,
        _1762,
        _1769,
        _1770,
        _1772,
        _1774,
        _1777,
        _1779,
        _1780,
        _1782,
    )
    from mastapy.utility_gui.charts import _1854, _1855
    from mastapy.bearings.bearing_results import _1946, _1947, _1950, _1958
    from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
        _2849,
    )
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4386
    from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
        _4717,
        _4721,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportNameableItem",)


Self = TypeVar("Self", bound="CustomReportNameableItem")


class CustomReportNameableItem(_1763.CustomReportItem):
    """CustomReportNameableItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_NAMEABLE_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportNameableItem")

    class _Cast_CustomReportNameableItem:
        """Special nested class for casting CustomReportNameableItem to subclasses."""

        def __init__(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
            parent: "CustomReportNameableItem",
        ):
            self._parent = parent

        @property
        def custom_report_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1763.CustomReportItem":
            return self._parent._cast(_1763.CustomReportItem)

        @property
        def shaft_damage_results_table_and_chart(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_20.ShaftDamageResultsTableAndChart":
            from mastapy.shafts import _20

            return self._parent._cast(_20.ShaftDamageResultsTableAndChart)

        @property
        def cylindrical_gear_table_with_mg_charts(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1035.CylindricalGearTableWithMGCharts":
            from mastapy.gears.gear_designs.cylindrical import _1035

            return self._parent._cast(_1035.CylindricalGearTableWithMGCharts)

        @property
        def ad_hoc_custom_table(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1742.AdHocCustomTable":
            from mastapy.utility.report import _1742

            return self._parent._cast(_1742.AdHocCustomTable)

        @property
        def custom_chart(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1750.CustomChart":
            from mastapy.utility.report import _1750

            return self._parent._cast(_1750.CustomChart)

        @property
        def custom_drawing(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1751.CustomDrawing":
            from mastapy.utility.report import _1751

            return self._parent._cast(_1751.CustomDrawing)

        @property
        def custom_graphic(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1752.CustomGraphic":
            from mastapy.utility.report import _1752

            return self._parent._cast(_1752.CustomGraphic)

        @property
        def custom_image(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1753.CustomImage":
            from mastapy.utility.report import _1753

            return self._parent._cast(_1753.CustomImage)

        @property
        def custom_report_cad_drawing(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1755.CustomReportCadDrawing":
            from mastapy.utility.report import _1755

            return self._parent._cast(_1755.CustomReportCadDrawing)

        @property
        def custom_report_chart(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1756.CustomReportChart":
            from mastapy.utility.report import _1756

            return self._parent._cast(_1756.CustomReportChart)

        @property
        def custom_report_definition_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1760.CustomReportDefinitionItem":
            from mastapy.utility.report import _1760

            return self._parent._cast(_1760.CustomReportDefinitionItem)

        @property
        def custom_report_html_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1762.CustomReportHtmlItem":
            from mastapy.utility.report import _1762

            return self._parent._cast(_1762.CustomReportHtmlItem)

        @property
        def custom_report_multi_property_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1769.CustomReportMultiPropertyItem":
            from mastapy.utility.report import _1769

            return self._parent._cast(_1769.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1770.CustomReportMultiPropertyItemBase":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_named_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1772.CustomReportNamedItem":
            from mastapy.utility.report import _1772

            return self._parent._cast(_1772.CustomReportNamedItem)

        @property
        def custom_report_status_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1774.CustomReportStatusItem":
            from mastapy.utility.report import _1774

            return self._parent._cast(_1774.CustomReportStatusItem)

        @property
        def custom_report_text(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1777.CustomReportText":
            from mastapy.utility.report import _1777

            return self._parent._cast(_1777.CustomReportText)

        @property
        def custom_sub_report(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1779.CustomSubReport":
            from mastapy.utility.report import _1779

            return self._parent._cast(_1779.CustomSubReport)

        @property
        def custom_table(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1780.CustomTable":
            from mastapy.utility.report import _1780

            return self._parent._cast(_1780.CustomTable)

        @property
        def dynamic_custom_report_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1782.DynamicCustomReportItem":
            from mastapy.utility.report import _1782

            return self._parent._cast(_1782.DynamicCustomReportItem)

        @property
        def custom_line_chart(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1854.CustomLineChart":
            from mastapy.utility_gui.charts import _1854

            return self._parent._cast(_1854.CustomLineChart)

        @property
        def custom_table_and_chart(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1855.CustomTableAndChart":
            from mastapy.utility_gui.charts import _1855

            return self._parent._cast(_1855.CustomTableAndChart)

        @property
        def loaded_ball_element_chart_reporter(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1946.LoadedBallElementChartReporter":
            from mastapy.bearings.bearing_results import _1946

            return self._parent._cast(_1946.LoadedBallElementChartReporter)

        @property
        def loaded_bearing_chart_reporter(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1947.LoadedBearingChartReporter":
            from mastapy.bearings.bearing_results import _1947

            return self._parent._cast(_1947.LoadedBearingChartReporter)

        @property
        def loaded_bearing_temperature_chart(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1950.LoadedBearingTemperatureChart":
            from mastapy.bearings.bearing_results import _1950

            return self._parent._cast(_1950.LoadedBearingTemperatureChart)

        @property
        def loaded_roller_element_chart_reporter(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_1958.LoadedRollerElementChartReporter":
            from mastapy.bearings.bearing_results import _1958

            return self._parent._cast(_1958.LoadedRollerElementChartReporter)

        @property
        def shaft_system_deflection_sections_report(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_2849.ShaftSystemDeflectionSectionsReport":
            from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
                _2849,
            )

            return self._parent._cast(_2849.ShaftSystemDeflectionSectionsReport)

        @property
        def parametric_study_histogram(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_4386.ParametricStudyHistogram":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4386,
            )

            return self._parent._cast(_4386.ParametricStudyHistogram)

        @property
        def campbell_diagram_report(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_4717.CampbellDiagramReport":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4717,
            )

            return self._parent._cast(_4717.CampbellDiagramReport)

        @property
        def per_mode_results_report(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "_4721.PerModeResultsReport":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4721,
            )

            return self._parent._cast(_4721.PerModeResultsReport)

        @property
        def custom_report_nameable_item(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem",
        ) -> "CustomReportNameableItem":
            return self._parent

        def __getattr__(
            self: "CustomReportNameableItem._Cast_CustomReportNameableItem", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportNameableItem.TYPE"):
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
    def x_position_for_cad(self: Self) -> "float":
        """float"""
        temp = self.wrapped.XPositionForCAD

        if temp is None:
            return 0.0

        return temp

    @x_position_for_cad.setter
    @enforce_parameter_types
    def x_position_for_cad(self: Self, value: "float"):
        self.wrapped.XPositionForCAD = float(value) if value is not None else 0.0

    @property
    def y_position_for_cad(self: Self) -> "float":
        """float"""
        temp = self.wrapped.YPositionForCAD

        if temp is None:
            return 0.0

        return temp

    @y_position_for_cad.setter
    @enforce_parameter_types
    def y_position_for_cad(self: Self, value: "float"):
        self.wrapped.YPositionForCAD = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "CustomReportNameableItem._Cast_CustomReportNameableItem":
        return self._Cast_CustomReportNameableItem(self)
