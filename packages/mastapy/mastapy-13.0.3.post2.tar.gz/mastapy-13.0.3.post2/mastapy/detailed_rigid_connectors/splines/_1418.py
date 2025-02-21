"""ISO4156SplineJointDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.detailed_rigid_connectors.splines import _1438
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO4156_SPLINE_JOINT_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "ISO4156SplineJointDesign"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.splines import _1415, _1419, _1433
    from mastapy.detailed_rigid_connectors import _1405


__docformat__ = "restructuredtext en"
__all__ = ("ISO4156SplineJointDesign",)


Self = TypeVar("Self", bound="ISO4156SplineJointDesign")


class ISO4156SplineJointDesign(_1438.StandardSplineJointDesign):
    """ISO4156SplineJointDesign

    This is a mastapy class.
    """

    TYPE = _ISO4156_SPLINE_JOINT_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO4156SplineJointDesign")

    class _Cast_ISO4156SplineJointDesign:
        """Special nested class for casting ISO4156SplineJointDesign to subclasses."""

        def __init__(
            self: "ISO4156SplineJointDesign._Cast_ISO4156SplineJointDesign",
            parent: "ISO4156SplineJointDesign",
        ):
            self._parent = parent

        @property
        def standard_spline_joint_design(
            self: "ISO4156SplineJointDesign._Cast_ISO4156SplineJointDesign",
        ) -> "_1438.StandardSplineJointDesign":
            return self._parent._cast(_1438.StandardSplineJointDesign)

        @property
        def spline_joint_design(
            self: "ISO4156SplineJointDesign._Cast_ISO4156SplineJointDesign",
        ) -> "_1433.SplineJointDesign":
            from mastapy.detailed_rigid_connectors.splines import _1433

            return self._parent._cast(_1433.SplineJointDesign)

        @property
        def detailed_rigid_connector_design(
            self: "ISO4156SplineJointDesign._Cast_ISO4156SplineJointDesign",
        ) -> "_1405.DetailedRigidConnectorDesign":
            from mastapy.detailed_rigid_connectors import _1405

            return self._parent._cast(_1405.DetailedRigidConnectorDesign)

        @property
        def gbt3478_spline_joint_design(
            self: "ISO4156SplineJointDesign._Cast_ISO4156SplineJointDesign",
        ) -> "_1415.GBT3478SplineJointDesign":
            from mastapy.detailed_rigid_connectors.splines import _1415

            return self._parent._cast(_1415.GBT3478SplineJointDesign)

        @property
        def jisb1603_spline_joint_design(
            self: "ISO4156SplineJointDesign._Cast_ISO4156SplineJointDesign",
        ) -> "_1419.JISB1603SplineJointDesign":
            from mastapy.detailed_rigid_connectors.splines import _1419

            return self._parent._cast(_1419.JISB1603SplineJointDesign)

        @property
        def iso4156_spline_joint_design(
            self: "ISO4156SplineJointDesign._Cast_ISO4156SplineJointDesign",
        ) -> "ISO4156SplineJointDesign":
            return self._parent

        def __getattr__(
            self: "ISO4156SplineJointDesign._Cast_ISO4156SplineJointDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO4156SplineJointDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def form_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FormClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_effective_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumEffectiveClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_effective_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumEffectiveClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ISO4156SplineJointDesign._Cast_ISO4156SplineJointDesign":
        return self._Cast_ISO4156SplineJointDesign(self)
