"""SynchroniserSleeveAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7391
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "SynchroniserSleeveAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.static_loads import _6971
    from mastapy.system_model.analyses_and_results.system_deflections import _2823
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7313,
        _7353,
        _7298,
        _7355,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SynchroniserSleeveAdvancedSystemDeflection")


class SynchroniserSleeveAdvancedSystemDeflection(
    _7391.SynchroniserPartAdvancedSystemDeflection
):
    """SynchroniserSleeveAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserSleeveAdvancedSystemDeflection"
    )

    class _Cast_SynchroniserSleeveAdvancedSystemDeflection:
        """Special nested class for casting SynchroniserSleeveAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SynchroniserSleeveAdvancedSystemDeflection._Cast_SynchroniserSleeveAdvancedSystemDeflection",
            parent: "SynchroniserSleeveAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def synchroniser_part_advanced_system_deflection(
            self: "SynchroniserSleeveAdvancedSystemDeflection._Cast_SynchroniserSleeveAdvancedSystemDeflection",
        ) -> "_7391.SynchroniserPartAdvancedSystemDeflection":
            return self._parent._cast(_7391.SynchroniserPartAdvancedSystemDeflection)

        @property
        def coupling_half_advanced_system_deflection(
            self: "SynchroniserSleeveAdvancedSystemDeflection._Cast_SynchroniserSleeveAdvancedSystemDeflection",
        ) -> "_7313.CouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7313,
            )

            return self._parent._cast(_7313.CouplingHalfAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "SynchroniserSleeveAdvancedSystemDeflection._Cast_SynchroniserSleeveAdvancedSystemDeflection",
        ) -> "_7353.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7353,
            )

            return self._parent._cast(_7353.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "SynchroniserSleeveAdvancedSystemDeflection._Cast_SynchroniserSleeveAdvancedSystemDeflection",
        ) -> "_7298.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7298,
            )

            return self._parent._cast(_7298.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "SynchroniserSleeveAdvancedSystemDeflection._Cast_SynchroniserSleeveAdvancedSystemDeflection",
        ) -> "_7355.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserSleeveAdvancedSystemDeflection._Cast_SynchroniserSleeveAdvancedSystemDeflection",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserSleeveAdvancedSystemDeflection._Cast_SynchroniserSleeveAdvancedSystemDeflection",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserSleeveAdvancedSystemDeflection._Cast_SynchroniserSleeveAdvancedSystemDeflection",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSleeveAdvancedSystemDeflection._Cast_SynchroniserSleeveAdvancedSystemDeflection",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveAdvancedSystemDeflection._Cast_SynchroniserSleeveAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_advanced_system_deflection(
            self: "SynchroniserSleeveAdvancedSystemDeflection._Cast_SynchroniserSleeveAdvancedSystemDeflection",
        ) -> "SynchroniserSleeveAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveAdvancedSystemDeflection._Cast_SynchroniserSleeveAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "SynchroniserSleeveAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2606.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6971.SynchroniserSleeveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

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
    ) -> "List[_2823.SynchroniserSleeveSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSleeveSystemDeflection]

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
    ) -> "SynchroniserSleeveAdvancedSystemDeflection._Cast_SynchroniserSleeveAdvancedSystemDeflection":
        return self._Cast_SynchroniserSleeveAdvancedSystemDeflection(self)
