"""ProcessSimulationInput"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PROCESS_SIMULATION_INPUT = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "ProcessSimulationInput",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _659,
        _663,
        _664,
        _690,
        _665,
        _672,
        _699,
    )
    from mastapy.math_utility import _1534


__docformat__ = "restructuredtext en"
__all__ = ("ProcessSimulationInput",)


Self = TypeVar("Self", bound="ProcessSimulationInput")


class ProcessSimulationInput(_0.APIBase):
    """ProcessSimulationInput

    This is a mastapy class.
    """

    TYPE = _PROCESS_SIMULATION_INPUT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ProcessSimulationInput")

    class _Cast_ProcessSimulationInput:
        """Special nested class for casting ProcessSimulationInput to subclasses."""

        def __init__(
            self: "ProcessSimulationInput._Cast_ProcessSimulationInput",
            parent: "ProcessSimulationInput",
        ):
            self._parent = parent

        @property
        def hobbing_process_simulation_input(
            self: "ProcessSimulationInput._Cast_ProcessSimulationInput",
        ) -> "_672.HobbingProcessSimulationInput":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _672,
            )

            return self._parent._cast(_672.HobbingProcessSimulationInput)

        @property
        def worm_grinding_process_simulation_input(
            self: "ProcessSimulationInput._Cast_ProcessSimulationInput",
        ) -> "_699.WormGrindingProcessSimulationInput":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _699,
            )

            return self._parent._cast(_699.WormGrindingProcessSimulationInput)

        @property
        def process_simulation_input(
            self: "ProcessSimulationInput._Cast_ProcessSimulationInput",
        ) -> "ProcessSimulationInput":
            return self._parent

        def __getattr__(
            self: "ProcessSimulationInput._Cast_ProcessSimulationInput", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ProcessSimulationInput.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_setting(self: Self) -> "_659.AnalysisMethod":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.AnalysisMethod"""
        temp = self.wrapped.AnalysisSetting

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew.AnalysisMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new._659",
            "AnalysisMethod",
        )(value)

    @analysis_setting.setter
    @enforce_parameter_types
    def analysis_setting(self: Self, value: "_659.AnalysisMethod"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew.AnalysisMethod",
        )
        self.wrapped.AnalysisSetting = value

    @property
    def centre_distance_offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CentreDistanceOffset

        if temp is None:
            return 0.0

        return temp

    @centre_distance_offset.setter
    @enforce_parameter_types
    def centre_distance_offset(self: Self, value: "float"):
        self.wrapped.CentreDistanceOffset = float(value) if value is not None else 0.0

    @property
    def centre_distance_offset_specification_method(
        self: Self,
    ) -> "_663.CentreDistanceOffsetMethod":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.CentreDistanceOffsetMethod"""
        temp = self.wrapped.CentreDistanceOffsetSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew.CentreDistanceOffsetMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new._663",
            "CentreDistanceOffsetMethod",
        )(value)

    @centre_distance_offset_specification_method.setter
    @enforce_parameter_types
    def centre_distance_offset_specification_method(
        self: Self, value: "_663.CentreDistanceOffsetMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew.CentreDistanceOffsetMethod",
        )
        self.wrapped.CentreDistanceOffsetSpecificationMethod = value

    @property
    def feed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Feed

        if temp is None:
            return 0.0

        return temp

    @feed.setter
    @enforce_parameter_types
    def feed(self: Self, value: "float"):
        self.wrapped.Feed = float(value) if value is not None else 0.0

    @property
    def gear_design_lead_crown_modification(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GearDesignLeadCrownModification

        if temp is None:
            return 0.0

        return temp

    @gear_design_lead_crown_modification.setter
    @enforce_parameter_types
    def gear_design_lead_crown_modification(self: Self, value: "float"):
        self.wrapped.GearDesignLeadCrownModification = (
            float(value) if value is not None else 0.0
        )

    @property
    def gear_designed_lead_crown_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GearDesignedLeadCrownLength

        if temp is None:
            return 0.0

        return temp

    @gear_designed_lead_crown_length.setter
    @enforce_parameter_types
    def gear_designed_lead_crown_length(self: Self, value: "float"):
        self.wrapped.GearDesignedLeadCrownLength = (
            float(value) if value is not None else 0.0
        )

    @property
    def shaft_angle_offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShaftAngleOffset

        if temp is None:
            return 0.0

        return temp

    @shaft_angle_offset.setter
    @enforce_parameter_types
    def shaft_angle_offset(self: Self, value: "float"):
        self.wrapped.ShaftAngleOffset = float(value) if value is not None else 0.0

    @property
    def start_height_above_the_gear_center(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartHeightAboveTheGearCenter

        if temp is None:
            return 0.0

        return temp

    @start_height_above_the_gear_center.setter
    @enforce_parameter_types
    def start_height_above_the_gear_center(self: Self, value: "float"):
        self.wrapped.StartHeightAboveTheGearCenter = (
            float(value) if value is not None else 0.0
        )

    @property
    def tooth_index(self: Self) -> "int":
        """int"""
        temp = self.wrapped.ToothIndex

        if temp is None:
            return 0

        return temp

    @tooth_index.setter
    @enforce_parameter_types
    def tooth_index(self: Self, value: "int"):
        self.wrapped.ToothIndex = int(value) if value is not None else 0

    @property
    def user_specified_center_distance_offset_relative_to_cutter_height(
        self: Self,
    ) -> "_1534.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.UserSpecifiedCenterDistanceOffsetRelativeToCutterHeight

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @user_specified_center_distance_offset_relative_to_cutter_height.setter
    @enforce_parameter_types
    def user_specified_center_distance_offset_relative_to_cutter_height(
        self: Self, value: "_1534.Vector2DListAccessor"
    ):
        self.wrapped.UserSpecifiedCenterDistanceOffsetRelativeToCutterHeight = (
            value.wrapped
        )

    @property
    def cutter_head_slide_error(self: Self) -> "_664.CutterHeadSlideError":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.CutterHeadSlideError

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CutterHeadSlideError

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cutter_mounting_error(self: Self) -> "_690.RackMountingError":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.RackMountingError

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CutterMountingError

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_mounting_error(self: Self) -> "_665.GearMountingError":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.GearMountingError

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMountingError

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def cast_to(self: Self) -> "ProcessSimulationInput._Cast_ProcessSimulationInput":
        return self._Cast_ProcessSimulationInput(self)
