"""CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7187,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7060,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7198,
        _7217,
        _7165,
        _7219,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self",
    bound="CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
)


class CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7187.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = (
        _CYLINDRICAL_PLANET_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7187.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7187.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7198.GearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7198,
            )

            return self._parent._cast(
                _7198.GearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7217.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7217,
            )

            return self._parent._cast(
                _7217.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7165.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7165,
            )

            return self._parent._cast(
                _7165.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7219.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7219,
            )

            return self._parent._cast(
                _7219.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7060.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7060.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
