"""UnbalancedMassCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5390,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "UnbalancedMassCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2497
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5260,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5345,
        _5293,
        _5347,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="UnbalancedMassCompoundModalAnalysisAtASpeed")


class UnbalancedMassCompoundModalAnalysisAtASpeed(
    _5390.VirtualComponentCompoundModalAnalysisAtASpeed
):
    """UnbalancedMassCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_UnbalancedMassCompoundModalAnalysisAtASpeed"
    )

    class _Cast_UnbalancedMassCompoundModalAnalysisAtASpeed:
        """Special nested class for casting UnbalancedMassCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "UnbalancedMassCompoundModalAnalysisAtASpeed._Cast_UnbalancedMassCompoundModalAnalysisAtASpeed",
            parent: "UnbalancedMassCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_modal_analysis_at_a_speed(
            self: "UnbalancedMassCompoundModalAnalysisAtASpeed._Cast_UnbalancedMassCompoundModalAnalysisAtASpeed",
        ) -> "_5390.VirtualComponentCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5390.VirtualComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "UnbalancedMassCompoundModalAnalysisAtASpeed._Cast_UnbalancedMassCompoundModalAnalysisAtASpeed",
        ) -> "_5345.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5345,
            )

            return self._parent._cast(
                _5345.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "UnbalancedMassCompoundModalAnalysisAtASpeed._Cast_UnbalancedMassCompoundModalAnalysisAtASpeed",
        ) -> "_5293.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5293,
            )

            return self._parent._cast(_5293.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "UnbalancedMassCompoundModalAnalysisAtASpeed._Cast_UnbalancedMassCompoundModalAnalysisAtASpeed",
        ) -> "_5347.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(_5347.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "UnbalancedMassCompoundModalAnalysisAtASpeed._Cast_UnbalancedMassCompoundModalAnalysisAtASpeed",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "UnbalancedMassCompoundModalAnalysisAtASpeed._Cast_UnbalancedMassCompoundModalAnalysisAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassCompoundModalAnalysisAtASpeed._Cast_UnbalancedMassCompoundModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_speed(
            self: "UnbalancedMassCompoundModalAnalysisAtASpeed._Cast_UnbalancedMassCompoundModalAnalysisAtASpeed",
        ) -> "UnbalancedMassCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassCompoundModalAnalysisAtASpeed._Cast_UnbalancedMassCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "UnbalancedMassCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2497.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

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
    ) -> "List[_5260.UnbalancedMassModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.UnbalancedMassModalAnalysisAtASpeed]

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
    ) -> "List[_5260.UnbalancedMassModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.UnbalancedMassModalAnalysisAtASpeed]

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
    ) -> "UnbalancedMassCompoundModalAnalysisAtASpeed._Cast_UnbalancedMassCompoundModalAnalysisAtASpeed":
        return self._Cast_UnbalancedMassCompoundModalAnalysisAtASpeed(self)
