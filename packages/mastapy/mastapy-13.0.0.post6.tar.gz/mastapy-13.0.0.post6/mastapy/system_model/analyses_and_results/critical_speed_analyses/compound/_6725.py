"""DatumCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6699,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "DatumCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2448
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6596
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6753,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("DatumCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="DatumCompoundCriticalSpeedAnalysis")


class DatumCompoundCriticalSpeedAnalysis(_6699.ComponentCompoundCriticalSpeedAnalysis):
    """DatumCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _DATUM_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DatumCompoundCriticalSpeedAnalysis")

    class _Cast_DatumCompoundCriticalSpeedAnalysis:
        """Special nested class for casting DatumCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "DatumCompoundCriticalSpeedAnalysis._Cast_DatumCompoundCriticalSpeedAnalysis",
            parent: "DatumCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_critical_speed_analysis(
            self: "DatumCompoundCriticalSpeedAnalysis._Cast_DatumCompoundCriticalSpeedAnalysis",
        ) -> "_6699.ComponentCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6699.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "DatumCompoundCriticalSpeedAnalysis._Cast_DatumCompoundCriticalSpeedAnalysis",
        ) -> "_6753.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6753,
            )

            return self._parent._cast(_6753.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "DatumCompoundCriticalSpeedAnalysis._Cast_DatumCompoundCriticalSpeedAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "DatumCompoundCriticalSpeedAnalysis._Cast_DatumCompoundCriticalSpeedAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "DatumCompoundCriticalSpeedAnalysis._Cast_DatumCompoundCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def datum_compound_critical_speed_analysis(
            self: "DatumCompoundCriticalSpeedAnalysis._Cast_DatumCompoundCriticalSpeedAnalysis",
        ) -> "DatumCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "DatumCompoundCriticalSpeedAnalysis._Cast_DatumCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "DatumCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2448.Datum":
        """mastapy.system_model.part_model.Datum

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
    ) -> "List[_6596.DatumCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.DatumCriticalSpeedAnalysis]

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
    ) -> "List[_6596.DatumCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.DatumCriticalSpeedAnalysis]

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
    ) -> "DatumCompoundCriticalSpeedAnalysis._Cast_DatumCompoundCriticalSpeedAnalysis":
        return self._Cast_DatumCompoundCriticalSpeedAnalysis(self)
