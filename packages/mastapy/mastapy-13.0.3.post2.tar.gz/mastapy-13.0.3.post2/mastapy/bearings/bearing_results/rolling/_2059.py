"""LoadedSphericalRollerBearingElement"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2048
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_SPHERICAL_ROLLER_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedSphericalRollerBearingElement",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2058, _2065, _2034


__docformat__ = "restructuredtext en"
__all__ = ("LoadedSphericalRollerBearingElement",)


Self = TypeVar("Self", bound="LoadedSphericalRollerBearingElement")


class LoadedSphericalRollerBearingElement(_2048.LoadedRollerBearingElement):
    """LoadedSphericalRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_SPHERICAL_ROLLER_BEARING_ELEMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedSphericalRollerBearingElement")

    class _Cast_LoadedSphericalRollerBearingElement:
        """Special nested class for casting LoadedSphericalRollerBearingElement to subclasses."""

        def __init__(
            self: "LoadedSphericalRollerBearingElement._Cast_LoadedSphericalRollerBearingElement",
            parent: "LoadedSphericalRollerBearingElement",
        ):
            self._parent = parent

        @property
        def loaded_roller_bearing_element(
            self: "LoadedSphericalRollerBearingElement._Cast_LoadedSphericalRollerBearingElement",
        ) -> "_2048.LoadedRollerBearingElement":
            return self._parent._cast(_2048.LoadedRollerBearingElement)

        @property
        def loaded_element(
            self: "LoadedSphericalRollerBearingElement._Cast_LoadedSphericalRollerBearingElement",
        ) -> "_2034.LoadedElement":
            from mastapy.bearings.bearing_results.rolling import _2034

            return self._parent._cast(_2034.LoadedElement)

        @property
        def loaded_spherical_radial_roller_bearing_element(
            self: "LoadedSphericalRollerBearingElement._Cast_LoadedSphericalRollerBearingElement",
        ) -> "_2058.LoadedSphericalRadialRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2058

            return self._parent._cast(_2058.LoadedSphericalRadialRollerBearingElement)

        @property
        def loaded_spherical_thrust_roller_bearing_element(
            self: "LoadedSphericalRollerBearingElement._Cast_LoadedSphericalRollerBearingElement",
        ) -> "_2065.LoadedSphericalThrustRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2065

            return self._parent._cast(_2065.LoadedSphericalThrustRollerBearingElement)

        @property
        def loaded_spherical_roller_bearing_element(
            self: "LoadedSphericalRollerBearingElement._Cast_LoadedSphericalRollerBearingElement",
        ) -> "LoadedSphericalRollerBearingElement":
            return self._parent

        def __getattr__(
            self: "LoadedSphericalRollerBearingElement._Cast_LoadedSphericalRollerBearingElement",
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
        self: Self, instance_to_wrap: "LoadedSphericalRollerBearingElement.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "LoadedSphericalRollerBearingElement._Cast_LoadedSphericalRollerBearingElement"
    ):
        return self._Cast_LoadedSphericalRollerBearingElement(self)
