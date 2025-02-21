"""CVTMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5387
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CVTMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2586
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5488,
        _5375,
        _5466,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CVTMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CVTMultibodyDynamicsAnalysis")


class CVTMultibodyDynamicsAnalysis(_5387.BeltDriveMultibodyDynamicsAnalysis):
    """CVTMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTMultibodyDynamicsAnalysis")

    class _Cast_CVTMultibodyDynamicsAnalysis:
        """Special nested class for casting CVTMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
            parent: "CVTMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def belt_drive_multibody_dynamics_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_5387.BeltDriveMultibodyDynamicsAnalysis":
            return self._parent._cast(_5387.BeltDriveMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_5488.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(
                _5488.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_5375.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5375

            return self._parent._cast(_5375.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_5466.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(_5466.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_7548.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_multibody_dynamics_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "CVTMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTMultibodyDynamicsAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2586.CVT":
        """mastapy.system_model.part_model.couplings.CVT

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
    ) -> "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis":
        return self._Cast_CVTMultibodyDynamicsAnalysis(self)
