"""TolerancedValueSpecification"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _1067
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOLERANCED_VALUE_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "TolerancedValueSpecification"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1037, _1040
    from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import (
        _1091,
        _1092,
    )


__docformat__ = "restructuredtext en"
__all__ = ("TolerancedValueSpecification",)


Self = TypeVar("Self", bound="TolerancedValueSpecification")
T = TypeVar("T")


class TolerancedValueSpecification(_1067.RelativeMeasurementViewModel[T]):
    """TolerancedValueSpecification

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _TOLERANCED_VALUE_SPECIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TolerancedValueSpecification")

    class _Cast_TolerancedValueSpecification:
        """Special nested class for casting TolerancedValueSpecification to subclasses."""

        def __init__(
            self: "TolerancedValueSpecification._Cast_TolerancedValueSpecification",
            parent: "TolerancedValueSpecification",
        ):
            self._parent = parent

        @property
        def relative_measurement_view_model(
            self: "TolerancedValueSpecification._Cast_TolerancedValueSpecification",
        ) -> "_1067.RelativeMeasurementViewModel":
            return self._parent._cast(_1067.RelativeMeasurementViewModel)

        @property
        def cylindrical_mesh_angular_backlash(
            self: "TolerancedValueSpecification._Cast_TolerancedValueSpecification",
        ) -> "_1037.CylindricalMeshAngularBacklash":
            from mastapy.gears.gear_designs.cylindrical import _1037

            return self._parent._cast(_1037.CylindricalMeshAngularBacklash)

        @property
        def cylindrical_mesh_linear_backlash_specification(
            self: "TolerancedValueSpecification._Cast_TolerancedValueSpecification",
        ) -> "_1040.CylindricalMeshLinearBacklashSpecification":
            from mastapy.gears.gear_designs.cylindrical import _1040

            return self._parent._cast(_1040.CylindricalMeshLinearBacklashSpecification)

        @property
        def nominal_value_specification(
            self: "TolerancedValueSpecification._Cast_TolerancedValueSpecification",
        ) -> "_1091.NominalValueSpecification":
            from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import (
                _1091,
            )

            return self._parent._cast(_1091.NominalValueSpecification)

        @property
        def no_value_specification(
            self: "TolerancedValueSpecification._Cast_TolerancedValueSpecification",
        ) -> "_1092.NoValueSpecification":
            from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import (
                _1092,
            )

            return self._parent._cast(_1092.NoValueSpecification)

        @property
        def toleranced_value_specification(
            self: "TolerancedValueSpecification._Cast_TolerancedValueSpecification",
        ) -> "TolerancedValueSpecification":
            return self._parent

        def __getattr__(
            self: "TolerancedValueSpecification._Cast_TolerancedValueSpecification",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TolerancedValueSpecification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_mean(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AverageMean

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @average_mean.setter
    @enforce_parameter_types
    def average_mean(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AverageMean = value

    @property
    def maximum(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Maximum

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum.setter
    @enforce_parameter_types
    def maximum(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Maximum = value

    @property
    def minimum(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Minimum

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum.setter
    @enforce_parameter_types
    def minimum(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Minimum = value

    @property
    def spread(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Spread

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @spread.setter
    @enforce_parameter_types
    def spread(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Spread = value

    @property
    def cast_to(
        self: Self,
    ) -> "TolerancedValueSpecification._Cast_TolerancedValueSpecification":
        return self._Cast_TolerancedValueSpecification(self)
