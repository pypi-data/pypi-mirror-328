"""RollingRingAssemblyCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7503,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "RollingRingAssemblyCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7367,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7405,
        _7484,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="RollingRingAssemblyCompoundAdvancedSystemDeflection")


class RollingRingAssemblyCompoundAdvancedSystemDeflection(
    _7503.SpecialisedAssemblyCompoundAdvancedSystemDeflection
):
    """RollingRingAssemblyCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingAssemblyCompoundAdvancedSystemDeflection"
    )

    class _Cast_RollingRingAssemblyCompoundAdvancedSystemDeflection:
        """Special nested class for casting RollingRingAssemblyCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "RollingRingAssemblyCompoundAdvancedSystemDeflection._Cast_RollingRingAssemblyCompoundAdvancedSystemDeflection",
            parent: "RollingRingAssemblyCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "RollingRingAssemblyCompoundAdvancedSystemDeflection._Cast_RollingRingAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7503.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7503.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "RollingRingAssemblyCompoundAdvancedSystemDeflection._Cast_RollingRingAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7405.AbstractAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7405,
            )

            return self._parent._cast(
                _7405.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "RollingRingAssemblyCompoundAdvancedSystemDeflection._Cast_RollingRingAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7484.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7484,
            )

            return self._parent._cast(_7484.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "RollingRingAssemblyCompoundAdvancedSystemDeflection._Cast_RollingRingAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingAssemblyCompoundAdvancedSystemDeflection._Cast_RollingRingAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyCompoundAdvancedSystemDeflection._Cast_RollingRingAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_compound_advanced_system_deflection(
            self: "RollingRingAssemblyCompoundAdvancedSystemDeflection._Cast_RollingRingAssemblyCompoundAdvancedSystemDeflection",
        ) -> "RollingRingAssemblyCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyCompoundAdvancedSystemDeflection._Cast_RollingRingAssemblyCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "RollingRingAssemblyCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2597.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2597.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

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
    ) -> "List[_7367.RollingRingAssemblyAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.RollingRingAssemblyAdvancedSystemDeflection]

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
    ) -> "List[_7367.RollingRingAssemblyAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.RollingRingAssemblyAdvancedSystemDeflection]

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
    ) -> "RollingRingAssemblyCompoundAdvancedSystemDeflection._Cast_RollingRingAssemblyCompoundAdvancedSystemDeflection":
        return self._Cast_RollingRingAssemblyCompoundAdvancedSystemDeflection(self)
