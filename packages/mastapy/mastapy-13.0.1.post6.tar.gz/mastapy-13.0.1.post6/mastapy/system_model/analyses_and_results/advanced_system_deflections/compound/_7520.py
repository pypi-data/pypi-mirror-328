"""SynchroniserHalfCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7521,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "SynchroniserHalfCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2604
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7390,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7445,
        _7483,
        _7431,
        _7485,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SynchroniserHalfCompoundAdvancedSystemDeflection")


class SynchroniserHalfCompoundAdvancedSystemDeflection(
    _7521.SynchroniserPartCompoundAdvancedSystemDeflection
):
    """SynchroniserHalfCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserHalfCompoundAdvancedSystemDeflection"
    )

    class _Cast_SynchroniserHalfCompoundAdvancedSystemDeflection:
        """Special nested class for casting SynchroniserHalfCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
            parent: "SynchroniserHalfCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_advanced_system_deflection(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
        ) -> "_7521.SynchroniserPartCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7521.SynchroniserPartCompoundAdvancedSystemDeflection
            )

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
        ) -> "_7445.CouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7445,
            )

            return self._parent._cast(
                _7445.CouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
        ) -> "_7483.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7483,
            )

            return self._parent._cast(
                _7483.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
        ) -> "_7431.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(_7431.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
        ) -> "_7485.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_advanced_system_deflection(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
        ) -> "SynchroniserHalfCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "SynchroniserHalfCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2604.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

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
    ) -> "List[_7390.SynchroniserHalfAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SynchroniserHalfAdvancedSystemDeflection]

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
    ) -> "List[_7390.SynchroniserHalfAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SynchroniserHalfAdvancedSystemDeflection]

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
    ) -> "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection":
        return self._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection(self)
