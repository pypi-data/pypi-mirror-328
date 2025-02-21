"""StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7246,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7124,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7157,
        _7145,
        _7173,
        _7199,
        _7218,
        _7166,
        _7220,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self",
    bound="StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
)


class StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7246.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = (
        _STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7246.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7246.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7157.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7157,
            )

            return self._parent._cast(
                _7157.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7145.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7145,
            )

            return self._parent._cast(
                _7145.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7173.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7173,
            )

            return self._parent._cast(
                _7173.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7199.GearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7199,
            )

            return self._parent._cast(
                _7199.GearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7218.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7218,
            )

            return self._parent._cast(
                _7218.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7166.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7166,
            )

            return self._parent._cast(
                _7166.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7220.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7220,
            )

            return self._parent._cast(
                _7220.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7124.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7124.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
