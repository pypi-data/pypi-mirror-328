"""ConceptGearCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6733,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "ConceptGearCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2521
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6572
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6752,
        _6700,
        _6754,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConceptGearCompoundCriticalSpeedAnalysis")


class ConceptGearCompoundCriticalSpeedAnalysis(_6733.GearCompoundCriticalSpeedAnalysis):
    """ConceptGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearCompoundCriticalSpeedAnalysis"
    )

    class _Cast_ConceptGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ConceptGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis",
            parent: "ConceptGearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_compound_critical_speed_analysis(
            self: "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis",
        ) -> "_6733.GearCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6733.GearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis",
        ) -> "_6752.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6752,
            )

            return self._parent._cast(
                _6752.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis",
        ) -> "_6700.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6700,
            )

            return self._parent._cast(_6700.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis",
        ) -> "_6754.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6754,
            )

            return self._parent._cast(_6754.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_gear_compound_critical_speed_analysis(
            self: "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis",
        ) -> "ConceptGearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "ConceptGearCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2521.ConceptGear":
        """mastapy.system_model.part_model.gears.ConceptGear

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
    ) -> "List[_6572.ConceptGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConceptGearCriticalSpeedAnalysis]

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
    ) -> "List[_6572.ConceptGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConceptGearCriticalSpeedAnalysis]

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
    ) -> "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis":
        return self._Cast_ConceptGearCompoundCriticalSpeedAnalysis(self)
