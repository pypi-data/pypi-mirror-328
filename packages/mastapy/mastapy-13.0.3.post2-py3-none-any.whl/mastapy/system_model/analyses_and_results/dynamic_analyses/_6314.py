"""BevelGearDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "BevelGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6309,
        _6312,
        _6313,
        _6399,
        _6405,
        _6408,
        _6411,
        _6412,
        _6426,
        _6330,
        _6358,
        _6377,
        _6323,
        _6379,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearDynamicAnalysis",)


Self = TypeVar("Self", bound="BevelGearDynamicAnalysis")


class BevelGearDynamicAnalysis(_6302.AGMAGleasonConicalGearDynamicAnalysis):
    """BevelGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearDynamicAnalysis")

    class _Cast_BevelGearDynamicAnalysis:
        """Special nested class for casting BevelGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
            parent: "BevelGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_6302.AGMAGleasonConicalGearDynamicAnalysis":
            return self._parent._cast(_6302.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_6330.ConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6330

            return self._parent._cast(_6330.ConicalGearDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_6358.GearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_6377.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377

            return self._parent._cast(_6377.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_6323.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(_6323.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_6379.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_6309.BevelDifferentialGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309

            return self._parent._cast(_6309.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_6312.BevelDifferentialPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_6313.BevelDifferentialSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313

            return self._parent._cast(_6313.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_6399.SpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6399

            return self._parent._cast(_6399.SpiralBevelGearDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_6405.StraightBevelDiffGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6405

            return self._parent._cast(_6405.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_6408.StraightBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6408

            return self._parent._cast(_6408.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_6411.StraightBevelPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6411

            return self._parent._cast(_6411.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_6412.StraightBevelSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6412

            return self._parent._cast(_6412.StraightBevelSunGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "_6426.ZerolBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6426

            return self._parent._cast(_6426.ZerolBevelGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis",
        ) -> "BevelGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2539.BevelGear":
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
    ) -> "BevelGearDynamicAnalysis._Cast_BevelGearDynamicAnalysis":
        return self._Cast_BevelGearDynamicAnalysis(self)
