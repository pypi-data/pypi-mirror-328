"""LoadedAxialThrustNeedleRollerBearingRow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _1995
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_AXIAL_THRUST_NEEDLE_ROLLER_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedAxialThrustNeedleRollerBearingRow",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _1997, _2025, _2030, _2034


__docformat__ = "restructuredtext en"
__all__ = ("LoadedAxialThrustNeedleRollerBearingRow",)


Self = TypeVar("Self", bound="LoadedAxialThrustNeedleRollerBearingRow")


class LoadedAxialThrustNeedleRollerBearingRow(
    _1995.LoadedAxialThrustCylindricalRollerBearingRow
):
    """LoadedAxialThrustNeedleRollerBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_AXIAL_THRUST_NEEDLE_ROLLER_BEARING_ROW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedAxialThrustNeedleRollerBearingRow"
    )

    class _Cast_LoadedAxialThrustNeedleRollerBearingRow:
        """Special nested class for casting LoadedAxialThrustNeedleRollerBearingRow to subclasses."""

        def __init__(
            self: "LoadedAxialThrustNeedleRollerBearingRow._Cast_LoadedAxialThrustNeedleRollerBearingRow",
            parent: "LoadedAxialThrustNeedleRollerBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_row(
            self: "LoadedAxialThrustNeedleRollerBearingRow._Cast_LoadedAxialThrustNeedleRollerBearingRow",
        ) -> "_1995.LoadedAxialThrustCylindricalRollerBearingRow":
            return self._parent._cast(
                _1995.LoadedAxialThrustCylindricalRollerBearingRow
            )

        @property
        def loaded_non_barrel_roller_bearing_row(
            self: "LoadedAxialThrustNeedleRollerBearingRow._Cast_LoadedAxialThrustNeedleRollerBearingRow",
        ) -> "_2025.LoadedNonBarrelRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2025

            return self._parent._cast(_2025.LoadedNonBarrelRollerBearingRow)

        @property
        def loaded_roller_bearing_row(
            self: "LoadedAxialThrustNeedleRollerBearingRow._Cast_LoadedAxialThrustNeedleRollerBearingRow",
        ) -> "_2030.LoadedRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2030

            return self._parent._cast(_2030.LoadedRollerBearingRow)

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedAxialThrustNeedleRollerBearingRow._Cast_LoadedAxialThrustNeedleRollerBearingRow",
        ) -> "_2034.LoadedRollingBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2034

            return self._parent._cast(_2034.LoadedRollingBearingRow)

        @property
        def loaded_axial_thrust_needle_roller_bearing_row(
            self: "LoadedAxialThrustNeedleRollerBearingRow._Cast_LoadedAxialThrustNeedleRollerBearingRow",
        ) -> "LoadedAxialThrustNeedleRollerBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedAxialThrustNeedleRollerBearingRow._Cast_LoadedAxialThrustNeedleRollerBearingRow",
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
        self: Self, instance_to_wrap: "LoadedAxialThrustNeedleRollerBearingRow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(
        self: Self,
    ) -> "_1997.LoadedAxialThrustNeedleRollerBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedAxialThrustNeedleRollerBearingResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedAxialThrustNeedleRollerBearingRow._Cast_LoadedAxialThrustNeedleRollerBearingRow":
        return self._Cast_LoadedAxialThrustNeedleRollerBearingRow(self)
