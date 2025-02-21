"""GuideDxfModelAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7319
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "GuideDxfModelAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2475
    from mastapy.system_model.analyses_and_results.static_loads import _6918
    from mastapy.system_model.analyses_and_results.system_deflections import _2783
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7376,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="GuideDxfModelAdvancedSystemDeflection")


class GuideDxfModelAdvancedSystemDeflection(_7319.ComponentAdvancedSystemDeflection):
    """GuideDxfModelAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GuideDxfModelAdvancedSystemDeflection"
    )

    class _Cast_GuideDxfModelAdvancedSystemDeflection:
        """Special nested class for casting GuideDxfModelAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "GuideDxfModelAdvancedSystemDeflection._Cast_GuideDxfModelAdvancedSystemDeflection",
            parent: "GuideDxfModelAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_advanced_system_deflection(
            self: "GuideDxfModelAdvancedSystemDeflection._Cast_GuideDxfModelAdvancedSystemDeflection",
        ) -> "_7319.ComponentAdvancedSystemDeflection":
            return self._parent._cast(_7319.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "GuideDxfModelAdvancedSystemDeflection._Cast_GuideDxfModelAdvancedSystemDeflection",
        ) -> "_7376.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7376,
            )

            return self._parent._cast(_7376.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "GuideDxfModelAdvancedSystemDeflection._Cast_GuideDxfModelAdvancedSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GuideDxfModelAdvancedSystemDeflection._Cast_GuideDxfModelAdvancedSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GuideDxfModelAdvancedSystemDeflection._Cast_GuideDxfModelAdvancedSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GuideDxfModelAdvancedSystemDeflection._Cast_GuideDxfModelAdvancedSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelAdvancedSystemDeflection._Cast_GuideDxfModelAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def guide_dxf_model_advanced_system_deflection(
            self: "GuideDxfModelAdvancedSystemDeflection._Cast_GuideDxfModelAdvancedSystemDeflection",
        ) -> "GuideDxfModelAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelAdvancedSystemDeflection._Cast_GuideDxfModelAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "GuideDxfModelAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2475.GuideDxfModel":
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
    def component_load_case(self: Self) -> "_6918.GuideDxfModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2783.GuideDxfModelSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.GuideDxfModelSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GuideDxfModelAdvancedSystemDeflection._Cast_GuideDxfModelAdvancedSystemDeflection":
        return self._Cast_GuideDxfModelAdvancedSystemDeflection(self)
