"""SpringDamperConnectionSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2729
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "SpringDamperConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2350
    from mastapy.system_model.analyses_and_results.static_loads import _6957
    from mastapy.system_model.analyses_and_results.power_flows import _4139
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2767,
        _2727,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7540,
        _7541,
        _7538,
    )
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionSystemDeflection",)


Self = TypeVar("Self", bound="SpringDamperConnectionSystemDeflection")


class SpringDamperConnectionSystemDeflection(_2729.CouplingConnectionSystemDeflection):
    """SpringDamperConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperConnectionSystemDeflection"
    )

    class _Cast_SpringDamperConnectionSystemDeflection:
        """Special nested class for casting SpringDamperConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "SpringDamperConnectionSystemDeflection._Cast_SpringDamperConnectionSystemDeflection",
            parent: "SpringDamperConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_connection_system_deflection(
            self: "SpringDamperConnectionSystemDeflection._Cast_SpringDamperConnectionSystemDeflection",
        ) -> "_2729.CouplingConnectionSystemDeflection":
            return self._parent._cast(_2729.CouplingConnectionSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "SpringDamperConnectionSystemDeflection._Cast_SpringDamperConnectionSystemDeflection",
        ) -> "_2767.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(
                _2767.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "SpringDamperConnectionSystemDeflection._Cast_SpringDamperConnectionSystemDeflection",
        ) -> "_2727.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "SpringDamperConnectionSystemDeflection._Cast_SpringDamperConnectionSystemDeflection",
        ) -> "_7540.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "SpringDamperConnectionSystemDeflection._Cast_SpringDamperConnectionSystemDeflection",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpringDamperConnectionSystemDeflection._Cast_SpringDamperConnectionSystemDeflection",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpringDamperConnectionSystemDeflection._Cast_SpringDamperConnectionSystemDeflection",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperConnectionSystemDeflection._Cast_SpringDamperConnectionSystemDeflection",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionSystemDeflection._Cast_SpringDamperConnectionSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spring_damper_connection_system_deflection(
            self: "SpringDamperConnectionSystemDeflection._Cast_SpringDamperConnectionSystemDeflection",
        ) -> "SpringDamperConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionSystemDeflection._Cast_SpringDamperConnectionSystemDeflection",
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
        self: Self, instance_to_wrap: "SpringDamperConnectionSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2350.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6957.SpringDamperConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4139.SpringDamperConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.SpringDamperConnectionPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperConnectionSystemDeflection._Cast_SpringDamperConnectionSystemDeflection":
        return self._Cast_SpringDamperConnectionSystemDeflection(self)
