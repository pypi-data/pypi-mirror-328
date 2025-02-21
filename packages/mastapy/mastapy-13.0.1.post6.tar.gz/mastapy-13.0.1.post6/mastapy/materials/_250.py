"""CompositeFatigueSafetyFactorItem"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.materials import _253
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOSITE_FATIGUE_SAFETY_FACTOR_ITEM = python_net_import(
    "SMT.MastaAPI.Materials", "CompositeFatigueSafetyFactorItem"
)

if TYPE_CHECKING:
    from mastapy.materials import _254, _280


__docformat__ = "restructuredtext en"
__all__ = ("CompositeFatigueSafetyFactorItem",)


Self = TypeVar("Self", bound="CompositeFatigueSafetyFactorItem")


class CompositeFatigueSafetyFactorItem(_253.FatigueSafetyFactorItem):
    """CompositeFatigueSafetyFactorItem

    This is a mastapy class.
    """

    TYPE = _COMPOSITE_FATIGUE_SAFETY_FACTOR_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CompositeFatigueSafetyFactorItem")

    class _Cast_CompositeFatigueSafetyFactorItem:
        """Special nested class for casting CompositeFatigueSafetyFactorItem to subclasses."""

        def __init__(
            self: "CompositeFatigueSafetyFactorItem._Cast_CompositeFatigueSafetyFactorItem",
            parent: "CompositeFatigueSafetyFactorItem",
        ):
            self._parent = parent

        @property
        def fatigue_safety_factor_item(
            self: "CompositeFatigueSafetyFactorItem._Cast_CompositeFatigueSafetyFactorItem",
        ) -> "_253.FatigueSafetyFactorItem":
            return self._parent._cast(_253.FatigueSafetyFactorItem)

        @property
        def fatigue_safety_factor_item_base(
            self: "CompositeFatigueSafetyFactorItem._Cast_CompositeFatigueSafetyFactorItem",
        ) -> "_254.FatigueSafetyFactorItemBase":
            from mastapy.materials import _254

            return self._parent._cast(_254.FatigueSafetyFactorItemBase)

        @property
        def safety_factor_item(
            self: "CompositeFatigueSafetyFactorItem._Cast_CompositeFatigueSafetyFactorItem",
        ) -> "_280.SafetyFactorItem":
            from mastapy.materials import _280

            return self._parent._cast(_280.SafetyFactorItem)

        @property
        def composite_fatigue_safety_factor_item(
            self: "CompositeFatigueSafetyFactorItem._Cast_CompositeFatigueSafetyFactorItem",
        ) -> "CompositeFatigueSafetyFactorItem":
            return self._parent

        def __getattr__(
            self: "CompositeFatigueSafetyFactorItem._Cast_CompositeFatigueSafetyFactorItem",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CompositeFatigueSafetyFactorItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CompositeFatigueSafetyFactorItem._Cast_CompositeFatigueSafetyFactorItem":
        return self._Cast_CompositeFatigueSafetyFactorItem(self)
