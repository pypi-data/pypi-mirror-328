"""ClutchHalfCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7445,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ClutchHalfCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2579
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7296,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7483,
        _7431,
        _7485,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalfCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ClutchHalfCompoundAdvancedSystemDeflection")


class ClutchHalfCompoundAdvancedSystemDeflection(
    _7445.CouplingHalfCompoundAdvancedSystemDeflection
):
    """ClutchHalfCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ClutchHalfCompoundAdvancedSystemDeflection"
    )

    class _Cast_ClutchHalfCompoundAdvancedSystemDeflection:
        """Special nested class for casting ClutchHalfCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ClutchHalfCompoundAdvancedSystemDeflection._Cast_ClutchHalfCompoundAdvancedSystemDeflection",
            parent: "ClutchHalfCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "ClutchHalfCompoundAdvancedSystemDeflection._Cast_ClutchHalfCompoundAdvancedSystemDeflection",
        ) -> "_7445.CouplingHalfCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7445.CouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "ClutchHalfCompoundAdvancedSystemDeflection._Cast_ClutchHalfCompoundAdvancedSystemDeflection",
        ) -> "_7483.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7483,
            )

            return self._parent._cast(
                _7483.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "ClutchHalfCompoundAdvancedSystemDeflection._Cast_ClutchHalfCompoundAdvancedSystemDeflection",
        ) -> "_7431.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(_7431.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "ClutchHalfCompoundAdvancedSystemDeflection._Cast_ClutchHalfCompoundAdvancedSystemDeflection",
        ) -> "_7485.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ClutchHalfCompoundAdvancedSystemDeflection._Cast_ClutchHalfCompoundAdvancedSystemDeflection",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchHalfCompoundAdvancedSystemDeflection._Cast_ClutchHalfCompoundAdvancedSystemDeflection",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHalfCompoundAdvancedSystemDeflection._Cast_ClutchHalfCompoundAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_half_compound_advanced_system_deflection(
            self: "ClutchHalfCompoundAdvancedSystemDeflection._Cast_ClutchHalfCompoundAdvancedSystemDeflection",
        ) -> "ClutchHalfCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ClutchHalfCompoundAdvancedSystemDeflection._Cast_ClutchHalfCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ClutchHalfCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2579.ClutchHalf":
        """mastapy.system_model.part_model.couplings.ClutchHalf

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
    ) -> "List[_7296.ClutchHalfAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ClutchHalfAdvancedSystemDeflection]

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
    ) -> "List[_7296.ClutchHalfAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ClutchHalfAdvancedSystemDeflection]

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
    ) -> "ClutchHalfCompoundAdvancedSystemDeflection._Cast_ClutchHalfCompoundAdvancedSystemDeflection":
        return self._Cast_ClutchHalfCompoundAdvancedSystemDeflection(self)
