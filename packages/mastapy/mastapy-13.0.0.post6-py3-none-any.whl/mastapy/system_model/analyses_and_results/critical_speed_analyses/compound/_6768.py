"""RootAssemblyCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6681,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "RootAssemblyCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6639
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6674,
        _6753,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="RootAssemblyCompoundCriticalSpeedAnalysis")


class RootAssemblyCompoundCriticalSpeedAnalysis(
    _6681.AssemblyCompoundCriticalSpeedAnalysis
):
    """RootAssemblyCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RootAssemblyCompoundCriticalSpeedAnalysis"
    )

    class _Cast_RootAssemblyCompoundCriticalSpeedAnalysis:
        """Special nested class for casting RootAssemblyCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "RootAssemblyCompoundCriticalSpeedAnalysis._Cast_RootAssemblyCompoundCriticalSpeedAnalysis",
            parent: "RootAssemblyCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def assembly_compound_critical_speed_analysis(
            self: "RootAssemblyCompoundCriticalSpeedAnalysis._Cast_RootAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6681.AssemblyCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6681.AssemblyCompoundCriticalSpeedAnalysis)

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "RootAssemblyCompoundCriticalSpeedAnalysis._Cast_RootAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6674.AbstractAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6674,
            )

            return self._parent._cast(
                _6674.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "RootAssemblyCompoundCriticalSpeedAnalysis._Cast_RootAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_6753.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6753,
            )

            return self._parent._cast(_6753.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "RootAssemblyCompoundCriticalSpeedAnalysis._Cast_RootAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RootAssemblyCompoundCriticalSpeedAnalysis._Cast_RootAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyCompoundCriticalSpeedAnalysis._Cast_RootAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def root_assembly_compound_critical_speed_analysis(
            self: "RootAssemblyCompoundCriticalSpeedAnalysis._Cast_RootAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "RootAssemblyCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "RootAssemblyCompoundCriticalSpeedAnalysis._Cast_RootAssemblyCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "RootAssemblyCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6639.RootAssemblyCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.RootAssemblyCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6639.RootAssemblyCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.RootAssemblyCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblyCompoundCriticalSpeedAnalysis._Cast_RootAssemblyCompoundCriticalSpeedAnalysis":
        return self._Cast_RootAssemblyCompoundCriticalSpeedAnalysis(self)
