"""ZerolBevelGearMeshCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4184
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ZerolBevelGearMeshCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2331
    from mastapy.system_model.analyses_and_results.power_flows import _4164
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
__all__ = ("ZerolBevelGearMeshCompoundPowerFlow",)


Self = TypeVar("Self", bound="ZerolBevelGearMeshCompoundPowerFlow")


class ZerolBevelGearMeshCompoundPowerFlow(_4184.BevelGearMeshCompoundPowerFlow):
    """ZerolBevelGearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearMeshCompoundPowerFlow")

    class _Cast_ZerolBevelGearMeshCompoundPowerFlow:
        """Special nested class for casting ZerolBevelGearMeshCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshCompoundPowerFlow._Cast_ZerolBevelGearMeshCompoundPowerFlow",
            parent: "ZerolBevelGearMeshCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_power_flow(
            self: "ZerolBevelGearMeshCompoundPowerFlow._Cast_ZerolBevelGearMeshCompoundPowerFlow",
        ) -> "_4184.BevelGearMeshCompoundPowerFlow":
            return self._parent._cast(_4184.BevelGearMeshCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_mesh_compound_power_flow(
            self: "ZerolBevelGearMeshCompoundPowerFlow._Cast_ZerolBevelGearMeshCompoundPowerFlow",
        ) -> "_4172.AGMAGleasonConicalGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4172,
            )

            return self._parent._cast(_4172.AGMAGleasonConicalGearMeshCompoundPowerFlow)

        @property
        def conical_gear_mesh_compound_power_flow(
            self: "ZerolBevelGearMeshCompoundPowerFlow._Cast_ZerolBevelGearMeshCompoundPowerFlow",
        ) -> "_4200.ConicalGearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4200,
            )

            return self._parent._cast(_4200.ConicalGearMeshCompoundPowerFlow)

        @property
        def gear_mesh_compound_power_flow(
            self: "ZerolBevelGearMeshCompoundPowerFlow._Cast_ZerolBevelGearMeshCompoundPowerFlow",
        ) -> "_4226.GearMeshCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4226,
            )

            return self._parent._cast(_4226.GearMeshCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "ZerolBevelGearMeshCompoundPowerFlow._Cast_ZerolBevelGearMeshCompoundPowerFlow",
        ) -> "_4232.InterMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4232,
            )

            return self._parent._cast(
                _4232.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "ZerolBevelGearMeshCompoundPowerFlow._Cast_ZerolBevelGearMeshCompoundPowerFlow",
        ) -> "_4202.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4202,
            )

            return self._parent._cast(_4202.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "ZerolBevelGearMeshCompoundPowerFlow._Cast_ZerolBevelGearMeshCompoundPowerFlow",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearMeshCompoundPowerFlow._Cast_ZerolBevelGearMeshCompoundPowerFlow",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearMeshCompoundPowerFlow._Cast_ZerolBevelGearMeshCompoundPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_power_flow(
            self: "ZerolBevelGearMeshCompoundPowerFlow._Cast_ZerolBevelGearMeshCompoundPowerFlow",
        ) -> "ZerolBevelGearMeshCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshCompoundPowerFlow._Cast_ZerolBevelGearMeshCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "ZerolBevelGearMeshCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2331.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2331.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

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
    ) -> "List[_4164.ZerolBevelGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ZerolBevelGearMeshPowerFlow]

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
    ) -> "List[_4164.ZerolBevelGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ZerolBevelGearMeshPowerFlow]

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
    ) -> (
        "ZerolBevelGearMeshCompoundPowerFlow._Cast_ZerolBevelGearMeshCompoundPowerFlow"
    ):
        return self._Cast_ZerolBevelGearMeshCompoundPowerFlow(self)
