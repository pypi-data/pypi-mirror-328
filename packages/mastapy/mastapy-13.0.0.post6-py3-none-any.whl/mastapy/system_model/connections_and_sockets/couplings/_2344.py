"""ConceptCouplingConnection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.couplings import _2346
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "ConceptCouplingConnection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2281, _2272
    from mastapy.system_model import _2203


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnection",)


Self = TypeVar("Self", bound="ConceptCouplingConnection")


class ConceptCouplingConnection(_2346.CouplingConnection):
    """ConceptCouplingConnection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCouplingConnection")

    class _Cast_ConceptCouplingConnection:
        """Special nested class for casting ConceptCouplingConnection to subclasses."""

        def __init__(
            self: "ConceptCouplingConnection._Cast_ConceptCouplingConnection",
            parent: "ConceptCouplingConnection",
        ):
            self._parent = parent

        @property
        def coupling_connection(
            self: "ConceptCouplingConnection._Cast_ConceptCouplingConnection",
        ) -> "_2346.CouplingConnection":
            return self._parent._cast(_2346.CouplingConnection)

        @property
        def inter_mountable_component_connection(
            self: "ConceptCouplingConnection._Cast_ConceptCouplingConnection",
        ) -> "_2281.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2281

            return self._parent._cast(_2281.InterMountableComponentConnection)

        @property
        def connection(
            self: "ConceptCouplingConnection._Cast_ConceptCouplingConnection",
        ) -> "_2272.Connection":
            from mastapy.system_model.connections_and_sockets import _2272

            return self._parent._cast(_2272.Connection)

        @property
        def design_entity(
            self: "ConceptCouplingConnection._Cast_ConceptCouplingConnection",
        ) -> "_2203.DesignEntity":
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def concept_coupling_connection(
            self: "ConceptCouplingConnection._Cast_ConceptCouplingConnection",
        ) -> "ConceptCouplingConnection":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnection._Cast_ConceptCouplingConnection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptCouplingConnection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingConnection._Cast_ConceptCouplingConnection":
        return self._Cast_ConceptCouplingConnection(self)
