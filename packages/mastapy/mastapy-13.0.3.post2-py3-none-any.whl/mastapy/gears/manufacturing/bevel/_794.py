"""ConicalSetManufacturingConfig"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.gears.gear_designs.conical import _1175, _1176
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.gears.manufacturing.bevel import _796
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_SET_MANUFACTURING_CONFIG = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalSetManufacturingConfig"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel import _779, _788
    from mastapy.gears.analysis import _1249, _1244, _1235


__docformat__ = "restructuredtext en"
__all__ = ("ConicalSetManufacturingConfig",)


Self = TypeVar("Self", bound="ConicalSetManufacturingConfig")


class ConicalSetManufacturingConfig(_796.ConicalSetMicroGeometryConfigBase):
    """ConicalSetManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_SET_MANUFACTURING_CONFIG
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalSetManufacturingConfig")

    class _Cast_ConicalSetManufacturingConfig:
        """Special nested class for casting ConicalSetManufacturingConfig to subclasses."""

        def __init__(
            self: "ConicalSetManufacturingConfig._Cast_ConicalSetManufacturingConfig",
            parent: "ConicalSetManufacturingConfig",
        ):
            self._parent = parent

        @property
        def conical_set_micro_geometry_config_base(
            self: "ConicalSetManufacturingConfig._Cast_ConicalSetManufacturingConfig",
        ) -> "_796.ConicalSetMicroGeometryConfigBase":
            return self._parent._cast(_796.ConicalSetMicroGeometryConfigBase)

        @property
        def gear_set_implementation_detail(
            self: "ConicalSetManufacturingConfig._Cast_ConicalSetManufacturingConfig",
        ) -> "_1249.GearSetImplementationDetail":
            from mastapy.gears.analysis import _1249

            return self._parent._cast(_1249.GearSetImplementationDetail)

        @property
        def gear_set_design_analysis(
            self: "ConicalSetManufacturingConfig._Cast_ConicalSetManufacturingConfig",
        ) -> "_1244.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1244

            return self._parent._cast(_1244.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "ConicalSetManufacturingConfig._Cast_ConicalSetManufacturingConfig",
        ) -> "_1235.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1235

            return self._parent._cast(_1235.AbstractGearSetAnalysis)

        @property
        def conical_set_manufacturing_config(
            self: "ConicalSetManufacturingConfig._Cast_ConicalSetManufacturingConfig",
        ) -> "ConicalSetManufacturingConfig":
            return self._parent

        def __getattr__(
            self: "ConicalSetManufacturingConfig._Cast_ConicalSetManufacturingConfig",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalSetManufacturingConfig.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def machine_setting_calculation_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ConicalMachineSettingCalculationMethods":
        """EnumWithSelectedValue[mastapy.gears.gear_designs.conical.ConicalMachineSettingCalculationMethods]"""
        temp = self.wrapped.MachineSettingCalculationMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ConicalMachineSettingCalculationMethods.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @machine_setting_calculation_method.setter
    @enforce_parameter_types
    def machine_setting_calculation_method(
        self: Self, value: "_1175.ConicalMachineSettingCalculationMethods"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ConicalMachineSettingCalculationMethods.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.MachineSettingCalculationMethod = value

    @property
    def manufacture_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ConicalManufactureMethods":
        """EnumWithSelectedValue[mastapy.gears.gear_designs.conical.ConicalManufactureMethods]"""
        temp = self.wrapped.ManufactureMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ConicalManufactureMethods.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @manufacture_method.setter
    @enforce_parameter_types
    def manufacture_method(self: Self, value: "_1176.ConicalManufactureMethods"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ConicalManufactureMethods.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ManufactureMethod = value

    @property
    def gear_manufacturing_configurations(
        self: Self,
    ) -> "List[_779.ConicalGearManufacturingConfig]":
        """List[mastapy.gears.manufacturing.bevel.ConicalGearManufacturingConfig]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearManufacturingConfigurations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes(self: Self) -> "List[_788.ConicalMeshManufacturingConfig]":
        """List[mastapy.gears.manufacturing.bevel.ConicalMeshManufacturingConfig]

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

    def duplicate(self: Self) -> "ConicalSetManufacturingConfig":
        """mastapy.gears.manufacturing.bevel.ConicalSetManufacturingConfig"""
        method_result = self.wrapped.Duplicate()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalSetManufacturingConfig._Cast_ConicalSetManufacturingConfig":
        return self._Cast_ConicalSetManufacturingConfig(self)
