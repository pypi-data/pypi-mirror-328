"""SynchroniserCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7525,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "SynchroniserCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2623
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7410,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7427,
        _7506,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SynchroniserCompoundAdvancedSystemDeflection")


class SynchroniserCompoundAdvancedSystemDeflection(
    _7525.SpecialisedAssemblyCompoundAdvancedSystemDeflection
):
    """SynchroniserCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserCompoundAdvancedSystemDeflection"
    )

    class _Cast_SynchroniserCompoundAdvancedSystemDeflection:
        """Special nested class for casting SynchroniserCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SynchroniserCompoundAdvancedSystemDeflection._Cast_SynchroniserCompoundAdvancedSystemDeflection",
            parent: "SynchroniserCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "SynchroniserCompoundAdvancedSystemDeflection._Cast_SynchroniserCompoundAdvancedSystemDeflection",
        ) -> "_7525.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7525.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "SynchroniserCompoundAdvancedSystemDeflection._Cast_SynchroniserCompoundAdvancedSystemDeflection",
        ) -> "_7427.AbstractAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7427,
            )

            return self._parent._cast(
                _7427.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "SynchroniserCompoundAdvancedSystemDeflection._Cast_SynchroniserCompoundAdvancedSystemDeflection",
        ) -> "_7506.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(_7506.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "SynchroniserCompoundAdvancedSystemDeflection._Cast_SynchroniserCompoundAdvancedSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserCompoundAdvancedSystemDeflection._Cast_SynchroniserCompoundAdvancedSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserCompoundAdvancedSystemDeflection._Cast_SynchroniserCompoundAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def synchroniser_compound_advanced_system_deflection(
            self: "SynchroniserCompoundAdvancedSystemDeflection._Cast_SynchroniserCompoundAdvancedSystemDeflection",
        ) -> "SynchroniserCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SynchroniserCompoundAdvancedSystemDeflection._Cast_SynchroniserCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "SynchroniserCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2623.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2623.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7410.SynchroniserAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SynchroniserAdvancedSystemDeflection]

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
    ) -> "List[_7410.SynchroniserAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SynchroniserAdvancedSystemDeflection]

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
    ) -> "SynchroniserCompoundAdvancedSystemDeflection._Cast_SynchroniserCompoundAdvancedSystemDeflection":
        return self._Cast_SynchroniserCompoundAdvancedSystemDeflection(self)
