"""OilSealAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7047,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "OilSealAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.static_loads import _6927
    from mastapy.system_model.analyses_and_results.system_deflections import _2784
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7089,
        _7036,
        _7091,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("OilSealAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="OilSealAdvancedTimeSteppingAnalysisForModulation")


class OilSealAdvancedTimeSteppingAnalysisForModulation(
    _7047.ConnectorAdvancedTimeSteppingAnalysisForModulation
):
    """OilSealAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_OilSealAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_OilSealAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting OilSealAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "OilSealAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealAdvancedTimeSteppingAnalysisForModulation",
            parent: "OilSealAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def connector_advanced_time_stepping_analysis_for_modulation(
            self: "OilSealAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7047.ConnectorAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7047.ConnectorAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "OilSealAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7089.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7089,
            )

            return self._parent._cast(
                _7089.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "OilSealAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7036.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7036,
            )

            return self._parent._cast(
                _7036.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "OilSealAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7091.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7091,
            )

            return self._parent._cast(
                _7091.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "OilSealAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "OilSealAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "OilSealAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "OilSealAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def oil_seal_advanced_time_stepping_analysis_for_modulation(
            self: "OilSealAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealAdvancedTimeSteppingAnalysisForModulation",
        ) -> "OilSealAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "OilSealAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "OilSealAdvancedTimeSteppingAnalysisForModulation.TYPE",
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
    def component_load_case(self: Self) -> "_6927.OilSealLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2784.OilSealSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.OilSealSystemDeflection

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
    ) -> "OilSealAdvancedTimeSteppingAnalysisForModulation._Cast_OilSealAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_OilSealAdvancedTimeSteppingAnalysisForModulation(self)
