"""ExternalCADModelCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3922
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "ExternalCADModelCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2452
    from mastapy.system_model.analyses_and_results.stability_analyses import _3817
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3976,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="ExternalCADModelCompoundStabilityAnalysis")


class ExternalCADModelCompoundStabilityAnalysis(
    _3922.ComponentCompoundStabilityAnalysis
):
    """ExternalCADModelCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ExternalCADModelCompoundStabilityAnalysis"
    )

    class _Cast_ExternalCADModelCompoundStabilityAnalysis:
        """Special nested class for casting ExternalCADModelCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "ExternalCADModelCompoundStabilityAnalysis._Cast_ExternalCADModelCompoundStabilityAnalysis",
            parent: "ExternalCADModelCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_stability_analysis(
            self: "ExternalCADModelCompoundStabilityAnalysis._Cast_ExternalCADModelCompoundStabilityAnalysis",
        ) -> "_3922.ComponentCompoundStabilityAnalysis":
            return self._parent._cast(_3922.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "ExternalCADModelCompoundStabilityAnalysis._Cast_ExternalCADModelCompoundStabilityAnalysis",
        ) -> "_3976.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "ExternalCADModelCompoundStabilityAnalysis._Cast_ExternalCADModelCompoundStabilityAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ExternalCADModelCompoundStabilityAnalysis._Cast_ExternalCADModelCompoundStabilityAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelCompoundStabilityAnalysis._Cast_ExternalCADModelCompoundStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def external_cad_model_compound_stability_analysis(
            self: "ExternalCADModelCompoundStabilityAnalysis._Cast_ExternalCADModelCompoundStabilityAnalysis",
        ) -> "ExternalCADModelCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelCompoundStabilityAnalysis._Cast_ExternalCADModelCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "ExternalCADModelCompoundStabilityAnalysis.TYPE"
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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3817.ExternalCADModelStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ExternalCADModelStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3817.ExternalCADModelStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ExternalCADModelStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ExternalCADModelCompoundStabilityAnalysis._Cast_ExternalCADModelCompoundStabilityAnalysis":
        return self._Cast_ExternalCADModelCompoundStabilityAnalysis(self)
