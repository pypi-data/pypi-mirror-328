"""StraightBevelPlanetGearStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3875
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "StraightBevelPlanetGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2549
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3781,
        _3769,
        _3797,
        _3825,
        _3842,
        _3788,
        _3844,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearStabilityAnalysis",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearStabilityAnalysis")


class StraightBevelPlanetGearStabilityAnalysis(
    _3875.StraightBevelDiffGearStabilityAnalysis
):
    """StraightBevelPlanetGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearStabilityAnalysis"
    )

    class _Cast_StraightBevelPlanetGearStabilityAnalysis:
        """Special nested class for casting StraightBevelPlanetGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
            parent: "StraightBevelPlanetGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3875.StraightBevelDiffGearStabilityAnalysis":
            return self._parent._cast(_3875.StraightBevelDiffGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3781.BevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3781,
            )

            return self._parent._cast(_3781.BevelGearStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3769.AGMAGleasonConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3769,
            )

            return self._parent._cast(_3769.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3797.ConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3797,
            )

            return self._parent._cast(_3797.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3825.GearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3825,
            )

            return self._parent._cast(_3825.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3842.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3788.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3844.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "StraightBevelPlanetGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelPlanetGearStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2549.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

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
    ) -> "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis":
        return self._Cast_StraightBevelPlanetGearStabilityAnalysis(self)
