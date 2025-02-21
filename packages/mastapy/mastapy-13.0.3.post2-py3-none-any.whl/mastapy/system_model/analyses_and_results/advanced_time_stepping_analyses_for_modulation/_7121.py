"""PulleyAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7071,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "PulleyAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2611
    from mastapy.system_model.analyses_and_results.static_loads import _6962
    from mastapy.system_model.analyses_and_results.system_deflections import _2814
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7074,
        _7110,
        _7057,
        _7112,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PulleyAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="PulleyAdvancedTimeSteppingAnalysisForModulation")


class PulleyAdvancedTimeSteppingAnalysisForModulation(
    _7071.CouplingHalfAdvancedTimeSteppingAnalysisForModulation
):
    """PulleyAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _PULLEY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PulleyAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_PulleyAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting PulleyAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "PulleyAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyAdvancedTimeSteppingAnalysisForModulation",
            parent: "PulleyAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "PulleyAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7071.CouplingHalfAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7071.CouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "PulleyAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7110.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7110,
            )

            return self._parent._cast(
                _7110.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "PulleyAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7057.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7057,
            )

            return self._parent._cast(
                _7057.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "PulleyAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7112.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7112,
            )

            return self._parent._cast(
                _7112.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "PulleyAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PulleyAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PulleyAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PulleyAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleyAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_pulley_advanced_time_stepping_analysis_for_modulation(
            self: "PulleyAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7074.CVTPulleyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7074,
            )

            return self._parent._cast(
                _7074.CVTPulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def pulley_advanced_time_stepping_analysis_for_modulation(
            self: "PulleyAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "PulleyAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "PulleyAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "PulleyAdvancedTimeSteppingAnalysisForModulation.TYPE",
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
    def component_load_case(self: Self) -> "_6962.PulleyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2814.PulleySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PulleySystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PulleyAdvancedTimeSteppingAnalysisForModulation._Cast_PulleyAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_PulleyAdvancedTimeSteppingAnalysisForModulation(self)
