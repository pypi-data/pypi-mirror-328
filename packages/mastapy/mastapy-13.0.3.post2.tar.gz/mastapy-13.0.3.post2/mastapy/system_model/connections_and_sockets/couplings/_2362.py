"""ClutchConnection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.couplings import _2366
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "ClutchConnection"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2301, _2292
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("ClutchConnection",)


Self = TypeVar("Self", bound="ClutchConnection")


class ClutchConnection(_2366.CouplingConnection):
    """ClutchConnection

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchConnection")

    class _Cast_ClutchConnection:
        """Special nested class for casting ClutchConnection to subclasses."""

        def __init__(
            self: "ClutchConnection._Cast_ClutchConnection", parent: "ClutchConnection"
        ):
            self._parent = parent

        @property
        def coupling_connection(
            self: "ClutchConnection._Cast_ClutchConnection",
        ) -> "_2366.CouplingConnection":
            return self._parent._cast(_2366.CouplingConnection)

        @property
        def inter_mountable_component_connection(
            self: "ClutchConnection._Cast_ClutchConnection",
        ) -> "_2301.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2301

            return self._parent._cast(_2301.InterMountableComponentConnection)

        @property
        def connection(
            self: "ClutchConnection._Cast_ClutchConnection",
        ) -> "_2292.Connection":
            from mastapy.system_model.connections_and_sockets import _2292

            return self._parent._cast(_2292.Connection)

        @property
        def design_entity(
            self: "ClutchConnection._Cast_ClutchConnection",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def clutch_connection(
            self: "ClutchConnection._Cast_ClutchConnection",
        ) -> "ClutchConnection":
            return self._parent

        def __getattr__(self: "ClutchConnection._Cast_ClutchConnection", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchConnection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def effective_torque_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveTorqueRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_capacity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueCapacity

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "ClutchConnection._Cast_ClutchConnection":
        return self._Cast_ClutchConnection(self)
