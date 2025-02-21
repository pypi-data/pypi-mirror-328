"""HypoidGearSetDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs.agma_gleason_conical import _1195
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Hypoid", "HypoidGearSetDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.hypoid import _985, _986
    from mastapy.gears.gear_designs.conical import _1156
    from mastapy.gears.gear_designs import _950, _948


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetDesign",)


Self = TypeVar("Self", bound="HypoidGearSetDesign")


class HypoidGearSetDesign(_1195.AGMAGleasonConicalGearSetDesign):
    """HypoidGearSetDesign

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearSetDesign")

    class _Cast_HypoidGearSetDesign:
        """Special nested class for casting HypoidGearSetDesign to subclasses."""

        def __init__(
            self: "HypoidGearSetDesign._Cast_HypoidGearSetDesign",
            parent: "HypoidGearSetDesign",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_design(
            self: "HypoidGearSetDesign._Cast_HypoidGearSetDesign",
        ) -> "_1195.AGMAGleasonConicalGearSetDesign":
            return self._parent._cast(_1195.AGMAGleasonConicalGearSetDesign)

        @property
        def conical_gear_set_design(
            self: "HypoidGearSetDesign._Cast_HypoidGearSetDesign",
        ) -> "_1156.ConicalGearSetDesign":
            from mastapy.gears.gear_designs.conical import _1156

            return self._parent._cast(_1156.ConicalGearSetDesign)

        @property
        def gear_set_design(
            self: "HypoidGearSetDesign._Cast_HypoidGearSetDesign",
        ) -> "_950.GearSetDesign":
            from mastapy.gears.gear_designs import _950

            return self._parent._cast(_950.GearSetDesign)

        @property
        def gear_design_component(
            self: "HypoidGearSetDesign._Cast_HypoidGearSetDesign",
        ) -> "_948.GearDesignComponent":
            from mastapy.gears.gear_designs import _948

            return self._parent._cast(_948.GearDesignComponent)

        @property
        def hypoid_gear_set_design(
            self: "HypoidGearSetDesign._Cast_HypoidGearSetDesign",
        ) -> "HypoidGearSetDesign":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetDesign._Cast_HypoidGearSetDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearSetDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_pressure_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AveragePressureAngle

        if temp is None:
            return 0.0

        return temp

    @average_pressure_angle.setter
    @enforce_parameter_types
    def average_pressure_angle(self: Self, value: "float"):
        self.wrapped.AveragePressureAngle = float(value) if value is not None else 0.0

    @property
    def backlash_allowance_max(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BacklashAllowanceMax

        if temp is None:
            return 0.0

        return temp

    @property
    def backlash_allowance_min(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BacklashAllowanceMin

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_crown_gear_addendum_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicCrownGearAddendumFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_crown_gear_dedendum_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicCrownGearDedendumFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Clearance

        if temp is None:
            return 0.0

        return temp

    @property
    def depth_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DepthFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @depth_factor.setter
    @enforce_parameter_types
    def depth_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DepthFactor = value

    @property
    def desired_pinion_spiral_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DesiredPinionSpiralAngle

        if temp is None:
            return 0.0

        return temp

    @desired_pinion_spiral_angle.setter
    @enforce_parameter_types
    def desired_pinion_spiral_angle(self: Self, value: "float"):
        self.wrapped.DesiredPinionSpiralAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def diametral_pitch(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DiametralPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_from_midpoint_of_tooth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DistanceFromMidpointOfTooth

        if temp is None:
            return 0.0

        return temp

    @distance_from_midpoint_of_tooth.setter
    @enforce_parameter_types
    def distance_from_midpoint_of_tooth(self: Self, value: "float"):
        self.wrapped.DistanceFromMidpointOfTooth = (
            float(value) if value is not None else 0.0
        )

    @property
    def elastic_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def face_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def geometry_factor_i(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryFactorI

        if temp is None:
            return 0.0

        return temp

    @property
    def hardness_ratio_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HardnessRatioFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def influence_factor_of_limit_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InfluenceFactorOfLimitPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def limit_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LimitPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_circular_pitch(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanCircularPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_clearance_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MeanClearanceFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @mean_clearance_factor.setter
    @enforce_parameter_types
    def mean_clearance_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MeanClearanceFactor = value

    @property
    def mean_diametral_pitch(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanDiametralPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def modified_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModifiedContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @offset.setter
    @enforce_parameter_types
    def offset(self: Self, value: "float"):
        self.wrapped.Offset = float(value) if value is not None else 0.0

    @property
    def pinion_concave_root_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionConcaveRootPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_convex_root_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionConvexRootPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_face_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionFaceAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_inner_dedendum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionInnerDedendum

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_inner_dedendum_limit(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionInnerDedendumLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_inner_spiral_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionInnerSpiralAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_mean_pitch_concave_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionMeanPitchConcavePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_mean_pitch_convex_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionMeanPitchConvexPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_number_of_teeth(self: Self) -> "int":
        """int"""
        temp = self.wrapped.PinionNumberOfTeeth

        if temp is None:
            return 0

        return temp

    @pinion_number_of_teeth.setter
    @enforce_parameter_types
    def pinion_number_of_teeth(self: Self, value: "int"):
        self.wrapped.PinionNumberOfTeeth = int(value) if value is not None else 0

    @property
    def pinion_offset_angle_in_pitch_plane_at_inner_end(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionOffsetAngleInPitchPlaneAtInnerEnd

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_offset_angle_in_pitch_plane(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionOffsetAngleInPitchPlane

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_offset_angle_in_root_plane(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionOffsetAngleInRootPlane

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_passed_undercut_check(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionPassedUndercutCheck

        if temp is None:
            return False

        return temp

    @property
    def pinion_pitch_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionPitchAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_root_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionRootAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_thickness_modification_coefficient_backlash_included(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionThicknessModificationCoefficientBacklashIncluded

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_limit_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchLimitPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_shift_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileShiftCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def ratio_between_offset_and_wheel_pitch_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RatioBetweenOffsetAndWheelPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @ratio_between_offset_and_wheel_pitch_diameter.setter
    @enforce_parameter_types
    def ratio_between_offset_and_wheel_pitch_diameter(self: Self, value: "float"):
        self.wrapped.RatioBetweenOffsetAndWheelPitchDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def rough_cutter_point_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughCutterPointWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def shaft_angle_departure_from_perpendicular(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftAngleDepartureFromPerpendicular

        if temp is None:
            return 0.0

        return temp

    @property
    def size_factor_bending(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def specified_wheel_addendum_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpecifiedWheelAddendumAngle

        if temp is None:
            return 0.0

        return temp

    @specified_wheel_addendum_angle.setter
    @enforce_parameter_types
    def specified_wheel_addendum_angle(self: Self, value: "float"):
        self.wrapped.SpecifiedWheelAddendumAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def specified_wheel_dedendum_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpecifiedWheelDedendumAngle

        if temp is None:
            return 0.0

        return temp

    @specified_wheel_dedendum_angle.setter
    @enforce_parameter_types
    def specified_wheel_dedendum_angle(self: Self, value: "float"):
        self.wrapped.SpecifiedWheelDedendumAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def stock_allowance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StockAllowance

        if temp is None:
            return 0.0

        return temp

    @stock_allowance.setter
    @enforce_parameter_types
    def stock_allowance(self: Self, value: "float"):
        self.wrapped.StockAllowance = float(value) if value is not None else 0.0

    @property
    def strength_balance_obtained(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrengthBalanceObtained

        if temp is None:
            return 0.0

        return temp

    @property
    def thickness_modification_coefficient_theoretical(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThicknessModificationCoefficientTheoretical

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_thickness_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothThicknessFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def total_number_of_teeth(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalNumberOfTeeth

        if temp is None:
            return 0

        return temp

    @property
    def wheel_addendum_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.WheelAddendumFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @wheel_addendum_factor.setter
    @enforce_parameter_types
    def wheel_addendum_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.WheelAddendumFactor = value

    @property
    def wheel_face_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelFaceAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_face_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelFaceWidth

        if temp is None:
            return 0.0

        return temp

    @wheel_face_width.setter
    @enforce_parameter_types
    def wheel_face_width(self: Self, value: "float"):
        self.wrapped.WheelFaceWidth = float(value) if value is not None else 0.0

    @property
    def wheel_finish_cutter_point_width(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.WheelFinishCutterPointWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @wheel_finish_cutter_point_width.setter
    @enforce_parameter_types
    def wheel_finish_cutter_point_width(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.WheelFinishCutterPointWidth = value

    @property
    def wheel_finish_cutter_point_width_suppressed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelFinishCutterPointWidthSuppressed

        if temp is None:
            return 0.0

        return temp

    @wheel_finish_cutter_point_width_suppressed.setter
    @enforce_parameter_types
    def wheel_finish_cutter_point_width_suppressed(self: Self, value: "float"):
        self.wrapped.WheelFinishCutterPointWidthSuppressed = (
            float(value) if value is not None else 0.0
        )

    @property
    def wheel_inner_blade_angle_convex(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelInnerBladeAngleConvex

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_inner_cone_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelInnerConeDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_inner_pitch_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelInnerPitchRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_inner_spiral_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelInnerSpiralAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_inside_point_to_cross_point_along_wheel_axis(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelInsidePointToCrossPointAlongWheelAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_mean_whole_depth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelMeanWholeDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_mean_working_depth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelMeanWorkingDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_number_of_teeth(self: Self) -> "int":
        """int"""
        temp = self.wrapped.WheelNumberOfTeeth

        if temp is None:
            return 0

        return temp

    @wheel_number_of_teeth.setter
    @enforce_parameter_types
    def wheel_number_of_teeth(self: Self, value: "int"):
        self.wrapped.WheelNumberOfTeeth = int(value) if value is not None else 0

    @property
    def wheel_outer_blade_angle_concave(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelOuterBladeAngleConcave

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_outer_spiral_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelOuterSpiralAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_pitch_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelPitchAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_pitch_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @wheel_pitch_diameter.setter
    @enforce_parameter_types
    def wheel_pitch_diameter(self: Self, value: "float"):
        self.wrapped.WheelPitchDiameter = float(value) if value is not None else 0.0

    @property
    def wheel_root_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelRootAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_thickness_modification_coefficient_backlash_included(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelThicknessModificationCoefficientBacklashIncluded

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_whole_depth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelWholeDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_working_depth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelWorkingDepth

        if temp is None:
            return 0.0

        return temp

    @wheel_working_depth.setter
    @enforce_parameter_types
    def wheel_working_depth(self: Self, value: "float"):
        self.wrapped.WheelWorkingDepth = float(value) if value is not None else 0.0

    @property
    def gears(self: Self) -> "List[_985.HypoidGearDesign]":
        """List[mastapy.gears.gear_designs.hypoid.HypoidGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_gears(self: Self) -> "List[_985.HypoidGearDesign]":
        """List[mastapy.gears.gear_designs.hypoid.HypoidGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes(self: Self) -> "List[_986.HypoidGearMeshDesign]":
        """List[mastapy.gears.gear_designs.hypoid.HypoidGearMeshDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Meshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes(self: Self) -> "List[_986.HypoidGearMeshDesign]":
        """List[mastapy.gears.gear_designs.hypoid.HypoidGearMeshDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "HypoidGearSetDesign._Cast_HypoidGearSetDesign":
        return self._Cast_HypoidGearSetDesign(self)
