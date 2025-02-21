"""ConicalGearToothSurface"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_TOOTH_SURFACE = python_net_import(
    "SMT.MastaAPI.Gears", "ConicalGearToothSurface"
)

if TYPE_CHECKING:
    from mastapy.gears import _327
    from mastapy.gears.manufacturing.bevel import (
        _780,
        _801,
        _802,
        _804,
        _806,
        _807,
        _808,
        _809,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearToothSurface",)


Self = TypeVar("Self", bound="ConicalGearToothSurface")


class ConicalGearToothSurface(_0.APIBase):
    """ConicalGearToothSurface

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_TOOTH_SURFACE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearToothSurface")

    class _Cast_ConicalGearToothSurface:
        """Special nested class for casting ConicalGearToothSurface to subclasses."""

        def __init__(
            self: "ConicalGearToothSurface._Cast_ConicalGearToothSurface",
            parent: "ConicalGearToothSurface",
        ):
            self._parent = parent

        @property
        def gear_nurbs_surface(
            self: "ConicalGearToothSurface._Cast_ConicalGearToothSurface",
        ) -> "_327.GearNURBSSurface":
            from mastapy.gears import _327

            return self._parent._cast(_327.GearNURBSSurface)

        @property
        def conical_meshed_wheel_flank_manufacturing_config(
            self: "ConicalGearToothSurface._Cast_ConicalGearToothSurface",
        ) -> "_780.ConicalMeshedWheelFlankManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _780

            return self._parent._cast(_780.ConicalMeshedWheelFlankManufacturingConfig)

        @property
        def pinion_bevel_generating_modified_roll_machine_settings(
            self: "ConicalGearToothSurface._Cast_ConicalGearToothSurface",
        ) -> "_801.PinionBevelGeneratingModifiedRollMachineSettings":
            from mastapy.gears.manufacturing.bevel import _801

            return self._parent._cast(
                _801.PinionBevelGeneratingModifiedRollMachineSettings
            )

        @property
        def pinion_bevel_generating_tilt_machine_settings(
            self: "ConicalGearToothSurface._Cast_ConicalGearToothSurface",
        ) -> "_802.PinionBevelGeneratingTiltMachineSettings":
            from mastapy.gears.manufacturing.bevel import _802

            return self._parent._cast(_802.PinionBevelGeneratingTiltMachineSettings)

        @property
        def pinion_conical_machine_settings_specified(
            self: "ConicalGearToothSurface._Cast_ConicalGearToothSurface",
        ) -> "_804.PinionConicalMachineSettingsSpecified":
            from mastapy.gears.manufacturing.bevel import _804

            return self._parent._cast(_804.PinionConicalMachineSettingsSpecified)

        @property
        def pinion_finish_machine_settings(
            self: "ConicalGearToothSurface._Cast_ConicalGearToothSurface",
        ) -> "_806.PinionFinishMachineSettings":
            from mastapy.gears.manufacturing.bevel import _806

            return self._parent._cast(_806.PinionFinishMachineSettings)

        @property
        def pinion_hypoid_formate_tilt_machine_settings(
            self: "ConicalGearToothSurface._Cast_ConicalGearToothSurface",
        ) -> "_807.PinionHypoidFormateTiltMachineSettings":
            from mastapy.gears.manufacturing.bevel import _807

            return self._parent._cast(_807.PinionHypoidFormateTiltMachineSettings)

        @property
        def pinion_hypoid_generating_tilt_machine_settings(
            self: "ConicalGearToothSurface._Cast_ConicalGearToothSurface",
        ) -> "_808.PinionHypoidGeneratingTiltMachineSettings":
            from mastapy.gears.manufacturing.bevel import _808

            return self._parent._cast(_808.PinionHypoidGeneratingTiltMachineSettings)

        @property
        def pinion_machine_settings_smt(
            self: "ConicalGearToothSurface._Cast_ConicalGearToothSurface",
        ) -> "_809.PinionMachineSettingsSMT":
            from mastapy.gears.manufacturing.bevel import _809

            return self._parent._cast(_809.PinionMachineSettingsSMT)

        @property
        def conical_gear_tooth_surface(
            self: "ConicalGearToothSurface._Cast_ConicalGearToothSurface",
        ) -> "ConicalGearToothSurface":
            return self._parent

        def __getattr__(
            self: "ConicalGearToothSurface._Cast_ConicalGearToothSurface", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearToothSurface.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ConicalGearToothSurface._Cast_ConicalGearToothSurface":
        return self._Cast_ConicalGearToothSurface(self)
