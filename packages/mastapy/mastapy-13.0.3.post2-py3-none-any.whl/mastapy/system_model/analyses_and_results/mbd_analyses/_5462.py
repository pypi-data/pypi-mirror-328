"""GuideDxfModelMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5425
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "GuideDxfModelMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2475
    from mastapy.system_model.analyses_and_results.static_loads import _6918
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5488
    from mastapy.system_model.analyses_and_results.analysis_cases import _7570, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="GuideDxfModelMultibodyDynamicsAnalysis")


class GuideDxfModelMultibodyDynamicsAnalysis(_5425.ComponentMultibodyDynamicsAnalysis):
    """GuideDxfModelMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GuideDxfModelMultibodyDynamicsAnalysis"
    )

    class _Cast_GuideDxfModelMultibodyDynamicsAnalysis:
        """Special nested class for casting GuideDxfModelMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "GuideDxfModelMultibodyDynamicsAnalysis._Cast_GuideDxfModelMultibodyDynamicsAnalysis",
            parent: "GuideDxfModelMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def component_multibody_dynamics_analysis(
            self: "GuideDxfModelMultibodyDynamicsAnalysis._Cast_GuideDxfModelMultibodyDynamicsAnalysis",
        ) -> "_5425.ComponentMultibodyDynamicsAnalysis":
            return self._parent._cast(_5425.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "GuideDxfModelMultibodyDynamicsAnalysis._Cast_GuideDxfModelMultibodyDynamicsAnalysis",
        ) -> "_5488.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "GuideDxfModelMultibodyDynamicsAnalysis._Cast_GuideDxfModelMultibodyDynamicsAnalysis",
        ) -> "_7570.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7570

            return self._parent._cast(_7570.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GuideDxfModelMultibodyDynamicsAnalysis._Cast_GuideDxfModelMultibodyDynamicsAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GuideDxfModelMultibodyDynamicsAnalysis._Cast_GuideDxfModelMultibodyDynamicsAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GuideDxfModelMultibodyDynamicsAnalysis._Cast_GuideDxfModelMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelMultibodyDynamicsAnalysis._Cast_GuideDxfModelMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def guide_dxf_model_multibody_dynamics_analysis(
            self: "GuideDxfModelMultibodyDynamicsAnalysis._Cast_GuideDxfModelMultibodyDynamicsAnalysis",
        ) -> "GuideDxfModelMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelMultibodyDynamicsAnalysis._Cast_GuideDxfModelMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "GuideDxfModelMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2475.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6918.GuideDxfModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase

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
    ) -> "GuideDxfModelMultibodyDynamicsAnalysis._Cast_GuideDxfModelMultibodyDynamicsAnalysis":
        return self._Cast_GuideDxfModelMultibodyDynamicsAnalysis(self)
