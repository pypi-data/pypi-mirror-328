"""PartToPartShearCouplingConnectionPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4090
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "PartToPartShearCouplingConnectionPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2368
    from mastapy.system_model.analyses_and_results.static_loads import _6951
    from mastapy.system_model.analyses_and_results.power_flows import _4121, _4088
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionPowerFlow",)


Self = TypeVar("Self", bound="PartToPartShearCouplingConnectionPowerFlow")


class PartToPartShearCouplingConnectionPowerFlow(_4090.CouplingConnectionPowerFlow):
    """PartToPartShearCouplingConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingConnectionPowerFlow"
    )

    class _Cast_PartToPartShearCouplingConnectionPowerFlow:
        """Special nested class for casting PartToPartShearCouplingConnectionPowerFlow to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionPowerFlow._Cast_PartToPartShearCouplingConnectionPowerFlow",
            parent: "PartToPartShearCouplingConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_connection_power_flow(
            self: "PartToPartShearCouplingConnectionPowerFlow._Cast_PartToPartShearCouplingConnectionPowerFlow",
        ) -> "_4090.CouplingConnectionPowerFlow":
            return self._parent._cast(_4090.CouplingConnectionPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "PartToPartShearCouplingConnectionPowerFlow._Cast_PartToPartShearCouplingConnectionPowerFlow",
        ) -> "_4121.InterMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4121

            return self._parent._cast(_4121.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "PartToPartShearCouplingConnectionPowerFlow._Cast_PartToPartShearCouplingConnectionPowerFlow",
        ) -> "_4088.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "PartToPartShearCouplingConnectionPowerFlow._Cast_PartToPartShearCouplingConnectionPowerFlow",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PartToPartShearCouplingConnectionPowerFlow._Cast_PartToPartShearCouplingConnectionPowerFlow",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PartToPartShearCouplingConnectionPowerFlow._Cast_PartToPartShearCouplingConnectionPowerFlow",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingConnectionPowerFlow._Cast_PartToPartShearCouplingConnectionPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionPowerFlow._Cast_PartToPartShearCouplingConnectionPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_power_flow(
            self: "PartToPartShearCouplingConnectionPowerFlow._Cast_PartToPartShearCouplingConnectionPowerFlow",
        ) -> "PartToPartShearCouplingConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionPowerFlow._Cast_PartToPartShearCouplingConnectionPowerFlow",
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
        self: Self, instance_to_wrap: "PartToPartShearCouplingConnectionPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2368.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6951.PartToPartShearCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingConnectionPowerFlow._Cast_PartToPartShearCouplingConnectionPowerFlow":
        return self._Cast_PartToPartShearCouplingConnectionPowerFlow(self)
