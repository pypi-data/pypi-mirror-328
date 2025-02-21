"""PulleyCompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7201,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2611
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7121,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7204,
        _7239,
        _7187,
        _7241,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="PulleyCompoundAdvancedTimeSteppingAnalysisForModulation")


class PulleyCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7201.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """PulleyCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _PULLEY_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_PulleyCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting PulleyCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7201.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7201.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7239.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7239,
            )

            return self._parent._cast(
                _7239.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7187.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7187,
            )

            return self._parent._cast(
                _7187.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7241.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7241,
            )

            return self._parent._cast(
                _7241.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7204.CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7204,
            )

            return self._parent._cast(
                _7204.CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def pulley_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2611.Pulley":
        """mastapy.system_model.part_model.couplings.Pulley

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
    ) -> "List[_7121.PulleyAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.PulleyAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7121.PulleyAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.PulleyAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_PulleyCompoundAdvancedTimeSteppingAnalysisForModulation(self)
