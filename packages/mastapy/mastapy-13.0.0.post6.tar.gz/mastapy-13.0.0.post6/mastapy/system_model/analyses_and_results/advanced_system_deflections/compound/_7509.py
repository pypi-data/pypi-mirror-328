"""SpringDamperHalfCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7444,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "SpringDamperHalfCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2601
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7379,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7482,
        _7430,
        _7484,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SpringDamperHalfCompoundAdvancedSystemDeflection")


class SpringDamperHalfCompoundAdvancedSystemDeflection(
    _7444.CouplingHalfCompoundAdvancedSystemDeflection
):
    """SpringDamperHalfCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperHalfCompoundAdvancedSystemDeflection"
    )

    class _Cast_SpringDamperHalfCompoundAdvancedSystemDeflection:
        """Special nested class for casting SpringDamperHalfCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection",
            parent: "SpringDamperHalfCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection",
        ) -> "_7444.CouplingHalfCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7444.CouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection",
        ) -> "_7482.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(
                _7482.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection",
        ) -> "_7430.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7430,
            )

            return self._parent._cast(_7430.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection",
        ) -> "_7484.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7484,
            )

            return self._parent._cast(_7484.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spring_damper_half_compound_advanced_system_deflection(
            self: "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection",
        ) -> "SpringDamperHalfCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "SpringDamperHalfCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2601.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7379.SpringDamperHalfAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SpringDamperHalfAdvancedSystemDeflection]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7379.SpringDamperHalfAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SpringDamperHalfAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "SpringDamperHalfCompoundAdvancedSystemDeflection._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection":
        return self._Cast_SpringDamperHalfCompoundAdvancedSystemDeflection(self)
