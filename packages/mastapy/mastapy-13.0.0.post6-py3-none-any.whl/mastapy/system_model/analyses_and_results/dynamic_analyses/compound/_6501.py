"""RootAssemblyCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6414
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "RootAssemblyCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6372
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6407,
        _6486,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="RootAssemblyCompoundDynamicAnalysis")


class RootAssemblyCompoundDynamicAnalysis(_6414.AssemblyCompoundDynamicAnalysis):
    """RootAssemblyCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RootAssemblyCompoundDynamicAnalysis")

    class _Cast_RootAssemblyCompoundDynamicAnalysis:
        """Special nested class for casting RootAssemblyCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "RootAssemblyCompoundDynamicAnalysis._Cast_RootAssemblyCompoundDynamicAnalysis",
            parent: "RootAssemblyCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def assembly_compound_dynamic_analysis(
            self: "RootAssemblyCompoundDynamicAnalysis._Cast_RootAssemblyCompoundDynamicAnalysis",
        ) -> "_6414.AssemblyCompoundDynamicAnalysis":
            return self._parent._cast(_6414.AssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "RootAssemblyCompoundDynamicAnalysis._Cast_RootAssemblyCompoundDynamicAnalysis",
        ) -> "_6407.AbstractAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6407,
            )

            return self._parent._cast(_6407.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "RootAssemblyCompoundDynamicAnalysis._Cast_RootAssemblyCompoundDynamicAnalysis",
        ) -> "_6486.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6486,
            )

            return self._parent._cast(_6486.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "RootAssemblyCompoundDynamicAnalysis._Cast_RootAssemblyCompoundDynamicAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RootAssemblyCompoundDynamicAnalysis._Cast_RootAssemblyCompoundDynamicAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyCompoundDynamicAnalysis._Cast_RootAssemblyCompoundDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def root_assembly_compound_dynamic_analysis(
            self: "RootAssemblyCompoundDynamicAnalysis._Cast_RootAssemblyCompoundDynamicAnalysis",
        ) -> "RootAssemblyCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "RootAssemblyCompoundDynamicAnalysis._Cast_RootAssemblyCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "RootAssemblyCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6372.RootAssemblyDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.RootAssemblyDynamicAnalysis]

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
    ) -> "List[_6372.RootAssemblyDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.RootAssemblyDynamicAnalysis]

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
    ) -> (
        "RootAssemblyCompoundDynamicAnalysis._Cast_RootAssemblyCompoundDynamicAnalysis"
    ):
        return self._Cast_RootAssemblyCompoundDynamicAnalysis(self)
