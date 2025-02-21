"""ConceptCouplingHalfMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5417
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ConceptCouplingHalfMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2582
    from mastapy.system_model.analyses_and_results.static_loads import _6840
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5464,
        _5404,
        _5467,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalfMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingHalfMultibodyDynamicsAnalysis")


class ConceptCouplingHalfMultibodyDynamicsAnalysis(
    _5417.CouplingHalfMultibodyDynamicsAnalysis
):
    """ConceptCouplingHalfMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis"
    )

    class _Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis:
        """Special nested class for casting ConceptCouplingHalfMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
            parent: "ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5417.CouplingHalfMultibodyDynamicsAnalysis":
            return self._parent._cast(_5417.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5464.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5404.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(_5404.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5467.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(_5467.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_7549.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_coupling_half_multibody_dynamics_analysis(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "ConceptCouplingHalfMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "ConceptCouplingHalfMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2582.ConceptCouplingHalf":
        """mastapy.system_model.part_model.couplings.ConceptCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6840.ConceptCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase

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
    ) -> "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis":
        return self._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis(self)
