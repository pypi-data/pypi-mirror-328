"""PlanetaryConnectionSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2805
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "PlanetaryConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2287
    from mastapy.system_model.analyses_and_results.static_loads import _6932
    from mastapy.system_model.analyses_and_results.power_flows import _4117
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2688,
        _2727,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7539,
        _7540,
        _7537,
    )
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionSystemDeflection",)


Self = TypeVar("Self", bound="PlanetaryConnectionSystemDeflection")


class PlanetaryConnectionSystemDeflection(
    _2805.ShaftToMountableComponentConnectionSystemDeflection
):
    """PlanetaryConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryConnectionSystemDeflection")

    class _Cast_PlanetaryConnectionSystemDeflection:
        """Special nested class for casting PlanetaryConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
            parent: "PlanetaryConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_system_deflection(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
        ) -> "_2805.ShaftToMountableComponentConnectionSystemDeflection":
            return self._parent._cast(
                _2805.ShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_system_deflection(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
        ) -> "_2688.AbstractShaftToMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2688,
            )

            return self._parent._cast(
                _2688.AbstractShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
        ) -> "_2727.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
        ) -> "_7539.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
        ) -> "_7540.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_connection_system_deflection(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
        ) -> "PlanetaryConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
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
        self: Self, instance_to_wrap: "PlanetaryConnectionSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2287.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6932.PlanetaryConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4117.PlanetaryConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PlanetaryConnectionPowerFlow

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
    ) -> (
        "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection"
    ):
        return self._Cast_PlanetaryConnectionSystemDeflection(self)
