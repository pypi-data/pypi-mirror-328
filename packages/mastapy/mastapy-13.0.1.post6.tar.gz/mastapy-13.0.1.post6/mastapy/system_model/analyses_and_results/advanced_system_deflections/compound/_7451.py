"""CycloidalDiscCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7407,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "CycloidalDiscCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2569
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7318,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7408,
        _7431,
        _7485,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CycloidalDiscCompoundAdvancedSystemDeflection")


class CycloidalDiscCompoundAdvancedSystemDeflection(
    _7407.AbstractShaftCompoundAdvancedSystemDeflection
):
    """CycloidalDiscCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscCompoundAdvancedSystemDeflection"
    )

    class _Cast_CycloidalDiscCompoundAdvancedSystemDeflection:
        """Special nested class for casting CycloidalDiscCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CycloidalDiscCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCompoundAdvancedSystemDeflection",
            parent: "CycloidalDiscCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_advanced_system_deflection(
            self: "CycloidalDiscCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCompoundAdvancedSystemDeflection",
        ) -> "_7407.AbstractShaftCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7407.AbstractShaftCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_or_housing_compound_advanced_system_deflection(
            self: "CycloidalDiscCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCompoundAdvancedSystemDeflection",
        ) -> "_7408.AbstractShaftOrHousingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7408,
            )

            return self._parent._cast(
                _7408.AbstractShaftOrHousingCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "CycloidalDiscCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCompoundAdvancedSystemDeflection",
        ) -> "_7431.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(_7431.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "CycloidalDiscCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCompoundAdvancedSystemDeflection",
        ) -> "_7485.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "CycloidalDiscCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCompoundAdvancedSystemDeflection",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCompoundAdvancedSystemDeflection",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCompoundAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_advanced_system_deflection(
            self: "CycloidalDiscCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCompoundAdvancedSystemDeflection",
        ) -> "CycloidalDiscCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "CycloidalDiscCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2569.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

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
    ) -> "List[_7318.CycloidalDiscAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CycloidalDiscAdvancedSystemDeflection]

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
    ) -> "List[_7318.CycloidalDiscAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CycloidalDiscAdvancedSystemDeflection]

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
    ) -> "CycloidalDiscCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCompoundAdvancedSystemDeflection":
        return self._Cast_CycloidalDiscCompoundAdvancedSystemDeflection(self)
