"""StaticLoadAnalysisCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7535
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATIC_LOAD_ANALYSIS_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases",
    "StaticLoadAnalysisCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6805
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2825,
        _2832,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3035,
        _3089,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3350,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3609,
    )
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3816,
        _3870,
    )
    from mastapy.system_model.analyses_and_results.power_flows import _4122
    from mastapy.system_model.analyses_and_results.modal_analyses import _4625, _4654
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4909,
        _4935,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5194,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5732,
        _5761,
        _5765,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6070,
        _6086,
    )
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6329
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6583
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7010,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7274,
        _7276,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7537, _7544
    from mastapy.system_model.analyses_and_results import _2650


__docformat__ = "restructuredtext en"
__all__ = ("StaticLoadAnalysisCase",)


Self = TypeVar("Self", bound="StaticLoadAnalysisCase")


class StaticLoadAnalysisCase(_7535.AnalysisCase):
    """StaticLoadAnalysisCase

    This is a mastapy class.
    """

    TYPE = _STATIC_LOAD_ANALYSIS_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StaticLoadAnalysisCase")

    class _Cast_StaticLoadAnalysisCase:
        """Special nested class for casting StaticLoadAnalysisCase to subclasses."""

        def __init__(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
            parent: "StaticLoadAnalysisCase",
        ):
            self._parent = parent

        @property
        def analysis_case(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_7535.AnalysisCase":
            return self._parent._cast(_7535.AnalysisCase)

        @property
        def context(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_2650.Context":
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.Context)

        @property
        def system_deflection(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_2825.SystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2825,
            )

            return self._parent._cast(_2825.SystemDeflection)

        @property
        def torsional_system_deflection(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_2832.TorsionalSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2832,
            )

            return self._parent._cast(_2832.TorsionalSystemDeflection)

        @property
        def dynamic_model_for_steady_state_synchronous_response(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_3035.DynamicModelForSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3035,
            )

            return self._parent._cast(
                _3035.DynamicModelForSteadyStateSynchronousResponse
            )

        @property
        def steady_state_synchronous_response(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_3089.SteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3089,
            )

            return self._parent._cast(_3089.SteadyStateSynchronousResponse)

        @property
        def steady_state_synchronous_response_on_a_shaft(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_3350.SteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3350,
            )

            return self._parent._cast(_3350.SteadyStateSynchronousResponseOnAShaft)

        @property
        def steady_state_synchronous_response_at_a_speed(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_3609.SteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3609,
            )

            return self._parent._cast(_3609.SteadyStateSynchronousResponseAtASpeed)

        @property
        def dynamic_model_for_stability_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_3816.DynamicModelForStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3816,
            )

            return self._parent._cast(_3816.DynamicModelForStabilityAnalysis)

        @property
        def stability_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_3870.StabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3870,
            )

            return self._parent._cast(_3870.StabilityAnalysis)

        @property
        def power_flow(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_4122.PowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PowerFlow)

        @property
        def dynamic_model_for_modal_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_4625.DynamicModelForModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4625

            return self._parent._cast(_4625.DynamicModelForModalAnalysis)

        @property
        def modal_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_4654.ModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654

            return self._parent._cast(_4654.ModalAnalysis)

        @property
        def dynamic_model_at_a_stiffness(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_4909.DynamicModelAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4909,
            )

            return self._parent._cast(_4909.DynamicModelAtAStiffness)

        @property
        def modal_analysis_at_a_stiffness(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_4935.ModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4935,
            )

            return self._parent._cast(_4935.ModalAnalysisAtAStiffness)

        @property
        def modal_analysis_at_a_speed(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_5194.ModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(_5194.ModalAnalysisAtASpeed)

        @property
        def dynamic_model_for_harmonic_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_5732.DynamicModelForHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5732,
            )

            return self._parent._cast(_5732.DynamicModelForHarmonicAnalysis)

        @property
        def harmonic_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_5761.HarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5761,
            )

            return self._parent._cast(_5761.HarmonicAnalysis)

        @property
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_5765.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5765,
            )

            return self._parent._cast(
                _5765.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def harmonic_analysis_of_single_excitation(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_6070.HarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6070,
            )

            return self._parent._cast(_6070.HarmonicAnalysisOfSingleExcitation)

        @property
        def modal_analysis_for_harmonic_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_6086.ModalAnalysisForHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(_6086.ModalAnalysisForHarmonicAnalysis)

        @property
        def dynamic_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_6329.DynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6329

            return self._parent._cast(_6329.DynamicAnalysis)

        @property
        def critical_speed_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_6583.CriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6583,
            )

            return self._parent._cast(_6583.CriticalSpeedAnalysis)

        @property
        def advanced_time_stepping_analysis_for_modulation(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_7010.AdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7010,
            )

            return self._parent._cast(_7010.AdvancedTimeSteppingAnalysisForModulation)

        @property
        def advanced_system_deflection(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_7274.AdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7274,
            )

            return self._parent._cast(_7274.AdvancedSystemDeflection)

        @property
        def advanced_system_deflection_sub_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_7276.AdvancedSystemDeflectionSubAnalysis":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7276,
            )

            return self._parent._cast(_7276.AdvancedSystemDeflectionSubAnalysis)

        @property
        def compound_analysis_case(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_7537.CompoundAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.CompoundAnalysisCase)

        @property
        def fe_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "_7544.FEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.FEAnalysis)

        @property
        def static_load_analysis_case(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "StaticLoadAnalysisCase":
            return self._parent

        def __getattr__(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StaticLoadAnalysisCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_case(self: Self) -> "_6805.StaticLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase":
        return self._Cast_StaticLoadAnalysisCase(self)
