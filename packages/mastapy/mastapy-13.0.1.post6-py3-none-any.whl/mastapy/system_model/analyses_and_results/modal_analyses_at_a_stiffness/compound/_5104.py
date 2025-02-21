"""SynchroniserSleeveCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5103,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "SynchroniserSleeveCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4975,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5027,
        _5065,
        _5013,
        _5067,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="SynchroniserSleeveCompoundModalAnalysisAtAStiffness")


class SynchroniserSleeveCompoundModalAnalysisAtAStiffness(
    _5103.SynchroniserPartCompoundModalAnalysisAtAStiffness
):
    """SynchroniserSleeveCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserSleeveCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_SynchroniserSleeveCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting SynchroniserSleeveCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "SynchroniserSleeveCompoundModalAnalysisAtAStiffness._Cast_SynchroniserSleeveCompoundModalAnalysisAtAStiffness",
            parent: "SynchroniserSleeveCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserSleeveCompoundModalAnalysisAtAStiffness._Cast_SynchroniserSleeveCompoundModalAnalysisAtAStiffness",
        ) -> "_5103.SynchroniserPartCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5103.SynchroniserPartCompoundModalAnalysisAtAStiffness
            )

        @property
        def coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserSleeveCompoundModalAnalysisAtAStiffness._Cast_SynchroniserSleeveCompoundModalAnalysisAtAStiffness",
        ) -> "_5027.CouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5027,
            )

            return self._parent._cast(
                _5027.CouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserSleeveCompoundModalAnalysisAtAStiffness._Cast_SynchroniserSleeveCompoundModalAnalysisAtAStiffness",
        ) -> "_5065.MountableComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5065,
            )

            return self._parent._cast(
                _5065.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserSleeveCompoundModalAnalysisAtAStiffness._Cast_SynchroniserSleeveCompoundModalAnalysisAtAStiffness",
        ) -> "_5013.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5013,
            )

            return self._parent._cast(_5013.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserSleeveCompoundModalAnalysisAtAStiffness._Cast_SynchroniserSleeveCompoundModalAnalysisAtAStiffness",
        ) -> "_5067.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(_5067.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "SynchroniserSleeveCompoundModalAnalysisAtAStiffness._Cast_SynchroniserSleeveCompoundModalAnalysisAtAStiffness",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserSleeveCompoundModalAnalysisAtAStiffness._Cast_SynchroniserSleeveCompoundModalAnalysisAtAStiffness",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveCompoundModalAnalysisAtAStiffness._Cast_SynchroniserSleeveCompoundModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_stiffness(
            self: "SynchroniserSleeveCompoundModalAnalysisAtAStiffness._Cast_SynchroniserSleeveCompoundModalAnalysisAtAStiffness",
        ) -> "SynchroniserSleeveCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveCompoundModalAnalysisAtAStiffness._Cast_SynchroniserSleeveCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "SynchroniserSleeveCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2606.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

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
    ) -> "List[_4975.SynchroniserSleeveModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.SynchroniserSleeveModalAnalysisAtAStiffness]

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
    ) -> "List[_4975.SynchroniserSleeveModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.SynchroniserSleeveModalAnalysisAtAStiffness]

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
    ) -> "SynchroniserSleeveCompoundModalAnalysisAtAStiffness._Cast_SynchroniserSleeveCompoundModalAnalysisAtAStiffness":
        return self._Cast_SynchroniserSleeveCompoundModalAnalysisAtAStiffness(self)
