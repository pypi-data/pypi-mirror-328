"""AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7174,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7016,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7150,
        _7194,
        _7205,
        _7244,
        _7228,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self",
    bound="AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
)


class AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7174.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7174.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7174.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7228,
            )

            return self._parent._cast(
                _7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7150.AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7150,
            )

            return self._parent._cast(
                _7150.AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7194.CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7194,
            )

            return self._parent._cast(
                _7194.CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def fe_part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7205.FEPartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7205,
            )

            return self._parent._cast(
                _7205.FEPartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7244.ShaftCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7244,
            )

            return self._parent._cast(
                _7244.ShaftCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_or_housing_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7016.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7016.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
