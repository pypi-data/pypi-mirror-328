"""KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6611
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2538
    from mastapy.system_model.analyses_and_results.static_loads import _6915
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6574,
        _6603,
        _6622,
        _6567,
        _6624,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis")


class KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis(
    _6611.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
        ) -> "_6611.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis":
            return self._parent._cast(
                _6611.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
            )

        @property
        def conical_gear_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
        ) -> "_6574.ConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6574,
            )

            return self._parent._cast(_6574.ConicalGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
        ) -> "_6603.GearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6603,
            )

            return self._parent._cast(_6603.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
        ) -> "_6622.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
        ) -> "_6567.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6567,
            )

            return self._parent._cast(_6567.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
        ) -> "_6624.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(_6624.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2538.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6915.KlingelnbergCycloPalloidHypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase

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
    ) -> "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis(self)
