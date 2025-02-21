"""CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7451,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7340,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7524,
        _7430,
        _7462,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self",
    bound="CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
)


class CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection(
    _7451.CoaxialConnectionCompoundAdvancedSystemDeflection
):
    """CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = (
        _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
            parent: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_advanced_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7451.CoaxialConnectionCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7451.CoaxialConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def shaft_to_mountable_component_connection_compound_advanced_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
        ) -> (
            "_7524.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7524,
            )

            return self._parent._cast(
                _7524.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7430.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7430,
            )

            return self._parent._cast(
                _7430.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7462.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7462,
            )

            return self._parent._cast(_7462.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7340.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection]

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
    ) -> "List[_7340.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection]

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
    ) -> "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection":
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection(
            self
        )
