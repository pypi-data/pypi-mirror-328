"""BevelVirtualCylindricalGearISO10300MethodB2"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.virtual_cylindrical_gears import _391
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_VIRTUAL_CYLINDRICAL_GEAR_ISO10300_METHOD_B2 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears",
    "BevelVirtualCylindricalGearISO10300MethodB2",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.virtual_cylindrical_gears import _389


__docformat__ = "restructuredtext en"
__all__ = ("BevelVirtualCylindricalGearISO10300MethodB2",)


Self = TypeVar("Self", bound="BevelVirtualCylindricalGearISO10300MethodB2")


class BevelVirtualCylindricalGearISO10300MethodB2(
    _391.VirtualCylindricalGearISO10300MethodB2
):
    """BevelVirtualCylindricalGearISO10300MethodB2

    This is a mastapy class.
    """

    TYPE = _BEVEL_VIRTUAL_CYLINDRICAL_GEAR_ISO10300_METHOD_B2
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelVirtualCylindricalGearISO10300MethodB2"
    )

    class _Cast_BevelVirtualCylindricalGearISO10300MethodB2:
        """Special nested class for casting BevelVirtualCylindricalGearISO10300MethodB2 to subclasses."""

        def __init__(
            self: "BevelVirtualCylindricalGearISO10300MethodB2._Cast_BevelVirtualCylindricalGearISO10300MethodB2",
            parent: "BevelVirtualCylindricalGearISO10300MethodB2",
        ):
            self._parent = parent

        @property
        def virtual_cylindrical_gear_iso10300_method_b2(
            self: "BevelVirtualCylindricalGearISO10300MethodB2._Cast_BevelVirtualCylindricalGearISO10300MethodB2",
        ) -> "_391.VirtualCylindricalGearISO10300MethodB2":
            return self._parent._cast(_391.VirtualCylindricalGearISO10300MethodB2)

        @property
        def virtual_cylindrical_gear_basic(
            self: "BevelVirtualCylindricalGearISO10300MethodB2._Cast_BevelVirtualCylindricalGearISO10300MethodB2",
        ) -> "_389.VirtualCylindricalGearBasic":
            from mastapy.gears.rating.virtual_cylindrical_gears import _389

            return self._parent._cast(_389.VirtualCylindricalGearBasic)

        @property
        def bevel_virtual_cylindrical_gear_iso10300_method_b2(
            self: "BevelVirtualCylindricalGearISO10300MethodB2._Cast_BevelVirtualCylindricalGearISO10300MethodB2",
        ) -> "BevelVirtualCylindricalGearISO10300MethodB2":
            return self._parent

        def __getattr__(
            self: "BevelVirtualCylindricalGearISO10300MethodB2._Cast_BevelVirtualCylindricalGearISO10300MethodB2",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "BevelVirtualCylindricalGearISO10300MethodB2.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "BevelVirtualCylindricalGearISO10300MethodB2._Cast_BevelVirtualCylindricalGearISO10300MethodB2":
        return self._Cast_BevelVirtualCylindricalGearISO10300MethodB2(self)
