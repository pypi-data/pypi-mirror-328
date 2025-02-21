"""ExternalCADModelStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3788
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ExternalCADModelStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2452
    from mastapy.system_model.analyses_and_results.static_loads import _6884
    from mastapy.system_model.analyses_and_results.stability_analyses import _3844
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelStabilityAnalysis",)


Self = TypeVar("Self", bound="ExternalCADModelStabilityAnalysis")


class ExternalCADModelStabilityAnalysis(_3788.ComponentStabilityAnalysis):
    """ExternalCADModelStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ExternalCADModelStabilityAnalysis")

    class _Cast_ExternalCADModelStabilityAnalysis:
        """Special nested class for casting ExternalCADModelStabilityAnalysis to subclasses."""

        def __init__(
            self: "ExternalCADModelStabilityAnalysis._Cast_ExternalCADModelStabilityAnalysis",
            parent: "ExternalCADModelStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def component_stability_analysis(
            self: "ExternalCADModelStabilityAnalysis._Cast_ExternalCADModelStabilityAnalysis",
        ) -> "_3788.ComponentStabilityAnalysis":
            return self._parent._cast(_3788.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "ExternalCADModelStabilityAnalysis._Cast_ExternalCADModelStabilityAnalysis",
        ) -> "_3844.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ExternalCADModelStabilityAnalysis._Cast_ExternalCADModelStabilityAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ExternalCADModelStabilityAnalysis._Cast_ExternalCADModelStabilityAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ExternalCADModelStabilityAnalysis._Cast_ExternalCADModelStabilityAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ExternalCADModelStabilityAnalysis._Cast_ExternalCADModelStabilityAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelStabilityAnalysis._Cast_ExternalCADModelStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def external_cad_model_stability_analysis(
            self: "ExternalCADModelStabilityAnalysis._Cast_ExternalCADModelStabilityAnalysis",
        ) -> "ExternalCADModelStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelStabilityAnalysis._Cast_ExternalCADModelStabilityAnalysis",
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
        self: Self, instance_to_wrap: "ExternalCADModelStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2452.ExternalCADModel":
        """mastapy.system_model.part_model.ExternalCADModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6884.ExternalCADModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase

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
    ) -> "ExternalCADModelStabilityAnalysis._Cast_ExternalCADModelStabilityAnalysis":
        return self._Cast_ExternalCADModelStabilityAnalysis(self)
