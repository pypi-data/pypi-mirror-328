"""PowerLoad"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import (
    list_with_selected_item,
    enum_with_selected_value,
    overridable,
)
from mastapy.electric_machines import _1261
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model import _2219
from mastapy.system_model.part_model import _2479
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "PowerLoad")

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2449, _2481, _2464, _2444, _2468
    from mastapy.math_utility.measured_data import _1565
    from mastapy.materials.efficiency import _298
    from mastapy.system_model import _2203


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoad",)


Self = TypeVar("Self", bound="PowerLoad")


class PowerLoad(_2479.VirtualComponent):
    """PowerLoad

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerLoad")

    class _Cast_PowerLoad:
        """Special nested class for casting PowerLoad to subclasses."""

        def __init__(self: "PowerLoad._Cast_PowerLoad", parent: "PowerLoad"):
            self._parent = parent

        @property
        def virtual_component(
            self: "PowerLoad._Cast_PowerLoad",
        ) -> "_2479.VirtualComponent":
            return self._parent._cast(_2479.VirtualComponent)

        @property
        def mountable_component(
            self: "PowerLoad._Cast_PowerLoad",
        ) -> "_2464.MountableComponent":
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.MountableComponent)

        @property
        def component(self: "PowerLoad._Cast_PowerLoad") -> "_2444.Component":
            from mastapy.system_model.part_model import _2444

            return self._parent._cast(_2444.Component)

        @property
        def part(self: "PowerLoad._Cast_PowerLoad") -> "_2468.Part":
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(self: "PowerLoad._Cast_PowerLoad") -> "_2203.DesignEntity":
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def power_load(self: "PowerLoad._Cast_PowerLoad") -> "PowerLoad":
            return self._parent

        def __getattr__(self: "PowerLoad._Cast_PowerLoad", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerLoad.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def effective_length_of_stator(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EffectiveLengthOfStator

        if temp is None:
            return 0.0

        return temp

    @effective_length_of_stator.setter
    @enforce_parameter_types
    def effective_length_of_stator(self: Self, value: "float"):
        self.wrapped.EffectiveLengthOfStator = (
            float(value) if value is not None else 0.0
        )

    @property
    def electric_machine_detail_selector(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_ElectricMachineDetail":
        """ListWithSelectedItem[mastapy.electric_machines.ElectricMachineDetail]"""
        temp = self.wrapped.ElectricMachineDetailSelector

        if temp is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_ElectricMachineDetail",
        )(temp)

    @electric_machine_detail_selector.setter
    @enforce_parameter_types
    def electric_machine_detail_selector(
        self: Self, value: "_1261.ElectricMachineDetail"
    ):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_ElectricMachineDetail.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_ElectricMachineDetail.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.ElectricMachineDetailSelector = value

    @property
    def electric_machine_search_region_specification_method(
        self: Self,
    ) -> "_2449.ElectricMachineSearchRegionSpecificationMethod":
        """mastapy.system_model.part_model.ElectricMachineSearchRegionSpecificationMethod"""
        temp = self.wrapped.ElectricMachineSearchRegionSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.PartModel.ElectricMachineSearchRegionSpecificationMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.part_model._2449",
            "ElectricMachineSearchRegionSpecificationMethod",
        )(value)

    @electric_machine_search_region_specification_method.setter
    @enforce_parameter_types
    def electric_machine_search_region_specification_method(
        self: Self, value: "_2449.ElectricMachineSearchRegionSpecificationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.PartModel.ElectricMachineSearchRegionSpecificationMethod",
        )
        self.wrapped.ElectricMachineSearchRegionSpecificationMethod = value

    @property
    def engine_fuel_consumption_grid(self: Self) -> "_1565.GriddedSurfaceAccessor":
        """mastapy.math_utility.measured_data.GriddedSurfaceAccessor"""
        temp = self.wrapped.EngineFuelConsumptionGrid

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @engine_fuel_consumption_grid.setter
    @enforce_parameter_types
    def engine_fuel_consumption_grid(self: Self, value: "_1565.GriddedSurfaceAccessor"):
        self.wrapped.EngineFuelConsumptionGrid = value.wrapped

    @property
    def engine_torque_grid(self: Self) -> "_1565.GriddedSurfaceAccessor":
        """mastapy.math_utility.measured_data.GriddedSurfaceAccessor"""
        temp = self.wrapped.EngineTorqueGrid

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @engine_torque_grid.setter
    @enforce_parameter_types
    def engine_torque_grid(self: Self, value: "_1565.GriddedSurfaceAccessor"):
        self.wrapped.EngineTorqueGrid = value.wrapped

    @property
    def include_in_torsional_stiffness_calculation(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeInTorsionalStiffnessCalculation

        if temp is None:
            return False

        return temp

    @include_in_torsional_stiffness_calculation.setter
    @enforce_parameter_types
    def include_in_torsional_stiffness_calculation(self: Self, value: "bool"):
        self.wrapped.IncludeInTorsionalStiffnessCalculation = (
            bool(value) if value is not None else False
        )

    @property
    def inner_diameter_of_stator_teeth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerDiameterOfStatorTeeth

        if temp is None:
            return 0.0

        return temp

    @inner_diameter_of_stator_teeth.setter
    @enforce_parameter_types
    def inner_diameter_of_stator_teeth(self: Self, value: "float"):
        self.wrapped.InnerDiameterOfStatorTeeth = (
            float(value) if value is not None else 0.0
        )

    @property
    def number_of_wheels(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfWheels

        if temp is None:
            return 0

        return temp

    @number_of_wheels.setter
    @enforce_parameter_types
    def number_of_wheels(self: Self, value: "int"):
        self.wrapped.NumberOfWheels = int(value) if value is not None else 0

    @property
    def number_of_blades(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfBlades

        if temp is None:
            return 0

        return temp

    @number_of_blades.setter
    @enforce_parameter_types
    def number_of_blades(self: Self, value: "int"):
        self.wrapped.NumberOfBlades = int(value) if value is not None else 0

    @property
    def number_of_slots(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfSlots

        if temp is None:
            return 0

        return temp

    @number_of_slots.setter
    @enforce_parameter_types
    def number_of_slots(self: Self, value: "int"):
        self.wrapped.NumberOfSlots = int(value) if value is not None else 0

    @property
    def positive_is_forwards(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.PositiveIsForwards

        if temp is None:
            return False

        return temp

    @positive_is_forwards.setter
    @enforce_parameter_types
    def positive_is_forwards(self: Self, value: "bool"):
        self.wrapped.PositiveIsForwards = bool(value) if value is not None else False

    @property
    def power_load_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_PowerLoadType":
        """EnumWithSelectedValue[mastapy.system_model.PowerLoadType]"""
        temp = self.wrapped.PowerLoadType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_PowerLoadType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @power_load_type.setter
    @enforce_parameter_types
    def power_load_type(self: Self, value: "_2219.PowerLoadType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_PowerLoadType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.PowerLoadType = value

    @property
    def torsional_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TorsionalStiffness

        if temp is None:
            return 0.0

        return temp

    @torsional_stiffness.setter
    @enforce_parameter_types
    def torsional_stiffness(self: Self, value: "float"):
        self.wrapped.TorsionalStiffness = float(value) if value is not None else 0.0

    @property
    def tyre_rolling_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TyreRollingRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tyre_rolling_radius.setter
    @enforce_parameter_types
    def tyre_rolling_radius(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TyreRollingRadius = value

    @property
    def width_for_drawing(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.WidthForDrawing

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @width_for_drawing.setter
    @enforce_parameter_types
    def width_for_drawing(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.WidthForDrawing = value

    @property
    def electric_machine_detail(self: Self) -> "_1261.ElectricMachineDetail":
        """mastapy.electric_machines.ElectricMachineDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectricMachineDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def oil_pump_detail(self: Self) -> "_298.OilPumpDetail":
        """mastapy.materials.efficiency.OilPumpDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OilPumpDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def single_blade_details(self: Self) -> "_2481.WindTurbineSingleBladeDetails":
        """mastapy.system_model.part_model.WindTurbineSingleBladeDetails

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SingleBladeDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PowerLoad._Cast_PowerLoad":
        return self._Cast_PowerLoad(self)
