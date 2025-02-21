"""BevelGearMeshPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4057
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "BevelGearMeshPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4064,
        _4157,
        _4163,
        _4166,
        _4185,
        _4085,
        _4114,
        _4121,
        _4088,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshPowerFlow",)


Self = TypeVar("Self", bound="BevelGearMeshPowerFlow")


class BevelGearMeshPowerFlow(_4057.AGMAGleasonConicalGearMeshPowerFlow):
    """BevelGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshPowerFlow")

    class _Cast_BevelGearMeshPowerFlow:
        """Special nested class for casting BevelGearMeshPowerFlow to subclasses."""

        def __init__(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
            parent: "BevelGearMeshPowerFlow",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_4057.AGMAGleasonConicalGearMeshPowerFlow":
            return self._parent._cast(_4057.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_4085.ConicalGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4085

            return self._parent._cast(_4085.ConicalGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_4114.GearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.GearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_4121.InterMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4121

            return self._parent._cast(_4121.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_4088.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_4064.BevelDifferentialGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4064

            return self._parent._cast(_4064.BevelDifferentialGearMeshPowerFlow)

        @property
        def spiral_bevel_gear_mesh_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_4157.SpiralBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4157

            return self._parent._cast(_4157.SpiralBevelGearMeshPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_4163.StraightBevelDiffGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4163

            return self._parent._cast(_4163.StraightBevelDiffGearMeshPowerFlow)

        @property
        def straight_bevel_gear_mesh_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_4166.StraightBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4166

            return self._parent._cast(_4166.StraightBevelGearMeshPowerFlow)

        @property
        def zerol_bevel_gear_mesh_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_4185.ZerolBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4185

            return self._parent._cast(_4185.ZerolBevelGearMeshPowerFlow)

        @property
        def bevel_gear_mesh_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "BevelGearMeshPowerFlow":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMeshPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2323.BevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow":
        return self._Cast_BevelGearMeshPowerFlow(self)
