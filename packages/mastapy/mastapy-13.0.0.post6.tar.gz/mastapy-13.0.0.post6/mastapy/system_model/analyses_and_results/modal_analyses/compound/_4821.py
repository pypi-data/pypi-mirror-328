"""RootAssemblyCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4734
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "RootAssemblyCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4676
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4727,
        _4806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyCompoundModalAnalysis",)


Self = TypeVar("Self", bound="RootAssemblyCompoundModalAnalysis")


class RootAssemblyCompoundModalAnalysis(_4734.AssemblyCompoundModalAnalysis):
    """RootAssemblyCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RootAssemblyCompoundModalAnalysis")

    class _Cast_RootAssemblyCompoundModalAnalysis:
        """Special nested class for casting RootAssemblyCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "RootAssemblyCompoundModalAnalysis._Cast_RootAssemblyCompoundModalAnalysis",
            parent: "RootAssemblyCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def assembly_compound_modal_analysis(
            self: "RootAssemblyCompoundModalAnalysis._Cast_RootAssemblyCompoundModalAnalysis",
        ) -> "_4734.AssemblyCompoundModalAnalysis":
            return self._parent._cast(_4734.AssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "RootAssemblyCompoundModalAnalysis._Cast_RootAssemblyCompoundModalAnalysis",
        ) -> "_4727.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4727,
            )

            return self._parent._cast(_4727.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "RootAssemblyCompoundModalAnalysis._Cast_RootAssemblyCompoundModalAnalysis",
        ) -> "_4806.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4806,
            )

            return self._parent._cast(_4806.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "RootAssemblyCompoundModalAnalysis._Cast_RootAssemblyCompoundModalAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RootAssemblyCompoundModalAnalysis._Cast_RootAssemblyCompoundModalAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyCompoundModalAnalysis._Cast_RootAssemblyCompoundModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def root_assembly_compound_modal_analysis(
            self: "RootAssemblyCompoundModalAnalysis._Cast_RootAssemblyCompoundModalAnalysis",
        ) -> "RootAssemblyCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "RootAssemblyCompoundModalAnalysis._Cast_RootAssemblyCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "RootAssemblyCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4676.RootAssemblyModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.RootAssemblyModalAnalysis]

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
    def assembly_analysis_cases(self: Self) -> "List[_4676.RootAssemblyModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.RootAssemblyModalAnalysis]

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
    ) -> "RootAssemblyCompoundModalAnalysis._Cast_RootAssemblyCompoundModalAnalysis":
        return self._Cast_RootAssemblyCompoundModalAnalysis(self)
