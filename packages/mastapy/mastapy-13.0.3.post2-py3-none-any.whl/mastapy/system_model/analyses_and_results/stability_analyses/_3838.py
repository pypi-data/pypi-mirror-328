"""ExternalCADModelStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3809
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ExternalCADModelStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2472
    from mastapy.system_model.analyses_and_results.static_loads import _6905
    from mastapy.system_model.analyses_and_results.stability_analyses import _3865
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelStabilityAnalysis",)


Self = TypeVar("Self", bound="ExternalCADModelStabilityAnalysis")


class ExternalCADModelStabilityAnalysis(_3809.ComponentStabilityAnalysis):
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
        ) -> "_3809.ComponentStabilityAnalysis":
            return self._parent._cast(_3809.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "ExternalCADModelStabilityAnalysis._Cast_ExternalCADModelStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ExternalCADModelStabilityAnalysis._Cast_ExternalCADModelStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ExternalCADModelStabilityAnalysis._Cast_ExternalCADModelStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ExternalCADModelStabilityAnalysis._Cast_ExternalCADModelStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ExternalCADModelStabilityAnalysis._Cast_ExternalCADModelStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelStabilityAnalysis._Cast_ExternalCADModelStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

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
    def component_design(self: Self) -> "_2472.ExternalCADModel":
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
    def component_load_case(self: Self) -> "_6905.ExternalCADModelLoadCase":
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
