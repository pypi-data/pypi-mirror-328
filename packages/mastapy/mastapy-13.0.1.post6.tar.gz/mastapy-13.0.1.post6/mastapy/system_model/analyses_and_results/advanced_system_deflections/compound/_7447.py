"""CVTCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7416,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "CVTCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7314,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7504,
        _7406,
        _7485,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("CVTCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CVTCompoundAdvancedSystemDeflection")


class CVTCompoundAdvancedSystemDeflection(
    _7416.BeltDriveCompoundAdvancedSystemDeflection
):
    """CVTCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTCompoundAdvancedSystemDeflection")

    class _Cast_CVTCompoundAdvancedSystemDeflection:
        """Special nested class for casting CVTCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CVTCompoundAdvancedSystemDeflection._Cast_CVTCompoundAdvancedSystemDeflection",
            parent: "CVTCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def belt_drive_compound_advanced_system_deflection(
            self: "CVTCompoundAdvancedSystemDeflection._Cast_CVTCompoundAdvancedSystemDeflection",
        ) -> "_7416.BeltDriveCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7416.BeltDriveCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "CVTCompoundAdvancedSystemDeflection._Cast_CVTCompoundAdvancedSystemDeflection",
        ) -> "_7504.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "CVTCompoundAdvancedSystemDeflection._Cast_CVTCompoundAdvancedSystemDeflection",
        ) -> "_7406.AbstractAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7406,
            )

            return self._parent._cast(
                _7406.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "CVTCompoundAdvancedSystemDeflection._Cast_CVTCompoundAdvancedSystemDeflection",
        ) -> "_7485.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "CVTCompoundAdvancedSystemDeflection._Cast_CVTCompoundAdvancedSystemDeflection",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTCompoundAdvancedSystemDeflection._Cast_CVTCompoundAdvancedSystemDeflection",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTCompoundAdvancedSystemDeflection._Cast_CVTCompoundAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_compound_advanced_system_deflection(
            self: "CVTCompoundAdvancedSystemDeflection._Cast_CVTCompoundAdvancedSystemDeflection",
        ) -> "CVTCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CVTCompoundAdvancedSystemDeflection._Cast_CVTCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "CVTCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7314.CVTAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CVTAdvancedSystemDeflection]

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
    ) -> "List[_7314.CVTAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CVTAdvancedSystemDeflection]

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
    ) -> (
        "CVTCompoundAdvancedSystemDeflection._Cast_CVTCompoundAdvancedSystemDeflection"
    ):
        return self._Cast_CVTCompoundAdvancedSystemDeflection(self)
