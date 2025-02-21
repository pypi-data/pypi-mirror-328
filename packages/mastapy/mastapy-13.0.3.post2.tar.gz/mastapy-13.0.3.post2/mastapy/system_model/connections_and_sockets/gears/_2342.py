"""KlingelnbergSpiralBevelGearTeethSocket"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2337
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_SPIRAL_BEVEL_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergSpiralBevelGearTeethSocket",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2328, _2334
    from mastapy.system_model.connections_and_sockets import _2316


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergSpiralBevelGearTeethSocket",)


Self = TypeVar("Self", bound="KlingelnbergSpiralBevelGearTeethSocket")


class KlingelnbergSpiralBevelGearTeethSocket(_2337.KlingelnbergConicalGearTeethSocket):
    """KlingelnbergSpiralBevelGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_SPIRAL_BEVEL_GEAR_TEETH_SOCKET
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergSpiralBevelGearTeethSocket"
    )

    class _Cast_KlingelnbergSpiralBevelGearTeethSocket:
        """Special nested class for casting KlingelnbergSpiralBevelGearTeethSocket to subclasses."""

        def __init__(
            self: "KlingelnbergSpiralBevelGearTeethSocket._Cast_KlingelnbergSpiralBevelGearTeethSocket",
            parent: "KlingelnbergSpiralBevelGearTeethSocket",
        ):
            self._parent = parent

        @property
        def klingelnberg_conical_gear_teeth_socket(
            self: "KlingelnbergSpiralBevelGearTeethSocket._Cast_KlingelnbergSpiralBevelGearTeethSocket",
        ) -> "_2337.KlingelnbergConicalGearTeethSocket":
            return self._parent._cast(_2337.KlingelnbergConicalGearTeethSocket)

        @property
        def conical_gear_teeth_socket(
            self: "KlingelnbergSpiralBevelGearTeethSocket._Cast_KlingelnbergSpiralBevelGearTeethSocket",
        ) -> "_2328.ConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2328

            return self._parent._cast(_2328.ConicalGearTeethSocket)

        @property
        def gear_teeth_socket(
            self: "KlingelnbergSpiralBevelGearTeethSocket._Cast_KlingelnbergSpiralBevelGearTeethSocket",
        ) -> "_2334.GearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2334

            return self._parent._cast(_2334.GearTeethSocket)

        @property
        def socket(
            self: "KlingelnbergSpiralBevelGearTeethSocket._Cast_KlingelnbergSpiralBevelGearTeethSocket",
        ) -> "_2316.Socket":
            from mastapy.system_model.connections_and_sockets import _2316

            return self._parent._cast(_2316.Socket)

        @property
        def klingelnberg_spiral_bevel_gear_teeth_socket(
            self: "KlingelnbergSpiralBevelGearTeethSocket._Cast_KlingelnbergSpiralBevelGearTeethSocket",
        ) -> "KlingelnbergSpiralBevelGearTeethSocket":
            return self._parent

        def __getattr__(
            self: "KlingelnbergSpiralBevelGearTeethSocket._Cast_KlingelnbergSpiralBevelGearTeethSocket",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "KlingelnbergSpiralBevelGearTeethSocket.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergSpiralBevelGearTeethSocket._Cast_KlingelnbergSpiralBevelGearTeethSocket":
        return self._Cast_KlingelnbergSpiralBevelGearTeethSocket(self)
