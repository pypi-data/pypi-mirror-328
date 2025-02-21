"""AGMAGleasonConicalGearSetCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6577
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2514
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6556,
        _6561,
        _6610,
        _6647,
        _6653,
        _6656,
        _6674,
        _6606,
        _6644,
        _6543,
        _6625,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCriticalSpeedAnalysis")


class AGMAGleasonConicalGearSetCriticalSpeedAnalysis(
    _6577.ConicalGearSetCriticalSpeedAnalysis
):
    """AGMAGleasonConicalGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
            parent: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6577.ConicalGearSetCriticalSpeedAnalysis":
            return self._parent._cast(_6577.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6606.GearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6606,
            )

            return self._parent._cast(_6606.GearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6644.SpecialisedAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(_6644.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6543.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6543,
            )

            return self._parent._cast(_6543.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6625.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6556.BevelDifferentialGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6556,
            )

            return self._parent._cast(
                _6556.BevelDifferentialGearSetCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_set_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6561.BevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6561,
            )

            return self._parent._cast(_6561.BevelGearSetCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6610.HypoidGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6610,
            )

            return self._parent._cast(_6610.HypoidGearSetCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_set_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6647.SpiralBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6647,
            )

            return self._parent._cast(_6647.SpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6653.StraightBevelDiffGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6653,
            )

            return self._parent._cast(
                _6653.StraightBevelDiffGearSetCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6656.StraightBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6656,
            )

            return self._parent._cast(_6656.StraightBevelGearSetCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6674.ZerolBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6674,
            )

            return self._parent._cast(_6674.ZerolBevelGearSetCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "AGMAGleasonConicalGearSetCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2514.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis(self)
