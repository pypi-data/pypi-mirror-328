"""SpiralBevelGearMeshCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4184
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "SpiralBevelGearMeshCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323
    from mastapy.system_model.analyses_and_results.power_flows import _4136
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4172,
        _4200,
        _4226,
        _4232,
        _4202,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshCompoundPowerFlow",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshCompoundPowerFlow")


class SpiralBevelGearMeshCompoundPowerFlow(_4184.BevelGearMeshCompoundPowerFlow):
    """SpiralBevelGearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearMeshCompoundPowerFlow")

    class _Cast_SpiralBevelGearMeshCompoundPowerFlow:
        """Special nested class for casting SpiralBevelGearMeshCompoundPowerFlow to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshCompoundPowerFlow._Cast_SpiralBevelGearMeshCompoundPowerFlow",
            parent: "SpiralBevelGearMeshCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_power_flow(
            self: "SpiralBevelGearMeshCompoundPowerFlow._Cast_SpiralBevelGearMeshCompoundPowerFlow",
        ) -> "_4184.BevelGearMeshCompoundPowerFlow":
            return self._parent._cast(_4184.BevelGearMeshCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_mesh_compound_power_flow(
            self: "SpiralBevelGearMeshCompoundPowerFlow._Cast_SpiralBevelGearMeshCompoundPowerFlow",
        ) -> "_4172.AGMAGleasonConicalGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4172,
            )

            return self._parent._cast(_4172.AGMAGleasonConicalGearMeshCompoundPowerFlow)

        @property
        def conical_gear_mesh_compound_power_flow(
            self: "SpiralBevelGearMeshCompoundPowerFlow._Cast_SpiralBevelGearMeshCompoundPowerFlow",
        ) -> "_4200.ConicalGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4200,
            )

            return self._parent._cast(_4200.ConicalGearMeshCompoundPowerFlow)

        @property
        def gear_mesh_compound_power_flow(
            self: "SpiralBevelGearMeshCompoundPowerFlow._Cast_SpiralBevelGearMeshCompoundPowerFlow",
        ) -> "_4226.GearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4226,
            )

            return self._parent._cast(_4226.GearMeshCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "SpiralBevelGearMeshCompoundPowerFlow._Cast_SpiralBevelGearMeshCompoundPowerFlow",
        ) -> "_4232.InterMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4232,
            )

            return self._parent._cast(
                _4232.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "SpiralBevelGearMeshCompoundPowerFlow._Cast_SpiralBevelGearMeshCompoundPowerFlow",
        ) -> "_4202.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4202,
            )

            return self._parent._cast(_4202.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "SpiralBevelGearMeshCompoundPowerFlow._Cast_SpiralBevelGearMeshCompoundPowerFlow",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearMeshCompoundPowerFlow._Cast_SpiralBevelGearMeshCompoundPowerFlow",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshCompoundPowerFlow._Cast_SpiralBevelGearMeshCompoundPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_power_flow(
            self: "SpiralBevelGearMeshCompoundPowerFlow._Cast_SpiralBevelGearMeshCompoundPowerFlow",
        ) -> "SpiralBevelGearMeshCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshCompoundPowerFlow._Cast_SpiralBevelGearMeshCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "SpiralBevelGearMeshCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2323.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2323.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4136.SpiralBevelGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpiralBevelGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4136.SpiralBevelGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpiralBevelGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearMeshCompoundPowerFlow._Cast_SpiralBevelGearMeshCompoundPowerFlow":
        return self._Cast_SpiralBevelGearMeshCompoundPowerFlow(self)
