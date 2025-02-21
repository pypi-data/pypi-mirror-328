"""OilSealCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6578
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "OilSealCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.static_loads import _6926
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6622,
        _6567,
        _6624,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("OilSealCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="OilSealCriticalSpeedAnalysis")


class OilSealCriticalSpeedAnalysis(_6578.ConnectorCriticalSpeedAnalysis):
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
        ) -> "_6578.ConnectorCriticalSpeedAnalysis":
            return self._parent._cast(_6578.ConnectorCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_6622.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_6567.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6567,
            )

            return self._parent._cast(_6567.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_6624.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(_6624.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "OilSealCriticalSpeedAnalysis._Cast_OilSealCriticalSpeedAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

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
    def component_load_case(self: Self) -> "_6926.OilSealLoadCase":
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
