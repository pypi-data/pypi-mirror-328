"""MassDiscCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5109,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "MassDiscCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4932,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5064,
        _5012,
        _5066,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="MassDiscCompoundModalAnalysisAtAStiffness")


class MassDiscCompoundModalAnalysisAtAStiffness(
    _5109.VirtualComponentCompoundModalAnalysisAtAStiffness
):
    """MassDiscCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MassDiscCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_MassDiscCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting MassDiscCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "MassDiscCompoundModalAnalysisAtAStiffness._Cast_MassDiscCompoundModalAnalysisAtAStiffness",
            parent: "MassDiscCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_modal_analysis_at_a_stiffness(
            self: "MassDiscCompoundModalAnalysisAtAStiffness._Cast_MassDiscCompoundModalAnalysisAtAStiffness",
        ) -> "_5109.VirtualComponentCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5109.VirtualComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "MassDiscCompoundModalAnalysisAtAStiffness._Cast_MassDiscCompoundModalAnalysisAtAStiffness",
        ) -> "_5064.MountableComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5064,
            )

            return self._parent._cast(
                _5064.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "MassDiscCompoundModalAnalysisAtAStiffness._Cast_MassDiscCompoundModalAnalysisAtAStiffness",
        ) -> "_5012.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5012,
            )

            return self._parent._cast(_5012.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "MassDiscCompoundModalAnalysisAtAStiffness._Cast_MassDiscCompoundModalAnalysisAtAStiffness",
        ) -> "_5066.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5066,
            )

            return self._parent._cast(_5066.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "MassDiscCompoundModalAnalysisAtAStiffness._Cast_MassDiscCompoundModalAnalysisAtAStiffness",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MassDiscCompoundModalAnalysisAtAStiffness._Cast_MassDiscCompoundModalAnalysisAtAStiffness",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscCompoundModalAnalysisAtAStiffness._Cast_MassDiscCompoundModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def mass_disc_compound_modal_analysis_at_a_stiffness(
            self: "MassDiscCompoundModalAnalysisAtAStiffness._Cast_MassDiscCompoundModalAnalysisAtAStiffness",
        ) -> "MassDiscCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "MassDiscCompoundModalAnalysisAtAStiffness._Cast_MassDiscCompoundModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "MassDiscCompoundModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2462.MassDisc":
        """mastapy.system_model.part_model.MassDisc

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
    ) -> "List[_4932.MassDiscModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.MassDiscModalAnalysisAtAStiffness]

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
    def planetaries(self: Self) -> "List[MassDiscCompoundModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound.MassDiscCompoundModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4932.MassDiscModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.MassDiscModalAnalysisAtAStiffness]

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
    ) -> "MassDiscCompoundModalAnalysisAtAStiffness._Cast_MassDiscCompoundModalAnalysisAtAStiffness":
        return self._Cast_MassDiscCompoundModalAnalysisAtAStiffness(self)
