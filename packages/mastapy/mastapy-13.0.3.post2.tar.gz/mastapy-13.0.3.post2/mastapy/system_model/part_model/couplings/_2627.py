"""SynchroniserSleeve"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.part_model.couplings import _2626
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserSleeve"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.part_model import _2484, _2464, _2488
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeve",)


Self = TypeVar("Self", bound="SynchroniserSleeve")


class SynchroniserSleeve(_2626.SynchroniserPart):
    """SynchroniserSleeve

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserSleeve")

    class _Cast_SynchroniserSleeve:
        """Special nested class for casting SynchroniserSleeve to subclasses."""

        def __init__(
            self: "SynchroniserSleeve._Cast_SynchroniserSleeve",
            parent: "SynchroniserSleeve",
        ):
            self._parent = parent

        @property
        def synchroniser_part(
            self: "SynchroniserSleeve._Cast_SynchroniserSleeve",
        ) -> "_2626.SynchroniserPart":
            return self._parent._cast(_2626.SynchroniserPart)

        @property
        def coupling_half(
            self: "SynchroniserSleeve._Cast_SynchroniserSleeve",
        ) -> "_2605.CouplingHalf":
            from mastapy.system_model.part_model.couplings import _2605

            return self._parent._cast(_2605.CouplingHalf)

        @property
        def mountable_component(
            self: "SynchroniserSleeve._Cast_SynchroniserSleeve",
        ) -> "_2484.MountableComponent":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.MountableComponent)

        @property
        def component(
            self: "SynchroniserSleeve._Cast_SynchroniserSleeve",
        ) -> "_2464.Component":
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.Component)

        @property
        def part(self: "SynchroniserSleeve._Cast_SynchroniserSleeve") -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(
            self: "SynchroniserSleeve._Cast_SynchroniserSleeve",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def synchroniser_sleeve(
            self: "SynchroniserSleeve._Cast_SynchroniserSleeve",
        ) -> "SynchroniserSleeve":
            return self._parent

        def __getattr__(self: "SynchroniserSleeve._Cast_SynchroniserSleeve", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserSleeve.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hub_bore(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.HubBore

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @hub_bore.setter
    @enforce_parameter_types
    def hub_bore(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.HubBore = value

    @property
    def hub_height(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HubHeight

        if temp is None:
            return 0.0

        return temp

    @hub_height.setter
    @enforce_parameter_types
    def hub_height(self: Self, value: "float"):
        self.wrapped.HubHeight = float(value) if value is not None else 0.0

    @property
    def hub_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HubWidth

        if temp is None:
            return 0.0

        return temp

    @hub_width.setter
    @enforce_parameter_types
    def hub_width(self: Self, value: "float"):
        self.wrapped.HubWidth = float(value) if value is not None else 0.0

    @property
    def sleeve_outer_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SleeveOuterDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @sleeve_outer_diameter.setter
    @enforce_parameter_types
    def sleeve_outer_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SleeveOuterDiameter = value

    @property
    def sleeve_selection_height(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SleeveSelectionHeight

        if temp is None:
            return 0.0

        return temp

    @sleeve_selection_height.setter
    @enforce_parameter_types
    def sleeve_selection_height(self: Self, value: "float"):
        self.wrapped.SleeveSelectionHeight = float(value) if value is not None else 0.0

    @property
    def sleeve_selection_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SleeveSelectionWidth

        if temp is None:
            return 0.0

        return temp

    @sleeve_selection_width.setter
    @enforce_parameter_types
    def sleeve_selection_width(self: Self, value: "float"):
        self.wrapped.SleeveSelectionWidth = float(value) if value is not None else 0.0

    @property
    def sleeve_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SleeveWidth

        if temp is None:
            return 0.0

        return temp

    @sleeve_width.setter
    @enforce_parameter_types
    def sleeve_width(self: Self, value: "float"):
        self.wrapped.SleeveWidth = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "SynchroniserSleeve._Cast_SynchroniserSleeve":
        return self._Cast_SynchroniserSleeve(self)
