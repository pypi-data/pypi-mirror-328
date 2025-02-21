"""ISO10300SingleFlankRatingHypoidMethodB2"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.iso_10300 import _436
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO10300_SINGLE_FLANK_RATING_HYPOID_METHOD_B2 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Iso10300", "ISO10300SingleFlankRatingHypoidMethodB2"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.iso_10300 import _432
    from mastapy.gears.rating.conical import _546
    from mastapy.gears.rating import _367


__docformat__ = "restructuredtext en"
__all__ = ("ISO10300SingleFlankRatingHypoidMethodB2",)


Self = TypeVar("Self", bound="ISO10300SingleFlankRatingHypoidMethodB2")


class ISO10300SingleFlankRatingHypoidMethodB2(_436.ISO10300SingleFlankRatingMethodB2):
    """ISO10300SingleFlankRatingHypoidMethodB2

    This is a mastapy class.
    """

    TYPE = _ISO10300_SINGLE_FLANK_RATING_HYPOID_METHOD_B2
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ISO10300SingleFlankRatingHypoidMethodB2"
    )

    class _Cast_ISO10300SingleFlankRatingHypoidMethodB2:
        """Special nested class for casting ISO10300SingleFlankRatingHypoidMethodB2 to subclasses."""

        def __init__(
            self: "ISO10300SingleFlankRatingHypoidMethodB2._Cast_ISO10300SingleFlankRatingHypoidMethodB2",
            parent: "ISO10300SingleFlankRatingHypoidMethodB2",
        ):
            self._parent = parent

        @property
        def iso10300_single_flank_rating_method_b2(
            self: "ISO10300SingleFlankRatingHypoidMethodB2._Cast_ISO10300SingleFlankRatingHypoidMethodB2",
        ) -> "_436.ISO10300SingleFlankRatingMethodB2":
            return self._parent._cast(_436.ISO10300SingleFlankRatingMethodB2)

        @property
        def iso10300_single_flank_rating(
            self: "ISO10300SingleFlankRatingHypoidMethodB2._Cast_ISO10300SingleFlankRatingHypoidMethodB2",
        ) -> "_432.ISO10300SingleFlankRating":
            pass

            from mastapy.gears.rating.iso_10300 import _432

            return self._parent._cast(_432.ISO10300SingleFlankRating)

        @property
        def conical_gear_single_flank_rating(
            self: "ISO10300SingleFlankRatingHypoidMethodB2._Cast_ISO10300SingleFlankRatingHypoidMethodB2",
        ) -> "_546.ConicalGearSingleFlankRating":
            from mastapy.gears.rating.conical import _546

            return self._parent._cast(_546.ConicalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(
            self: "ISO10300SingleFlankRatingHypoidMethodB2._Cast_ISO10300SingleFlankRatingHypoidMethodB2",
        ) -> "_367.GearSingleFlankRating":
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.GearSingleFlankRating)

        @property
        def iso10300_single_flank_rating_hypoid_method_b2(
            self: "ISO10300SingleFlankRatingHypoidMethodB2._Cast_ISO10300SingleFlankRatingHypoidMethodB2",
        ) -> "ISO10300SingleFlankRatingHypoidMethodB2":
            return self._parent

        def __getattr__(
            self: "ISO10300SingleFlankRatingHypoidMethodB2._Cast_ISO10300SingleFlankRatingHypoidMethodB2",
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
        self: Self, instance_to_wrap: "ISO10300SingleFlankRatingHypoidMethodB2.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_between_centreline_and_line_from_point_of_load_application_and_fillet_point_on_pinion(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.AngleBetweenCentrelineAndLineFromPointOfLoadApplicationAndFilletPointOnPinion
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def angle_between_centreline_and_line_from_point_of_load_application_and_fillet_point_on_wheel(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.AngleBetweenCentrelineAndLineFromPointOfLoadApplicationAndFilletPointOnWheel
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def auxiliary_value_hn1o(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryValueHN1o

        if temp is None:
            return 0.0

        return temp

    @property
    def auxiliary_value_hn2o(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryValueHN2o

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_shift_due_to_load_for_pinion(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactShiftDueToLoadForPinion

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_shift_due_to_load_for_wheel(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactShiftDueToLoadForWheel

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_from_centreline_to_tool_critical_coast_side_fillet_point(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DistanceFromCentrelineToToolCriticalCoastSideFilletPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_from_centreline_to_tool_critical_drive_side_fillet_point(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DistanceFromCentrelineToToolCriticalDriveSideFilletPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_from_pitch_circle_to_point_of_load_application(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DistanceFromPitchCircleToPointOfLoadApplication

        if temp is None:
            return 0.0

        return temp

    @property
    def generated_pressure_angle_of_wheel_at_fillet_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeneratedPressureAngleOfWheelAtFilletPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def horizontal_distance_from_centreline_to_fillet_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HorizontalDistanceFromCentrelineToFilletPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def intermediate_angle_different_between_beta_c_and_delta_alpha(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IntermediateAngleDifferentBetweenBetaCAndDeltaAlpha

        if temp is None:
            return 0.0

        return temp

    @property
    def intermediate_angle_different_between_beta_d_and_delta_alpha(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IntermediateAngleDifferentBetweenBetaDAndDeltaAlpha

        if temp is None:
            return 0.0

        return temp

    @property
    def intermediate_angle_beta_a(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IntermediateAngleBetaA

        if temp is None:
            return 0.0

        return temp

    @property
    def intermediate_value_g1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IntermediateValueG1

        if temp is None:
            return 0.0

        return temp

    @property
    def intermediate_value_eta_c(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IntermediateValueEtaC

        if temp is None:
            return 0.0

        return temp

    @property
    def intermediate_value_eta_d(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IntermediateValueEtaD

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_angle_between_centreline_and_pinion_fillet(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionAngleBetweenCentrelineAndPinionFillet

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_angle_from_centreline_to_fillet_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionAngleFromCentrelineToFilletPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_angle_from_centreline_to_pinion_tip(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionAngleFromCentrelineToPinionTip

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_angle_from_centreline_to_tooth_surface_at_critical_coast_side_fillet_point(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.PinionAngleFromCentrelineToToothSurfaceAtCriticalCoastSideFilletPoint
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_angle_from_centreline_to_tooth_surface_at_critical_drive_side_fillet_point(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.PinionAngleFromCentrelineToToothSurfaceAtCriticalDriveSideFilletPoint
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_angle_from_pitch_to_point_of_load_application(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionAngleFromPitchToPointOfLoadApplication

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_angle_from_wheel_tip_to_point_of_load_application(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionAngleFromWheelTipToPointOfLoadApplication

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_angle_to_fillet_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionAngleToFilletPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_angle_unbalance_between_fillet_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionAngleUnbalanceBetweenFilletPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_difference_angle_between_tool_and_surface_at_coast_side_fillet_point(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.PinionDifferenceAngleBetweenToolAndSurfaceAtCoastSideFilletPoint
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_difference_angle_between_tool_and_surface_at_drive_side_fillet_point(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.PinionDifferenceAngleBetweenToolAndSurfaceAtDriveSideFilletPoint
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_horizontal_distance_to_critical_fillet_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionHorizontalDistanceToCriticalFilletPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_load_height_at_weakest_section(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionLoadHeightAtWeakestSection

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_pressure_angle_at_point_of_load_application(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionPressureAngleAtPointOfLoadApplication

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_radial_distance_to_point_of_load_application(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionRadialDistanceToPointOfLoadApplication

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_radius_to_fillet_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionRadiusToFilletPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_tooth_strength_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionToothStrengthFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def radius_from_tool_centre_to_critical_pinion_coast_side_fillet_point(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadiusFromToolCentreToCriticalPinionCoastSideFilletPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def radius_from_tool_centre_to_critical_pinion_drive_side_fillet_point(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadiusFromToolCentreToCriticalPinionDriveSideFilletPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_form_factor_for_hypoid_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothFormFactorForHypoidGear

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_radius_to_point_of_load_application_for_pinion(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseRadiusToPointOfLoadApplicationForPinion

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_radius_to_point_of_load_application_for_wheel(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseRadiusToPointOfLoadApplicationForWheel

        if temp is None:
            return 0.0

        return temp

    @property
    def vertical_distance_from_pitch_circle_to_critical_fillet_point(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VerticalDistanceFromPitchCircleToCriticalFilletPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def vertical_distance_from_pitch_circle_to_fillet_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VerticalDistanceFromPitchCircleToFilletPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_angle_between_centreline_and_critical_point_coast_side_fillet_point(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.WheelAngleBetweenCentrelineAndCriticalPointCoastSideFilletPoint
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_angle_between_centreline_and_critical_point_drive_side_fillet_point(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.WheelAngleBetweenCentrelineAndCriticalPointDriveSideFilletPoint
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_angle_between_centreline_and_fillet_point_on_coast_side(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelAngleBetweenCentrelineAndFilletPointOnCoastSide

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_angle_between_centreline_and_fillet_point_on_drive_side(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelAngleBetweenCentrelineAndFilletPointOnDriveSide

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_angle_between_centreline_and_pinion_fillet(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelAngleBetweenCentrelineAndPinionFillet

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_angle_between_fillet_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelAngleBetweenFilletPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_angle_difference_between_path_of_action_and_tooth_surface_at_pinion_fillet(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.WheelAngleDifferenceBetweenPathOfActionAndToothSurfaceAtPinionFillet
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_angle_from_centreline_to_tooth_surface_at_critical_fillet_point_on_coast_side(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.WheelAngleFromCentrelineToToothSurfaceAtCriticalFilletPointOnCoastSide
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_angle_from_centreline_to_tooth_surface_at_critical_fillet_point_on_drive_side(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.WheelAngleFromCentrelineToToothSurfaceAtCriticalFilletPointOnDriveSide
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_angle_from_pinion_tip_to_point_of_load_application(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelAngleFromPinionTipToPointOfLoadApplication

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_difference_angle_between_tool_and_surface_at_coast_side_fillet_point(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.WheelDifferenceAngleBetweenToolAndSurfaceAtCoastSideFilletPoint
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_difference_angle_between_tool_and_surface_at_drive_side_fillet_point(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.WheelDifferenceAngleBetweenToolAndSurfaceAtDriveSideFilletPoint
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_horizontal_distance_from_centreline_to_critical_fillet_point(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelHorizontalDistanceFromCentrelineToCriticalFilletPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_load_height_at_weakest_section(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelLoadHeightAtWeakestSection

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_radius_to_pinion_fillet_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelRadiusToPinionFilletPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_rotation_through_path_of_action(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelRotationThroughPathOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_tooth_strength_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelToothStrengthFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def h3(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.H3

        if temp is None:
            return 0.0

        return temp

    @property
    def h3o(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.H3o

        if temp is None:
            return 0.0

        return temp

    @property
    def h4(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.H4

        if temp is None:
            return 0.0

        return temp

    @property
    def h4o(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.H4o

        if temp is None:
            return 0.0

        return temp

    @property
    def deltar_3(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Deltar3

        if temp is None:
            return 0.0

        return temp

    @property
    def deltar_4(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Deltar4

        if temp is None:
            return 0.0

        return temp

    @property
    def deltar_5(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Deltar5

        if temp is None:
            return 0.0

        return temp

    @property
    def alpha_do(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AlphaDo

        if temp is None:
            return 0.0

        return temp

    @property
    def mu_d2(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MuD2

        if temp is None:
            return 0.0

        return temp

    @property
    def mu_d(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MuD

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ISO10300SingleFlankRatingHypoidMethodB2._Cast_ISO10300SingleFlankRatingHypoidMethodB2":
        return self._Cast_ISO10300SingleFlankRatingHypoidMethodB2(self)
