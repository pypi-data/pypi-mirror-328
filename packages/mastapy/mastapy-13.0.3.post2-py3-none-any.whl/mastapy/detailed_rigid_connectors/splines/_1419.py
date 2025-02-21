"""JISB1603SplineJointDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.detailed_rigid_connectors.splines import _1418
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_JISB1603_SPLINE_JOINT_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "JISB1603SplineJointDesign"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.splines import _1438, _1433
    from mastapy.detailed_rigid_connectors import _1405


__docformat__ = "restructuredtext en"
__all__ = ("JISB1603SplineJointDesign",)


Self = TypeVar("Self", bound="JISB1603SplineJointDesign")


class JISB1603SplineJointDesign(_1418.ISO4156SplineJointDesign):
    """JISB1603SplineJointDesign

    This is a mastapy class.
    """

    TYPE = _JISB1603_SPLINE_JOINT_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_JISB1603SplineJointDesign")

    class _Cast_JISB1603SplineJointDesign:
        """Special nested class for casting JISB1603SplineJointDesign to subclasses."""

        def __init__(
            self: "JISB1603SplineJointDesign._Cast_JISB1603SplineJointDesign",
            parent: "JISB1603SplineJointDesign",
        ):
            self._parent = parent

        @property
        def iso4156_spline_joint_design(
            self: "JISB1603SplineJointDesign._Cast_JISB1603SplineJointDesign",
        ) -> "_1418.ISO4156SplineJointDesign":
            return self._parent._cast(_1418.ISO4156SplineJointDesign)

        @property
        def standard_spline_joint_design(
            self: "JISB1603SplineJointDesign._Cast_JISB1603SplineJointDesign",
        ) -> "_1438.StandardSplineJointDesign":
            from mastapy.detailed_rigid_connectors.splines import _1438

            return self._parent._cast(_1438.StandardSplineJointDesign)

        @property
        def spline_joint_design(
            self: "JISB1603SplineJointDesign._Cast_JISB1603SplineJointDesign",
        ) -> "_1433.SplineJointDesign":
            from mastapy.detailed_rigid_connectors.splines import _1433

            return self._parent._cast(_1433.SplineJointDesign)

        @property
        def detailed_rigid_connector_design(
            self: "JISB1603SplineJointDesign._Cast_JISB1603SplineJointDesign",
        ) -> "_1405.DetailedRigidConnectorDesign":
            from mastapy.detailed_rigid_connectors import _1405

            return self._parent._cast(_1405.DetailedRigidConnectorDesign)

        @property
        def jisb1603_spline_joint_design(
            self: "JISB1603SplineJointDesign._Cast_JISB1603SplineJointDesign",
        ) -> "JISB1603SplineJointDesign":
            return self._parent

        def __getattr__(
            self: "JISB1603SplineJointDesign._Cast_JISB1603SplineJointDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "JISB1603SplineJointDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "JISB1603SplineJointDesign._Cast_JISB1603SplineJointDesign":
        return self._Cast_JISB1603SplineJointDesign(self)
