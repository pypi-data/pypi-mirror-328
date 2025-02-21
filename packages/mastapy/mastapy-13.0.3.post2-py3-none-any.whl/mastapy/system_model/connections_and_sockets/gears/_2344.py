"""SpiralBevelGearTeethSocket"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2324
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "SpiralBevelGearTeethSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2320, _2328, _2334
    from mastapy.system_model.connections_and_sockets import _2316


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearTeethSocket",)


Self = TypeVar("Self", bound="SpiralBevelGearTeethSocket")


class SpiralBevelGearTeethSocket(_2324.BevelGearTeethSocket):
    """SpiralBevelGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearTeethSocket")

    class _Cast_SpiralBevelGearTeethSocket:
        """Special nested class for casting SpiralBevelGearTeethSocket to subclasses."""

        def __init__(
            self: "SpiralBevelGearTeethSocket._Cast_SpiralBevelGearTeethSocket",
            parent: "SpiralBevelGearTeethSocket",
        ):
            self._parent = parent

        @property
        def bevel_gear_teeth_socket(
            self: "SpiralBevelGearTeethSocket._Cast_SpiralBevelGearTeethSocket",
        ) -> "_2324.BevelGearTeethSocket":
            return self._parent._cast(_2324.BevelGearTeethSocket)

        @property
        def agma_gleason_conical_gear_teeth_socket(
            self: "SpiralBevelGearTeethSocket._Cast_SpiralBevelGearTeethSocket",
        ) -> "_2320.AGMAGleasonConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2320

            return self._parent._cast(_2320.AGMAGleasonConicalGearTeethSocket)

        @property
        def conical_gear_teeth_socket(
            self: "SpiralBevelGearTeethSocket._Cast_SpiralBevelGearTeethSocket",
        ) -> "_2328.ConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2328

            return self._parent._cast(_2328.ConicalGearTeethSocket)

        @property
        def gear_teeth_socket(
            self: "SpiralBevelGearTeethSocket._Cast_SpiralBevelGearTeethSocket",
        ) -> "_2334.GearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2334

            return self._parent._cast(_2334.GearTeethSocket)

        @property
        def socket(
            self: "SpiralBevelGearTeethSocket._Cast_SpiralBevelGearTeethSocket",
        ) -> "_2316.Socket":
            from mastapy.system_model.connections_and_sockets import _2316

            return self._parent._cast(_2316.Socket)

        @property
        def spiral_bevel_gear_teeth_socket(
            self: "SpiralBevelGearTeethSocket._Cast_SpiralBevelGearTeethSocket",
        ) -> "SpiralBevelGearTeethSocket":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearTeethSocket._Cast_SpiralBevelGearTeethSocket",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearTeethSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearTeethSocket._Cast_SpiralBevelGearTeethSocket":
        return self._Cast_SpiralBevelGearTeethSocket(self)
