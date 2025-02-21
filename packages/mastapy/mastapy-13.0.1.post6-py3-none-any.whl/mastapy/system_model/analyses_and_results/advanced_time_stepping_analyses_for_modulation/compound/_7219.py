"""OilSealCompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7177,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7090,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7218,
        _7166,
        _7220,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("OilSealCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="OilSealCompoundAdvancedTimeSteppingAnalysisForModulation")


class OilSealCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7177.ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """OilSealCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_OilSealCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_OilSealCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting OilSealCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def connector_compound_advanced_time_stepping_analysis_for_modulation(
            self: "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7177.ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7177.ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealCompoundAdvancedTimeSteppingAnalysisForModulation",
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
            self: "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7166.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7166,
            )

            return self._parent._cast(
                _7166.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7220.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7220,
            )

            return self._parent._cast(
                _7220.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def oil_seal_compound_advanced_time_stepping_analysis_for_modulation(
            self: "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2466.OilSeal":
        """mastapy.system_model.part_model.OilSeal

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
    ) -> "List[_7090.OilSealAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.OilSealAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7090.OilSealAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.OilSealAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_OilSealCompoundAdvancedTimeSteppingAnalysisForModulation(self)
