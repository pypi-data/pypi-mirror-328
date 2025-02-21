"""WormGearMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5439
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "WormGearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2551
    from mastapy.system_model.analyses_and_results.static_loads import _6983
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5464,
        _5404,
        _5467,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="WormGearMultibodyDynamicsAnalysis")


class WormGearMultibodyDynamicsAnalysis(_5439.GearMultibodyDynamicsAnalysis):
    """WormGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearMultibodyDynamicsAnalysis")

    class _Cast_WormGearMultibodyDynamicsAnalysis:
        """Special nested class for casting WormGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "WormGearMultibodyDynamicsAnalysis._Cast_WormGearMultibodyDynamicsAnalysis",
            parent: "WormGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def gear_multibody_dynamics_analysis(
            self: "WormGearMultibodyDynamicsAnalysis._Cast_WormGearMultibodyDynamicsAnalysis",
        ) -> "_5439.GearMultibodyDynamicsAnalysis":
            return self._parent._cast(_5439.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "WormGearMultibodyDynamicsAnalysis._Cast_WormGearMultibodyDynamicsAnalysis",
        ) -> "_5464.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "WormGearMultibodyDynamicsAnalysis._Cast_WormGearMultibodyDynamicsAnalysis",
        ) -> "_5404.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(_5404.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "WormGearMultibodyDynamicsAnalysis._Cast_WormGearMultibodyDynamicsAnalysis",
        ) -> "_5467.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(_5467.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "WormGearMultibodyDynamicsAnalysis._Cast_WormGearMultibodyDynamicsAnalysis",
        ) -> "_7549.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "WormGearMultibodyDynamicsAnalysis._Cast_WormGearMultibodyDynamicsAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "WormGearMultibodyDynamicsAnalysis._Cast_WormGearMultibodyDynamicsAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearMultibodyDynamicsAnalysis._Cast_WormGearMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMultibodyDynamicsAnalysis._Cast_WormGearMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def worm_gear_multibody_dynamics_analysis(
            self: "WormGearMultibodyDynamicsAnalysis._Cast_WormGearMultibodyDynamicsAnalysis",
        ) -> "WormGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearMultibodyDynamicsAnalysis._Cast_WormGearMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "WormGearMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2551.WormGear":
        """mastapy.system_model.part_model.gears.WormGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6983.WormGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase

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
    ) -> "WormGearMultibodyDynamicsAnalysis._Cast_WormGearMultibodyDynamicsAnalysis":
        return self._Cast_WormGearMultibodyDynamicsAnalysis(self)
