"""SynchroniserPartCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5027,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "SynchroniserPartCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4974,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5102,
        _5104,
        _5065,
        _5013,
        _5067,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="SynchroniserPartCompoundModalAnalysisAtAStiffness")


class SynchroniserPartCompoundModalAnalysisAtAStiffness(
    _5027.CouplingHalfCompoundModalAnalysisAtAStiffness
):
    """SynchroniserPartCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting SynchroniserPartCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
            parent: "SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ) -> "_5027.CouplingHalfCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5027.CouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ) -> "_5065.MountableComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5065,
            )

            return self._parent._cast(
                _5065.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ) -> "_5013.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5013,
            )

            return self._parent._cast(_5013.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ) -> "_5067.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(_5067.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ) -> "_5102.SynchroniserHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5102,
            )

            return self._parent._cast(
                _5102.SynchroniserHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ) -> "_5104.SynchroniserSleeveCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5104,
            )

            return self._parent._cast(
                _5104.SynchroniserSleeveCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
        ) -> "SynchroniserPartCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "SynchroniserPartCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4974.SynchroniserPartModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.SynchroniserPartModalAnalysisAtAStiffness]

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
    ) -> "List[_4974.SynchroniserPartModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.SynchroniserPartModalAnalysisAtAStiffness]

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
    ) -> "SynchroniserPartCompoundModalAnalysisAtAStiffness._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness":
        return self._Cast_SynchroniserPartCompoundModalAnalysisAtAStiffness(self)
