"""KlingelnbergCycloPalloidHypoidGearMeshLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6913
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2319
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6846,
        _6892,
        _6911,
        _6849,
    )
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshLoadCase",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearMeshLoadCase")


class KlingelnbergCycloPalloidHypoidGearMeshLoadCase(
    _6913.KlingelnbergCycloPalloidConicalGearMeshLoadCase
):
    """KlingelnbergCycloPalloidHypoidGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshLoadCase to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
        ) -> "_6913.KlingelnbergCycloPalloidConicalGearMeshLoadCase":
            return self._parent._cast(
                _6913.KlingelnbergCycloPalloidConicalGearMeshLoadCase
            )

        @property
        def conical_gear_mesh_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
        ) -> "_6846.ConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ConicalGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
        ) -> "_6892.GearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6892

            return self._parent._cast(_6892.GearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
        ) -> "_6911.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6911

            return self._parent._cast(_6911.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
        ) -> "_6849.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2319.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase(self)
