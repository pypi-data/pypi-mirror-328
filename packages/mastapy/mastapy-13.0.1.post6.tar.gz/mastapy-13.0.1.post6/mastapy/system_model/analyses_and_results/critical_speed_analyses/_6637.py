"""RollingRingAssemblyCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6644
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "RollingRingAssemblyCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.static_loads import _6946
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6543,
        _6625,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="RollingRingAssemblyCriticalSpeedAnalysis")


class RollingRingAssemblyCriticalSpeedAnalysis(
    _6644.SpecialisedAssemblyCriticalSpeedAnalysis
):
    """RollingRingAssemblyCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingAssemblyCriticalSpeedAnalysis"
    )

    class _Cast_RollingRingAssemblyCriticalSpeedAnalysis:
        """Special nested class for casting RollingRingAssemblyCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
            parent: "RollingRingAssemblyCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
        ) -> "_6644.SpecialisedAssemblyCriticalSpeedAnalysis":
            return self._parent._cast(_6644.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
        ) -> "_6543.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6543,
            )

            return self._parent._cast(_6543.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
        ) -> "_6625.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_critical_speed_analysis(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
        ) -> "RollingRingAssemblyCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "RollingRingAssemblyCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2597.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6946.RollingRingAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis":
        return self._Cast_RollingRingAssemblyCriticalSpeedAnalysis(self)
