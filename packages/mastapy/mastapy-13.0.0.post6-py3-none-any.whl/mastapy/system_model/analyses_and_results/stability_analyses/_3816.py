"""DynamicModelForStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_MODEL_FOR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "DynamicModelForStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7543,
        _7549,
        _7534,
    )
    from mastapy.system_model.analyses_and_results import _2650


__docformat__ = "restructuredtext en"
__all__ = ("DynamicModelForStabilityAnalysis",)


Self = TypeVar("Self", bound="DynamicModelForStabilityAnalysis")


class DynamicModelForStabilityAnalysis(_6328.DynamicAnalysis):
    """DynamicModelForStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_MODEL_FOR_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicModelForStabilityAnalysis")

    class _Cast_DynamicModelForStabilityAnalysis:
        """Special nested class for casting DynamicModelForStabilityAnalysis to subclasses."""

        def __init__(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
            parent: "DynamicModelForStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def dynamic_analysis(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
        ) -> "_6328.DynamicAnalysis":
            return self._parent._cast(_6328.DynamicAnalysis)

        @property
        def fe_analysis(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
        ) -> "_7543.FEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.FEAnalysis)

        @property
        def static_load_analysis_case(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
        ) -> "_7549.StaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
        ) -> "_7534.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.AnalysisCase)

        @property
        def context(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
        ) -> "_2650.Context":
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.Context)

        @property
        def dynamic_model_for_stability_analysis(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
        ) -> "DynamicModelForStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicModelForStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis":
        return self._Cast_DynamicModelForStabilityAnalysis(self)
