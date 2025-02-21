"""BevelDifferentialGearMesh"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2323
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "BevelDifferentialGearMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.bevel import _1199
    from mastapy.system_model.connections_and_sockets.gears import _2319, _2327, _2333
    from mastapy.system_model.connections_and_sockets import _2301, _2292
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMesh",)


Self = TypeVar("Self", bound="BevelDifferentialGearMesh")


class BevelDifferentialGearMesh(_2323.BevelGearMesh):
    """BevelDifferentialGearMesh

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialGearMesh")

    class _Cast_BevelDifferentialGearMesh:
        """Special nested class for casting BevelDifferentialGearMesh to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh",
            parent: "BevelDifferentialGearMesh",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh(
            self: "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh",
        ) -> "_2323.BevelGearMesh":
            return self._parent._cast(_2323.BevelGearMesh)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh",
        ) -> "_2319.AGMAGleasonConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2319

            return self._parent._cast(_2319.AGMAGleasonConicalGearMesh)

        @property
        def conical_gear_mesh(
            self: "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh",
        ) -> "_2327.ConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2327

            return self._parent._cast(_2327.ConicalGearMesh)

        @property
        def gear_mesh(
            self: "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh",
        ) -> "_2333.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2333

            return self._parent._cast(_2333.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh",
        ) -> "_2301.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2301

            return self._parent._cast(_2301.InterMountableComponentConnection)

        @property
        def connection(
            self: "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh",
        ) -> "_2292.Connection":
            from mastapy.system_model.connections_and_sockets import _2292

            return self._parent._cast(_2292.Connection)

        @property
        def design_entity(
            self: "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def bevel_differential_gear_mesh(
            self: "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh",
        ) -> "BevelDifferentialGearMesh":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelDifferentialGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_mesh_design(self: Self) -> "_1199.BevelGearMeshDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearMesh._Cast_BevelDifferentialGearMesh":
        return self._Cast_BevelDifferentialGearMesh(self)
