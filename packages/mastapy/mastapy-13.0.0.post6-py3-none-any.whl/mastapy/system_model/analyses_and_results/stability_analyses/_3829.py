"""HypoidGearStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3769
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "HypoidGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534
    from mastapy.system_model.analyses_and_results.static_loads import _6905
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3797,
        _3825,
        _3842,
        _3788,
        _3844,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearStabilityAnalysis",)


Self = TypeVar("Self", bound="HypoidGearStabilityAnalysis")


class HypoidGearStabilityAnalysis(_3769.AGMAGleasonConicalGearStabilityAnalysis):
    """HypoidGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearStabilityAnalysis")

    class _Cast_HypoidGearStabilityAnalysis:
        """Special nested class for casting HypoidGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearStabilityAnalysis._Cast_HypoidGearStabilityAnalysis",
            parent: "HypoidGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "HypoidGearStabilityAnalysis._Cast_HypoidGearStabilityAnalysis",
        ) -> "_3769.AGMAGleasonConicalGearStabilityAnalysis":
            return self._parent._cast(_3769.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "HypoidGearStabilityAnalysis._Cast_HypoidGearStabilityAnalysis",
        ) -> "_3797.ConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3797,
            )

            return self._parent._cast(_3797.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "HypoidGearStabilityAnalysis._Cast_HypoidGearStabilityAnalysis",
        ) -> "_3825.GearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3825,
            )

            return self._parent._cast(_3825.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "HypoidGearStabilityAnalysis._Cast_HypoidGearStabilityAnalysis",
        ) -> "_3842.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "HypoidGearStabilityAnalysis._Cast_HypoidGearStabilityAnalysis",
        ) -> "_3788.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "HypoidGearStabilityAnalysis._Cast_HypoidGearStabilityAnalysis",
        ) -> "_3844.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearStabilityAnalysis._Cast_HypoidGearStabilityAnalysis",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearStabilityAnalysis._Cast_HypoidGearStabilityAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearStabilityAnalysis._Cast_HypoidGearStabilityAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearStabilityAnalysis._Cast_HypoidGearStabilityAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearStabilityAnalysis._Cast_HypoidGearStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def hypoid_gear_stability_analysis(
            self: "HypoidGearStabilityAnalysis._Cast_HypoidGearStabilityAnalysis",
        ) -> "HypoidGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearStabilityAnalysis._Cast_HypoidGearStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2534.HypoidGear":
        """mastapy.system_model.part_model.gears.HypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6905.HypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase

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
    ) -> "HypoidGearStabilityAnalysis._Cast_HypoidGearStabilityAnalysis":
        return self._Cast_HypoidGearStabilityAnalysis(self)
