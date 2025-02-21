"""ConceptCouplingHalfCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6713,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "ConceptCouplingHalfCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2582
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6570
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6751,
        _6699,
        _6753,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalfCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingHalfCompoundCriticalSpeedAnalysis")


class ConceptCouplingHalfCompoundCriticalSpeedAnalysis(
    _6713.CouplingHalfCompoundCriticalSpeedAnalysis
):
    """ConceptCouplingHalfCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingHalfCompoundCriticalSpeedAnalysis"
    )

    class _Cast_ConceptCouplingHalfCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ConceptCouplingHalfCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingHalfCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingHalfCompoundCriticalSpeedAnalysis",
            parent: "ConceptCouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_critical_speed_analysis(
            self: "ConceptCouplingHalfCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6713.CouplingHalfCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6713.CouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "ConceptCouplingHalfCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6751.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(
                _6751.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "ConceptCouplingHalfCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6699.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6699,
            )

            return self._parent._cast(_6699.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "ConceptCouplingHalfCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6753.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6753,
            )

            return self._parent._cast(_6753.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "ConceptCouplingHalfCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingHalfCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHalfCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_coupling_half_compound_critical_speed_analysis(
            self: "ConceptCouplingHalfCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "ConceptCouplingHalfCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalfCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingHalfCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "ConceptCouplingHalfCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2582.ConceptCouplingHalf":
        """mastapy.system_model.part_model.couplings.ConceptCouplingHalf

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
    ) -> "List[_6570.ConceptCouplingHalfCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConceptCouplingHalfCriticalSpeedAnalysis]

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
    ) -> "List[_6570.ConceptCouplingHalfCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConceptCouplingHalfCriticalSpeedAnalysis]

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
    ) -> "ConceptCouplingHalfCompoundCriticalSpeedAnalysis._Cast_ConceptCouplingHalfCompoundCriticalSpeedAnalysis":
        return self._Cast_ConceptCouplingHalfCompoundCriticalSpeedAnalysis(self)
