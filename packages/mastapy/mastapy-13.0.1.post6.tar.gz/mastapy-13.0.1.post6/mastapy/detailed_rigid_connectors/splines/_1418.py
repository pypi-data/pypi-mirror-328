"""StandardSplineHalfDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.detailed_rigid_connectors.splines import _1413
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STANDARD_SPLINE_HALF_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "StandardSplineHalfDesign"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.splines import _1391, _1395, _1398, _1406
    from mastapy.detailed_rigid_connectors import _1387


__docformat__ = "restructuredtext en"
__all__ = ("StandardSplineHalfDesign",)


Self = TypeVar("Self", bound="StandardSplineHalfDesign")


class StandardSplineHalfDesign(_1413.SplineHalfDesign):
    """StandardSplineHalfDesign

    This is a mastapy class.
    """

    TYPE = _STANDARD_SPLINE_HALF_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StandardSplineHalfDesign")

    class _Cast_StandardSplineHalfDesign:
        """Special nested class for casting StandardSplineHalfDesign to subclasses."""

        def __init__(
            self: "StandardSplineHalfDesign._Cast_StandardSplineHalfDesign",
            parent: "StandardSplineHalfDesign",
        ):
            self._parent = parent

        @property
        def spline_half_design(
            self: "StandardSplineHalfDesign._Cast_StandardSplineHalfDesign",
        ) -> "_1413.SplineHalfDesign":
            return self._parent._cast(_1413.SplineHalfDesign)

        @property
        def detailed_rigid_connector_half_design(
            self: "StandardSplineHalfDesign._Cast_StandardSplineHalfDesign",
        ) -> "_1387.DetailedRigidConnectorHalfDesign":
            from mastapy.detailed_rigid_connectors import _1387

            return self._parent._cast(_1387.DetailedRigidConnectorHalfDesign)

        @property
        def din5480_spline_half_design(
            self: "StandardSplineHalfDesign._Cast_StandardSplineHalfDesign",
        ) -> "_1391.DIN5480SplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1391

            return self._parent._cast(_1391.DIN5480SplineHalfDesign)

        @property
        def gbt3478_spline_half_design(
            self: "StandardSplineHalfDesign._Cast_StandardSplineHalfDesign",
        ) -> "_1395.GBT3478SplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1395

            return self._parent._cast(_1395.GBT3478SplineHalfDesign)

        @property
        def iso4156_spline_half_design(
            self: "StandardSplineHalfDesign._Cast_StandardSplineHalfDesign",
        ) -> "_1398.ISO4156SplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1398

            return self._parent._cast(_1398.ISO4156SplineHalfDesign)

        @property
        def sae_spline_half_design(
            self: "StandardSplineHalfDesign._Cast_StandardSplineHalfDesign",
        ) -> "_1406.SAESplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1406

            return self._parent._cast(_1406.SAESplineHalfDesign)

        @property
        def standard_spline_half_design(
            self: "StandardSplineHalfDesign._Cast_StandardSplineHalfDesign",
        ) -> "StandardSplineHalfDesign":
            return self._parent

        def __getattr__(
            self: "StandardSplineHalfDesign._Cast_StandardSplineHalfDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StandardSplineHalfDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "StandardSplineHalfDesign._Cast_StandardSplineHalfDesign":
        return self._Cast_StandardSplineHalfDesign(self)
