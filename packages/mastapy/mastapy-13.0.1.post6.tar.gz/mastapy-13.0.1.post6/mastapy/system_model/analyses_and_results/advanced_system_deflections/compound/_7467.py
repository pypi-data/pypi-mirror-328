"""GuideDxfModelCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7431,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "GuideDxfModelCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7336,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7485,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="GuideDxfModelCompoundAdvancedSystemDeflection")


class GuideDxfModelCompoundAdvancedSystemDeflection(
    _7431.ComponentCompoundAdvancedSystemDeflection
):
    """GuideDxfModelCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GuideDxfModelCompoundAdvancedSystemDeflection"
    )

    class _Cast_GuideDxfModelCompoundAdvancedSystemDeflection:
        """Special nested class for casting GuideDxfModelCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "GuideDxfModelCompoundAdvancedSystemDeflection._Cast_GuideDxfModelCompoundAdvancedSystemDeflection",
            parent: "GuideDxfModelCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_compound_advanced_system_deflection(
            self: "GuideDxfModelCompoundAdvancedSystemDeflection._Cast_GuideDxfModelCompoundAdvancedSystemDeflection",
        ) -> "_7431.ComponentCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7431.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "GuideDxfModelCompoundAdvancedSystemDeflection._Cast_GuideDxfModelCompoundAdvancedSystemDeflection",
        ) -> "_7485.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "GuideDxfModelCompoundAdvancedSystemDeflection._Cast_GuideDxfModelCompoundAdvancedSystemDeflection",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GuideDxfModelCompoundAdvancedSystemDeflection._Cast_GuideDxfModelCompoundAdvancedSystemDeflection",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelCompoundAdvancedSystemDeflection._Cast_GuideDxfModelCompoundAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def guide_dxf_model_compound_advanced_system_deflection(
            self: "GuideDxfModelCompoundAdvancedSystemDeflection._Cast_GuideDxfModelCompoundAdvancedSystemDeflection",
        ) -> "GuideDxfModelCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelCompoundAdvancedSystemDeflection._Cast_GuideDxfModelCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "GuideDxfModelCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2455.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

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
    ) -> "List[_7336.GuideDxfModelAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.GuideDxfModelAdvancedSystemDeflection]

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
    ) -> "List[_7336.GuideDxfModelAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.GuideDxfModelAdvancedSystemDeflection]

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
    ) -> "GuideDxfModelCompoundAdvancedSystemDeflection._Cast_GuideDxfModelCompoundAdvancedSystemDeflection":
        return self._Cast_GuideDxfModelCompoundAdvancedSystemDeflection(self)
