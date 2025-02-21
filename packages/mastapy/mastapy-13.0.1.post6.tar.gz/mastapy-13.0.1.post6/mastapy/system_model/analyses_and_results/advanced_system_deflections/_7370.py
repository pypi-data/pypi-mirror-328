"""RootAssemblyAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7280
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "RootAssemblyAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7274,
        _7270,
        _7355,
    )
    from mastapy.system_model.part_model import _2474
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="RootAssemblyAdvancedSystemDeflection")


class RootAssemblyAdvancedSystemDeflection(_7280.AssemblyAdvancedSystemDeflection):
    """RootAssemblyAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RootAssemblyAdvancedSystemDeflection")

    class _Cast_RootAssemblyAdvancedSystemDeflection:
        """Special nested class for casting RootAssemblyAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "RootAssemblyAdvancedSystemDeflection._Cast_RootAssemblyAdvancedSystemDeflection",
            parent: "RootAssemblyAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def assembly_advanced_system_deflection(
            self: "RootAssemblyAdvancedSystemDeflection._Cast_RootAssemblyAdvancedSystemDeflection",
        ) -> "_7280.AssemblyAdvancedSystemDeflection":
            return self._parent._cast(_7280.AssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "RootAssemblyAdvancedSystemDeflection._Cast_RootAssemblyAdvancedSystemDeflection",
        ) -> "_7270.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7270,
            )

            return self._parent._cast(_7270.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "RootAssemblyAdvancedSystemDeflection._Cast_RootAssemblyAdvancedSystemDeflection",
        ) -> "_7355.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "RootAssemblyAdvancedSystemDeflection._Cast_RootAssemblyAdvancedSystemDeflection",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RootAssemblyAdvancedSystemDeflection._Cast_RootAssemblyAdvancedSystemDeflection",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RootAssemblyAdvancedSystemDeflection._Cast_RootAssemblyAdvancedSystemDeflection",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RootAssemblyAdvancedSystemDeflection._Cast_RootAssemblyAdvancedSystemDeflection",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyAdvancedSystemDeflection._Cast_RootAssemblyAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def root_assembly_advanced_system_deflection(
            self: "RootAssemblyAdvancedSystemDeflection._Cast_RootAssemblyAdvancedSystemDeflection",
        ) -> "RootAssemblyAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "RootAssemblyAdvancedSystemDeflection._Cast_RootAssemblyAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "RootAssemblyAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_system_deflection_inputs(
        self: Self,
    ) -> "_7274.AdvancedSystemDeflection":
        """mastapy.system_model.analyses_and_results.advanced_system_deflections.AdvancedSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedSystemDeflectionInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2474.RootAssembly":
        """mastapy.system_model.part_model.RootAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblyAdvancedSystemDeflection._Cast_RootAssemblyAdvancedSystemDeflection":
        return self._Cast_RootAssemblyAdvancedSystemDeflection(self)
