"""PointLoad"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._math.vector_2d import Vector2D
from mastapy._internal import conversion
from mastapy.system_model.part_model import _2479
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "PointLoad")

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2464, _2444, _2468
    from mastapy.system_model import _2203


__docformat__ = "restructuredtext en"
__all__ = ("PointLoad",)


Self = TypeVar("Self", bound="PointLoad")


class PointLoad(_2479.VirtualComponent):
    """PointLoad

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointLoad")

    class _Cast_PointLoad:
        """Special nested class for casting PointLoad to subclasses."""

        def __init__(self: "PointLoad._Cast_PointLoad", parent: "PointLoad"):
            self._parent = parent

        @property
        def virtual_component(
            self: "PointLoad._Cast_PointLoad",
        ) -> "_2479.VirtualComponent":
            return self._parent._cast(_2479.VirtualComponent)

        @property
        def mountable_component(
            self: "PointLoad._Cast_PointLoad",
        ) -> "_2464.MountableComponent":
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.MountableComponent)

        @property
        def component(self: "PointLoad._Cast_PointLoad") -> "_2444.Component":
            from mastapy.system_model.part_model import _2444

            return self._parent._cast(_2444.Component)

        @property
        def part(self: "PointLoad._Cast_PointLoad") -> "_2468.Part":
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(self: "PointLoad._Cast_PointLoad") -> "_2203.DesignEntity":
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def point_load(self: "PointLoad._Cast_PointLoad") -> "PointLoad":
            return self._parent

        def __getattr__(self: "PointLoad._Cast_PointLoad", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PointLoad.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def offset(self: Self) -> "Vector2D":
        """Vector2D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Offset

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def set_offset(self: Self, radius: "float", angle: "float"):
        """Method does not return.

        Args:
            radius (float)
            angle (float)
        """
        radius = float(radius)
        angle = float(angle)
        self.wrapped.SetOffset(radius if radius else 0.0, angle if angle else 0.0)

    @property
    def cast_to(self: Self) -> "PointLoad._Cast_PointLoad":
        return self._Cast_PointLoad(self)
