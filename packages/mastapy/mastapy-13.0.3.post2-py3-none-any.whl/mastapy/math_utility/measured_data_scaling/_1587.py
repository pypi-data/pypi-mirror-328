"""DataScalingOptions"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.math_utility import _1524
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.utility.units_and_measurements.measurements import (
    _1630,
    _1631,
    _1635,
    _1639,
    _1647,
    _1654,
    _1660,
    _1666,
    _1694,
    _1702,
    _1683,
    _1707,
    _1708,
    _1712,
    _1711,
    _1717,
    _1727,
    _1685,
    _1741,
    _1633,
    _1657,
    _1750,
    _1732,
    _1733,
    _1744,
    _1745,
    _1743,
    _1706,
    _1749,
    _1688,
    _1742,
    _1634,
)
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_SCALING_OPTIONS = python_net_import(
    "SMT.MastaAPI.MathUtility.MeasuredDataScaling", "DataScalingOptions"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1508
    from mastapy.math_utility.measured_data_scaling import _1588


__docformat__ = "restructuredtext en"
__all__ = ("DataScalingOptions",)


Self = TypeVar("Self", bound="DataScalingOptions")


class DataScalingOptions(_0.APIBase):
    """DataScalingOptions

    This is a mastapy class.
    """

    TYPE = _DATA_SCALING_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DataScalingOptions")

    class _Cast_DataScalingOptions:
        """Special nested class for casting DataScalingOptions to subclasses."""

        def __init__(
            self: "DataScalingOptions._Cast_DataScalingOptions",
            parent: "DataScalingOptions",
        ):
            self._parent = parent

        @property
        def data_scaling_options(
            self: "DataScalingOptions._Cast_DataScalingOptions",
        ) -> "DataScalingOptions":
            return self._parent

        def __getattr__(self: "DataScalingOptions._Cast_DataScalingOptions", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DataScalingOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def dynamic_scaling(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling":
        """EnumWithSelectedValue[mastapy.math_utility.DynamicsResponseScaling]"""
        temp = self.wrapped.DynamicScaling

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @dynamic_scaling.setter
    @enforce_parameter_types
    def dynamic_scaling(self: Self, value: "_1524.DynamicsResponseScaling"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DynamicScaling = value

    @property
    def weighting(self: Self) -> "_1508.AcousticWeighting":
        """mastapy.math_utility.AcousticWeighting"""
        temp = self.wrapped.Weighting

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.MathUtility.AcousticWeighting"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.math_utility._1508", "AcousticWeighting"
        )(value)

    @weighting.setter
    @enforce_parameter_types
    def weighting(self: Self, value: "_1508.AcousticWeighting"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.MathUtility.AcousticWeighting"
        )
        self.wrapped.Weighting = value

    @property
    def acceleration_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1630.Acceleration]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Acceleration]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AccelerationReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1630.Acceleration](temp)

    @property
    def angle_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1631.Angle]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Angle]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngleReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1631.Angle](temp)

    @property
    def angular_acceleration_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1635.AngularAcceleration]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.AngularAcceleration]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularAccelerationReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1635.AngularAcceleration](
            temp
        )

    @property
    def angular_velocity_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1639.AngularVelocity]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.AngularVelocity]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularVelocityReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1639.AngularVelocity](temp)

    @property
    def damage_rate(self: Self) -> "_1588.DataScalingReferenceValues[_1647.DamageRate]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.DamageRate]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DamageRate

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1647.DamageRate](temp)

    @property
    def energy_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1654.Energy]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Energy]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EnergyReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1654.Energy](temp)

    @property
    def force_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1660.Force]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Force]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1660.Force](temp)

    @property
    def frequency_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1666.Frequency]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Frequency]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrequencyReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1666.Frequency](temp)

    @property
    def linear_stiffness_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1694.LinearStiffness]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.LinearStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearStiffnessReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1694.LinearStiffness](temp)

    @property
    def mass_per_unit_time_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1702.MassPerUnitTime]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.MassPerUnitTime]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPerUnitTimeReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1702.MassPerUnitTime](temp)

    @property
    def medium_length_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1683.LengthMedium]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.LengthMedium]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MediumLengthReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1683.LengthMedium](temp)

    @property
    def percentage(self: Self) -> "_1588.DataScalingReferenceValues[_1707.Percentage]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Percentage]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Percentage

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1707.Percentage](temp)

    @property
    def power_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1708.Power]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Power]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1708.Power](temp)

    @property
    def power_small_per_unit_area_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1712.PowerSmallPerArea]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.PowerSmallPerArea]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerSmallPerUnitAreaReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1712.PowerSmallPerArea](
            temp
        )

    @property
    def power_small_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1711.PowerSmall]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.PowerSmall]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerSmallReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1711.PowerSmall](temp)

    @property
    def pressure_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1717.Pressure]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Pressure]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PressureReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1717.Pressure](temp)

    @property
    def safety_factor(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1727.SafetyFactor]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.SafetyFactor]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1727.SafetyFactor](temp)

    @property
    def short_length_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1685.LengthShort]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.LengthShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShortLengthReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1685.LengthShort](temp)

    @property
    def short_time_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1741.TimeShort]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.TimeShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShortTimeReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1741.TimeShort](temp)

    @property
    def small_angle_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1633.AngleSmall]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.AngleSmall]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmallAngleReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1633.AngleSmall](temp)

    @property
    def small_energy_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1657.EnergySmall]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.EnergySmall]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmallEnergyReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1657.EnergySmall](temp)

    @property
    def small_velocity_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1750.VelocitySmall]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.VelocitySmall]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmallVelocityReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1750.VelocitySmall](temp)

    @property
    def stress_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1732.Stress]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Stress]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1732.Stress](temp)

    @property
    def temperature_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1733.Temperature]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Temperature]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TemperatureReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1733.Temperature](temp)

    @property
    def torque_converter_inverse_k(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1744.TorqueConverterInverseK]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.TorqueConverterInverseK]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueConverterInverseK

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _1744.TorqueConverterInverseK
        ](temp)

    @property
    def torque_converter_k(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1745.TorqueConverterK]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.TorqueConverterK]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueConverterK

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1745.TorqueConverterK](
            temp
        )

    @property
    def torque_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1743.Torque]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Torque]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1743.Torque](temp)

    @property
    def unmeasureable(self: Self) -> "_1588.DataScalingReferenceValues[_1706.Number]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Number]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Unmeasureable

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1706.Number](temp)

    @property
    def velocity_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1749.Velocity]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Velocity]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VelocityReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1749.Velocity](temp)

    @property
    def very_short_length_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1688.LengthVeryShort]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.LengthVeryShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VeryShortLengthReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1688.LengthVeryShort](temp)

    @property
    def very_short_time_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1742.TimeVeryShort]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.TimeVeryShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VeryShortTimeReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1742.TimeVeryShort](temp)

    @property
    def very_small_angle_reference_values(
        self: Self,
    ) -> "_1588.DataScalingReferenceValues[_1634.AngleVerySmall]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.AngleVerySmall]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VerySmallAngleReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1634.AngleVerySmall](temp)

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "DataScalingOptions._Cast_DataScalingOptions":
        return self._Cast_DataScalingOptions(self)
