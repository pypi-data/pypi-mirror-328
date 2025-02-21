"""LoadedPadFluidFilmBearingResults"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.bearings.bearing_results.fluid_film import _2119
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_PAD_FLUID_FILM_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.FluidFilm", "LoadedPadFluidFilmBearingResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.fluid_film import _2127, _2128
    from mastapy.bearings.bearing_results import _1954, _1957, _1949
    from mastapy.bearings import _1875


__docformat__ = "restructuredtext en"
__all__ = ("LoadedPadFluidFilmBearingResults",)


Self = TypeVar("Self", bound="LoadedPadFluidFilmBearingResults")


class LoadedPadFluidFilmBearingResults(_2119.LoadedFluidFilmBearingResults):
    """LoadedPadFluidFilmBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_PAD_FLUID_FILM_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedPadFluidFilmBearingResults")

    class _Cast_LoadedPadFluidFilmBearingResults:
        """Special nested class for casting LoadedPadFluidFilmBearingResults to subclasses."""

        def __init__(
            self: "LoadedPadFluidFilmBearingResults._Cast_LoadedPadFluidFilmBearingResults",
            parent: "LoadedPadFluidFilmBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_fluid_film_bearing_results(
            self: "LoadedPadFluidFilmBearingResults._Cast_LoadedPadFluidFilmBearingResults",
        ) -> "_2119.LoadedFluidFilmBearingResults":
            return self._parent._cast(_2119.LoadedFluidFilmBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedPadFluidFilmBearingResults._Cast_LoadedPadFluidFilmBearingResults",
        ) -> "_1954.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1954

            return self._parent._cast(_1954.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedPadFluidFilmBearingResults._Cast_LoadedPadFluidFilmBearingResults",
        ) -> "_1957.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1957

            return self._parent._cast(_1957.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedPadFluidFilmBearingResults._Cast_LoadedPadFluidFilmBearingResults",
        ) -> "_1949.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1949

            return self._parent._cast(_1949.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedPadFluidFilmBearingResults._Cast_LoadedPadFluidFilmBearingResults",
        ) -> "_1875.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1875

            return self._parent._cast(_1875.BearingLoadCaseResultsLightweight)

        @property
        def loaded_tilting_pad_journal_bearing_results(
            self: "LoadedPadFluidFilmBearingResults._Cast_LoadedPadFluidFilmBearingResults",
        ) -> "_2127.LoadedTiltingPadJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2127

            return self._parent._cast(_2127.LoadedTiltingPadJournalBearingResults)

        @property
        def loaded_tilting_pad_thrust_bearing_results(
            self: "LoadedPadFluidFilmBearingResults._Cast_LoadedPadFluidFilmBearingResults",
        ) -> "_2128.LoadedTiltingPadThrustBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2128

            return self._parent._cast(_2128.LoadedTiltingPadThrustBearingResults)

        @property
        def loaded_pad_fluid_film_bearing_results(
            self: "LoadedPadFluidFilmBearingResults._Cast_LoadedPadFluidFilmBearingResults",
        ) -> "LoadedPadFluidFilmBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedPadFluidFilmBearingResults._Cast_LoadedPadFluidFilmBearingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedPadFluidFilmBearingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_film_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def oil_inlet_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OilInletTemperature

        if temp is None:
            return 0.0

        return temp

    @oil_inlet_temperature.setter
    @enforce_parameter_types
    def oil_inlet_temperature(self: Self, value: "float"):
        self.wrapped.OilInletTemperature = float(value) if value is not None else 0.0

    @property
    def reynolds_number(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReynoldsNumber

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedPadFluidFilmBearingResults._Cast_LoadedPadFluidFilmBearingResults":
        return self._Cast_LoadedPadFluidFilmBearingResults(self)
