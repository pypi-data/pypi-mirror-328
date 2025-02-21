"""LoadedAxialThrustNeedleRollerBearingResults"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _1994
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_AXIAL_THRUST_NEEDLE_ROLLER_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedAxialThrustNeedleRollerBearingResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2024, _2029, _2033
    from mastapy.bearings.bearing_results import _1954, _1957, _1949
    from mastapy.bearings import _1875


__docformat__ = "restructuredtext en"
__all__ = ("LoadedAxialThrustNeedleRollerBearingResults",)


Self = TypeVar("Self", bound="LoadedAxialThrustNeedleRollerBearingResults")


class LoadedAxialThrustNeedleRollerBearingResults(
    _1994.LoadedAxialThrustCylindricalRollerBearingResults
):
    """LoadedAxialThrustNeedleRollerBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_AXIAL_THRUST_NEEDLE_ROLLER_BEARING_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedAxialThrustNeedleRollerBearingResults"
    )

    class _Cast_LoadedAxialThrustNeedleRollerBearingResults:
        """Special nested class for casting LoadedAxialThrustNeedleRollerBearingResults to subclasses."""

        def __init__(
            self: "LoadedAxialThrustNeedleRollerBearingResults._Cast_LoadedAxialThrustNeedleRollerBearingResults",
            parent: "LoadedAxialThrustNeedleRollerBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(
            self: "LoadedAxialThrustNeedleRollerBearingResults._Cast_LoadedAxialThrustNeedleRollerBearingResults",
        ) -> "_1994.LoadedAxialThrustCylindricalRollerBearingResults":
            return self._parent._cast(
                _1994.LoadedAxialThrustCylindricalRollerBearingResults
            )

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "LoadedAxialThrustNeedleRollerBearingResults._Cast_LoadedAxialThrustNeedleRollerBearingResults",
        ) -> "_2024.LoadedNonBarrelRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2024

            return self._parent._cast(_2024.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "LoadedAxialThrustNeedleRollerBearingResults._Cast_LoadedAxialThrustNeedleRollerBearingResults",
        ) -> "_2029.LoadedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2029

            return self._parent._cast(_2029.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedAxialThrustNeedleRollerBearingResults._Cast_LoadedAxialThrustNeedleRollerBearingResults",
        ) -> "_2033.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2033

            return self._parent._cast(_2033.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedAxialThrustNeedleRollerBearingResults._Cast_LoadedAxialThrustNeedleRollerBearingResults",
        ) -> "_1954.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1954

            return self._parent._cast(_1954.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedAxialThrustNeedleRollerBearingResults._Cast_LoadedAxialThrustNeedleRollerBearingResults",
        ) -> "_1957.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1957

            return self._parent._cast(_1957.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedAxialThrustNeedleRollerBearingResults._Cast_LoadedAxialThrustNeedleRollerBearingResults",
        ) -> "_1949.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1949

            return self._parent._cast(_1949.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedAxialThrustNeedleRollerBearingResults._Cast_LoadedAxialThrustNeedleRollerBearingResults",
        ) -> "_1875.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1875

            return self._parent._cast(_1875.BearingLoadCaseResultsLightweight)

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(
            self: "LoadedAxialThrustNeedleRollerBearingResults._Cast_LoadedAxialThrustNeedleRollerBearingResults",
        ) -> "LoadedAxialThrustNeedleRollerBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedAxialThrustNeedleRollerBearingResults._Cast_LoadedAxialThrustNeedleRollerBearingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "LoadedAxialThrustNeedleRollerBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedAxialThrustNeedleRollerBearingResults._Cast_LoadedAxialThrustNeedleRollerBearingResults":
        return self._Cast_LoadedAxialThrustNeedleRollerBearingResults(self)
