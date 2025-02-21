"""GuideDxfModelCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6700,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "GuideDxfModelCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6607
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6754,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="GuideDxfModelCompoundCriticalSpeedAnalysis")


class GuideDxfModelCompoundCriticalSpeedAnalysis(
    _6700.ComponentCompoundCriticalSpeedAnalysis
):
    """GuideDxfModelCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GuideDxfModelCompoundCriticalSpeedAnalysis"
    )

    class _Cast_GuideDxfModelCompoundCriticalSpeedAnalysis:
        """Special nested class for casting GuideDxfModelCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "GuideDxfModelCompoundCriticalSpeedAnalysis._Cast_GuideDxfModelCompoundCriticalSpeedAnalysis",
            parent: "GuideDxfModelCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_critical_speed_analysis(
            self: "GuideDxfModelCompoundCriticalSpeedAnalysis._Cast_GuideDxfModelCompoundCriticalSpeedAnalysis",
        ) -> "_6700.ComponentCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6700.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "GuideDxfModelCompoundCriticalSpeedAnalysis._Cast_GuideDxfModelCompoundCriticalSpeedAnalysis",
        ) -> "_6754.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6754,
            )

            return self._parent._cast(_6754.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "GuideDxfModelCompoundCriticalSpeedAnalysis._Cast_GuideDxfModelCompoundCriticalSpeedAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GuideDxfModelCompoundCriticalSpeedAnalysis._Cast_GuideDxfModelCompoundCriticalSpeedAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelCompoundCriticalSpeedAnalysis._Cast_GuideDxfModelCompoundCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def guide_dxf_model_compound_critical_speed_analysis(
            self: "GuideDxfModelCompoundCriticalSpeedAnalysis._Cast_GuideDxfModelCompoundCriticalSpeedAnalysis",
        ) -> "GuideDxfModelCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelCompoundCriticalSpeedAnalysis._Cast_GuideDxfModelCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "GuideDxfModelCompoundCriticalSpeedAnalysis.TYPE"
    ):
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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6607.GuideDxfModelCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.GuideDxfModelCriticalSpeedAnalysis]

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
    ) -> "List[_6607.GuideDxfModelCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.GuideDxfModelCriticalSpeedAnalysis]

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
    ) -> "GuideDxfModelCompoundCriticalSpeedAnalysis._Cast_GuideDxfModelCompoundCriticalSpeedAnalysis":
        return self._Cast_GuideDxfModelCompoundCriticalSpeedAnalysis(self)
