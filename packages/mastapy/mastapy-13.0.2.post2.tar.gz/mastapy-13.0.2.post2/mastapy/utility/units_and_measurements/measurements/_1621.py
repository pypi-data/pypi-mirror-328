"""AnglePerUnitTemperature"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGLE_PER_UNIT_TEMPERATURE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "AnglePerUnitTemperature"
)


__docformat__ = "restructuredtext en"
__all__ = ("AnglePerUnitTemperature",)


Self = TypeVar("Self", bound="AnglePerUnitTemperature")


class AnglePerUnitTemperature(_1612.MeasurementBase):
    """AnglePerUnitTemperature

    This is a mastapy class.
    """

    TYPE = _ANGLE_PER_UNIT_TEMPERATURE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AnglePerUnitTemperature")

    class _Cast_AnglePerUnitTemperature:
        """Special nested class for casting AnglePerUnitTemperature to subclasses."""

        def __init__(
            self: "AnglePerUnitTemperature._Cast_AnglePerUnitTemperature",
            parent: "AnglePerUnitTemperature",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "AnglePerUnitTemperature._Cast_AnglePerUnitTemperature",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def angle_per_unit_temperature(
            self: "AnglePerUnitTemperature._Cast_AnglePerUnitTemperature",
        ) -> "AnglePerUnitTemperature":
            return self._parent

        def __getattr__(
            self: "AnglePerUnitTemperature._Cast_AnglePerUnitTemperature", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AnglePerUnitTemperature.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AnglePerUnitTemperature._Cast_AnglePerUnitTemperature":
        return self._Cast_AnglePerUnitTemperature(self)
