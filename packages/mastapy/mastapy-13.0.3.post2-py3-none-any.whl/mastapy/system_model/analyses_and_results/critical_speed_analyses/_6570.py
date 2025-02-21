"""AGMAGleasonConicalGearSetCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6598
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6577,
        _6582,
        _6631,
        _6668,
        _6674,
        _6677,
        _6695,
        _6627,
        _6665,
        _6564,
        _6646,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCriticalSpeedAnalysis")


class AGMAGleasonConicalGearSetCriticalSpeedAnalysis(
    _6598.ConicalGearSetCriticalSpeedAnalysis
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
        ) -> "_6598.ConicalGearSetCriticalSpeedAnalysis":
            return self._parent._cast(_6598.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6627.GearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(_6627.GearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6665.SpecialisedAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6665,
            )

            return self._parent._cast(_6665.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6564.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(_6564.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6646.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6577.BevelDifferentialGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6577,
            )

            return self._parent._cast(
                _6577.BevelDifferentialGearSetCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_set_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6582.BevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6582,
            )

            return self._parent._cast(_6582.BevelGearSetCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6631.HypoidGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6631,
            )

            return self._parent._cast(_6631.HypoidGearSetCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_set_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6668.SpiralBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6668,
            )

            return self._parent._cast(_6668.SpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6674.StraightBevelDiffGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6674,
            )

            return self._parent._cast(
                _6674.StraightBevelDiffGearSetCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6677.StraightBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6677,
            )

            return self._parent._cast(_6677.StraightBevelGearSetCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6695.ZerolBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6695,
            )

            return self._parent._cast(_6695.ZerolBevelGearSetCriticalSpeedAnalysis)

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
    def assembly_design(self: Self) -> "_2534.AGMAGleasonConicalGearSet":
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
