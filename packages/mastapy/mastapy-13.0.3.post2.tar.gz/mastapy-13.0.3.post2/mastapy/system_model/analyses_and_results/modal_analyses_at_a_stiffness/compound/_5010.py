"""AbstractShaftCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5011,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "AbstractShaftCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4879,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5054,
        _5104,
        _5034,
        _5088,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="AbstractShaftCompoundModalAnalysisAtAStiffness")


class AbstractShaftCompoundModalAnalysisAtAStiffness(
    _5011.AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness
):
    """AbstractShaftCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_AbstractShaftCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting AbstractShaftCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftCompoundModalAnalysisAtAStiffness",
            parent: "AbstractShaftCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftCompoundModalAnalysisAtAStiffness",
        ) -> "_5011.AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5011.AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftCompoundModalAnalysisAtAStiffness",
        ) -> "_5034.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5034,
            )

            return self._parent._cast(_5034.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(_5088.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftCompoundModalAnalysisAtAStiffness",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftCompoundModalAnalysisAtAStiffness",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftCompoundModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftCompoundModalAnalysisAtAStiffness",
        ) -> "_5054.CycloidalDiscCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5054,
            )

            return self._parent._cast(
                _5054.CycloidalDiscCompoundModalAnalysisAtAStiffness
            )

        @property
        def shaft_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftCompoundModalAnalysisAtAStiffness",
        ) -> "_5104.ShaftCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5104,
            )

            return self._parent._cast(_5104.ShaftCompoundModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftCompoundModalAnalysisAtAStiffness",
        ) -> "AbstractShaftCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "AbstractShaftCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4879.AbstractShaftModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.AbstractShaftModalAnalysisAtAStiffness]

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
    ) -> "List[_4879.AbstractShaftModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.AbstractShaftModalAnalysisAtAStiffness]

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
    ) -> "AbstractShaftCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftCompoundModalAnalysisAtAStiffness":
        return self._Cast_AbstractShaftCompoundModalAnalysisAtAStiffness(self)
