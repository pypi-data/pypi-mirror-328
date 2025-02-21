"""ConnectorCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2929
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ConnectorCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2728
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2859,
        _2930,
        _2949,
        _2876,
        _2931,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorCompoundSystemDeflection",)


Self = TypeVar("Self", bound="ConnectorCompoundSystemDeflection")


class ConnectorCompoundSystemDeflection(
    _2929.MountableComponentCompoundSystemDeflection
):
    """ConnectorCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorCompoundSystemDeflection")

    class _Cast_ConnectorCompoundSystemDeflection:
        """Special nested class for casting ConnectorCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
            parent: "ConnectorCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_system_deflection(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
        ) -> "_2929.MountableComponentCompoundSystemDeflection":
            return self._parent._cast(_2929.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
        ) -> "_2876.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2876,
            )

            return self._parent._cast(_2876.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
        ) -> "_2931.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(_2931.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bearing_compound_system_deflection(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
        ) -> "_2859.BearingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2859,
            )

            return self._parent._cast(_2859.BearingCompoundSystemDeflection)

        @property
        def oil_seal_compound_system_deflection(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
        ) -> "_2930.OilSealCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2930,
            )

            return self._parent._cast(_2930.OilSealCompoundSystemDeflection)

        @property
        def shaft_hub_connection_compound_system_deflection(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
        ) -> "_2949.ShaftHubConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2949,
            )

            return self._parent._cast(_2949.ShaftHubConnectionCompoundSystemDeflection)

        @property
        def connector_compound_system_deflection(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
        ) -> "ConnectorCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "ConnectorCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_2728.ConnectorSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConnectorSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2728.ConnectorSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConnectorSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection":
        return self._Cast_ConnectorCompoundSystemDeflection(self)
