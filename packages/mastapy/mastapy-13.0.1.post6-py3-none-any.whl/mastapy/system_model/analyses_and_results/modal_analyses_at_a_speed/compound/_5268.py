"""ClutchCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5284,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "ClutchCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2578
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5140,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5345,
        _5247,
        _5326,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ClutchCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ClutchCompoundModalAnalysisAtASpeed")


class ClutchCompoundModalAnalysisAtASpeed(_5284.CouplingCompoundModalAnalysisAtASpeed):
    """ClutchCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CLUTCH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchCompoundModalAnalysisAtASpeed")

    class _Cast_ClutchCompoundModalAnalysisAtASpeed:
        """Special nested class for casting ClutchCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ClutchCompoundModalAnalysisAtASpeed._Cast_ClutchCompoundModalAnalysisAtASpeed",
            parent: "ClutchCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_compound_modal_analysis_at_a_speed(
            self: "ClutchCompoundModalAnalysisAtASpeed._Cast_ClutchCompoundModalAnalysisAtASpeed",
        ) -> "_5284.CouplingCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5284.CouplingCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "ClutchCompoundModalAnalysisAtASpeed._Cast_ClutchCompoundModalAnalysisAtASpeed",
        ) -> "_5345.SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5345,
            )

            return self._parent._cast(
                _5345.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "ClutchCompoundModalAnalysisAtASpeed._Cast_ClutchCompoundModalAnalysisAtASpeed",
        ) -> "_5247.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5247,
            )

            return self._parent._cast(
                _5247.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "ClutchCompoundModalAnalysisAtASpeed._Cast_ClutchCompoundModalAnalysisAtASpeed",
        ) -> "_5326.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5326,
            )

            return self._parent._cast(_5326.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "ClutchCompoundModalAnalysisAtASpeed._Cast_ClutchCompoundModalAnalysisAtASpeed",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchCompoundModalAnalysisAtASpeed._Cast_ClutchCompoundModalAnalysisAtASpeed",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchCompoundModalAnalysisAtASpeed._Cast_ClutchCompoundModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_compound_modal_analysis_at_a_speed(
            self: "ClutchCompoundModalAnalysisAtASpeed._Cast_ClutchCompoundModalAnalysisAtASpeed",
        ) -> "ClutchCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ClutchCompoundModalAnalysisAtASpeed._Cast_ClutchCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "ClutchCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2578.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2578.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5140.ClutchModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ClutchModalAnalysisAtASpeed]

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
    ) -> "List[_5140.ClutchModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ClutchModalAnalysisAtASpeed]

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
        "ClutchCompoundModalAnalysisAtASpeed._Cast_ClutchCompoundModalAnalysisAtASpeed"
    ):
        return self._Cast_ClutchCompoundModalAnalysisAtASpeed(self)
