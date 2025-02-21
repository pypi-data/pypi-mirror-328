"""CycloidalDiscAxialLeftSocket"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2300
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_AXIAL_LEFT_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscAxialLeftSocket",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2314, _2296, _2316


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscAxialLeftSocket",)


Self = TypeVar("Self", bound="CycloidalDiscAxialLeftSocket")


class CycloidalDiscAxialLeftSocket(_2300.InnerShaftSocketBase):
    """CycloidalDiscAxialLeftSocket

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_AXIAL_LEFT_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscAxialLeftSocket")

    class _Cast_CycloidalDiscAxialLeftSocket:
        """Special nested class for casting CycloidalDiscAxialLeftSocket to subclasses."""

        def __init__(
            self: "CycloidalDiscAxialLeftSocket._Cast_CycloidalDiscAxialLeftSocket",
            parent: "CycloidalDiscAxialLeftSocket",
        ):
            self._parent = parent

        @property
        def inner_shaft_socket_base(
            self: "CycloidalDiscAxialLeftSocket._Cast_CycloidalDiscAxialLeftSocket",
        ) -> "_2300.InnerShaftSocketBase":
            return self._parent._cast(_2300.InnerShaftSocketBase)

        @property
        def shaft_socket(
            self: "CycloidalDiscAxialLeftSocket._Cast_CycloidalDiscAxialLeftSocket",
        ) -> "_2314.ShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2314

            return self._parent._cast(_2314.ShaftSocket)

        @property
        def cylindrical_socket(
            self: "CycloidalDiscAxialLeftSocket._Cast_CycloidalDiscAxialLeftSocket",
        ) -> "_2296.CylindricalSocket":
            from mastapy.system_model.connections_and_sockets import _2296

            return self._parent._cast(_2296.CylindricalSocket)

        @property
        def socket(
            self: "CycloidalDiscAxialLeftSocket._Cast_CycloidalDiscAxialLeftSocket",
        ) -> "_2316.Socket":
            from mastapy.system_model.connections_and_sockets import _2316

            return self._parent._cast(_2316.Socket)

        @property
        def cycloidal_disc_axial_left_socket(
            self: "CycloidalDiscAxialLeftSocket._Cast_CycloidalDiscAxialLeftSocket",
        ) -> "CycloidalDiscAxialLeftSocket":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscAxialLeftSocket._Cast_CycloidalDiscAxialLeftSocket",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscAxialLeftSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscAxialLeftSocket._Cast_CycloidalDiscAxialLeftSocket":
        return self._Cast_CycloidalDiscAxialLeftSocket(self)
