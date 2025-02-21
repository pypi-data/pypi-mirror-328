"""ZerolBevelGearCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7422,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ZerolBevelGearCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2553
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7403,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7410,
        _7438,
        _7464,
        _7483,
        _7431,
        _7485,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ZerolBevelGearCompoundAdvancedSystemDeflection")


class ZerolBevelGearCompoundAdvancedSystemDeflection(
    _7422.BevelGearCompoundAdvancedSystemDeflection
):
    """ZerolBevelGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearCompoundAdvancedSystemDeflection"
    )

    class _Cast_ZerolBevelGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting ZerolBevelGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ZerolBevelGearCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearCompoundAdvancedSystemDeflection",
            parent: "ZerolBevelGearCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_advanced_system_deflection(
            self: "ZerolBevelGearCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearCompoundAdvancedSystemDeflection",
        ) -> "_7422.BevelGearCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7422.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(
            self: "ZerolBevelGearCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearCompoundAdvancedSystemDeflection",
        ) -> "_7410.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7410,
            )

            return self._parent._cast(
                _7410.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "ZerolBevelGearCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearCompoundAdvancedSystemDeflection",
        ) -> "_7438.ConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7438,
            )

            return self._parent._cast(_7438.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(
            self: "ZerolBevelGearCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearCompoundAdvancedSystemDeflection",
        ) -> "_7464.GearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7464,
            )

            return self._parent._cast(_7464.GearCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "ZerolBevelGearCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearCompoundAdvancedSystemDeflection",
        ) -> "_7483.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7483,
            )

            return self._parent._cast(
                _7483.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "ZerolBevelGearCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearCompoundAdvancedSystemDeflection",
        ) -> "_7431.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(_7431.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "ZerolBevelGearCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearCompoundAdvancedSystemDeflection",
        ) -> "_7485.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ZerolBevelGearCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearCompoundAdvancedSystemDeflection",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearCompoundAdvancedSystemDeflection",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearCompoundAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_compound_advanced_system_deflection(
            self: "ZerolBevelGearCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearCompoundAdvancedSystemDeflection",
        ) -> "ZerolBevelGearCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "ZerolBevelGearCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2553.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

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
    ) -> "List[_7403.ZerolBevelGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ZerolBevelGearAdvancedSystemDeflection]

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
    ) -> "List[_7403.ZerolBevelGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ZerolBevelGearAdvancedSystemDeflection]

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
    ) -> "ZerolBevelGearCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearCompoundAdvancedSystemDeflection":
        return self._Cast_ZerolBevelGearCompoundAdvancedSystemDeflection(self)
