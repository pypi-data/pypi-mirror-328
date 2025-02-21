"""RingTolerance"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.tolerances import _1929
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_TOLERANCE = python_net_import("SMT.MastaAPI.Bearings.Tolerances", "RingTolerance")

if TYPE_CHECKING:
    from mastapy.bearings.tolerances import _1938, _1926, _1932, _1921


__docformat__ = "restructuredtext en"
__all__ = ("RingTolerance",)


Self = TypeVar("Self", bound="RingTolerance")


class RingTolerance(_1929.InterferenceTolerance):
    """RingTolerance

    This is a mastapy class.
    """

    TYPE = _RING_TOLERANCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingTolerance")

    class _Cast_RingTolerance:
        """Special nested class for casting RingTolerance to subclasses."""

        def __init__(
            self: "RingTolerance._Cast_RingTolerance", parent: "RingTolerance"
        ):
            self._parent = parent

        @property
        def interference_tolerance(
            self: "RingTolerance._Cast_RingTolerance",
        ) -> "_1929.InterferenceTolerance":
            return self._parent._cast(_1929.InterferenceTolerance)

        @property
        def bearing_connection_component(
            self: "RingTolerance._Cast_RingTolerance",
        ) -> "_1921.BearingConnectionComponent":
            from mastapy.bearings.tolerances import _1921

            return self._parent._cast(_1921.BearingConnectionComponent)

        @property
        def inner_ring_tolerance(
            self: "RingTolerance._Cast_RingTolerance",
        ) -> "_1926.InnerRingTolerance":
            from mastapy.bearings.tolerances import _1926

            return self._parent._cast(_1926.InnerRingTolerance)

        @property
        def outer_ring_tolerance(
            self: "RingTolerance._Cast_RingTolerance",
        ) -> "_1932.OuterRingTolerance":
            from mastapy.bearings.tolerances import _1932

            return self._parent._cast(_1932.OuterRingTolerance)

        @property
        def ring_tolerance(
            self: "RingTolerance._Cast_RingTolerance",
        ) -> "RingTolerance":
            return self._parent

        def __getattr__(self: "RingTolerance._Cast_RingTolerance", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingTolerance.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def roundness_specification(self: Self) -> "_1938.RoundnessSpecification":
        """mastapy.bearings.tolerances.RoundnessSpecification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoundnessSpecification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "RingTolerance._Cast_RingTolerance":
        return self._Cast_RingTolerance(self)
