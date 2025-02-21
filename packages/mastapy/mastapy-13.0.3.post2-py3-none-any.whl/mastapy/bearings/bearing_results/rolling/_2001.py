"""LoadedAbstractSphericalRollerBearingStripLoadResults"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2051
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ABSTRACT_SPHERICAL_ROLLER_BEARING_STRIP_LOAD_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedAbstractSphericalRollerBearingStripLoadResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2011, _2062, _2079


__docformat__ = "restructuredtext en"
__all__ = ("LoadedAbstractSphericalRollerBearingStripLoadResults",)


Self = TypeVar("Self", bound="LoadedAbstractSphericalRollerBearingStripLoadResults")


class LoadedAbstractSphericalRollerBearingStripLoadResults(
    _2051.LoadedRollerStripLoadResults
):
    """LoadedAbstractSphericalRollerBearingStripLoadResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ABSTRACT_SPHERICAL_ROLLER_BEARING_STRIP_LOAD_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedAbstractSphericalRollerBearingStripLoadResults"
    )

    class _Cast_LoadedAbstractSphericalRollerBearingStripLoadResults:
        """Special nested class for casting LoadedAbstractSphericalRollerBearingStripLoadResults to subclasses."""

        def __init__(
            self: "LoadedAbstractSphericalRollerBearingStripLoadResults._Cast_LoadedAbstractSphericalRollerBearingStripLoadResults",
            parent: "LoadedAbstractSphericalRollerBearingStripLoadResults",
        ):
            self._parent = parent

        @property
        def loaded_roller_strip_load_results(
            self: "LoadedAbstractSphericalRollerBearingStripLoadResults._Cast_LoadedAbstractSphericalRollerBearingStripLoadResults",
        ) -> "_2051.LoadedRollerStripLoadResults":
            return self._parent._cast(_2051.LoadedRollerStripLoadResults)

        @property
        def loaded_asymmetric_spherical_roller_bearing_strip_load_results(
            self: "LoadedAbstractSphericalRollerBearingStripLoadResults._Cast_LoadedAbstractSphericalRollerBearingStripLoadResults",
        ) -> "_2011.LoadedAsymmetricSphericalRollerBearingStripLoadResults":
            from mastapy.bearings.bearing_results.rolling import _2011

            return self._parent._cast(
                _2011.LoadedAsymmetricSphericalRollerBearingStripLoadResults
            )

        @property
        def loaded_spherical_roller_radial_bearing_strip_load_results(
            self: "LoadedAbstractSphericalRollerBearingStripLoadResults._Cast_LoadedAbstractSphericalRollerBearingStripLoadResults",
        ) -> "_2062.LoadedSphericalRollerRadialBearingStripLoadResults":
            from mastapy.bearings.bearing_results.rolling import _2062

            return self._parent._cast(
                _2062.LoadedSphericalRollerRadialBearingStripLoadResults
            )

        @property
        def loaded_toroidal_roller_bearing_strip_load_results(
            self: "LoadedAbstractSphericalRollerBearingStripLoadResults._Cast_LoadedAbstractSphericalRollerBearingStripLoadResults",
        ) -> "_2079.LoadedToroidalRollerBearingStripLoadResults":
            from mastapy.bearings.bearing_results.rolling import _2079

            return self._parent._cast(_2079.LoadedToroidalRollerBearingStripLoadResults)

        @property
        def loaded_abstract_spherical_roller_bearing_strip_load_results(
            self: "LoadedAbstractSphericalRollerBearingStripLoadResults._Cast_LoadedAbstractSphericalRollerBearingStripLoadResults",
        ) -> "LoadedAbstractSphericalRollerBearingStripLoadResults":
            return self._parent

        def __getattr__(
            self: "LoadedAbstractSphericalRollerBearingStripLoadResults._Cast_LoadedAbstractSphericalRollerBearingStripLoadResults",
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
        self: Self,
        instance_to_wrap: "LoadedAbstractSphericalRollerBearingStripLoadResults.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedAbstractSphericalRollerBearingStripLoadResults._Cast_LoadedAbstractSphericalRollerBearingStripLoadResults":
        return self._Cast_LoadedAbstractSphericalRollerBearingStripLoadResults(self)
