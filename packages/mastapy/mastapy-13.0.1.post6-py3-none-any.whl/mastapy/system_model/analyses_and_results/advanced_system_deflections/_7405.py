"""ZerolBevelGearSetAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7291
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ZerolBevelGearSetAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2554
    from mastapy.system_model.analyses_and_results.static_loads import _6988
    from mastapy.gears.rating.zerol_bevel import _371
    from mastapy.system_model.analyses_and_results.system_deflections import _2840
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7403,
        _7404,
        _7279,
        _7307,
        _7335,
        _7374,
        _7270,
        _7355,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ZerolBevelGearSetAdvancedSystemDeflection")


class ZerolBevelGearSetAdvancedSystemDeflection(
    _7291.BevelGearSetAdvancedSystemDeflection
):
    """ZerolBevelGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearSetAdvancedSystemDeflection"
    )

    class _Cast_ZerolBevelGearSetAdvancedSystemDeflection:
        """Special nested class for casting ZerolBevelGearSetAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetAdvancedSystemDeflection._Cast_ZerolBevelGearSetAdvancedSystemDeflection",
            parent: "ZerolBevelGearSetAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "ZerolBevelGearSetAdvancedSystemDeflection._Cast_ZerolBevelGearSetAdvancedSystemDeflection",
        ) -> "_7291.BevelGearSetAdvancedSystemDeflection":
            return self._parent._cast(_7291.BevelGearSetAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "ZerolBevelGearSetAdvancedSystemDeflection._Cast_ZerolBevelGearSetAdvancedSystemDeflection",
        ) -> "_7279.AGMAGleasonConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7279,
            )

            return self._parent._cast(
                _7279.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "ZerolBevelGearSetAdvancedSystemDeflection._Cast_ZerolBevelGearSetAdvancedSystemDeflection",
        ) -> "_7307.ConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7307,
            )

            return self._parent._cast(_7307.ConicalGearSetAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "ZerolBevelGearSetAdvancedSystemDeflection._Cast_ZerolBevelGearSetAdvancedSystemDeflection",
        ) -> "_7335.GearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7335,
            )

            return self._parent._cast(_7335.GearSetAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "ZerolBevelGearSetAdvancedSystemDeflection._Cast_ZerolBevelGearSetAdvancedSystemDeflection",
        ) -> "_7374.SpecialisedAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7374,
            )

            return self._parent._cast(_7374.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "ZerolBevelGearSetAdvancedSystemDeflection._Cast_ZerolBevelGearSetAdvancedSystemDeflection",
        ) -> "_7270.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7270,
            )

            return self._parent._cast(_7270.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "ZerolBevelGearSetAdvancedSystemDeflection._Cast_ZerolBevelGearSetAdvancedSystemDeflection",
        ) -> "_7355.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearSetAdvancedSystemDeflection._Cast_ZerolBevelGearSetAdvancedSystemDeflection",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearSetAdvancedSystemDeflection._Cast_ZerolBevelGearSetAdvancedSystemDeflection",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearSetAdvancedSystemDeflection._Cast_ZerolBevelGearSetAdvancedSystemDeflection",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearSetAdvancedSystemDeflection._Cast_ZerolBevelGearSetAdvancedSystemDeflection",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetAdvancedSystemDeflection._Cast_ZerolBevelGearSetAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(
            self: "ZerolBevelGearSetAdvancedSystemDeflection._Cast_ZerolBevelGearSetAdvancedSystemDeflection",
        ) -> "ZerolBevelGearSetAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetAdvancedSystemDeflection._Cast_ZerolBevelGearSetAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ZerolBevelGearSetAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2554.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6988.ZerolBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_371.ZerolBevelGearSetRating":
        """mastapy.gears.rating.zerol_bevel.ZerolBevelGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_371.ZerolBevelGearSetRating":
        """mastapy.gears.rating.zerol_bevel.ZerolBevelGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_system_deflection_results(
        self: Self,
    ) -> "List[_2840.ZerolBevelGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSetSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_gears_advanced_system_deflection(
        self: Self,
    ) -> "List[_7403.ZerolBevelGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ZerolBevelGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_advanced_system_deflection(
        self: Self,
    ) -> "List[_7404.ZerolBevelGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ZerolBevelGearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearSetAdvancedSystemDeflection._Cast_ZerolBevelGearSetAdvancedSystemDeflection":
        return self._Cast_ZerolBevelGearSetAdvancedSystemDeflection(self)
