"""LoadedRollerBearingResults"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2033
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLER_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedRollerBearingResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import (
        _1989,
        _1994,
        _1997,
        _2005,
        _2009,
        _2021,
        _2024,
        _2040,
        _2043,
        _2048,
        _2057,
    )
    from mastapy.bearings.bearing_results import _1954, _1957, _1949
    from mastapy.bearings import _1875


__docformat__ = "restructuredtext en"
__all__ = ("LoadedRollerBearingResults",)


Self = TypeVar("Self", bound="LoadedRollerBearingResults")


class LoadedRollerBearingResults(_2033.LoadedRollingBearingResults):
    """LoadedRollerBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLER_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedRollerBearingResults")

    class _Cast_LoadedRollerBearingResults:
        """Special nested class for casting LoadedRollerBearingResults to subclasses."""

        def __init__(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
            parent: "LoadedRollerBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_2033.LoadedRollingBearingResults":
            return self._parent._cast(_2033.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_1954.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1954

            return self._parent._cast(_1954.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_1957.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1957

            return self._parent._cast(_1957.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_1949.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1949

            return self._parent._cast(_1949.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_1875.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1875

            return self._parent._cast(_1875.BearingLoadCaseResultsLightweight)

        @property
        def loaded_asymmetric_spherical_roller_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_1989.LoadedAsymmetricSphericalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _1989

            return self._parent._cast(
                _1989.LoadedAsymmetricSphericalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_1994.LoadedAxialThrustCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _1994

            return self._parent._cast(
                _1994.LoadedAxialThrustCylindricalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_1997.LoadedAxialThrustNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _1997

            return self._parent._cast(_1997.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_crossed_roller_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_2005.LoadedCrossedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2005

            return self._parent._cast(_2005.LoadedCrossedRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_2009.LoadedCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2009

            return self._parent._cast(_2009.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_needle_roller_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_2021.LoadedNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2021

            return self._parent._cast(_2021.LoadedNeedleRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_2024.LoadedNonBarrelRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2024

            return self._parent._cast(_2024.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_spherical_roller_radial_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_2040.LoadedSphericalRollerRadialBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2040

            return self._parent._cast(_2040.LoadedSphericalRollerRadialBearingResults)

        @property
        def loaded_spherical_roller_thrust_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_2043.LoadedSphericalRollerThrustBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2043

            return self._parent._cast(_2043.LoadedSphericalRollerThrustBearingResults)

        @property
        def loaded_taper_roller_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_2048.LoadedTaperRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2048

            return self._parent._cast(_2048.LoadedTaperRollerBearingResults)

        @property
        def loaded_toroidal_roller_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_2057.LoadedToroidalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2057

            return self._parent._cast(_2057.LoadedToroidalRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "LoadedRollerBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedRollerBearingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def element_angular_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def element_centrifugal_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementCentrifugalForce

        if temp is None:
            return 0.0

        return temp

    @property
    def element_surface_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementSurfaceVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_contact_width_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianContactWidthInner

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_contact_width_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianContactWidthOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumShearStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumShearStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults":
        return self._Cast_LoadedRollerBearingResults(self)
