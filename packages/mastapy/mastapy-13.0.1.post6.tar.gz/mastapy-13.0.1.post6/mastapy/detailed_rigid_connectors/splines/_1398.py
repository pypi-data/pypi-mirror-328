"""ISO4156SplineHalfDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.detailed_rigid_connectors.splines import _1418
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO4156_SPLINE_HALF_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "ISO4156SplineHalfDesign"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.splines import _1395, _1413
    from mastapy.detailed_rigid_connectors import _1387


__docformat__ = "restructuredtext en"
__all__ = ("ISO4156SplineHalfDesign",)


Self = TypeVar("Self", bound="ISO4156SplineHalfDesign")


class ISO4156SplineHalfDesign(_1418.StandardSplineHalfDesign):
    """ISO4156SplineHalfDesign

    This is a mastapy class.
    """

    TYPE = _ISO4156_SPLINE_HALF_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO4156SplineHalfDesign")

    class _Cast_ISO4156SplineHalfDesign:
        """Special nested class for casting ISO4156SplineHalfDesign to subclasses."""

        def __init__(
            self: "ISO4156SplineHalfDesign._Cast_ISO4156SplineHalfDesign",
            parent: "ISO4156SplineHalfDesign",
        ):
            self._parent = parent

        @property
        def standard_spline_half_design(
            self: "ISO4156SplineHalfDesign._Cast_ISO4156SplineHalfDesign",
        ) -> "_1418.StandardSplineHalfDesign":
            return self._parent._cast(_1418.StandardSplineHalfDesign)

        @property
        def spline_half_design(
            self: "ISO4156SplineHalfDesign._Cast_ISO4156SplineHalfDesign",
        ) -> "_1413.SplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1413

            return self._parent._cast(_1413.SplineHalfDesign)

        @property
        def detailed_rigid_connector_half_design(
            self: "ISO4156SplineHalfDesign._Cast_ISO4156SplineHalfDesign",
        ) -> "_1387.DetailedRigidConnectorHalfDesign":
            from mastapy.detailed_rigid_connectors import _1387

            return self._parent._cast(_1387.DetailedRigidConnectorHalfDesign)

        @property
        def gbt3478_spline_half_design(
            self: "ISO4156SplineHalfDesign._Cast_ISO4156SplineHalfDesign",
        ) -> "_1395.GBT3478SplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1395

            return self._parent._cast(_1395.GBT3478SplineHalfDesign)

        @property
        def iso4156_spline_half_design(
            self: "ISO4156SplineHalfDesign._Cast_ISO4156SplineHalfDesign",
        ) -> "ISO4156SplineHalfDesign":
            return self._parent

        def __getattr__(
            self: "ISO4156SplineHalfDesign._Cast_ISO4156SplineHalfDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO4156SplineHalfDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_maximum_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumMaximumFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rack_addendum_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicRackAddendumFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rack_dedendum_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicRackDedendumFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_actual_space_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumActualSpaceWidth

        if temp is None:
            return 0.0

        return temp

    @maximum_actual_space_width.setter
    @enforce_parameter_types
    def maximum_actual_space_width(self: Self, value: "float"):
        self.wrapped.MaximumActualSpaceWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_actual_tooth_thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumActualToothThickness

        if temp is None:
            return 0.0

        return temp

    @maximum_actual_tooth_thickness.setter
    @enforce_parameter_types
    def maximum_actual_tooth_thickness(self: Self, value: "float"):
        self.wrapped.MaximumActualToothThickness = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_dimension_over_balls(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumDimensionOverBalls

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_effective_space_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumEffectiveSpaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_effective_tooth_thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumEffectiveToothThickness

        if temp is None:
            return 0.0

        return temp

    @maximum_effective_tooth_thickness.setter
    @enforce_parameter_types
    def maximum_effective_tooth_thickness(self: Self, value: "float"):
        self.wrapped.MaximumEffectiveToothThickness = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_major_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumMajorDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_minor_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumMinorDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_actual_space_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumActualSpaceWidth

        if temp is None:
            return 0.0

        return temp

    @minimum_actual_space_width.setter
    @enforce_parameter_types
    def minimum_actual_space_width(self: Self, value: "float"):
        self.wrapped.MinimumActualSpaceWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_actual_tooth_thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumActualToothThickness

        if temp is None:
            return 0.0

        return temp

    @minimum_actual_tooth_thickness.setter
    @enforce_parameter_types
    def minimum_actual_tooth_thickness(self: Self, value: "float"):
        self.wrapped.MinimumActualToothThickness = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_dimension_over_balls(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumDimensionOverBalls

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_effective_space_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumEffectiveSpaceWidth

        if temp is None:
            return 0.0

        return temp

    @minimum_effective_space_width.setter
    @enforce_parameter_types
    def minimum_effective_space_width(self: Self, value: "float"):
        self.wrapped.MinimumEffectiveSpaceWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_effective_tooth_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumEffectiveToothThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_major_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumMajorDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_minor_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumMinorDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def root_fillet_radius_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RootFilletRadiusFactor

        if temp is None:
            return 0.0

        return temp

    @root_fillet_radius_factor.setter
    @enforce_parameter_types
    def root_fillet_radius_factor(self: Self, value: "float"):
        self.wrapped.RootFilletRadiusFactor = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "ISO4156SplineHalfDesign._Cast_ISO4156SplineHalfDesign":
        return self._Cast_ISO4156SplineHalfDesign(self)
