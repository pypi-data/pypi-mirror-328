"""OilSealCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6579
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "OilSealCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.static_loads import _6927
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6623,
        _6568,
        _6625,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("OilSealCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="OilSealCriticalSpeedAnalysis")


class OilSealCriticalSpeedAnalysis(_6579.ConnectorCriticalSpeedAnalysis):
    """OilSealCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OilSealCriticalSpeedAnalysis")

    class _Cast_OilSealCriticalSpeedAnalysis:
        """Special nested class for casting OilSealCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
            parent: "OilSealCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def connector_critical_speed_analysis(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_6579.ConnectorCriticalSpeedAnalysis":
            return self._parent._cast(_6579.ConnectorCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_6623.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6623,
            )

            return self._parent._cast(_6623.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_6568.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6568,
            )

            return self._parent._cast(_6568.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_6625.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def oil_seal_critical_speed_analysis(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "OilSealCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OilSealCriticalSpeedAnalysis.TYPE"):
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
    def cast_to(
        self: Self,
    ) -> "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis":
        return self._Cast_OilSealCriticalSpeedAnalysis(self)
