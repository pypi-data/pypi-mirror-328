"""CycloidalDiscAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7007,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2569
    from mastapy.system_model.analyses_and_results.static_loads import _6860
    from mastapy.system_model.analyses_and_results.system_deflections import _2738
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7008,
        _7036,
        _7091,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="CycloidalDiscAdvancedTimeSteppingAnalysisForModulation")


class CycloidalDiscAdvancedTimeSteppingAnalysisForModulation(
    _7007.AbstractShaftAdvancedTimeSteppingAnalysisForModulation
):
    """CycloidalDiscAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_CycloidalDiscAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CycloidalDiscAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
            parent: "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def abstract_shaft_advanced_time_stepping_analysis_for_modulation(
            self: "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7007.AbstractShaftAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7007.AbstractShaftAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_or_housing_advanced_time_stepping_analysis_for_modulation(
            self: "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7008.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7008,
            )

            return self._parent._cast(
                _7008.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7036.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7036,
            )

            return self._parent._cast(
                _7036.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7091.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7091,
            )

            return self._parent._cast(
                _7091.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_advanced_time_stepping_analysis_for_modulation(
            self: "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2569.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6860.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2738.CycloidalDiscSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscSystemDeflection

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
    ) -> "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CycloidalDiscAdvancedTimeSteppingAnalysisForModulation(self)
