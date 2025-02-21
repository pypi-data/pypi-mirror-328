"""MeasurementComponentMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5515
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "MeasurementComponentMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2463
    from mastapy.system_model.analyses_and_results.static_loads import _6923
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5464,
        _5404,
        _5467,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="MeasurementComponentMultibodyDynamicsAnalysis")


class MeasurementComponentMultibodyDynamicsAnalysis(
    _5515.VirtualComponentMultibodyDynamicsAnalysis
):
    """MeasurementComponentMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MeasurementComponentMultibodyDynamicsAnalysis"
    )

    class _Cast_MeasurementComponentMultibodyDynamicsAnalysis:
        """Special nested class for casting MeasurementComponentMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "MeasurementComponentMultibodyDynamicsAnalysis._Cast_MeasurementComponentMultibodyDynamicsAnalysis",
            parent: "MeasurementComponentMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_multibody_dynamics_analysis(
            self: "MeasurementComponentMultibodyDynamicsAnalysis._Cast_MeasurementComponentMultibodyDynamicsAnalysis",
        ) -> "_5515.VirtualComponentMultibodyDynamicsAnalysis":
            return self._parent._cast(_5515.VirtualComponentMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "MeasurementComponentMultibodyDynamicsAnalysis._Cast_MeasurementComponentMultibodyDynamicsAnalysis",
        ) -> "_5464.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "MeasurementComponentMultibodyDynamicsAnalysis._Cast_MeasurementComponentMultibodyDynamicsAnalysis",
        ) -> "_5404.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(_5404.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "MeasurementComponentMultibodyDynamicsAnalysis._Cast_MeasurementComponentMultibodyDynamicsAnalysis",
        ) -> "_5467.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(_5467.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "MeasurementComponentMultibodyDynamicsAnalysis._Cast_MeasurementComponentMultibodyDynamicsAnalysis",
        ) -> "_7549.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MeasurementComponentMultibodyDynamicsAnalysis._Cast_MeasurementComponentMultibodyDynamicsAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MeasurementComponentMultibodyDynamicsAnalysis._Cast_MeasurementComponentMultibodyDynamicsAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MeasurementComponentMultibodyDynamicsAnalysis._Cast_MeasurementComponentMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentMultibodyDynamicsAnalysis._Cast_MeasurementComponentMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def measurement_component_multibody_dynamics_analysis(
            self: "MeasurementComponentMultibodyDynamicsAnalysis._Cast_MeasurementComponentMultibodyDynamicsAnalysis",
        ) -> "MeasurementComponentMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentMultibodyDynamicsAnalysis._Cast_MeasurementComponentMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "MeasurementComponentMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2463.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6923.MeasurementComponentLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase

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
    ) -> "MeasurementComponentMultibodyDynamicsAnalysis._Cast_MeasurementComponentMultibodyDynamicsAnalysis":
        return self._Cast_MeasurementComponentMultibodyDynamicsAnalysis(self)
