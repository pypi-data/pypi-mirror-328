"""ExternalCADModelCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2876
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ExternalCADModelCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2452
    from mastapy.system_model.analyses_and_results.system_deflections import _2752
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2931,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelCompoundSystemDeflection",)


Self = TypeVar("Self", bound="ExternalCADModelCompoundSystemDeflection")


class ExternalCADModelCompoundSystemDeflection(_2876.ComponentCompoundSystemDeflection):
    """ExternalCADModelCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ExternalCADModelCompoundSystemDeflection"
    )

    class _Cast_ExternalCADModelCompoundSystemDeflection:
        """Special nested class for casting ExternalCADModelCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "ExternalCADModelCompoundSystemDeflection._Cast_ExternalCADModelCompoundSystemDeflection",
            parent: "ExternalCADModelCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_compound_system_deflection(
            self: "ExternalCADModelCompoundSystemDeflection._Cast_ExternalCADModelCompoundSystemDeflection",
        ) -> "_2876.ComponentCompoundSystemDeflection":
            return self._parent._cast(_2876.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "ExternalCADModelCompoundSystemDeflection._Cast_ExternalCADModelCompoundSystemDeflection",
        ) -> "_2931.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(_2931.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ExternalCADModelCompoundSystemDeflection._Cast_ExternalCADModelCompoundSystemDeflection",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ExternalCADModelCompoundSystemDeflection._Cast_ExternalCADModelCompoundSystemDeflection",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelCompoundSystemDeflection._Cast_ExternalCADModelCompoundSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def external_cad_model_compound_system_deflection(
            self: "ExternalCADModelCompoundSystemDeflection._Cast_ExternalCADModelCompoundSystemDeflection",
        ) -> "ExternalCADModelCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelCompoundSystemDeflection._Cast_ExternalCADModelCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "ExternalCADModelCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2452.ExternalCADModel":
        """mastapy.system_model.part_model.ExternalCADModel

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
    ) -> "List[_2752.ExternalCADModelSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ExternalCADModelSystemDeflection]

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
    ) -> "List[_2752.ExternalCADModelSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ExternalCADModelSystemDeflection]

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
    ) -> "ExternalCADModelCompoundSystemDeflection._Cast_ExternalCADModelCompoundSystemDeflection":
        return self._Cast_ExternalCADModelCompoundSystemDeflection(self)
