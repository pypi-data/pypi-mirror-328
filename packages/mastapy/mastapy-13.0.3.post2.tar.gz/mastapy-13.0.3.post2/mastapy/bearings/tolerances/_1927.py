"""InnerSupportTolerance"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.tolerances import _1942
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INNER_SUPPORT_TOLERANCE = python_net_import(
    "SMT.MastaAPI.Bearings.Tolerances", "InnerSupportTolerance"
)

if TYPE_CHECKING:
    from mastapy.bearings.tolerances import _1929, _1921


__docformat__ = "restructuredtext en"
__all__ = ("InnerSupportTolerance",)


Self = TypeVar("Self", bound="InnerSupportTolerance")


class InnerSupportTolerance(_1942.SupportTolerance):
    """InnerSupportTolerance

    This is a mastapy class.
    """

    TYPE = _INNER_SUPPORT_TOLERANCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InnerSupportTolerance")

    class _Cast_InnerSupportTolerance:
        """Special nested class for casting InnerSupportTolerance to subclasses."""

        def __init__(
            self: "InnerSupportTolerance._Cast_InnerSupportTolerance",
            parent: "InnerSupportTolerance",
        ):
            self._parent = parent

        @property
        def support_tolerance(
            self: "InnerSupportTolerance._Cast_InnerSupportTolerance",
        ) -> "_1942.SupportTolerance":
            return self._parent._cast(_1942.SupportTolerance)

        @property
        def interference_tolerance(
            self: "InnerSupportTolerance._Cast_InnerSupportTolerance",
        ) -> "_1929.InterferenceTolerance":
            from mastapy.bearings.tolerances import _1929

            return self._parent._cast(_1929.InterferenceTolerance)

        @property
        def bearing_connection_component(
            self: "InnerSupportTolerance._Cast_InnerSupportTolerance",
        ) -> "_1921.BearingConnectionComponent":
            from mastapy.bearings.tolerances import _1921

            return self._parent._cast(_1921.BearingConnectionComponent)

        @property
        def inner_support_tolerance(
            self: "InnerSupportTolerance._Cast_InnerSupportTolerance",
        ) -> "InnerSupportTolerance":
            return self._parent

        def __getattr__(
            self: "InnerSupportTolerance._Cast_InnerSupportTolerance", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InnerSupportTolerance.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "InnerSupportTolerance._Cast_InnerSupportTolerance":
        return self._Cast_InnerSupportTolerance(self)
