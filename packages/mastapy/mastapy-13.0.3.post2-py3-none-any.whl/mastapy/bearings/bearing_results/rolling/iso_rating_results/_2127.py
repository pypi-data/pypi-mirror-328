"""RollerISO2812007Results"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2123
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_ISO2812007_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.IsoRatingResults",
    "RollerISO2812007Results",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2125


__docformat__ = "restructuredtext en"
__all__ = ("RollerISO2812007Results",)


Self = TypeVar("Self", bound="RollerISO2812007Results")


class RollerISO2812007Results(_2123.ISO2812007Results):
    """RollerISO2812007Results

    This is a mastapy class.
    """

    TYPE = _ROLLER_ISO2812007_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollerISO2812007Results")

    class _Cast_RollerISO2812007Results:
        """Special nested class for casting RollerISO2812007Results to subclasses."""

        def __init__(
            self: "RollerISO2812007Results._Cast_RollerISO2812007Results",
            parent: "RollerISO2812007Results",
        ):
            self._parent = parent

        @property
        def iso2812007_results(
            self: "RollerISO2812007Results._Cast_RollerISO2812007Results",
        ) -> "_2123.ISO2812007Results":
            return self._parent._cast(_2123.ISO2812007Results)

        @property
        def iso_results(
            self: "RollerISO2812007Results._Cast_RollerISO2812007Results",
        ) -> "_2125.ISOResults":
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import (
                _2125,
            )

            return self._parent._cast(_2125.ISOResults)

        @property
        def roller_iso2812007_results(
            self: "RollerISO2812007Results._Cast_RollerISO2812007Results",
        ) -> "RollerISO2812007Results":
            return self._parent

        def __getattr__(
            self: "RollerISO2812007Results._Cast_RollerISO2812007Results", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollerISO2812007Results.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "RollerISO2812007Results._Cast_RollerISO2812007Results":
        return self._Cast_RollerISO2812007Results(self)
