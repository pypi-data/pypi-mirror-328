"""RootAssemblyCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7413,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "RootAssemblyCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7370,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7406,
        _7485,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="RootAssemblyCompoundAdvancedSystemDeflection")


class RootAssemblyCompoundAdvancedSystemDeflection(
    _7413.AssemblyCompoundAdvancedSystemDeflection
):
    """RootAssemblyCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RootAssemblyCompoundAdvancedSystemDeflection"
    )

    class _Cast_RootAssemblyCompoundAdvancedSystemDeflection:
        """Special nested class for casting RootAssemblyCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "RootAssemblyCompoundAdvancedSystemDeflection._Cast_RootAssemblyCompoundAdvancedSystemDeflection",
            parent: "RootAssemblyCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def assembly_compound_advanced_system_deflection(
            self: "RootAssemblyCompoundAdvancedSystemDeflection._Cast_RootAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7413.AssemblyCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7413.AssemblyCompoundAdvancedSystemDeflection)

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "RootAssemblyCompoundAdvancedSystemDeflection._Cast_RootAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7406.AbstractAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7406,
            )

            return self._parent._cast(
                _7406.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "RootAssemblyCompoundAdvancedSystemDeflection._Cast_RootAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7485.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "RootAssemblyCompoundAdvancedSystemDeflection._Cast_RootAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RootAssemblyCompoundAdvancedSystemDeflection._Cast_RootAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyCompoundAdvancedSystemDeflection._Cast_RootAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def root_assembly_compound_advanced_system_deflection(
            self: "RootAssemblyCompoundAdvancedSystemDeflection._Cast_RootAssemblyCompoundAdvancedSystemDeflection",
        ) -> "RootAssemblyCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "RootAssemblyCompoundAdvancedSystemDeflection._Cast_RootAssemblyCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "RootAssemblyCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7370.RootAssemblyAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.RootAssemblyAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7370.RootAssemblyAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.RootAssemblyAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblyCompoundAdvancedSystemDeflection._Cast_RootAssemblyCompoundAdvancedSystemDeflection":
        return self._Cast_RootAssemblyCompoundAdvancedSystemDeflection(self)
