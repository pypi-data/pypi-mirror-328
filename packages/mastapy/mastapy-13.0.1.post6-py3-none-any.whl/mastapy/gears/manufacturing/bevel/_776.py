"""ConicalGearManufacturingConfig"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.bevel import _778
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MANUFACTURING_CONFIG = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalGearManufacturingConfig"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel import _788, _794
    from mastapy.gears.analysis import _1221, _1218, _1215


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearManufacturingConfig",)


Self = TypeVar("Self", bound="ConicalGearManufacturingConfig")


class ConicalGearManufacturingConfig(_778.ConicalGearMicroGeometryConfigBase):
    """ConicalGearManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MANUFACTURING_CONFIG
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearManufacturingConfig")

    class _Cast_ConicalGearManufacturingConfig:
        """Special nested class for casting ConicalGearManufacturingConfig to subclasses."""

        def __init__(
            self: "ConicalGearManufacturingConfig._Cast_ConicalGearManufacturingConfig",
            parent: "ConicalGearManufacturingConfig",
        ):
            self._parent = parent

        @property
        def conical_gear_micro_geometry_config_base(
            self: "ConicalGearManufacturingConfig._Cast_ConicalGearManufacturingConfig",
        ) -> "_778.ConicalGearMicroGeometryConfigBase":
            return self._parent._cast(_778.ConicalGearMicroGeometryConfigBase)

        @property
        def gear_implementation_detail(
            self: "ConicalGearManufacturingConfig._Cast_ConicalGearManufacturingConfig",
        ) -> "_1221.GearImplementationDetail":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.GearImplementationDetail)

        @property
        def gear_design_analysis(
            self: "ConicalGearManufacturingConfig._Cast_ConicalGearManufacturingConfig",
        ) -> "_1218.GearDesignAnalysis":
            from mastapy.gears.analysis import _1218

            return self._parent._cast(_1218.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "ConicalGearManufacturingConfig._Cast_ConicalGearManufacturingConfig",
        ) -> "_1215.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearAnalysis)

        @property
        def conical_pinion_manufacturing_config(
            self: "ConicalGearManufacturingConfig._Cast_ConicalGearManufacturingConfig",
        ) -> "_788.ConicalPinionManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _788

            return self._parent._cast(_788.ConicalPinionManufacturingConfig)

        @property
        def conical_wheel_manufacturing_config(
            self: "ConicalGearManufacturingConfig._Cast_ConicalGearManufacturingConfig",
        ) -> "_794.ConicalWheelManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _794

            return self._parent._cast(_794.ConicalWheelManufacturingConfig)

        @property
        def conical_gear_manufacturing_config(
            self: "ConicalGearManufacturingConfig._Cast_ConicalGearManufacturingConfig",
        ) -> "ConicalGearManufacturingConfig":
            return self._parent

        def __getattr__(
            self: "ConicalGearManufacturingConfig._Cast_ConicalGearManufacturingConfig",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearManufacturingConfig.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearManufacturingConfig._Cast_ConicalGearManufacturingConfig":
        return self._Cast_ConicalGearManufacturingConfig(self)
