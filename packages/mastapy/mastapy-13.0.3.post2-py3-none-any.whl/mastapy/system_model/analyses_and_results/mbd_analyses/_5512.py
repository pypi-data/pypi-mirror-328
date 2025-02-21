"""SpiralBevelGearMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5416
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "SpiralBevelGearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2563
    from mastapy.system_model.analyses_and_results.static_loads import _6975
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5402,
        _5433,
        _5460,
        _5485,
        _5425,
        _5488,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7570, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearMultibodyDynamicsAnalysis")


class SpiralBevelGearMultibodyDynamicsAnalysis(
    _5416.BevelGearMultibodyDynamicsAnalysis
):
    """SpiralBevelGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMultibodyDynamicsAnalysis"
    )

    class _Cast_SpiralBevelGearMultibodyDynamicsAnalysis:
        """Special nested class for casting SpiralBevelGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
            parent: "SpiralBevelGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_5416.BevelGearMultibodyDynamicsAnalysis":
            return self._parent._cast(_5416.BevelGearMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_5402.AGMAGleasonConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5402

            return self._parent._cast(
                _5402.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_5433.ConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5433

            return self._parent._cast(_5433.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_5460.GearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5460

            return self._parent._cast(_5460.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_5485.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5485

            return self._parent._cast(_5485.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_5425.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(_5425.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_5488.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_7570.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7570

            return self._parent._cast(_7570.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_multibody_dynamics_analysis(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "SpiralBevelGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "SpiralBevelGearMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2563.SpiralBevelGear":
        """mastapy.system_model.part_model.gears.SpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6975.SpiralBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase

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
    ) -> "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis":
        return self._Cast_SpiralBevelGearMultibodyDynamicsAnalysis(self)
