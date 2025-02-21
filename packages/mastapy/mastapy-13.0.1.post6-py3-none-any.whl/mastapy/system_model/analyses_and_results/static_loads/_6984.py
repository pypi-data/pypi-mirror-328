"""WormGearMeshLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6893
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "WormGearMeshLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2329
    from mastapy.system_model.analyses_and_results.static_loads import _6912, _6850
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshLoadCase",)


Self = TypeVar("Self", bound="WormGearMeshLoadCase")


class WormGearMeshLoadCase(_6893.GearMeshLoadCase):
    """WormGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearMeshLoadCase")

    class _Cast_WormGearMeshLoadCase:
        """Special nested class for casting WormGearMeshLoadCase to subclasses."""

        def __init__(
            self: "WormGearMeshLoadCase._Cast_WormGearMeshLoadCase",
            parent: "WormGearMeshLoadCase",
        ):
            self._parent = parent

        @property
        def gear_mesh_load_case(
            self: "WormGearMeshLoadCase._Cast_WormGearMeshLoadCase",
        ) -> "_6893.GearMeshLoadCase":
            return self._parent._cast(_6893.GearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "WormGearMeshLoadCase._Cast_WormGearMeshLoadCase",
        ) -> "_6912.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6912

            return self._parent._cast(_6912.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "WormGearMeshLoadCase._Cast_WormGearMeshLoadCase",
        ) -> "_6850.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6850

            return self._parent._cast(_6850.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "WormGearMeshLoadCase._Cast_WormGearMeshLoadCase",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearMeshLoadCase._Cast_WormGearMeshLoadCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshLoadCase._Cast_WormGearMeshLoadCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_load_case(
            self: "WormGearMeshLoadCase._Cast_WormGearMeshLoadCase",
        ) -> "WormGearMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "WormGearMeshLoadCase._Cast_WormGearMeshLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearMeshLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2329.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "WormGearMeshLoadCase._Cast_WormGearMeshLoadCase":
        return self._Cast_WormGearMeshLoadCase(self)
