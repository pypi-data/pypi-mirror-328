"""CouplingConnectionPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4121
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "CouplingConnectionPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2366
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4074,
        _4079,
        _4136,
        _4160,
        _4176,
        _4088,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionPowerFlow",)


Self = TypeVar("Self", bound="CouplingConnectionPowerFlow")


class CouplingConnectionPowerFlow(_4121.InterMountableComponentConnectionPowerFlow):
    """CouplingConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnectionPowerFlow")

    class _Cast_CouplingConnectionPowerFlow:
        """Special nested class for casting CouplingConnectionPowerFlow to subclasses."""

        def __init__(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
            parent: "CouplingConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_power_flow(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ) -> "_4121.InterMountableComponentConnectionPowerFlow":
            return self._parent._cast(_4121.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ) -> "_4088.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_connection_power_flow(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ) -> "_4074.ClutchConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4074

            return self._parent._cast(_4074.ClutchConnectionPowerFlow)

        @property
        def concept_coupling_connection_power_flow(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ) -> "_4079.ConceptCouplingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4079

            return self._parent._cast(_4079.ConceptCouplingConnectionPowerFlow)

        @property
        def part_to_part_shear_coupling_connection_power_flow(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ) -> "_4136.PartToPartShearCouplingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4136

            return self._parent._cast(_4136.PartToPartShearCouplingConnectionPowerFlow)

        @property
        def spring_damper_connection_power_flow(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ) -> "_4160.SpringDamperConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4160

            return self._parent._cast(_4160.SpringDamperConnectionPowerFlow)

        @property
        def torque_converter_connection_power_flow(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ) -> "_4176.TorqueConverterConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4176

            return self._parent._cast(_4176.TorqueConverterConnectionPowerFlow)

        @property
        def coupling_connection_power_flow(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ) -> "CouplingConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingConnectionPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2366.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

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
    ) -> "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow":
        return self._Cast_CouplingConnectionPowerFlow(self)
