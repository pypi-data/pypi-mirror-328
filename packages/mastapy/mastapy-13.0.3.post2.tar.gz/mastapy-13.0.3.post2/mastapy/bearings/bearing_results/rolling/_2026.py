"""LoadedCrossedRollerBearingRow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2050
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_CROSSED_ROLLER_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedCrossedRollerBearingRow"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2025, _2054


__docformat__ = "restructuredtext en"
__all__ = ("LoadedCrossedRollerBearingRow",)


Self = TypeVar("Self", bound="LoadedCrossedRollerBearingRow")


class LoadedCrossedRollerBearingRow(_2050.LoadedRollerBearingRow):
    """LoadedCrossedRollerBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_CROSSED_ROLLER_BEARING_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedCrossedRollerBearingRow")

    class _Cast_LoadedCrossedRollerBearingRow:
        """Special nested class for casting LoadedCrossedRollerBearingRow to subclasses."""

        def __init__(
            self: "LoadedCrossedRollerBearingRow._Cast_LoadedCrossedRollerBearingRow",
            parent: "LoadedCrossedRollerBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_roller_bearing_row(
            self: "LoadedCrossedRollerBearingRow._Cast_LoadedCrossedRollerBearingRow",
        ) -> "_2050.LoadedRollerBearingRow":
            return self._parent._cast(_2050.LoadedRollerBearingRow)

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedCrossedRollerBearingRow._Cast_LoadedCrossedRollerBearingRow",
        ) -> "_2054.LoadedRollingBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2054

            return self._parent._cast(_2054.LoadedRollingBearingRow)

        @property
        def loaded_crossed_roller_bearing_row(
            self: "LoadedCrossedRollerBearingRow._Cast_LoadedCrossedRollerBearingRow",
        ) -> "LoadedCrossedRollerBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedCrossedRollerBearingRow._Cast_LoadedCrossedRollerBearingRow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedCrossedRollerBearingRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self: Self) -> "_2025.LoadedCrossedRollerBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedCrossedRollerBearingResults

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
    ) -> "LoadedCrossedRollerBearingRow._Cast_LoadedCrossedRollerBearingRow":
        return self._Cast_LoadedCrossedRollerBearingRow(self)
