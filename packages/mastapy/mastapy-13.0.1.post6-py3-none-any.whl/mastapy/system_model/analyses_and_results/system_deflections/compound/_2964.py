"""StraightBevelPlanetGearCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2958
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "StraightBevelPlanetGearCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2819
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2867,
        _2855,
        _2883,
        _2910,
        _2929,
        _2876,
        _2931,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearCompoundSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearCompoundSystemDeflection")


class StraightBevelPlanetGearCompoundSystemDeflection(
    _2958.StraightBevelDiffGearCompoundSystemDeflection
):
    """StraightBevelPlanetGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearCompoundSystemDeflection"
    )

    class _Cast_StraightBevelPlanetGearCompoundSystemDeflection:
        """Special nested class for casting StraightBevelPlanetGearCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
            parent: "StraightBevelPlanetGearCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_system_deflection(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ) -> "_2958.StraightBevelDiffGearCompoundSystemDeflection":
            return self._parent._cast(
                _2958.StraightBevelDiffGearCompoundSystemDeflection
            )

        @property
        def bevel_gear_compound_system_deflection(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ) -> "_2867.BevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2867,
            )

            return self._parent._cast(_2867.BevelGearCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ) -> "_2855.AGMAGleasonConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2855,
            )

            return self._parent._cast(
                _2855.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def conical_gear_compound_system_deflection(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ) -> "_2883.ConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2883,
            )

            return self._parent._cast(_2883.ConicalGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ) -> "_2910.GearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2910,
            )

            return self._parent._cast(_2910.GearCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ) -> "_2929.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(_2929.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ) -> "_2876.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2876,
            )

            return self._parent._cast(_2876.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ) -> "_2931.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(_2931.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_system_deflection(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ) -> "StraightBevelPlanetGearCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
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
        instance_to_wrap: "StraightBevelPlanetGearCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2819.StraightBevelPlanetGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.StraightBevelPlanetGearSystemDeflection]

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
    ) -> "List[_2819.StraightBevelPlanetGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.StraightBevelPlanetGearSystemDeflection]

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
    ) -> "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection":
        return self._Cast_StraightBevelPlanetGearCompoundSystemDeflection(self)
