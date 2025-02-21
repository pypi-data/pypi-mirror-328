"""LoadedBallBearingRow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results.rolling import _2054
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_BALL_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedBallBearingRow"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import (
        _2022,
        _2021,
        _2004,
        _2007,
        _2033,
        _2038,
        _2057,
        _2072,
        _2075,
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedBallBearingRow",)


Self = TypeVar("Self", bound="LoadedBallBearingRow")


class LoadedBallBearingRow(_2054.LoadedRollingBearingRow):
    """LoadedBallBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_BALL_BEARING_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedBallBearingRow")

    class _Cast_LoadedBallBearingRow:
        """Special nested class for casting LoadedBallBearingRow to subclasses."""

        def __init__(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow",
            parent: "LoadedBallBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow",
        ) -> "_2054.LoadedRollingBearingRow":
            return self._parent._cast(_2054.LoadedRollingBearingRow)

        @property
        def loaded_angular_contact_ball_bearing_row(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow",
        ) -> "_2004.LoadedAngularContactBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2004

            return self._parent._cast(_2004.LoadedAngularContactBallBearingRow)

        @property
        def loaded_angular_contact_thrust_ball_bearing_row(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow",
        ) -> "_2007.LoadedAngularContactThrustBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2007

            return self._parent._cast(_2007.LoadedAngularContactThrustBallBearingRow)

        @property
        def loaded_deep_groove_ball_bearing_row(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow",
        ) -> "_2033.LoadedDeepGrooveBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2033

            return self._parent._cast(_2033.LoadedDeepGrooveBallBearingRow)

        @property
        def loaded_four_point_contact_ball_bearing_row(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow",
        ) -> "_2038.LoadedFourPointContactBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2038

            return self._parent._cast(_2038.LoadedFourPointContactBallBearingRow)

        @property
        def loaded_self_aligning_ball_bearing_row(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow",
        ) -> "_2057.LoadedSelfAligningBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2057

            return self._parent._cast(_2057.LoadedSelfAligningBallBearingRow)

        @property
        def loaded_three_point_contact_ball_bearing_row(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow",
        ) -> "_2072.LoadedThreePointContactBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2072

            return self._parent._cast(_2072.LoadedThreePointContactBallBearingRow)

        @property
        def loaded_thrust_ball_bearing_row(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow",
        ) -> "_2075.LoadedThrustBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2075

            return self._parent._cast(_2075.LoadedThrustBallBearingRow)

        @property
        def loaded_ball_bearing_row(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow",
        ) -> "LoadedBallBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedBallBearingRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_ball_movement(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialBallMovement

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_equivalent_load_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicEquivalentLoadInner

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_equivalent_load_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicEquivalentLoadOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def element_with_worst_track_truncation(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementWithWorstTrackTruncation

        if temp is None:
            return ""

        return temp

    @property
    def hertzian_semi_major_dimension_highest_load_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMajorDimensionHighestLoadInner

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_major_dimension_highest_load_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMajorDimensionHighestLoadOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_minor_dimension_highest_load_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMinorDimensionHighestLoadInner

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_minor_dimension_highest_load_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMinorDimensionHighestLoadOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def smallest_arc_distance_of_raceway_edge_to_hertzian_contact(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmallestArcDistanceOfRacewayEdgeToHertzianContact

        if temp is None:
            return 0.0

        return temp

    @property
    def track_truncation_occurring_beyond_permissible_limit(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TrackTruncationOccurringBeyondPermissibleLimit

        if temp is None:
            return False

        return temp

    @property
    def truncation_warning(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TruncationWarning

        if temp is None:
            return ""

        return temp

    @property
    def worst_hertzian_ellipse_major_2b_track_truncation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstHertzianEllipseMajor2bTrackTruncation

        if temp is None:
            return 0.0

        return temp

    @property
    def loaded_bearing(self: Self) -> "_2022.LoadedBallBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedBallBearingResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def race_results(self: Self) -> "List[_2021.LoadedBallBearingRaceResults]":
        """List[mastapy.bearings.bearing_results.rolling.LoadedBallBearingRaceResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RaceResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "LoadedBallBearingRow._Cast_LoadedBallBearingRow":
        return self._Cast_LoadedBallBearingRow(self)
