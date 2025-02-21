"""CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7408,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2338
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7319,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7440,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self",
    bound="CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection",
)


class CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection(
    _7408.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
):
    """CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = (
        _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection",
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection",
            parent: "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_system_deflection(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7408.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7408.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7440.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7440,
            )

            return self._parent._cast(_7440.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_advanced_system_deflection(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection",
        ) -> "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2338.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(
        self: Self,
    ) -> "_2338.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

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
    ) -> "List[_7319.CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection]

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
    ) -> "List[_7319.CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection]

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
    ) -> "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection":
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection(
            self
        )
