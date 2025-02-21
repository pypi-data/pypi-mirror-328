"""LoadedSelfAligningBallBearingRow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2003
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_SELF_ALIGNING_BALL_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedSelfAligningBallBearingRow"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2036, _2034


__docformat__ = "restructuredtext en"
__all__ = ("LoadedSelfAligningBallBearingRow",)


Self = TypeVar("Self", bound="LoadedSelfAligningBallBearingRow")


class LoadedSelfAligningBallBearingRow(_2003.LoadedBallBearingRow):
    """LoadedSelfAligningBallBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_SELF_ALIGNING_BALL_BEARING_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedSelfAligningBallBearingRow")

    class _Cast_LoadedSelfAligningBallBearingRow:
        """Special nested class for casting LoadedSelfAligningBallBearingRow to subclasses."""

        def __init__(
            self: "LoadedSelfAligningBallBearingRow._Cast_LoadedSelfAligningBallBearingRow",
            parent: "LoadedSelfAligningBallBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_ball_bearing_row(
            self: "LoadedSelfAligningBallBearingRow._Cast_LoadedSelfAligningBallBearingRow",
        ) -> "_2003.LoadedBallBearingRow":
            return self._parent._cast(_2003.LoadedBallBearingRow)

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedSelfAligningBallBearingRow._Cast_LoadedSelfAligningBallBearingRow",
        ) -> "_2034.LoadedRollingBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2034

            return self._parent._cast(_2034.LoadedRollingBearingRow)

        @property
        def loaded_self_aligning_ball_bearing_row(
            self: "LoadedSelfAligningBallBearingRow._Cast_LoadedSelfAligningBallBearingRow",
        ) -> "LoadedSelfAligningBallBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedSelfAligningBallBearingRow._Cast_LoadedSelfAligningBallBearingRow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedSelfAligningBallBearingRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self: Self) -> "_2036.LoadedSelfAligningBallBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedSelfAligningBallBearingResults

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
    ) -> "LoadedSelfAligningBallBearingRow._Cast_LoadedSelfAligningBallBearingRow":
        return self._Cast_LoadedSelfAligningBallBearingRow(self)
