"""SynchroniserPartCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6714,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "SynchroniserPartCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6661
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6789,
        _6791,
        _6752,
        _6700,
        _6754,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartCompoundCriticalSpeedAnalysis")


class SynchroniserPartCompoundCriticalSpeedAnalysis(
    _6714.CouplingHalfCompoundCriticalSpeedAnalysis
):
    """SynchroniserPartCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartCompoundCriticalSpeedAnalysis"
    )

    class _Cast_SynchroniserPartCompoundCriticalSpeedAnalysis:
        """Special nested class for casting SynchroniserPartCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
            parent: "SynchroniserPartCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_critical_speed_analysis(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
        ) -> "_6714.CouplingHalfCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6714.CouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
        ) -> "_6752.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6752,
            )

            return self._parent._cast(
                _6752.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
        ) -> "_6700.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6700,
            )

            return self._parent._cast(_6700.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
        ) -> "_6754.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6754,
            )

            return self._parent._cast(_6754.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_critical_speed_analysis(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
        ) -> "_6789.SynchroniserHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6789,
            )

            return self._parent._cast(
                _6789.SynchroniserHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_sleeve_compound_critical_speed_analysis(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
        ) -> "_6791.SynchroniserSleeveCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6791,
            )

            return self._parent._cast(
                _6791.SynchroniserSleeveCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_part_compound_critical_speed_analysis(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
        ) -> "SynchroniserPartCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
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
        self: Self,
        instance_to_wrap: "SynchroniserPartCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6661.SynchroniserPartCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.SynchroniserPartCriticalSpeedAnalysis]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6661.SynchroniserPartCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.SynchroniserPartCriticalSpeedAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis":
        return self._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis(self)
