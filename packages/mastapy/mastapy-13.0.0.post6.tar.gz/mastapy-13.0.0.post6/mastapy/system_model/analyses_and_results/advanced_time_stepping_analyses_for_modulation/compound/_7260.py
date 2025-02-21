"""TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7179,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7131,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7217,
        _7165,
        _7219,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self",
    bound="TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",
)


class TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7179.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7179.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7179.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",
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
            self: "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7165.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7165,
            )

            return self._parent._cast(
                _7165.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7219.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7219,
            )

            return self._parent._cast(
                _7219.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_compound_advanced_time_stepping_analysis_for_modulation(
            self: "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2610.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

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
    ) -> "List[_7131.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7131.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
