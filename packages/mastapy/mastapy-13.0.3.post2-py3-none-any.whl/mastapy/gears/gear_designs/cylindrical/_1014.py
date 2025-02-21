"""Customer102DataSheetTolerances"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Any, Union, Tuple, List
from enum import Enum

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOMER_102_DATA_SHEET_TOLERANCES = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "Customer102DataSheetTolerances"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
        _1156,
        _1153,
        _1157,
    )
    from mastapy.gears.gear_designs.cylindrical import _1015


__docformat__ = "restructuredtext en"
__all__ = ("Customer102DataSheetTolerances",)


Self = TypeVar("Self", bound="Customer102DataSheetTolerances")


class Customer102DataSheetTolerances(_0.APIBase):
    """Customer102DataSheetTolerances

    This is a mastapy class.
    """

    TYPE = _CUSTOMER_102_DATA_SHEET_TOLERANCES

    class EatonManufacturingOptionsEnum(Enum):
        """EatonManufacturingOptionsEnum is a nested enum."""

        @classmethod
        def type_(cls):
            return _CUSTOMER_102_DATA_SHEET_TOLERANCES.EatonManufacturingOptionsEnum

        SHAVED = 0
        FLANK_AND_FULL_FILLET_GROUND_CBN = 1
        FLANK_ONLY_GROUND_CBN = 2
        FLANK_ONLY_GROUND_VITREOUS_WHEEL = 3
        FLANK_ONLY_FINE_HONE = 4
        FINISH_HOBSHAPERBROACH = 5

    def __enum_setattr(self: Self, attr: str, value: Any):
        raise AttributeError("Cannot set the attributes of an Enum.") from None

    def __enum_delattr(self: Self, attr: str):
        raise AttributeError("Cannot delete the attributes of an Enum.") from None

    EatonManufacturingOptionsEnum.__setattr__ = __enum_setattr
    EatonManufacturingOptionsEnum.__delattr__ = __enum_delattr
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Customer102DataSheetTolerances")

    class _Cast_Customer102DataSheetTolerances:
        """Special nested class for casting Customer102DataSheetTolerances to subclasses."""

        def __init__(
            self: "Customer102DataSheetTolerances._Cast_Customer102DataSheetTolerances",
            parent: "Customer102DataSheetTolerances",
        ):
            self._parent = parent

        @property
        def customer_102_data_sheet_tolerances(
            self: "Customer102DataSheetTolerances._Cast_Customer102DataSheetTolerances",
        ) -> "Customer102DataSheetTolerances":
            return self._parent

        def __getattr__(
            self: "Customer102DataSheetTolerances._Cast_Customer102DataSheetTolerances",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Customer102DataSheetTolerances.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crowning_tolerance(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CrowningTolerance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @crowning_tolerance.setter
    @enforce_parameter_types
    def crowning_tolerance(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CrowningTolerance = value

    @property
    def customer_102_manufacturing_options(
        self: Self,
    ) -> "Customer102DataSheetTolerances.EatonManufacturingOptionsEnum":
        """mastapy.gears.gear_designs.cylindrical.Customer102DataSheetTolerances.EatonManufacturingOptionsEnum"""
        temp = self.wrapped.Customer102ManufacturingOptions

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.Customer102DataSheetTolerances+EatonManufacturingOptionsEnum",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical.Customer102DataSheetTolerances.Customer102DataSheetTolerances",
            "EatonManufacturingOptionsEnum",
        )(value)

    @customer_102_manufacturing_options.setter
    @enforce_parameter_types
    def customer_102_manufacturing_options(
        self: Self,
        value: "Customer102DataSheetTolerances.EatonManufacturingOptionsEnum",
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.Customer102DataSheetTolerances+EatonManufacturingOptionsEnum",
        )
        self.wrapped.Customer102ManufacturingOptions = value

    @property
    def high_point_max(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.HighPointMax

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @high_point_max.setter
    @enforce_parameter_types
    def high_point_max(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.HighPointMax = value

    @property
    def high_point_min(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.HighPointMin

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @high_point_min.setter
    @enforce_parameter_types
    def high_point_min(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.HighPointMin = value

    @property
    def involute_variation(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InvoluteVariation

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @involute_variation.setter
    @enforce_parameter_types
    def involute_variation(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InvoluteVariation = value

    @property
    def lead_range(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadRange

        if temp is None:
            return 0.0

        return temp

    @property
    def lead_variation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadVariation

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_range(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchRange

        if temp is None:
            return 0.0

        return temp

    @property
    def quality_number_lead(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.QualityNumberLead

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @quality_number_lead.setter
    @enforce_parameter_types
    def quality_number_lead(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.QualityNumberLead = value

    @property
    def quality_number_runout(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.QualityNumberRunout

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @quality_number_runout.setter
    @enforce_parameter_types
    def quality_number_runout(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.QualityNumberRunout = value

    @property
    def quality_number_tooth_tooth(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.QualityNumberToothTooth

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @quality_number_tooth_tooth.setter
    @enforce_parameter_types
    def quality_number_tooth_tooth(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.QualityNumberToothTooth = value

    @property
    def specify_upper_and_lower_limits_separately(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyUpperAndLowerLimitsSeparately

        if temp is None:
            return False

        return temp

    @specify_upper_and_lower_limits_separately.setter
    @enforce_parameter_types
    def specify_upper_and_lower_limits_separately(self: Self, value: "bool"):
        self.wrapped.SpecifyUpperAndLowerLimitsSeparately = (
            bool(value) if value is not None else False
        )

    @property
    def use_mast_as_accuracy_grades(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseMASTAsAccuracyGrades

        if temp is None:
            return False

        return temp

    @use_mast_as_accuracy_grades.setter
    @enforce_parameter_types
    def use_mast_as_accuracy_grades(self: Self, value: "bool"):
        self.wrapped.UseMASTAsAccuracyGrades = (
            bool(value) if value is not None else False
        )

    @property
    def accuracy_grades_specified_accuracy(
        self: Self,
    ) -> "_1156.CylindricalAccuracyGrades":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.CylindricalAccuracyGrades

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AccuracyGradesSpecifiedAccuracy

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def customer_102agma2000_accuracy_grader(
        self: Self,
    ) -> "_1153.Customer102AGMA2000AccuracyGrader":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.Customer102AGMA2000AccuracyGrader

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Customer102AGMA2000AccuracyGrader

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_accuracy_tolerances(
        self: Self,
    ) -> "_1157.CylindricalGearAccuracyTolerances":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.CylindricalGearAccuracyTolerances

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearAccuracyTolerances

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def customer_102_tolerance_definitions(
        self: Self,
    ) -> "List[_1015.Customer102ToleranceDefinition]":
        """List[mastapy.gears.gear_designs.cylindrical.Customer102ToleranceDefinition]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Customer102ToleranceDefinitions

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

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
    ) -> "Customer102DataSheetTolerances._Cast_Customer102DataSheetTolerances":
        return self._Cast_Customer102DataSheetTolerances(self)
