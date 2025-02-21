"""KlingelnbergCycloPalloidConicalGearMeshPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4064
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2318
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4104,
        _4107,
        _4093,
        _4100,
        _4067,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshPowerFlow",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearMeshPowerFlow")


class KlingelnbergCycloPalloidConicalGearMeshPowerFlow(_4064.ConicalGearMeshPowerFlow):
    """KlingelnbergCycloPalloidConicalGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshPowerFlow"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshPowerFlow to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
            parent: "KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
        ) -> "_4064.ConicalGearMeshPowerFlow":
            return self._parent._cast(_4064.ConicalGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
        ) -> "_4093.GearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4093

            return self._parent._cast(_4093.GearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
        ) -> "_4100.InterMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4100

            return self._parent._cast(_4100.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
        ) -> "_4067.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
        ) -> "_4104.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4104

            return self._parent._cast(
                _4104.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
        ) -> "_4107.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4107

            return self._parent._cast(
                _4107.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshPowerFlow":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2318.KlingelnbergCycloPalloidConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh

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
    ) -> "KlingelnbergCycloPalloidConicalGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearMeshPowerFlow":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshPowerFlow(self)
