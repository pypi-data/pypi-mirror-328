"""PartToPartShearCouplingHalfMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5416
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2589
    from mastapy.system_model.analyses_and_results.static_loads import _6930
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5463,
        _5403,
        _5466,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalfMultibodyDynamicsAnalysis")


class PartToPartShearCouplingHalfMultibodyDynamicsAnalysis(
    _5416.CouplingHalfMultibodyDynamicsAnalysis
):
    """PartToPartShearCouplingHalfMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis"
    )

    class _Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis:
        """Special nested class for casting PartToPartShearCouplingHalfMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
            parent: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5416.CouplingHalfMultibodyDynamicsAnalysis":
            return self._parent._cast(_5416.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5463.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5403.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(_5403.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5466.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(_5466.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_7548.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2589.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6930.PartToPartShearCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase

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
    ) -> "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis":
        return self._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis(self)
