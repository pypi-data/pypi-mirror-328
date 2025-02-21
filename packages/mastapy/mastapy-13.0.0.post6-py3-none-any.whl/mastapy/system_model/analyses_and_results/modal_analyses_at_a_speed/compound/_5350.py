"""SpringDamperHalfCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5285,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "SpringDamperHalfCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2601
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5220,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5323,
        _5271,
        _5325,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="SpringDamperHalfCompoundModalAnalysisAtASpeed")


class SpringDamperHalfCompoundModalAnalysisAtASpeed(
    _5285.CouplingHalfCompoundModalAnalysisAtASpeed
):
    """SpringDamperHalfCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed"
    )

    class _Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed:
        """Special nested class for casting SpringDamperHalfCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed",
            parent: "SpringDamperHalfCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(
            self: "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5285.CouplingHalfCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5285.CouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5323.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5323,
            )

            return self._parent._cast(
                _5323.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5271.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5271,
            )

            return self._parent._cast(_5271.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5325.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5325,
            )

            return self._parent._cast(_5325.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spring_damper_half_compound_modal_analysis_at_a_speed(
            self: "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed",
        ) -> "SpringDamperHalfCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "SpringDamperHalfCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2601.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

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
    ) -> "List[_5220.SpringDamperHalfModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SpringDamperHalfModalAnalysisAtASpeed]

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
    ) -> "List[_5220.SpringDamperHalfModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SpringDamperHalfModalAnalysisAtASpeed]

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
    ) -> "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed":
        return self._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed(self)
