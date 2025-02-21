"""BevelGearStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3769
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "BevelGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2519
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3776,
        _3777,
        _3778,
        _3866,
        _3875,
        _3878,
        _3879,
        _3880,
        _3896,
        _3797,
        _3825,
        _3842,
        _3788,
        _3844,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearStabilityAnalysis",)


Self = TypeVar("Self", bound="BevelGearStabilityAnalysis")


class BevelGearStabilityAnalysis(_3769.AGMAGleasonConicalGearStabilityAnalysis):
    """BevelGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearStabilityAnalysis")

    class _Cast_BevelGearStabilityAnalysis:
        """Special nested class for casting BevelGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
            parent: "BevelGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "_3769.AGMAGleasonConicalGearStabilityAnalysis":
            return self._parent._cast(_3769.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "_3797.ConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3797,
            )

            return self._parent._cast(_3797.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "_3825.GearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3825,
            )

            return self._parent._cast(_3825.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "_3842.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "_3788.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "_3844.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "_3776.BevelDifferentialGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3776,
            )

            return self._parent._cast(_3776.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "_3777.BevelDifferentialPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3777,
            )

            return self._parent._cast(
                _3777.BevelDifferentialPlanetGearStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "_3778.BevelDifferentialSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3778,
            )

            return self._parent._cast(_3778.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def spiral_bevel_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "_3866.SpiralBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3866,
            )

            return self._parent._cast(_3866.SpiralBevelGearStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "_3875.StraightBevelDiffGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3875,
            )

            return self._parent._cast(_3875.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "_3878.StraightBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3878,
            )

            return self._parent._cast(_3878.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "_3879.StraightBevelPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3879,
            )

            return self._parent._cast(_3879.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "_3880.StraightBevelSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3880,
            )

            return self._parent._cast(_3880.StraightBevelSunGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "_3896.ZerolBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3896,
            )

            return self._parent._cast(_3896.ZerolBevelGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "BevelGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2519.BevelGear":
        """mastapy.system_model.part_model.gears.BevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis":
        return self._Cast_BevelGearStabilityAnalysis(self)
