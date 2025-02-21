"""AbstractVaryingInputComponent"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.nodal_analysis import _91
from mastapy.nodal_analysis.varying_input_components import _98
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_VARYING_INPUT_COMPONENT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.VaryingInputComponents", "AbstractVaryingInputComponent"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1534
    from mastapy.math_utility.measured_data import _1565
    from mastapy.nodal_analysis.varying_input_components import _94, _95, _96, _97, _99


__docformat__ = "restructuredtext en"
__all__ = ("AbstractVaryingInputComponent",)


Self = TypeVar("Self", bound="AbstractVaryingInputComponent")


class AbstractVaryingInputComponent(_0.APIBase):
    """AbstractVaryingInputComponent

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_VARYING_INPUT_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractVaryingInputComponent")

    class _Cast_AbstractVaryingInputComponent:
        """Special nested class for casting AbstractVaryingInputComponent to subclasses."""

        def __init__(
            self: "AbstractVaryingInputComponent._Cast_AbstractVaryingInputComponent",
            parent: "AbstractVaryingInputComponent",
        ):
            self._parent = parent

        @property
        def angle_input_component(
            self: "AbstractVaryingInputComponent._Cast_AbstractVaryingInputComponent",
        ) -> "_94.AngleInputComponent":
            from mastapy.nodal_analysis.varying_input_components import _94

            return self._parent._cast(_94.AngleInputComponent)

        @property
        def force_input_component(
            self: "AbstractVaryingInputComponent._Cast_AbstractVaryingInputComponent",
        ) -> "_95.ForceInputComponent":
            from mastapy.nodal_analysis.varying_input_components import _95

            return self._parent._cast(_95.ForceInputComponent)

        @property
        def moment_input_component(
            self: "AbstractVaryingInputComponent._Cast_AbstractVaryingInputComponent",
        ) -> "_96.MomentInputComponent":
            from mastapy.nodal_analysis.varying_input_components import _96

            return self._parent._cast(_96.MomentInputComponent)

        @property
        def non_dimensional_input_component(
            self: "AbstractVaryingInputComponent._Cast_AbstractVaryingInputComponent",
        ) -> "_97.NonDimensionalInputComponent":
            from mastapy.nodal_analysis.varying_input_components import _97

            return self._parent._cast(_97.NonDimensionalInputComponent)

        @property
        def velocity_input_component(
            self: "AbstractVaryingInputComponent._Cast_AbstractVaryingInputComponent",
        ) -> "_99.VelocityInputComponent":
            from mastapy.nodal_analysis.varying_input_components import _99

            return self._parent._cast(_99.VelocityInputComponent)

        @property
        def abstract_varying_input_component(
            self: "AbstractVaryingInputComponent._Cast_AbstractVaryingInputComponent",
        ) -> "AbstractVaryingInputComponent":
            return self._parent

        def __getattr__(
            self: "AbstractVaryingInputComponent._Cast_AbstractVaryingInputComponent",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractVaryingInputComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def include_values_before_zero_time(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeValuesBeforeZeroTime

        if temp is None:
            return False

        return temp

    @include_values_before_zero_time.setter
    @enforce_parameter_types
    def include_values_before_zero_time(self: Self, value: "bool"):
        self.wrapped.IncludeValuesBeforeZeroTime = (
            bool(value) if value is not None else False
        )

    @property
    def input_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ValueInputOption":
        """EnumWithSelectedValue[mastapy.nodal_analysis.ValueInputOption]"""
        temp = self.wrapped.InputType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ValueInputOption.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @input_type.setter
    @enforce_parameter_types
    def input_type(self: Self, value: "_91.ValueInputOption"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ValueInputOption.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.InputType = value

    @property
    def single_point_selection_method_for_value_vs_time(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_SinglePointSelectionMethod":
        """EnumWithSelectedValue[mastapy.nodal_analysis.varying_input_components.SinglePointSelectionMethod]"""
        temp = self.wrapped.SinglePointSelectionMethodForValueVsTime

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_SinglePointSelectionMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @single_point_selection_method_for_value_vs_time.setter
    @enforce_parameter_types
    def single_point_selection_method_for_value_vs_time(
        self: Self, value: "_98.SinglePointSelectionMethod"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_SinglePointSelectionMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.SinglePointSelectionMethodForValueVsTime = value

    @property
    def time_profile_repeats(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.TimeProfileRepeats

        if temp is None:
            return False

        return temp

    @time_profile_repeats.setter
    @enforce_parameter_types
    def time_profile_repeats(self: Self, value: "bool"):
        self.wrapped.TimeProfileRepeats = bool(value) if value is not None else False

    @property
    def value_vs_angle(self: Self) -> "_1534.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.ValueVsAngle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @value_vs_angle.setter
    @enforce_parameter_types
    def value_vs_angle(self: Self, value: "_1534.Vector2DListAccessor"):
        self.wrapped.ValueVsAngle = value.wrapped

    @property
    def value_vs_angle_and_speed(self: Self) -> "_1565.GriddedSurfaceAccessor":
        """mastapy.math_utility.measured_data.GriddedSurfaceAccessor"""
        temp = self.wrapped.ValueVsAngleAndSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @value_vs_angle_and_speed.setter
    @enforce_parameter_types
    def value_vs_angle_and_speed(self: Self, value: "_1565.GriddedSurfaceAccessor"):
        self.wrapped.ValueVsAngleAndSpeed = value.wrapped

    @property
    def value_vs_position(self: Self) -> "_1534.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.ValueVsPosition

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @value_vs_position.setter
    @enforce_parameter_types
    def value_vs_position(self: Self, value: "_1534.Vector2DListAccessor"):
        self.wrapped.ValueVsPosition = value.wrapped

    @property
    def value_vs_time(self: Self) -> "_1534.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.ValueVsTime

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @value_vs_time.setter
    @enforce_parameter_types
    def value_vs_time(self: Self, value: "_1534.Vector2DListAccessor"):
        self.wrapped.ValueVsTime = value.wrapped

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
    def cast_to(
        self: Self,
    ) -> "AbstractVaryingInputComponent._Cast_AbstractVaryingInputComponent":
        return self._Cast_AbstractVaryingInputComponent(self)
