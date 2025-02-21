"""AGMAGleasonConicalGearCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7438,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7277,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7417,
        _7420,
        _7421,
        _7422,
        _7468,
        _7505,
        _7511,
        _7514,
        _7517,
        _7518,
        _7532,
        _7464,
        _7483,
        _7431,
        _7485,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCompoundAdvancedSystemDeflection")


class AGMAGleasonConicalGearCompoundAdvancedSystemDeflection(
    _7438.ConicalGearCompoundAdvancedSystemDeflection
):
    """AGMAGleasonConicalGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
    )

    class _Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
            parent: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7438.ConicalGearCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7438.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7464.GearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7464,
            )

            return self._parent._cast(_7464.GearCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7483.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7483,
            )

            return self._parent._cast(
                _7483.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7431.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(_7431.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7485.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7417.BevelDifferentialGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7417,
            )

            return self._parent._cast(
                _7417.BevelDifferentialGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7420.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7420,
            )

            return self._parent._cast(
                _7420.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7421.BevelDifferentialSunGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7421,
            )

            return self._parent._cast(
                _7421.BevelDifferentialSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7422.BevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7422,
            )

            return self._parent._cast(_7422.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7468.HypoidGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7468,
            )

            return self._parent._cast(_7468.HypoidGearCompoundAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7505.SpiralBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7505,
            )

            return self._parent._cast(
                _7505.SpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7511.StraightBevelDiffGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(
                _7511.StraightBevelDiffGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7514.StraightBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7514,
            )

            return self._parent._cast(
                _7514.StraightBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7517.StraightBevelPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7517,
            )

            return self._parent._cast(
                _7517.StraightBevelPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7518.StraightBevelSunGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7518,
            )

            return self._parent._cast(
                _7518.StraightBevelSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7532.ZerolBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7532,
            )

            return self._parent._cast(
                _7532.ZerolBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7277.AGMAGleasonConicalGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AGMAGleasonConicalGearAdvancedSystemDeflection]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7277.AGMAGleasonConicalGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AGMAGleasonConicalGearAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection(self)
