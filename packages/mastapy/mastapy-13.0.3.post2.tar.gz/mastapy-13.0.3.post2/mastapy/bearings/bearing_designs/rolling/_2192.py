"""ThreePointContactBallBearing"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.bearings.bearing_designs.rolling import _2179
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_THREE_POINT_CONTACT_BALL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "ThreePointContactBallBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2160, _2185
    from mastapy.bearings.bearing_designs import _2151, _2154, _2150


__docformat__ = "restructuredtext en"
__all__ = ("ThreePointContactBallBearing",)


Self = TypeVar("Self", bound="ThreePointContactBallBearing")


class ThreePointContactBallBearing(_2179.MultiPointContactBallBearing):
    """ThreePointContactBallBearing

    This is a mastapy class.
    """

    TYPE = _THREE_POINT_CONTACT_BALL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ThreePointContactBallBearing")

    class _Cast_ThreePointContactBallBearing:
        """Special nested class for casting ThreePointContactBallBearing to subclasses."""

        def __init__(
            self: "ThreePointContactBallBearing._Cast_ThreePointContactBallBearing",
            parent: "ThreePointContactBallBearing",
        ):
            self._parent = parent

        @property
        def multi_point_contact_ball_bearing(
            self: "ThreePointContactBallBearing._Cast_ThreePointContactBallBearing",
        ) -> "_2179.MultiPointContactBallBearing":
            return self._parent._cast(_2179.MultiPointContactBallBearing)

        @property
        def ball_bearing(
            self: "ThreePointContactBallBearing._Cast_ThreePointContactBallBearing",
        ) -> "_2160.BallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2160

            return self._parent._cast(_2160.BallBearing)

        @property
        def rolling_bearing(
            self: "ThreePointContactBallBearing._Cast_ThreePointContactBallBearing",
        ) -> "_2185.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2185

            return self._parent._cast(_2185.RollingBearing)

        @property
        def detailed_bearing(
            self: "ThreePointContactBallBearing._Cast_ThreePointContactBallBearing",
        ) -> "_2151.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2151

            return self._parent._cast(_2151.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "ThreePointContactBallBearing._Cast_ThreePointContactBallBearing",
        ) -> "_2154.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2154

            return self._parent._cast(_2154.NonLinearBearing)

        @property
        def bearing_design(
            self: "ThreePointContactBallBearing._Cast_ThreePointContactBallBearing",
        ) -> "_2150.BearingDesign":
            from mastapy.bearings.bearing_designs import _2150

            return self._parent._cast(_2150.BearingDesign)

        @property
        def three_point_contact_ball_bearing(
            self: "ThreePointContactBallBearing._Cast_ThreePointContactBallBearing",
        ) -> "ThreePointContactBallBearing":
            return self._parent

        def __getattr__(
            self: "ThreePointContactBallBearing._Cast_ThreePointContactBallBearing",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ThreePointContactBallBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_radial_internal_clearance(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AssemblyRadialInternalClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @assembly_radial_internal_clearance.setter
    @enforce_parameter_types
    def assembly_radial_internal_clearance(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AssemblyRadialInternalClearance = value

    @property
    def inner_shim_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerShimAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_shim_angle.setter
    @enforce_parameter_types
    def inner_shim_angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerShimAngle = value

    @property
    def inner_shim_width(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerShimWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_shim_width.setter
    @enforce_parameter_types
    def inner_shim_width(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerShimWidth = value

    @property
    def cast_to(
        self: Self,
    ) -> "ThreePointContactBallBearing._Cast_ThreePointContactBallBearing":
        return self._Cast_ThreePointContactBallBearing(self)
