"""HobbingProcessProfileCalculation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _666
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_PROFILE_CALCULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "HobbingProcessProfileCalculation",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1026
    from mastapy.utility_gui.charts import _1867
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _662,
        _680,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HobbingProcessProfileCalculation",)


Self = TypeVar("Self", bound="HobbingProcessProfileCalculation")


class HobbingProcessProfileCalculation(_666.HobbingProcessCalculation):
    """HobbingProcessProfileCalculation

    This is a mastapy class.
    """

    TYPE = _HOBBING_PROCESS_PROFILE_CALCULATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HobbingProcessProfileCalculation")

    class _Cast_HobbingProcessProfileCalculation:
        """Special nested class for casting HobbingProcessProfileCalculation to subclasses."""

        def __init__(
            self: "HobbingProcessProfileCalculation._Cast_HobbingProcessProfileCalculation",
            parent: "HobbingProcessProfileCalculation",
        ):
            self._parent = parent

        @property
        def hobbing_process_calculation(
            self: "HobbingProcessProfileCalculation._Cast_HobbingProcessProfileCalculation",
        ) -> "_666.HobbingProcessCalculation":
            return self._parent._cast(_666.HobbingProcessCalculation)

        @property
        def process_calculation(
            self: "HobbingProcessProfileCalculation._Cast_HobbingProcessProfileCalculation",
        ) -> "_680.ProcessCalculation":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _680,
            )

            return self._parent._cast(_680.ProcessCalculation)

        @property
        def hobbing_process_profile_calculation(
            self: "HobbingProcessProfileCalculation._Cast_HobbingProcessProfileCalculation",
        ) -> "HobbingProcessProfileCalculation":
            return self._parent

        def __getattr__(
            self: "HobbingProcessProfileCalculation._Cast_HobbingProcessProfileCalculation",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HobbingProcessProfileCalculation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def chart_display_method(
        self: Self,
    ) -> "_1026.CylindricalGearProfileMeasurementType":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurementType"""
        temp = self.wrapped.ChartDisplayMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearProfileMeasurementType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1026",
            "CylindricalGearProfileMeasurementType",
        )(value)

    @chart_display_method.setter
    @enforce_parameter_types
    def chart_display_method(
        self: Self, value: "_1026.CylindricalGearProfileMeasurementType"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearProfileMeasurementType",
        )
        self.wrapped.ChartDisplayMethod = value

    @property
    def left_flank_profile_modification_chart(
        self: Self,
    ) -> "_1867.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlankProfileModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def number_of_profile_bands(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfProfileBands

        if temp is None:
            return 0

        return temp

    @number_of_profile_bands.setter
    @enforce_parameter_types
    def number_of_profile_bands(self: Self, value: "int"):
        self.wrapped.NumberOfProfileBands = int(value) if value is not None else 0

    @property
    def result_z_plane(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ResultZPlane

        if temp is None:
            return 0.0

        return temp

    @result_z_plane.setter
    @enforce_parameter_types
    def result_z_plane(self: Self, value: "float"):
        self.wrapped.ResultZPlane = float(value) if value is not None else 0.0

    @property
    def right_flank_profile_modification_chart(
        self: Self,
    ) -> "_1867.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlankProfileModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def left_flank(self: Self) -> "_662.CalculateProfileDeviationAccuracy":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.CalculateProfileDeviationAccuracy

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank(self: Self) -> "_662.CalculateProfileDeviationAccuracy":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.CalculateProfileDeviationAccuracy

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "HobbingProcessProfileCalculation._Cast_HobbingProcessProfileCalculation":
        return self._Cast_HobbingProcessProfileCalculation(self)
