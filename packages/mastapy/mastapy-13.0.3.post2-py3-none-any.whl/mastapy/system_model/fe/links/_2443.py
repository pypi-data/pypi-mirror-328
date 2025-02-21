"""MultiAngleConnectionFELink"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.fe.links import _2445
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MULTI_ANGLE_CONNECTION_FE_LINK = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.Links", "MultiAngleConnectionFELink"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe.links import _2441, _2450, _2438


__docformat__ = "restructuredtext en"
__all__ = ("MultiAngleConnectionFELink",)


Self = TypeVar("Self", bound="MultiAngleConnectionFELink")


class MultiAngleConnectionFELink(_2445.MultiNodeFELink):
    """MultiAngleConnectionFELink

    This is a mastapy class.
    """

    TYPE = _MULTI_ANGLE_CONNECTION_FE_LINK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MultiAngleConnectionFELink")

    class _Cast_MultiAngleConnectionFELink:
        """Special nested class for casting MultiAngleConnectionFELink to subclasses."""

        def __init__(
            self: "MultiAngleConnectionFELink._Cast_MultiAngleConnectionFELink",
            parent: "MultiAngleConnectionFELink",
        ):
            self._parent = parent

        @property
        def multi_node_fe_link(
            self: "MultiAngleConnectionFELink._Cast_MultiAngleConnectionFELink",
        ) -> "_2445.MultiNodeFELink":
            return self._parent._cast(_2445.MultiNodeFELink)

        @property
        def fe_link(
            self: "MultiAngleConnectionFELink._Cast_MultiAngleConnectionFELink",
        ) -> "_2438.FELink":
            from mastapy.system_model.fe.links import _2438

            return self._parent._cast(_2438.FELink)

        @property
        def gear_mesh_fe_link(
            self: "MultiAngleConnectionFELink._Cast_MultiAngleConnectionFELink",
        ) -> "_2441.GearMeshFELink":
            from mastapy.system_model.fe.links import _2441

            return self._parent._cast(_2441.GearMeshFELink)

        @property
        def rolling_ring_connection_fe_link(
            self: "MultiAngleConnectionFELink._Cast_MultiAngleConnectionFELink",
        ) -> "_2450.RollingRingConnectionFELink":
            from mastapy.system_model.fe.links import _2450

            return self._parent._cast(_2450.RollingRingConnectionFELink)

        @property
        def multi_angle_connection_fe_link(
            self: "MultiAngleConnectionFELink._Cast_MultiAngleConnectionFELink",
        ) -> "MultiAngleConnectionFELink":
            return self._parent

        def __getattr__(
            self: "MultiAngleConnectionFELink._Cast_MultiAngleConnectionFELink",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MultiAngleConnectionFELink.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "MultiAngleConnectionFELink._Cast_MultiAngleConnectionFELink":
        return self._Cast_MultiAngleConnectionFELink(self)
