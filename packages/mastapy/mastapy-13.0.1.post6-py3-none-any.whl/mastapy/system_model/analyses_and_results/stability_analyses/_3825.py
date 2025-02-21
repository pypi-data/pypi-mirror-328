"""GearStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3842
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "GearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2530
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3769,
        _3776,
        _3777,
        _3778,
        _3781,
        _3794,
        _3797,
        _3813,
        _3814,
        _3820,
        _3829,
        _3833,
        _3836,
        _3839,
        _3866,
        _3875,
        _3878,
        _3879,
        _3880,
        _3893,
        _3896,
        _3788,
        _3844,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("GearStabilityAnalysis",)


Self = TypeVar("Self", bound="GearStabilityAnalysis")


class GearStabilityAnalysis(_3842.MountableComponentStabilityAnalysis):
    """GearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearStabilityAnalysis")

    class _Cast_GearStabilityAnalysis:
        """Special nested class for casting GearStabilityAnalysis to subclasses."""

        def __init__(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
            parent: "GearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3842.MountableComponentStabilityAnalysis":
            return self._parent._cast(_3842.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3788.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3844.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3769.AGMAGleasonConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3769,
            )

            return self._parent._cast(_3769.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3776.BevelDifferentialGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3776,
            )

            return self._parent._cast(_3776.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3777.BevelDifferentialPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3777,
            )

            return self._parent._cast(
                _3777.BevelDifferentialPlanetGearStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3778.BevelDifferentialSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3778,
            )

            return self._parent._cast(_3778.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3781.BevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3781,
            )

            return self._parent._cast(_3781.BevelGearStabilityAnalysis)

        @property
        def concept_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3794.ConceptGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3794,
            )

            return self._parent._cast(_3794.ConceptGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3797.ConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3797,
            )

            return self._parent._cast(_3797.ConicalGearStabilityAnalysis)

        @property
        def cylindrical_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3813.CylindricalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3813,
            )

            return self._parent._cast(_3813.CylindricalGearStabilityAnalysis)

        @property
        def cylindrical_planet_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3814.CylindricalPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3814,
            )

            return self._parent._cast(_3814.CylindricalPlanetGearStabilityAnalysis)

        @property
        def face_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3820.FaceGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3820,
            )

            return self._parent._cast(_3820.FaceGearStabilityAnalysis)

        @property
        def hypoid_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3829.HypoidGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3829,
            )

            return self._parent._cast(_3829.HypoidGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3833.KlingelnbergCycloPalloidConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3833,
            )

            return self._parent._cast(
                _3833.KlingelnbergCycloPalloidConicalGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3836.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3836,
            )

            return self._parent._cast(
                _3836.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3839.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(
                _3839.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3866.SpiralBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3866,
            )

            return self._parent._cast(_3866.SpiralBevelGearStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3875.StraightBevelDiffGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3875,
            )

            return self._parent._cast(_3875.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3878.StraightBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3878,
            )

            return self._parent._cast(_3878.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3879.StraightBevelPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3879,
            )

            return self._parent._cast(_3879.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3880.StraightBevelSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3880,
            )

            return self._parent._cast(_3880.StraightBevelSunGearStabilityAnalysis)

        @property
        def worm_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3893.WormGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3893,
            )

            return self._parent._cast(_3893.WormGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3896.ZerolBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3896,
            )

            return self._parent._cast(_3896.ZerolBevelGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "GearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2530.Gear":
        """mastapy.system_model.part_model.gears.Gear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearStabilityAnalysis._Cast_GearStabilityAnalysis":
        return self._Cast_GearStabilityAnalysis(self)
