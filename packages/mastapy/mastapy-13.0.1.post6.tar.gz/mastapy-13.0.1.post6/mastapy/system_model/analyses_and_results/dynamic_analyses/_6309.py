"""ConicalGearDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "ConicalGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2523
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6281,
        _6288,
        _6291,
        _6292,
        _6293,
        _6341,
        _6345,
        _6348,
        _6351,
        _6378,
        _6384,
        _6387,
        _6390,
        _6391,
        _6405,
        _6356,
        _6302,
        _6358,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7547,
        _7548,
        _7545,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearDynamicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearDynamicAnalysis")


class ConicalGearDynamicAnalysis(_6337.GearDynamicAnalysis):
    """ConicalGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearDynamicAnalysis")

    class _Cast_ConicalGearDynamicAnalysis:
        """Special nested class for casting ConicalGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
            parent: "ConicalGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_dynamic_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_6337.GearDynamicAnalysis":
            return self._parent._cast(_6337.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_6356.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356

            return self._parent._cast(_6356.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_6302.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_6358.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_7547.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_6281.AGMAGleasonConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6281

            return self._parent._cast(_6281.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_6288.BevelDifferentialGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6288

            return self._parent._cast(_6288.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_6291.BevelDifferentialPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6291

            return self._parent._cast(_6291.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_6292.BevelDifferentialSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6292

            return self._parent._cast(_6292.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_6293.BevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6293

            return self._parent._cast(_6293.BevelGearDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_6341.HypoidGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341

            return self._parent._cast(_6341.HypoidGearDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_6345.KlingelnbergCycloPalloidConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345

            return self._parent._cast(
                _6345.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_6348.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6348

            return self._parent._cast(
                _6348.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_dynamic_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_6351.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351

            return self._parent._cast(
                _6351.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_dynamic_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_6378.SpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6378

            return self._parent._cast(_6378.SpiralBevelGearDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_6384.StraightBevelDiffGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_6387.StraightBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6387

            return self._parent._cast(_6387.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_6390.StraightBevelPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390

            return self._parent._cast(_6390.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_6391.StraightBevelSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6391

            return self._parent._cast(_6391.StraightBevelSunGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "_6405.ZerolBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6405

            return self._parent._cast(_6405.ZerolBevelGearDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
        ) -> "ConicalGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2523.ConicalGear":
        """mastapy.system_model.part_model.gears.ConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearDynamicAnalysis]

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
    ) -> "ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis":
        return self._Cast_ConicalGearDynamicAnalysis(self)
