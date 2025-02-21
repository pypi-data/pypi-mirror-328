"""PowerLoadCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7528,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "PowerLoadCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2472
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7363,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7483,
        _7431,
        _7485,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="PowerLoadCompoundAdvancedSystemDeflection")


class PowerLoadCompoundAdvancedSystemDeflection(
    _7528.VirtualComponentCompoundAdvancedSystemDeflection
):
    """PowerLoadCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PowerLoadCompoundAdvancedSystemDeflection"
    )

    class _Cast_PowerLoadCompoundAdvancedSystemDeflection:
        """Special nested class for casting PowerLoadCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection",
            parent: "PowerLoadCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_advanced_system_deflection(
            self: "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection",
        ) -> "_7528.VirtualComponentCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7528.VirtualComponentCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection",
        ) -> "_7483.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7483,
            )

            return self._parent._cast(
                _7483.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection",
        ) -> "_7431.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(_7431.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection",
        ) -> "_7485.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def power_load_compound_advanced_system_deflection(
            self: "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection",
        ) -> "PowerLoadCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "PowerLoadCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2472.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

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
    ) -> "List[_7363.PowerLoadAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.PowerLoadAdvancedSystemDeflection]

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
    ) -> "List[_7363.PowerLoadAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.PowerLoadAdvancedSystemDeflection]

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
    ) -> "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection":
        return self._Cast_PowerLoadCompoundAdvancedSystemDeflection(self)
