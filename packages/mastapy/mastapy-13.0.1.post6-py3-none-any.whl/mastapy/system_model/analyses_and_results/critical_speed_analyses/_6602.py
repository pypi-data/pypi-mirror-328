"""FEPartCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6545
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "FEPartCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2453
    from mastapy.system_model.analyses_and_results.static_loads import _6888
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6568,
        _6625,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("FEPartCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="FEPartCriticalSpeedAnalysis")


class FEPartCriticalSpeedAnalysis(_6545.AbstractShaftOrHousingCriticalSpeedAnalysis):
    """FEPartCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_PART_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartCriticalSpeedAnalysis")

    class _Cast_FEPartCriticalSpeedAnalysis:
        """Special nested class for casting FEPartCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "FEPartCriticalSpeedAnalysis._Cast_FEPartCriticalSpeedAnalysis",
            parent: "FEPartCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_critical_speed_analysis(
            self: "FEPartCriticalSpeedAnalysis._Cast_FEPartCriticalSpeedAnalysis",
        ) -> "_6545.AbstractShaftOrHousingCriticalSpeedAnalysis":
            return self._parent._cast(_6545.AbstractShaftOrHousingCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "FEPartCriticalSpeedAnalysis._Cast_FEPartCriticalSpeedAnalysis",
        ) -> "_6568.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6568,
            )

            return self._parent._cast(_6568.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "FEPartCriticalSpeedAnalysis._Cast_FEPartCriticalSpeedAnalysis",
        ) -> "_6625.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FEPartCriticalSpeedAnalysis._Cast_FEPartCriticalSpeedAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FEPartCriticalSpeedAnalysis._Cast_FEPartCriticalSpeedAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FEPartCriticalSpeedAnalysis._Cast_FEPartCriticalSpeedAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FEPartCriticalSpeedAnalysis._Cast_FEPartCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartCriticalSpeedAnalysis._Cast_FEPartCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def fe_part_critical_speed_analysis(
            self: "FEPartCriticalSpeedAnalysis._Cast_FEPartCriticalSpeedAnalysis",
        ) -> "FEPartCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "FEPartCriticalSpeedAnalysis._Cast_FEPartCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2453.FEPart":
        """mastapy.system_model.part_model.FEPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6888.FEPartLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[FEPartCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.FEPartCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FEPartCriticalSpeedAnalysis._Cast_FEPartCriticalSpeedAnalysis":
        return self._Cast_FEPartCriticalSpeedAnalysis(self)
