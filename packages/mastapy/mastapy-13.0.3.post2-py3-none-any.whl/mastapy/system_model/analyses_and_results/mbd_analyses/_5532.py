"""TorqueConverterPumpMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5438
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "TorqueConverterPumpMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2629
    from mastapy.system_model.analyses_and_results.static_loads import _6996
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5485,
        _5425,
        _5488,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7570, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterPumpMultibodyDynamicsAnalysis")


class TorqueConverterPumpMultibodyDynamicsAnalysis(
    _5438.CouplingHalfMultibodyDynamicsAnalysis
):
    """TorqueConverterPumpMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterPumpMultibodyDynamicsAnalysis"
    )

    class _Cast_TorqueConverterPumpMultibodyDynamicsAnalysis:
        """Special nested class for casting TorqueConverterPumpMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterPumpMultibodyDynamicsAnalysis._Cast_TorqueConverterPumpMultibodyDynamicsAnalysis",
            parent: "TorqueConverterPumpMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "TorqueConverterPumpMultibodyDynamicsAnalysis._Cast_TorqueConverterPumpMultibodyDynamicsAnalysis",
        ) -> "_5438.CouplingHalfMultibodyDynamicsAnalysis":
            return self._parent._cast(_5438.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "TorqueConverterPumpMultibodyDynamicsAnalysis._Cast_TorqueConverterPumpMultibodyDynamicsAnalysis",
        ) -> "_5485.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5485

            return self._parent._cast(_5485.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "TorqueConverterPumpMultibodyDynamicsAnalysis._Cast_TorqueConverterPumpMultibodyDynamicsAnalysis",
        ) -> "_5425.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(_5425.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "TorqueConverterPumpMultibodyDynamicsAnalysis._Cast_TorqueConverterPumpMultibodyDynamicsAnalysis",
        ) -> "_5488.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "TorqueConverterPumpMultibodyDynamicsAnalysis._Cast_TorqueConverterPumpMultibodyDynamicsAnalysis",
        ) -> "_7570.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7570

            return self._parent._cast(_7570.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterPumpMultibodyDynamicsAnalysis._Cast_TorqueConverterPumpMultibodyDynamicsAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterPumpMultibodyDynamicsAnalysis._Cast_TorqueConverterPumpMultibodyDynamicsAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterPumpMultibodyDynamicsAnalysis._Cast_TorqueConverterPumpMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpMultibodyDynamicsAnalysis._Cast_TorqueConverterPumpMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def torque_converter_pump_multibody_dynamics_analysis(
            self: "TorqueConverterPumpMultibodyDynamicsAnalysis._Cast_TorqueConverterPumpMultibodyDynamicsAnalysis",
        ) -> "TorqueConverterPumpMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpMultibodyDynamicsAnalysis._Cast_TorqueConverterPumpMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "TorqueConverterPumpMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2629.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6996.TorqueConverterPumpLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase

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
    ) -> "TorqueConverterPumpMultibodyDynamicsAnalysis._Cast_TorqueConverterPumpMultibodyDynamicsAnalysis":
        return self._Cast_TorqueConverterPumpMultibodyDynamicsAnalysis(self)
