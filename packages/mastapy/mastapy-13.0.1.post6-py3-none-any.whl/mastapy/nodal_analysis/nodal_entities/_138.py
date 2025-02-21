"""GearMeshNodePair"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _125
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_NODE_PAIR = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "GearMeshNodePair"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import _142, _144


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshNodePair",)


Self = TypeVar("Self", bound="GearMeshNodePair")


class GearMeshNodePair(_125.ArbitraryNodalComponent):
    """GearMeshNodePair

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_NODE_PAIR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshNodePair")

    class _Cast_GearMeshNodePair:
        """Special nested class for casting GearMeshNodePair to subclasses."""

        def __init__(
            self: "GearMeshNodePair._Cast_GearMeshNodePair", parent: "GearMeshNodePair"
        ):
            self._parent = parent

        @property
        def arbitrary_nodal_component(
            self: "GearMeshNodePair._Cast_GearMeshNodePair",
        ) -> "_125.ArbitraryNodalComponent":
            return self._parent._cast(_125.ArbitraryNodalComponent)

        @property
        def nodal_component(
            self: "GearMeshNodePair._Cast_GearMeshNodePair",
        ) -> "_142.NodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _142

            return self._parent._cast(_142.NodalComponent)

        @property
        def nodal_entity(
            self: "GearMeshNodePair._Cast_GearMeshNodePair",
        ) -> "_144.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _144

            return self._parent._cast(_144.NodalEntity)

        @property
        def gear_mesh_node_pair(
            self: "GearMeshNodePair._Cast_GearMeshNodePair",
        ) -> "GearMeshNodePair":
            return self._parent

        def __getattr__(self: "GearMeshNodePair._Cast_GearMeshNodePair", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshNodePair.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearMeshNodePair._Cast_GearMeshNodePair":
        return self._Cast_GearMeshNodePair(self)
