"""ConceptGearMesh"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2333
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConceptGearMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.concept import _1195
    from mastapy.system_model.connections_and_sockets import _2301, _2292
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearMesh",)


Self = TypeVar("Self", bound="ConceptGearMesh")


class ConceptGearMesh(_2333.GearMesh):
    """ConceptGearMesh

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearMesh")

    class _Cast_ConceptGearMesh:
        """Special nested class for casting ConceptGearMesh to subclasses."""

        def __init__(
            self: "ConceptGearMesh._Cast_ConceptGearMesh", parent: "ConceptGearMesh"
        ):
            self._parent = parent

        @property
        def gear_mesh(
            self: "ConceptGearMesh._Cast_ConceptGearMesh",
        ) -> "_2333.GearMesh":
            return self._parent._cast(_2333.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "ConceptGearMesh._Cast_ConceptGearMesh",
        ) -> "_2301.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2301

            return self._parent._cast(_2301.InterMountableComponentConnection)

        @property
        def connection(
            self: "ConceptGearMesh._Cast_ConceptGearMesh",
        ) -> "_2292.Connection":
            from mastapy.system_model.connections_and_sockets import _2292

            return self._parent._cast(_2292.Connection)

        @property
        def design_entity(
            self: "ConceptGearMesh._Cast_ConceptGearMesh",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def concept_gear_mesh(
            self: "ConceptGearMesh._Cast_ConceptGearMesh",
        ) -> "ConceptGearMesh":
            return self._parent

        def __getattr__(self: "ConceptGearMesh._Cast_ConceptGearMesh", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_drop_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinionDropAngle

        if temp is None:
            return 0.0

        return temp

    @pinion_drop_angle.setter
    @enforce_parameter_types
    def pinion_drop_angle(self: Self, value: "float"):
        self.wrapped.PinionDropAngle = float(value) if value is not None else 0.0

    @property
    def wheel_drop_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelDropAngle

        if temp is None:
            return 0.0

        return temp

    @wheel_drop_angle.setter
    @enforce_parameter_types
    def wheel_drop_angle(self: Self, value: "float"):
        self.wrapped.WheelDropAngle = float(value) if value is not None else 0.0

    @property
    def active_gear_mesh_design(self: Self) -> "_1195.ConceptGearMeshDesign":
        """mastapy.gears.gear_designs.concept.ConceptGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def concept_gear_mesh_design(self: Self) -> "_1195.ConceptGearMeshDesign":
        """mastapy.gears.gear_designs.concept.ConceptGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConceptGearMesh._Cast_ConceptGearMesh":
        return self._Cast_ConceptGearMesh(self)
