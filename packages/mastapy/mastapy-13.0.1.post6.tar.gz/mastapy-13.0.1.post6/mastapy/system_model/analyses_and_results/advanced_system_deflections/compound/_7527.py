"""UnbalancedMassCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7528,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "UnbalancedMassCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2477
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7398,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7483,
        _7431,
        _7485,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="UnbalancedMassCompoundAdvancedSystemDeflection")


class UnbalancedMassCompoundAdvancedSystemDeflection(
    _7528.VirtualComponentCompoundAdvancedSystemDeflection
):
    """UnbalancedMassCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_UnbalancedMassCompoundAdvancedSystemDeflection"
    )

    class _Cast_UnbalancedMassCompoundAdvancedSystemDeflection:
        """Special nested class for casting UnbalancedMassCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "UnbalancedMassCompoundAdvancedSystemDeflection._Cast_UnbalancedMassCompoundAdvancedSystemDeflection",
            parent: "UnbalancedMassCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_advanced_system_deflection(
            self: "UnbalancedMassCompoundAdvancedSystemDeflection._Cast_UnbalancedMassCompoundAdvancedSystemDeflection",
        ) -> "_7528.VirtualComponentCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7528.VirtualComponentCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "UnbalancedMassCompoundAdvancedSystemDeflection._Cast_UnbalancedMassCompoundAdvancedSystemDeflection",
        ) -> "_7483.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7483,
            )

            return self._parent._cast(
                _7483.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "UnbalancedMassCompoundAdvancedSystemDeflection._Cast_UnbalancedMassCompoundAdvancedSystemDeflection",
        ) -> "_7431.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(_7431.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "UnbalancedMassCompoundAdvancedSystemDeflection._Cast_UnbalancedMassCompoundAdvancedSystemDeflection",
        ) -> "_7485.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "UnbalancedMassCompoundAdvancedSystemDeflection._Cast_UnbalancedMassCompoundAdvancedSystemDeflection",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "UnbalancedMassCompoundAdvancedSystemDeflection._Cast_UnbalancedMassCompoundAdvancedSystemDeflection",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassCompoundAdvancedSystemDeflection._Cast_UnbalancedMassCompoundAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def unbalanced_mass_compound_advanced_system_deflection(
            self: "UnbalancedMassCompoundAdvancedSystemDeflection._Cast_UnbalancedMassCompoundAdvancedSystemDeflection",
        ) -> "UnbalancedMassCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassCompoundAdvancedSystemDeflection._Cast_UnbalancedMassCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "UnbalancedMassCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2477.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

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
    ) -> "List[_7398.UnbalancedMassAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.UnbalancedMassAdvancedSystemDeflection]

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
    ) -> "List[_7398.UnbalancedMassAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.UnbalancedMassAdvancedSystemDeflection]

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
    ) -> "UnbalancedMassCompoundAdvancedSystemDeflection._Cast_UnbalancedMassCompoundAdvancedSystemDeflection":
        return self._Cast_UnbalancedMassCompoundAdvancedSystemDeflection(self)
