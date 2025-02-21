"""AGMAGleasonConicalGearCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6583
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "AGMAGleasonConicalGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2520
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6562,
        _6565,
        _6566,
        _6567,
        _6616,
        _6653,
        _6659,
        _6662,
        _6665,
        _6666,
        _6680,
        _6612,
        _6631,
        _6576,
        _6633,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCriticalSpeedAnalysis")


class AGMAGleasonConicalGearCriticalSpeedAnalysis(
    _6583.ConicalGearCriticalSpeedAnalysis
):
    """AGMAGleasonConicalGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
            parent: "AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6583.ConicalGearCriticalSpeedAnalysis":
            return self._parent._cast(_6583.ConicalGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6612.GearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6612,
            )

            return self._parent._cast(_6612.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6631.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6631,
            )

            return self._parent._cast(_6631.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6576.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6576,
            )

            return self._parent._cast(_6576.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6633.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6562.BevelDifferentialGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6562,
            )

            return self._parent._cast(_6562.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6565.BevelDifferentialPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6565,
            )

            return self._parent._cast(
                _6565.BevelDifferentialPlanetGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6566.BevelDifferentialSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6566,
            )

            return self._parent._cast(
                _6566.BevelDifferentialSunGearCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6567.BevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6567,
            )

            return self._parent._cast(_6567.BevelGearCriticalSpeedAnalysis)

        @property
        def hypoid_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6616.HypoidGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6616,
            )

            return self._parent._cast(_6616.HypoidGearCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6653.SpiralBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6653,
            )

            return self._parent._cast(_6653.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6659.StraightBevelDiffGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6659,
            )

            return self._parent._cast(_6659.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6662.StraightBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6662,
            )

            return self._parent._cast(_6662.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6665.StraightBevelPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6665,
            )

            return self._parent._cast(
                _6665.StraightBevelPlanetGearCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6666.StraightBevelSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6666,
            )

            return self._parent._cast(_6666.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6680.ZerolBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6680,
            )

            return self._parent._cast(_6680.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "AGMAGleasonConicalGearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2520.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

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
    ) -> "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis":
        return self._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis(self)
