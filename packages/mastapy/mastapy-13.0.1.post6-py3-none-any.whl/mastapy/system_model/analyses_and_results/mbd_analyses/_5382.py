"""AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5413
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2514
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5391,
        _5396,
        _5444,
        _5492,
        _5498,
        _5501,
        _5522,
        _5440,
        _5489,
        _5376,
        _5467,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis")


class AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis(
    _5413.ConicalGearSetMultibodyDynamicsAnalysis
):
    """AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
            parent: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5413.ConicalGearSetMultibodyDynamicsAnalysis":
            return self._parent._cast(_5413.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5440.GearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5440

            return self._parent._cast(_5440.GearSetMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5489.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5489

            return self._parent._cast(
                _5489.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5376.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5376

            return self._parent._cast(_5376.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5467.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(_5467.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_7549.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5391.BevelDifferentialGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5391

            return self._parent._cast(
                _5391.BevelDifferentialGearSetMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5396.BevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5396

            return self._parent._cast(_5396.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5444.HypoidGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5444

            return self._parent._cast(_5444.HypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5492.SpiralBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5492

            return self._parent._cast(_5492.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5498.StraightBevelDiffGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5498

            return self._parent._cast(
                _5498.StraightBevelDiffGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5501.StraightBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5501

            return self._parent._cast(
                _5501.StraightBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5522.ZerolBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5522

            return self._parent._cast(_5522.ZerolBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis.TYPE",
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
    ) -> "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis(self)
