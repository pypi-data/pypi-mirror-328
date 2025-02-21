"""BoltCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4753
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "BoltCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2442
    from mastapy.system_model.analyses_and_results.modal_analyses import _4592
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4807
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("BoltCompoundModalAnalysis",)


Self = TypeVar("Self", bound="BoltCompoundModalAnalysis")


class BoltCompoundModalAnalysis(_4753.ComponentCompoundModalAnalysis):
    """BoltCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLT_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltCompoundModalAnalysis")

    class _Cast_BoltCompoundModalAnalysis:
        """Special nested class for casting BoltCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "BoltCompoundModalAnalysis._Cast_BoltCompoundModalAnalysis",
            parent: "BoltCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_modal_analysis(
            self: "BoltCompoundModalAnalysis._Cast_BoltCompoundModalAnalysis",
        ) -> "_4753.ComponentCompoundModalAnalysis":
            return self._parent._cast(_4753.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "BoltCompoundModalAnalysis._Cast_BoltCompoundModalAnalysis",
        ) -> "_4807.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(_4807.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "BoltCompoundModalAnalysis._Cast_BoltCompoundModalAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BoltCompoundModalAnalysis._Cast_BoltCompoundModalAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltCompoundModalAnalysis._Cast_BoltCompoundModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bolt_compound_modal_analysis(
            self: "BoltCompoundModalAnalysis._Cast_BoltCompoundModalAnalysis",
        ) -> "BoltCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BoltCompoundModalAnalysis._Cast_BoltCompoundModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2442.Bolt":
        """mastapy.system_model.part_model.Bolt

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4592.BoltModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BoltModalAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_4592.BoltModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BoltModalAnalysis]

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
    ) -> "BoltCompoundModalAnalysis._Cast_BoltCompoundModalAnalysis":
        return self._Cast_BoltCompoundModalAnalysis(self)
