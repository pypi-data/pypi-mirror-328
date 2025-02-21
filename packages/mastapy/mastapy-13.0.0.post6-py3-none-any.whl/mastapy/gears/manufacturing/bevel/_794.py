"""ConicalWheelManufacturingConfig"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import
from mastapy.gears.manufacturing.bevel import _776
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_CONICAL_WHEEL_MANUFACTURING_CONFIG = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalWheelManufacturingConfig"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel.basic_machine_settings import _824, _821
    from mastapy.gears.manufacturing.bevel.cutters import _815, _816
    from mastapy.gears.manufacturing.bevel import _778
    from mastapy.gears.analysis import _1221, _1218, _1215


__docformat__ = "restructuredtext en"
__all__ = ("ConicalWheelManufacturingConfig",)


Self = TypeVar("Self", bound="ConicalWheelManufacturingConfig")


class ConicalWheelManufacturingConfig(_776.ConicalGearManufacturingConfig):
    """ConicalWheelManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_WHEEL_MANUFACTURING_CONFIG
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalWheelManufacturingConfig")

    class _Cast_ConicalWheelManufacturingConfig:
        """Special nested class for casting ConicalWheelManufacturingConfig to subclasses."""

        def __init__(
            self: "ConicalWheelManufacturingConfig._Cast_ConicalWheelManufacturingConfig",
            parent: "ConicalWheelManufacturingConfig",
        ):
            self._parent = parent

        @property
        def conical_gear_manufacturing_config(
            self: "ConicalWheelManufacturingConfig._Cast_ConicalWheelManufacturingConfig",
        ) -> "_776.ConicalGearManufacturingConfig":
            return self._parent._cast(_776.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config_base(
            self: "ConicalWheelManufacturingConfig._Cast_ConicalWheelManufacturingConfig",
        ) -> "_778.ConicalGearMicroGeometryConfigBase":
            from mastapy.gears.manufacturing.bevel import _778

            return self._parent._cast(_778.ConicalGearMicroGeometryConfigBase)

        @property
        def gear_implementation_detail(
            self: "ConicalWheelManufacturingConfig._Cast_ConicalWheelManufacturingConfig",
        ) -> "_1221.GearImplementationDetail":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.GearImplementationDetail)

        @property
        def gear_design_analysis(
            self: "ConicalWheelManufacturingConfig._Cast_ConicalWheelManufacturingConfig",
        ) -> "_1218.GearDesignAnalysis":
            from mastapy.gears.analysis import _1218

            return self._parent._cast(_1218.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "ConicalWheelManufacturingConfig._Cast_ConicalWheelManufacturingConfig",
        ) -> "_1215.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearAnalysis)

        @property
        def conical_wheel_manufacturing_config(
            self: "ConicalWheelManufacturingConfig._Cast_ConicalWheelManufacturingConfig",
        ) -> "ConicalWheelManufacturingConfig":
            return self._parent

        def __getattr__(
            self: "ConicalWheelManufacturingConfig._Cast_ConicalWheelManufacturingConfig",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalWheelManufacturingConfig.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def use_cutter_tilt(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseCutterTilt

        if temp is None:
            return False

        return temp

    @use_cutter_tilt.setter
    @enforce_parameter_types
    def use_cutter_tilt(self: Self, value: "bool"):
        self.wrapped.UseCutterTilt = bool(value) if value is not None else False

    @property
    def wheel_finish_manufacturing_machine(self: Self) -> "str":
        """str"""
        temp = self.wrapped.WheelFinishManufacturingMachine.SelectedItemName

        if temp is None:
            return ""

        return temp

    @wheel_finish_manufacturing_machine.setter
    @enforce_parameter_types
    def wheel_finish_manufacturing_machine(self: Self, value: "str"):
        self.wrapped.WheelFinishManufacturingMachine.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def wheel_rough_manufacturing_machine(self: Self) -> "str":
        """str"""
        temp = self.wrapped.WheelRoughManufacturingMachine.SelectedItemName

        if temp is None:
            return ""

        return temp

    @wheel_rough_manufacturing_machine.setter
    @enforce_parameter_types
    def wheel_rough_manufacturing_machine(self: Self, value: "str"):
        self.wrapped.WheelRoughManufacturingMachine.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def specified_cradle_style_machine_settings(
        self: Self,
    ) -> "_824.CradleStyleConicalMachineSettingsGenerated":
        """mastapy.gears.manufacturing.bevel.basic_machine_settings.CradleStyleConicalMachineSettingsGenerated

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecifiedCradleStyleMachineSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def specified_machine_settings(
        self: Self,
    ) -> "_821.BasicConicalGearMachineSettings":
        """mastapy.gears.manufacturing.bevel.basic_machine_settings.BasicConicalGearMachineSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecifiedMachineSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def wheel_finish_cutter(self: Self) -> "_815.WheelFinishCutter":
        """mastapy.gears.manufacturing.bevel.cutters.WheelFinishCutter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelFinishCutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def wheel_rough_cutter(self: Self) -> "_816.WheelRoughCutter":
        """mastapy.gears.manufacturing.bevel.cutters.WheelRoughCutter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelRoughCutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalWheelManufacturingConfig._Cast_ConicalWheelManufacturingConfig":
        return self._Cast_ConicalWheelManufacturingConfig(self)
