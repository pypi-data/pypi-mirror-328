"""SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7239,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7125,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7141,
        _7220,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7239.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7239.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            return self._parent._cast(
                _7239.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7141.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7141,
            )

            return self._parent._cast(
                _7141.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7220.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7220,
            )

            return self._parent._cast(
                _7220.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2602.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2602.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7125.SynchroniserAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.SynchroniserAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7125.SynchroniserAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.SynchroniserAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
