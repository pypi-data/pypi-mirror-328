"""LoadedPlainOilFedJournalBearing"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.fluid_film import _2122
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_PLAIN_OIL_FED_JOURNAL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.FluidFilm", "LoadedPlainOilFedJournalBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.fluid_film import _2119
    from mastapy.bearings.bearing_results import _1954, _1957, _1949
    from mastapy.bearings import _1875


__docformat__ = "restructuredtext en"
__all__ = ("LoadedPlainOilFedJournalBearing",)


Self = TypeVar("Self", bound="LoadedPlainOilFedJournalBearing")


class LoadedPlainOilFedJournalBearing(_2122.LoadedPlainJournalBearingResults):
    """LoadedPlainOilFedJournalBearing

    This is a mastapy class.
    """

    TYPE = _LOADED_PLAIN_OIL_FED_JOURNAL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedPlainOilFedJournalBearing")

    class _Cast_LoadedPlainOilFedJournalBearing:
        """Special nested class for casting LoadedPlainOilFedJournalBearing to subclasses."""

        def __init__(
            self: "LoadedPlainOilFedJournalBearing._Cast_LoadedPlainOilFedJournalBearing",
            parent: "LoadedPlainOilFedJournalBearing",
        ):
            self._parent = parent

        @property
        def loaded_plain_journal_bearing_results(
            self: "LoadedPlainOilFedJournalBearing._Cast_LoadedPlainOilFedJournalBearing",
        ) -> "_2122.LoadedPlainJournalBearingResults":
            return self._parent._cast(_2122.LoadedPlainJournalBearingResults)

        @property
        def loaded_fluid_film_bearing_results(
            self: "LoadedPlainOilFedJournalBearing._Cast_LoadedPlainOilFedJournalBearing",
        ) -> "_2119.LoadedFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2119

            return self._parent._cast(_2119.LoadedFluidFilmBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedPlainOilFedJournalBearing._Cast_LoadedPlainOilFedJournalBearing",
        ) -> "_1954.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1954

            return self._parent._cast(_1954.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedPlainOilFedJournalBearing._Cast_LoadedPlainOilFedJournalBearing",
        ) -> "_1957.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1957

            return self._parent._cast(_1957.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedPlainOilFedJournalBearing._Cast_LoadedPlainOilFedJournalBearing",
        ) -> "_1949.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1949

            return self._parent._cast(_1949.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedPlainOilFedJournalBearing._Cast_LoadedPlainOilFedJournalBearing",
        ) -> "_1875.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1875

            return self._parent._cast(_1875.BearingLoadCaseResultsLightweight)

        @property
        def loaded_plain_oil_fed_journal_bearing(
            self: "LoadedPlainOilFedJournalBearing._Cast_LoadedPlainOilFedJournalBearing",
        ) -> "LoadedPlainOilFedJournalBearing":
            return self._parent

        def __getattr__(
            self: "LoadedPlainOilFedJournalBearing._Cast_LoadedPlainOilFedJournalBearing",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedPlainOilFedJournalBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_between_oil_feed_inlet_and_minimum_film_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngleBetweenOilFeedInletAndMinimumFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def angle_between_oil_feed_inlet_and_point_of_loading(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngleBetweenOilFeedInletAndPointOfLoading

        if temp is None:
            return 0.0

        return temp

    @property
    def combined_flow_rate(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CombinedFlowRate

        if temp is None:
            return 0.0

        return temp

    @property
    def current_oil_inlet_angular_position_from_the_x_axis(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurrentOilInletAngularPositionFromTheXAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def feed_pressure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FeedPressure

        if temp is None:
            return 0.0

        return temp

    @property
    def ideal_oil_inlet_angular_position_from_the_x_axis(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IdealOilInletAngularPositionFromTheXAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def oil_exit_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OilExitTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def pressure_flow_rate(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PressureFlowRate

        if temp is None:
            return 0.0

        return temp

    @property
    def side_flow_rate(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SideFlowRate

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedPlainOilFedJournalBearing._Cast_LoadedPlainOilFedJournalBearing":
        return self._Cast_LoadedPlainOilFedJournalBearing(self)
