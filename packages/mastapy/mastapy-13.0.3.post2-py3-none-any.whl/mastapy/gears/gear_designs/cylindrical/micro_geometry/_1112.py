"""CylindricalGearMicroGeometry"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1113
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "CylindricalGearMicroGeometry",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1107, _1135
    from mastapy.gears.analysis import _1239, _1236, _1233


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMicroGeometry",)


Self = TypeVar("Self", bound="CylindricalGearMicroGeometry")


class CylindricalGearMicroGeometry(_1113.CylindricalGearMicroGeometryBase):
    """CylindricalGearMicroGeometry

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearMicroGeometry")

    class _Cast_CylindricalGearMicroGeometry:
        """Special nested class for casting CylindricalGearMicroGeometry to subclasses."""

        def __init__(
            self: "CylindricalGearMicroGeometry._Cast_CylindricalGearMicroGeometry",
            parent: "CylindricalGearMicroGeometry",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_micro_geometry_base(
            self: "CylindricalGearMicroGeometry._Cast_CylindricalGearMicroGeometry",
        ) -> "_1113.CylindricalGearMicroGeometryBase":
            return self._parent._cast(_1113.CylindricalGearMicroGeometryBase)

        @property
        def gear_implementation_detail(
            self: "CylindricalGearMicroGeometry._Cast_CylindricalGearMicroGeometry",
        ) -> "_1239.GearImplementationDetail":
            from mastapy.gears.analysis import _1239

            return self._parent._cast(_1239.GearImplementationDetail)

        @property
        def gear_design_analysis(
            self: "CylindricalGearMicroGeometry._Cast_CylindricalGearMicroGeometry",
        ) -> "_1236.GearDesignAnalysis":
            from mastapy.gears.analysis import _1236

            return self._parent._cast(_1236.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "CylindricalGearMicroGeometry._Cast_CylindricalGearMicroGeometry",
        ) -> "_1233.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1233

            return self._parent._cast(_1233.AbstractGearAnalysis)

        @property
        def cylindrical_gear_micro_geometry(
            self: "CylindricalGearMicroGeometry._Cast_CylindricalGearMicroGeometry",
        ) -> "CylindricalGearMicroGeometry":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMicroGeometry._Cast_CylindricalGearMicroGeometry",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearMicroGeometry.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def left_flank(self: Self) -> "_1107.CylindricalGearFlankMicroGeometry":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearFlankMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank(self: Self) -> "_1107.CylindricalGearFlankMicroGeometry":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearFlankMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def flanks(self: Self) -> "List[_1107.CylindricalGearFlankMicroGeometry]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearFlankMicroGeometry]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Flanks

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshed_gears(self: Self) -> "List[_1135.MeshedCylindricalGearMicroGeometry]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.MeshedCylindricalGearMicroGeometry]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def both_flanks(self: Self) -> "_1107.CylindricalGearFlankMicroGeometry":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearFlankMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BothFlanks

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMicroGeometry._Cast_CylindricalGearMicroGeometry":
        return self._Cast_CylindricalGearMicroGeometry(self)
