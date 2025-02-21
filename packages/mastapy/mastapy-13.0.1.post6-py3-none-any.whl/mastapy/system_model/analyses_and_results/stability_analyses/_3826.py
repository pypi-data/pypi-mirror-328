"""GuideDxfModelStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3788
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "GuideDxfModelStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455
    from mastapy.system_model.analyses_and_results.static_loads import _6897
    from mastapy.system_model.analyses_and_results.stability_analyses import _3844
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelStabilityAnalysis",)


Self = TypeVar("Self", bound="GuideDxfModelStabilityAnalysis")


class GuideDxfModelStabilityAnalysis(_3788.ComponentStabilityAnalysis):
    """GuideDxfModelStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GuideDxfModelStabilityAnalysis")

    class _Cast_GuideDxfModelStabilityAnalysis:
        """Special nested class for casting GuideDxfModelStabilityAnalysis to subclasses."""

        def __init__(
            self: "GuideDxfModelStabilityAnalysis._Cast_GuideDxfModelStabilityAnalysis",
            parent: "GuideDxfModelStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def component_stability_analysis(
            self: "GuideDxfModelStabilityAnalysis._Cast_GuideDxfModelStabilityAnalysis",
        ) -> "_3788.ComponentStabilityAnalysis":
            return self._parent._cast(_3788.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "GuideDxfModelStabilityAnalysis._Cast_GuideDxfModelStabilityAnalysis",
        ) -> "_3844.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GuideDxfModelStabilityAnalysis._Cast_GuideDxfModelStabilityAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GuideDxfModelStabilityAnalysis._Cast_GuideDxfModelStabilityAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GuideDxfModelStabilityAnalysis._Cast_GuideDxfModelStabilityAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GuideDxfModelStabilityAnalysis._Cast_GuideDxfModelStabilityAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelStabilityAnalysis._Cast_GuideDxfModelStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def guide_dxf_model_stability_analysis(
            self: "GuideDxfModelStabilityAnalysis._Cast_GuideDxfModelStabilityAnalysis",
        ) -> "GuideDxfModelStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelStabilityAnalysis._Cast_GuideDxfModelStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GuideDxfModelStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2455.GuideDxfModel":
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
    def component_load_case(self: Self) -> "_6897.GuideDxfModelLoadCase":
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
    ) -> "GuideDxfModelStabilityAnalysis._Cast_GuideDxfModelStabilityAnalysis":
        return self._Cast_GuideDxfModelStabilityAnalysis(self)
