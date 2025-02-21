"""CVTPulleyDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "CVTPulleyDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2587
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6315,
        _6355,
        _6301,
        _6357,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7546,
        _7547,
        _7544,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyDynamicAnalysis",)


Self = TypeVar("Self", bound="CVTPulleyDynamicAnalysis")


class CVTPulleyDynamicAnalysis(_6366.PulleyDynamicAnalysis):
    """CVTPulleyDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyDynamicAnalysis")

    class _Cast_CVTPulleyDynamicAnalysis:
        """Special nested class for casting CVTPulleyDynamicAnalysis to subclasses."""

        def __init__(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
            parent: "CVTPulleyDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def pulley_dynamic_analysis(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_6366.PulleyDynamicAnalysis":
            return self._parent._cast(_6366.PulleyDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_6315.CouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315

            return self._parent._cast(_6315.CouplingHalfDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_6355.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_6301.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301

            return self._parent._cast(_6301.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_6357.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_7546.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis",
        ) -> "CVTPulleyDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleyDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2587.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTPulleyDynamicAnalysis._Cast_CVTPulleyDynamicAnalysis":
        return self._Cast_CVTPulleyDynamicAnalysis(self)
