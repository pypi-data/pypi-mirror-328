"""InterferenceTolerance"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings.tolerances import _1921
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERFERENCE_TOLERANCE = python_net_import(
    "SMT.MastaAPI.Bearings.Tolerances", "InterferenceTolerance"
)

if TYPE_CHECKING:
    from mastapy.bearings.tolerances import (
        _1924,
        _1926,
        _1927,
        _1932,
        _1933,
        _1937,
        _1942,
    )
    from mastapy.bearings import _1908


__docformat__ = "restructuredtext en"
__all__ = ("InterferenceTolerance",)


Self = TypeVar("Self", bound="InterferenceTolerance")


class InterferenceTolerance(_1921.BearingConnectionComponent):
    """InterferenceTolerance

    This is a mastapy class.
    """

    TYPE = _INTERFERENCE_TOLERANCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InterferenceTolerance")

    class _Cast_InterferenceTolerance:
        """Special nested class for casting InterferenceTolerance to subclasses."""

        def __init__(
            self: "InterferenceTolerance._Cast_InterferenceTolerance",
            parent: "InterferenceTolerance",
        ):
            self._parent = parent

        @property
        def bearing_connection_component(
            self: "InterferenceTolerance._Cast_InterferenceTolerance",
        ) -> "_1921.BearingConnectionComponent":
            return self._parent._cast(_1921.BearingConnectionComponent)

        @property
        def inner_ring_tolerance(
            self: "InterferenceTolerance._Cast_InterferenceTolerance",
        ) -> "_1926.InnerRingTolerance":
            from mastapy.bearings.tolerances import _1926

            return self._parent._cast(_1926.InnerRingTolerance)

        @property
        def inner_support_tolerance(
            self: "InterferenceTolerance._Cast_InterferenceTolerance",
        ) -> "_1927.InnerSupportTolerance":
            from mastapy.bearings.tolerances import _1927

            return self._parent._cast(_1927.InnerSupportTolerance)

        @property
        def outer_ring_tolerance(
            self: "InterferenceTolerance._Cast_InterferenceTolerance",
        ) -> "_1932.OuterRingTolerance":
            from mastapy.bearings.tolerances import _1932

            return self._parent._cast(_1932.OuterRingTolerance)

        @property
        def outer_support_tolerance(
            self: "InterferenceTolerance._Cast_InterferenceTolerance",
        ) -> "_1933.OuterSupportTolerance":
            from mastapy.bearings.tolerances import _1933

            return self._parent._cast(_1933.OuterSupportTolerance)

        @property
        def ring_tolerance(
            self: "InterferenceTolerance._Cast_InterferenceTolerance",
        ) -> "_1937.RingTolerance":
            from mastapy.bearings.tolerances import _1937

            return self._parent._cast(_1937.RingTolerance)

        @property
        def support_tolerance(
            self: "InterferenceTolerance._Cast_InterferenceTolerance",
        ) -> "_1942.SupportTolerance":
            from mastapy.bearings.tolerances import _1942

            return self._parent._cast(_1942.SupportTolerance)

        @property
        def interference_tolerance(
            self: "InterferenceTolerance._Cast_InterferenceTolerance",
        ) -> "InterferenceTolerance":
            return self._parent

        def __getattr__(
            self: "InterferenceTolerance._Cast_InterferenceTolerance", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InterferenceTolerance.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def definition_option(self: Self) -> "_1924.BearingToleranceDefinitionOptions":
        """mastapy.bearings.tolerances.BearingToleranceDefinitionOptions"""
        temp = self.wrapped.DefinitionOption

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.Tolerances.BearingToleranceDefinitionOptions"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.tolerances._1924", "BearingToleranceDefinitionOptions"
        )(value)

    @definition_option.setter
    @enforce_parameter_types
    def definition_option(self: Self, value: "_1924.BearingToleranceDefinitionOptions"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.Tolerances.BearingToleranceDefinitionOptions"
        )
        self.wrapped.DefinitionOption = value

    @property
    def mounting_point_surface_finish(
        self: Self,
    ) -> "_1908.MountingPointSurfaceFinishes":
        """mastapy.bearings.MountingPointSurfaceFinishes"""
        temp = self.wrapped.MountingPointSurfaceFinish

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.MountingPointSurfaceFinishes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings._1908", "MountingPointSurfaceFinishes"
        )(value)

    @mounting_point_surface_finish.setter
    @enforce_parameter_types
    def mounting_point_surface_finish(
        self: Self, value: "_1908.MountingPointSurfaceFinishes"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.MountingPointSurfaceFinishes"
        )
        self.wrapped.MountingPointSurfaceFinish = value

    @property
    def non_contacting_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NonContactingDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @non_contacting_diameter.setter
    @enforce_parameter_types
    def non_contacting_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NonContactingDiameter = value

    @property
    def surface_fitting_reduction(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SurfaceFittingReduction

        if temp is None:
            return 0.0

        return temp

    @surface_fitting_reduction.setter
    @enforce_parameter_types
    def surface_fitting_reduction(self: Self, value: "float"):
        self.wrapped.SurfaceFittingReduction = (
            float(value) if value is not None else 0.0
        )

    @property
    def tolerance_lower_limit(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ToleranceLowerLimit

        if temp is None:
            return 0.0

        return temp

    @tolerance_lower_limit.setter
    @enforce_parameter_types
    def tolerance_lower_limit(self: Self, value: "float"):
        self.wrapped.ToleranceLowerLimit = float(value) if value is not None else 0.0

    @property
    def tolerance_upper_limit(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ToleranceUpperLimit

        if temp is None:
            return 0.0

        return temp

    @tolerance_upper_limit.setter
    @enforce_parameter_types
    def tolerance_upper_limit(self: Self, value: "float"):
        self.wrapped.ToleranceUpperLimit = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "InterferenceTolerance._Cast_InterferenceTolerance":
        return self._Cast_InterferenceTolerance(self)
