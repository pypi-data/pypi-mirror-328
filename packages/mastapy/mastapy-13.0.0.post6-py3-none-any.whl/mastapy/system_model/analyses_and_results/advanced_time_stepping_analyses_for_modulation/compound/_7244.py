"""SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7179,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2601
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7115,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7217,
        _7165,
        _7219,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7179.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7179.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7179.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
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
            self: "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7165.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7165,
            )

            return self._parent._cast(
                _7165.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7219.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7219,
            )

            return self._parent._cast(
                _7219.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spring_damper_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2601.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

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
    ) -> "List[_7115.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7115.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
