"""BallBearing"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings.bearing_designs.rolling import _2185
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BALL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "BallBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import (
        _2161,
        _2155,
        _2156,
        _2170,
        _2174,
        _2179,
        _2186,
        _2192,
        _2193,
    )
    from mastapy.bearings.bearing_designs import _2151, _2154, _2150


__docformat__ = "restructuredtext en"
__all__ = ("BallBearing",)


Self = TypeVar("Self", bound="BallBearing")


class BallBearing(_2185.RollingBearing):
    """BallBearing

    This is a mastapy class.
    """

    TYPE = _BALL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BallBearing")

    class _Cast_BallBearing:
        """Special nested class for casting BallBearing to subclasses."""

        def __init__(self: "BallBearing._Cast_BallBearing", parent: "BallBearing"):
            self._parent = parent

        @property
        def rolling_bearing(
            self: "BallBearing._Cast_BallBearing",
        ) -> "_2185.RollingBearing":
            return self._parent._cast(_2185.RollingBearing)

        @property
        def detailed_bearing(
            self: "BallBearing._Cast_BallBearing",
        ) -> "_2151.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2151

            return self._parent._cast(_2151.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "BallBearing._Cast_BallBearing",
        ) -> "_2154.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2154

            return self._parent._cast(_2154.NonLinearBearing)

        @property
        def bearing_design(
            self: "BallBearing._Cast_BallBearing",
        ) -> "_2150.BearingDesign":
            from mastapy.bearings.bearing_designs import _2150

            return self._parent._cast(_2150.BearingDesign)

        @property
        def angular_contact_ball_bearing(
            self: "BallBearing._Cast_BallBearing",
        ) -> "_2155.AngularContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2155

            return self._parent._cast(_2155.AngularContactBallBearing)

        @property
        def angular_contact_thrust_ball_bearing(
            self: "BallBearing._Cast_BallBearing",
        ) -> "_2156.AngularContactThrustBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2156

            return self._parent._cast(_2156.AngularContactThrustBallBearing)

        @property
        def deep_groove_ball_bearing(
            self: "BallBearing._Cast_BallBearing",
        ) -> "_2170.DeepGrooveBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2170

            return self._parent._cast(_2170.DeepGrooveBallBearing)

        @property
        def four_point_contact_ball_bearing(
            self: "BallBearing._Cast_BallBearing",
        ) -> "_2174.FourPointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2174

            return self._parent._cast(_2174.FourPointContactBallBearing)

        @property
        def multi_point_contact_ball_bearing(
            self: "BallBearing._Cast_BallBearing",
        ) -> "_2179.MultiPointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2179

            return self._parent._cast(_2179.MultiPointContactBallBearing)

        @property
        def self_aligning_ball_bearing(
            self: "BallBearing._Cast_BallBearing",
        ) -> "_2186.SelfAligningBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2186

            return self._parent._cast(_2186.SelfAligningBallBearing)

        @property
        def three_point_contact_ball_bearing(
            self: "BallBearing._Cast_BallBearing",
        ) -> "_2192.ThreePointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2192

            return self._parent._cast(_2192.ThreePointContactBallBearing)

        @property
        def thrust_ball_bearing(
            self: "BallBearing._Cast_BallBearing",
        ) -> "_2193.ThrustBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2193

            return self._parent._cast(_2193.ThrustBallBearing)

        @property
        def ball_bearing(self: "BallBearing._Cast_BallBearing") -> "BallBearing":
            return self._parent

        def __getattr__(self: "BallBearing._Cast_BallBearing", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BallBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_radius_at_right_angle_to_rolling_direction_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactRadiusAtRightAngleToRollingDirectionInner

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_radius_at_right_angle_to_rolling_direction_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactRadiusAtRightAngleToRollingDirectionOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def curvature_sum_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurvatureSumInner

        if temp is None:
            return 0.0

        return temp

    @property
    def curvature_sum_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurvatureSumOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def element_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ElementDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @element_diameter.setter
    @enforce_parameter_types
    def element_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ElementDiameter = value

    @property
    def inner_groove_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerGrooveRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_groove_radius.setter
    @enforce_parameter_types
    def inner_groove_radius(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerGrooveRadius = value

    @property
    def inner_groove_radius_as_percentage_of_element_diameter(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerGrooveRadiusAsPercentageOfElementDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_groove_radius_as_percentage_of_element_diameter.setter
    @enforce_parameter_types
    def inner_groove_radius_as_percentage_of_element_diameter(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerGrooveRadiusAsPercentageOfElementDiameter = value

    @property
    def inner_left_shoulder_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerLeftShoulderDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_left_shoulder_diameter.setter
    @enforce_parameter_types
    def inner_left_shoulder_diameter(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerLeftShoulderDiameter = value

    @property
    def inner_race_osculation(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerRaceOsculation

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_race_osculation.setter
    @enforce_parameter_types
    def inner_race_osculation(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerRaceOsculation = value

    @property
    def inner_right_shoulder_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerRightShoulderDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_right_shoulder_diameter.setter
    @enforce_parameter_types
    def inner_right_shoulder_diameter(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerRightShoulderDiameter = value

    @property
    def inner_ring_left_shoulder_height(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerRingLeftShoulderHeight

        if temp is None:
            return 0.0

        return temp

    @inner_ring_left_shoulder_height.setter
    @enforce_parameter_types
    def inner_ring_left_shoulder_height(self: Self, value: "float"):
        self.wrapped.InnerRingLeftShoulderHeight = (
            float(value) if value is not None else 0.0
        )

    @property
    def inner_ring_right_shoulder_height(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerRingRightShoulderHeight

        if temp is None:
            return 0.0

        return temp

    @inner_ring_right_shoulder_height.setter
    @enforce_parameter_types
    def inner_ring_right_shoulder_height(self: Self, value: "float"):
        self.wrapped.InnerRingRightShoulderHeight = (
            float(value) if value is not None else 0.0
        )

    @property
    def inner_ring_shoulder_chamfer(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerRingShoulderChamfer

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_ring_shoulder_chamfer.setter
    @enforce_parameter_types
    def inner_ring_shoulder_chamfer(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerRingShoulderChamfer = value

    @property
    def outer_groove_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OuterGrooveRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @outer_groove_radius.setter
    @enforce_parameter_types
    def outer_groove_radius(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OuterGrooveRadius = value

    @property
    def outer_groove_radius_as_percentage_of_element_diameter(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OuterGrooveRadiusAsPercentageOfElementDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @outer_groove_radius_as_percentage_of_element_diameter.setter
    @enforce_parameter_types
    def outer_groove_radius_as_percentage_of_element_diameter(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OuterGrooveRadiusAsPercentageOfElementDiameter = value

    @property
    def outer_left_shoulder_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OuterLeftShoulderDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @outer_left_shoulder_diameter.setter
    @enforce_parameter_types
    def outer_left_shoulder_diameter(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OuterLeftShoulderDiameter = value

    @property
    def outer_race_osculation(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OuterRaceOsculation

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @outer_race_osculation.setter
    @enforce_parameter_types
    def outer_race_osculation(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OuterRaceOsculation = value

    @property
    def outer_right_shoulder_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OuterRightShoulderDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @outer_right_shoulder_diameter.setter
    @enforce_parameter_types
    def outer_right_shoulder_diameter(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OuterRightShoulderDiameter = value

    @property
    def outer_ring_left_shoulder_height(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterRingLeftShoulderHeight

        if temp is None:
            return 0.0

        return temp

    @outer_ring_left_shoulder_height.setter
    @enforce_parameter_types
    def outer_ring_left_shoulder_height(self: Self, value: "float"):
        self.wrapped.OuterRingLeftShoulderHeight = (
            float(value) if value is not None else 0.0
        )

    @property
    def outer_ring_right_shoulder_height(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterRingRightShoulderHeight

        if temp is None:
            return 0.0

        return temp

    @outer_ring_right_shoulder_height.setter
    @enforce_parameter_types
    def outer_ring_right_shoulder_height(self: Self, value: "float"):
        self.wrapped.OuterRingRightShoulderHeight = (
            float(value) if value is not None else 0.0
        )

    @property
    def outer_ring_shoulder_chamfer(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OuterRingShoulderChamfer

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @outer_ring_shoulder_chamfer.setter
    @enforce_parameter_types
    def outer_ring_shoulder_chamfer(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OuterRingShoulderChamfer = value

    @property
    def relative_curvature_difference_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeCurvatureDifferenceInner

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_curvature_difference_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeCurvatureDifferenceOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def shoulders(self: Self) -> "List[_2161.BallBearingShoulderDefinition]":
        """List[mastapy.bearings.bearing_designs.rolling.BallBearingShoulderDefinition]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Shoulders

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "BallBearing._Cast_BallBearing":
        return self._Cast_BallBearing(self)
