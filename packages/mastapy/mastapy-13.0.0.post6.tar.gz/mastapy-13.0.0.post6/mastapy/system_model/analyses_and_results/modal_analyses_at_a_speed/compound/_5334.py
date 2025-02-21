"""PulleyCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5285,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "PulleyCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2590
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5205,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5288,
        _5323,
        _5271,
        _5325,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("PulleyCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="PulleyCompoundModalAnalysisAtASpeed")


class PulleyCompoundModalAnalysisAtASpeed(
    _5285.CouplingHalfCompoundModalAnalysisAtASpeed
):
    """PulleyCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _PULLEY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PulleyCompoundModalAnalysisAtASpeed")

    class _Cast_PulleyCompoundModalAnalysisAtASpeed:
        """Special nested class for casting PulleyCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "PulleyCompoundModalAnalysisAtASpeed._Cast_PulleyCompoundModalAnalysisAtASpeed",
            parent: "PulleyCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(
            self: "PulleyCompoundModalAnalysisAtASpeed._Cast_PulleyCompoundModalAnalysisAtASpeed",
        ) -> "_5285.CouplingHalfCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5285.CouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "PulleyCompoundModalAnalysisAtASpeed._Cast_PulleyCompoundModalAnalysisAtASpeed",
        ) -> "_5323.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5323,
            )

            return self._parent._cast(
                _5323.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "PulleyCompoundModalAnalysisAtASpeed._Cast_PulleyCompoundModalAnalysisAtASpeed",
        ) -> "_5271.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5271,
            )

            return self._parent._cast(_5271.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "PulleyCompoundModalAnalysisAtASpeed._Cast_PulleyCompoundModalAnalysisAtASpeed",
        ) -> "_5325.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5325,
            )

            return self._parent._cast(_5325.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "PulleyCompoundModalAnalysisAtASpeed._Cast_PulleyCompoundModalAnalysisAtASpeed",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PulleyCompoundModalAnalysisAtASpeed._Cast_PulleyCompoundModalAnalysisAtASpeed",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleyCompoundModalAnalysisAtASpeed._Cast_PulleyCompoundModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis_at_a_speed(
            self: "PulleyCompoundModalAnalysisAtASpeed._Cast_PulleyCompoundModalAnalysisAtASpeed",
        ) -> "_5288.CVTPulleyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5288,
            )

            return self._parent._cast(_5288.CVTPulleyCompoundModalAnalysisAtASpeed)

        @property
        def pulley_compound_modal_analysis_at_a_speed(
            self: "PulleyCompoundModalAnalysisAtASpeed._Cast_PulleyCompoundModalAnalysisAtASpeed",
        ) -> "PulleyCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "PulleyCompoundModalAnalysisAtASpeed._Cast_PulleyCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "PulleyCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2590.Pulley":
        """mastapy.system_model.part_model.couplings.Pulley

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
    ) -> "List[_5205.PulleyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.PulleyModalAnalysisAtASpeed]

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
    ) -> "List[_5205.PulleyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.PulleyModalAnalysisAtASpeed]

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
    ) -> (
        "PulleyCompoundModalAnalysisAtASpeed._Cast_PulleyCompoundModalAnalysisAtASpeed"
    ):
        return self._Cast_PulleyCompoundModalAnalysisAtASpeed(self)
