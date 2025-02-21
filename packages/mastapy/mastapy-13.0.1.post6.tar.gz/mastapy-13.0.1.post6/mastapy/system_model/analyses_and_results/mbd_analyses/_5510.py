"""TorqueConverterMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5418
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "TorqueConverterMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2607
    from mastapy.system_model.analyses_and_results.static_loads import _6974
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5489,
        _5376,
        _5467,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterMultibodyDynamicsAnalysis")


class TorqueConverterMultibodyDynamicsAnalysis(_5418.CouplingMultibodyDynamicsAnalysis):
    """TorqueConverterMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterMultibodyDynamicsAnalysis"
    )

    class _Cast_TorqueConverterMultibodyDynamicsAnalysis:
        """Special nested class for casting TorqueConverterMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
            parent: "TorqueConverterMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_multibody_dynamics_analysis(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
        ) -> "_5418.CouplingMultibodyDynamicsAnalysis":
            return self._parent._cast(_5418.CouplingMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
        ) -> "_5489.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5489

            return self._parent._cast(
                _5489.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
        ) -> "_5376.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5376

            return self._parent._cast(_5376.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
        ) -> "_5467.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(_5467.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
        ) -> "_7549.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_multibody_dynamics_analysis(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
        ) -> "TorqueConverterMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "TorqueConverterMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2607.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6974.TorqueConverterLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis":
        return self._Cast_TorqueConverterMultibodyDynamicsAnalysis(self)
