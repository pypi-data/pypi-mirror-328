"""PowerLoadCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5390,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "PowerLoadCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2492
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5226,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5345,
        _5293,
        _5347,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="PowerLoadCompoundModalAnalysisAtASpeed")


class PowerLoadCompoundModalAnalysisAtASpeed(
    _5390.VirtualComponentCompoundModalAnalysisAtASpeed
):
    """PowerLoadCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PowerLoadCompoundModalAnalysisAtASpeed"
    )

    class _Cast_PowerLoadCompoundModalAnalysisAtASpeed:
        """Special nested class for casting PowerLoadCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "PowerLoadCompoundModalAnalysisAtASpeed._Cast_PowerLoadCompoundModalAnalysisAtASpeed",
            parent: "PowerLoadCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_modal_analysis_at_a_speed(
            self: "PowerLoadCompoundModalAnalysisAtASpeed._Cast_PowerLoadCompoundModalAnalysisAtASpeed",
        ) -> "_5390.VirtualComponentCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5390.VirtualComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "PowerLoadCompoundModalAnalysisAtASpeed._Cast_PowerLoadCompoundModalAnalysisAtASpeed",
        ) -> "_5345.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5345,
            )

            return self._parent._cast(
                _5345.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "PowerLoadCompoundModalAnalysisAtASpeed._Cast_PowerLoadCompoundModalAnalysisAtASpeed",
        ) -> "_5293.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5293,
            )

            return self._parent._cast(_5293.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "PowerLoadCompoundModalAnalysisAtASpeed._Cast_PowerLoadCompoundModalAnalysisAtASpeed",
        ) -> "_5347.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(_5347.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "PowerLoadCompoundModalAnalysisAtASpeed._Cast_PowerLoadCompoundModalAnalysisAtASpeed",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PowerLoadCompoundModalAnalysisAtASpeed._Cast_PowerLoadCompoundModalAnalysisAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadCompoundModalAnalysisAtASpeed._Cast_PowerLoadCompoundModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def power_load_compound_modal_analysis_at_a_speed(
            self: "PowerLoadCompoundModalAnalysisAtASpeed._Cast_PowerLoadCompoundModalAnalysisAtASpeed",
        ) -> "PowerLoadCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "PowerLoadCompoundModalAnalysisAtASpeed._Cast_PowerLoadCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "PowerLoadCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2492.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

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
    ) -> "List[_5226.PowerLoadModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.PowerLoadModalAnalysisAtASpeed]

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
    ) -> "List[_5226.PowerLoadModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.PowerLoadModalAnalysisAtASpeed]

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
    ) -> "PowerLoadCompoundModalAnalysisAtASpeed._Cast_PowerLoadCompoundModalAnalysisAtASpeed":
        return self._Cast_PowerLoadCompoundModalAnalysisAtASpeed(self)
