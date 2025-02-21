"""LoadedThrustBallBearingResults"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2002
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_THRUST_BALL_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedThrustBallBearingResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2033
    from mastapy.bearings.bearing_results import _1954, _1957, _1949
    from mastapy.bearings import _1875


__docformat__ = "restructuredtext en"
__all__ = ("LoadedThrustBallBearingResults",)


Self = TypeVar("Self", bound="LoadedThrustBallBearingResults")


class LoadedThrustBallBearingResults(_2002.LoadedBallBearingResults):
    """LoadedThrustBallBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_THRUST_BALL_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedThrustBallBearingResults")

    class _Cast_LoadedThrustBallBearingResults:
        """Special nested class for casting LoadedThrustBallBearingResults to subclasses."""

        def __init__(
            self: "LoadedThrustBallBearingResults._Cast_LoadedThrustBallBearingResults",
            parent: "LoadedThrustBallBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_ball_bearing_results(
            self: "LoadedThrustBallBearingResults._Cast_LoadedThrustBallBearingResults",
        ) -> "_2002.LoadedBallBearingResults":
            return self._parent._cast(_2002.LoadedBallBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedThrustBallBearingResults._Cast_LoadedThrustBallBearingResults",
        ) -> "_2033.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2033

            return self._parent._cast(_2033.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedThrustBallBearingResults._Cast_LoadedThrustBallBearingResults",
        ) -> "_1954.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1954

            return self._parent._cast(_1954.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedThrustBallBearingResults._Cast_LoadedThrustBallBearingResults",
        ) -> "_1957.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1957

            return self._parent._cast(_1957.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedThrustBallBearingResults._Cast_LoadedThrustBallBearingResults",
        ) -> "_1949.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1949

            return self._parent._cast(_1949.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedThrustBallBearingResults._Cast_LoadedThrustBallBearingResults",
        ) -> "_1875.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1875

            return self._parent._cast(_1875.BearingLoadCaseResultsLightweight)

        @property
        def loaded_thrust_ball_bearing_results(
            self: "LoadedThrustBallBearingResults._Cast_LoadedThrustBallBearingResults",
        ) -> "LoadedThrustBallBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedThrustBallBearingResults._Cast_LoadedThrustBallBearingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedThrustBallBearingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedThrustBallBearingResults._Cast_LoadedThrustBallBearingResults":
        return self._Cast_LoadedThrustBallBearingResults(self)
