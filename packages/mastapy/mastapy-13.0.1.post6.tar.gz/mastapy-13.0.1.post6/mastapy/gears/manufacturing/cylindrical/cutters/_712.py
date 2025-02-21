"""CylindricalGearRackDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.manufacturing.cylindrical.cutters import _713
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_RACK_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters", "CylindricalGearRackDesign"
)

if TYPE_CHECKING:
    from mastapy.gears import _333, _351
    from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _730
    from mastapy.gears.manufacturing.cylindrical.cutters import _708, _709, _706
    from mastapy.utility.databases import _1829


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearRackDesign",)


Self = TypeVar("Self", bound="CylindricalGearRackDesign")


class CylindricalGearRackDesign(_713.CylindricalGearRealCutterDesign):
    """CylindricalGearRackDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_RACK_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearRackDesign")

    class _Cast_CylindricalGearRackDesign:
        """Special nested class for casting CylindricalGearRackDesign to subclasses."""

        def __init__(
            self: "CylindricalGearRackDesign._Cast_CylindricalGearRackDesign",
            parent: "CylindricalGearRackDesign",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_real_cutter_design(
            self: "CylindricalGearRackDesign._Cast_CylindricalGearRackDesign",
        ) -> "_713.CylindricalGearRealCutterDesign":
            return self._parent._cast(_713.CylindricalGearRealCutterDesign)

        @property
        def cylindrical_gear_abstract_cutter_design(
            self: "CylindricalGearRackDesign._Cast_CylindricalGearRackDesign",
        ) -> "_706.CylindricalGearAbstractCutterDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _706

            return self._parent._cast(_706.CylindricalGearAbstractCutterDesign)

        @property
        def named_database_item(
            self: "CylindricalGearRackDesign._Cast_CylindricalGearRackDesign",
        ) -> "_1829.NamedDatabaseItem":
            from mastapy.utility.databases import _1829

            return self._parent._cast(_1829.NamedDatabaseItem)

        @property
        def cylindrical_gear_grinding_worm(
            self: "CylindricalGearRackDesign._Cast_CylindricalGearRackDesign",
        ) -> "_708.CylindricalGearGrindingWorm":
            from mastapy.gears.manufacturing.cylindrical.cutters import _708

            return self._parent._cast(_708.CylindricalGearGrindingWorm)

        @property
        def cylindrical_gear_hob_design(
            self: "CylindricalGearRackDesign._Cast_CylindricalGearRackDesign",
        ) -> "_709.CylindricalGearHobDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _709

            return self._parent._cast(_709.CylindricalGearHobDesign)

        @property
        def cylindrical_gear_rack_design(
            self: "CylindricalGearRackDesign._Cast_CylindricalGearRackDesign",
        ) -> "CylindricalGearRackDesign":
            return self._parent

        def __getattr__(
            self: "CylindricalGearRackDesign._Cast_CylindricalGearRackDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearRackDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def addendum(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Addendum

        if temp is None:
            return 0.0

        return temp

    @addendum.setter
    @enforce_parameter_types
    def addendum(self: Self, value: "float"):
        self.wrapped.Addendum = float(value) if value is not None else 0.0

    @property
    def addendum_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AddendumFactor

        if temp is None:
            return 0.0

        return temp

    @addendum_factor.setter
    @enforce_parameter_types
    def addendum_factor(self: Self, value: "float"):
        self.wrapped.AddendumFactor = float(value) if value is not None else 0.0

    @property
    def addendum_keeping_dedendum_constant(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AddendumKeepingDedendumConstant

        if temp is None:
            return 0.0

        return temp

    @addendum_keeping_dedendum_constant.setter
    @enforce_parameter_types
    def addendum_keeping_dedendum_constant(self: Self, value: "float"):
        self.wrapped.AddendumKeepingDedendumConstant = (
            float(value) if value is not None else 0.0
        )

    @property
    def dedendum(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Dedendum

        if temp is None:
            return 0.0

        return temp

    @dedendum.setter
    @enforce_parameter_types
    def dedendum(self: Self, value: "float"):
        self.wrapped.Dedendum = float(value) if value is not None else 0.0

    @property
    def dedendum_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DedendumFactor

        if temp is None:
            return 0.0

        return temp

    @dedendum_factor.setter
    @enforce_parameter_types
    def dedendum_factor(self: Self, value: "float"):
        self.wrapped.DedendumFactor = float(value) if value is not None else 0.0

    @property
    def edge_height(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EdgeHeight

        if temp is None:
            return 0.0

        return temp

    @edge_height.setter
    @enforce_parameter_types
    def edge_height(self: Self, value: "float"):
        self.wrapped.EdgeHeight = float(value) if value is not None else 0.0

    @property
    def edge_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EdgeRadius

        if temp is None:
            return 0.0

        return temp

    @edge_radius.setter
    @enforce_parameter_types
    def edge_radius(self: Self, value: "float"):
        self.wrapped.EdgeRadius = float(value) if value is not None else 0.0

    @property
    def effective_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EffectiveLength

        if temp is None:
            return 0.0

        return temp

    @effective_length.setter
    @enforce_parameter_types
    def effective_length(self: Self, value: "float"):
        self.wrapped.EffectiveLength = float(value) if value is not None else 0.0

    @property
    def flat_root_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlatRootWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def flat_tip_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FlatTipWidth

        if temp is None:
            return 0.0

        return temp

    @flat_tip_width.setter
    @enforce_parameter_types
    def flat_tip_width(self: Self, value: "float"):
        self.wrapped.FlatTipWidth = float(value) if value is not None else 0.0

    @property
    def hand(self: Self) -> "_333.Hand":
        """mastapy.gears.Hand"""
        temp = self.wrapped.Hand

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.Hand")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.gears._333", "Hand")(value)

    @hand.setter
    @enforce_parameter_types
    def hand(self: Self, value: "_333.Hand"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Gears.Hand")
        self.wrapped.Hand = value

    @property
    def normal_thickness(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NormalThickness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @normal_thickness.setter
    @enforce_parameter_types
    def normal_thickness(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NormalThickness = value

    @property
    def number_of_threads(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfThreads

        if temp is None:
            return 0

        return temp

    @number_of_threads.setter
    @enforce_parameter_types
    def number_of_threads(self: Self, value: "int"):
        self.wrapped.NumberOfThreads = int(value) if value is not None else 0

    @property
    def reference_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TipDiameter

        if temp is None:
            return 0.0

        return temp

    @tip_diameter.setter
    @enforce_parameter_types
    def tip_diameter(self: Self, value: "float"):
        self.wrapped.TipDiameter = float(value) if value is not None else 0.0

    @property
    def use_maximum_edge_radius(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseMaximumEdgeRadius

        if temp is None:
            return False

        return temp

    @use_maximum_edge_radius.setter
    @enforce_parameter_types
    def use_maximum_edge_radius(self: Self, value: "bool"):
        self.wrapped.UseMaximumEdgeRadius = bool(value) if value is not None else False

    @property
    def whole_depth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WholeDepth

        if temp is None:
            return 0.0

        return temp

    @whole_depth.setter
    @enforce_parameter_types
    def whole_depth(self: Self, value: "float"):
        self.wrapped.WholeDepth = float(value) if value is not None else 0.0

    @property
    def worm_type(self: Self) -> "_351.WormType":
        """mastapy.gears.WormType"""
        temp = self.wrapped.WormType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.WormType")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.gears._351", "WormType")(value)

    @worm_type.setter
    @enforce_parameter_types
    def worm_type(self: Self, value: "_351.WormType"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Gears.WormType")
        self.wrapped.WormType = value

    @property
    def nominal_rack_shape(self: Self) -> "_730.RackShape":
        """mastapy.gears.manufacturing.cylindrical.cutters.tangibles.RackShape

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalRackShape

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def convert_to_standard_thickness(self: Self):
        """Method does not return."""
        self.wrapped.ConvertToStandardThickness()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearRackDesign._Cast_CylindricalGearRackDesign":
        return self._Cast_CylindricalGearRackDesign(self)
