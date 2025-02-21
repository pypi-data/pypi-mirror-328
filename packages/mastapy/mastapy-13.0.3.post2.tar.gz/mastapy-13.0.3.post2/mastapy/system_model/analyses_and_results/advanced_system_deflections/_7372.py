"""MassDiscAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7420
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "MassDiscAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2482
    from mastapy.system_model.analyses_and_results.static_loads import _6943
    from mastapy.system_model.analyses_and_results.system_deflections import _2800
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7374,
        _7319,
        _7376,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="MassDiscAdvancedSystemDeflection")


class MassDiscAdvancedSystemDeflection(_7420.VirtualComponentAdvancedSystemDeflection):
    """MassDiscAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MassDiscAdvancedSystemDeflection")

    class _Cast_MassDiscAdvancedSystemDeflection:
        """Special nested class for casting MassDiscAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "MassDiscAdvancedSystemDeflection._Cast_MassDiscAdvancedSystemDeflection",
            parent: "MassDiscAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def virtual_component_advanced_system_deflection(
            self: "MassDiscAdvancedSystemDeflection._Cast_MassDiscAdvancedSystemDeflection",
        ) -> "_7420.VirtualComponentAdvancedSystemDeflection":
            return self._parent._cast(_7420.VirtualComponentAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "MassDiscAdvancedSystemDeflection._Cast_MassDiscAdvancedSystemDeflection",
        ) -> "_7374.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7374,
            )

            return self._parent._cast(_7374.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "MassDiscAdvancedSystemDeflection._Cast_MassDiscAdvancedSystemDeflection",
        ) -> "_7319.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7319,
            )

            return self._parent._cast(_7319.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "MassDiscAdvancedSystemDeflection._Cast_MassDiscAdvancedSystemDeflection",
        ) -> "_7376.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7376,
            )

            return self._parent._cast(_7376.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "MassDiscAdvancedSystemDeflection._Cast_MassDiscAdvancedSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MassDiscAdvancedSystemDeflection._Cast_MassDiscAdvancedSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MassDiscAdvancedSystemDeflection._Cast_MassDiscAdvancedSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MassDiscAdvancedSystemDeflection._Cast_MassDiscAdvancedSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscAdvancedSystemDeflection._Cast_MassDiscAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def mass_disc_advanced_system_deflection(
            self: "MassDiscAdvancedSystemDeflection._Cast_MassDiscAdvancedSystemDeflection",
        ) -> "MassDiscAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "MassDiscAdvancedSystemDeflection._Cast_MassDiscAdvancedSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MassDiscAdvancedSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2482.MassDisc":
        """mastapy.system_model.part_model.MassDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6943.MassDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase

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
    ) -> "List[_2800.MassDiscSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.MassDiscSystemDeflection]

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
    def planetaries(self: Self) -> "List[MassDiscAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.MassDiscAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "MassDiscAdvancedSystemDeflection._Cast_MassDiscAdvancedSystemDeflection":
        return self._Cast_MassDiscAdvancedSystemDeflection(self)
