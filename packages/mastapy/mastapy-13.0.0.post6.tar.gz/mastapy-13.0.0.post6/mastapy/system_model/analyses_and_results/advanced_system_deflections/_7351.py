"""MeasurementComponentAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7398
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "MeasurementComponentAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2463
    from mastapy.system_model.analyses_and_results.static_loads import _6922
    from mastapy.system_model.analyses_and_results.system_deflections import _2780
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7352,
        _7297,
        _7354,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="MeasurementComponentAdvancedSystemDeflection")


class MeasurementComponentAdvancedSystemDeflection(
    _7398.VirtualComponentAdvancedSystemDeflection
):
    """MeasurementComponentAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MeasurementComponentAdvancedSystemDeflection"
    )

    class _Cast_MeasurementComponentAdvancedSystemDeflection:
        """Special nested class for casting MeasurementComponentAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "MeasurementComponentAdvancedSystemDeflection._Cast_MeasurementComponentAdvancedSystemDeflection",
            parent: "MeasurementComponentAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def virtual_component_advanced_system_deflection(
            self: "MeasurementComponentAdvancedSystemDeflection._Cast_MeasurementComponentAdvancedSystemDeflection",
        ) -> "_7398.VirtualComponentAdvancedSystemDeflection":
            return self._parent._cast(_7398.VirtualComponentAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "MeasurementComponentAdvancedSystemDeflection._Cast_MeasurementComponentAdvancedSystemDeflection",
        ) -> "_7352.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "MeasurementComponentAdvancedSystemDeflection._Cast_MeasurementComponentAdvancedSystemDeflection",
        ) -> "_7297.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7297,
            )

            return self._parent._cast(_7297.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "MeasurementComponentAdvancedSystemDeflection._Cast_MeasurementComponentAdvancedSystemDeflection",
        ) -> "_7354.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(_7354.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "MeasurementComponentAdvancedSystemDeflection._Cast_MeasurementComponentAdvancedSystemDeflection",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MeasurementComponentAdvancedSystemDeflection._Cast_MeasurementComponentAdvancedSystemDeflection",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MeasurementComponentAdvancedSystemDeflection._Cast_MeasurementComponentAdvancedSystemDeflection",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MeasurementComponentAdvancedSystemDeflection._Cast_MeasurementComponentAdvancedSystemDeflection",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentAdvancedSystemDeflection._Cast_MeasurementComponentAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def measurement_component_advanced_system_deflection(
            self: "MeasurementComponentAdvancedSystemDeflection._Cast_MeasurementComponentAdvancedSystemDeflection",
        ) -> "MeasurementComponentAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentAdvancedSystemDeflection._Cast_MeasurementComponentAdvancedSystemDeflection",
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
        instance_to_wrap: "MeasurementComponentAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2463.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6922.MeasurementComponentLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase

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
    ) -> "List[_2780.MeasurementComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.MeasurementComponentSystemDeflection]

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
    ) -> "MeasurementComponentAdvancedSystemDeflection._Cast_MeasurementComponentAdvancedSystemDeflection":
        return self._Cast_MeasurementComponentAdvancedSystemDeflection(self)
