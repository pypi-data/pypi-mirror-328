"""Mass"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1605
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Mass"
)


__docformat__ = "restructuredtext en"
__all__ = ("Mass",)


Self = TypeVar("Self", bound="Mass")


class Mass(_1605.MeasurementBase):
    """Mass

    This is a mastapy class.
    """

    TYPE = _MASS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Mass")

    class _Cast_Mass:
        """Special nested class for casting Mass to subclasses."""

        def __init__(self: "Mass._Cast_Mass", parent: "Mass"):
            self._parent = parent

        @property
        def measurement_base(self: "Mass._Cast_Mass") -> "_1605.MeasurementBase":
            return self._parent._cast(_1605.MeasurementBase)

        @property
        def mass(self: "Mass._Cast_Mass") -> "Mass":
            return self._parent

        def __getattr__(self: "Mass._Cast_Mass", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Mass.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Mass._Cast_Mass":
        return self._Cast_Mass(self)
