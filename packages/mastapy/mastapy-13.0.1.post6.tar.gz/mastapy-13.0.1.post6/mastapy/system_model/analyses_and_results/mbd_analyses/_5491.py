"""SpiralBevelGearMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5395
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "SpiralBevelGearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.static_loads import _6954
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5381,
        _5412,
        _5439,
        _5464,
        _5404,
        _5467,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearMultibodyDynamicsAnalysis")


class SpiralBevelGearMultibodyDynamicsAnalysis(
    _5395.BevelGearMultibodyDynamicsAnalysis
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
        ) -> "_5395.BevelGearMultibodyDynamicsAnalysis":
            return self._parent._cast(_5395.BevelGearMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_5381.AGMAGleasonConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5381

            return self._parent._cast(
                _5381.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_5412.ConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412

            return self._parent._cast(_5412.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_5439.GearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439

            return self._parent._cast(_5439.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_5464.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_5404.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(_5404.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_5467.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(_5467.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_7549.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

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
    def component_design(self: Self) -> "_2543.SpiralBevelGear":
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
    def component_load_case(self: Self) -> "_6954.SpiralBevelGearLoadCase":
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
