"""WormGearCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5304,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "WormGearCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2551
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5241,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5323,
        _5271,
        _5325,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("WormGearCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="WormGearCompoundModalAnalysisAtASpeed")


class WormGearCompoundModalAnalysisAtASpeed(_5304.GearCompoundModalAnalysisAtASpeed):
    """WormGearCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_WormGearCompoundModalAnalysisAtASpeed"
    )

    class _Cast_WormGearCompoundModalAnalysisAtASpeed:
        """Special nested class for casting WormGearCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "WormGearCompoundModalAnalysisAtASpeed._Cast_WormGearCompoundModalAnalysisAtASpeed",
            parent: "WormGearCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_compound_modal_analysis_at_a_speed(
            self: "WormGearCompoundModalAnalysisAtASpeed._Cast_WormGearCompoundModalAnalysisAtASpeed",
        ) -> "_5304.GearCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5304.GearCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "WormGearCompoundModalAnalysisAtASpeed._Cast_WormGearCompoundModalAnalysisAtASpeed",
        ) -> "_5323.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5323,
            )

            return self._parent._cast(
                _5323.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "WormGearCompoundModalAnalysisAtASpeed._Cast_WormGearCompoundModalAnalysisAtASpeed",
        ) -> "_5271.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5271,
            )

            return self._parent._cast(_5271.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "WormGearCompoundModalAnalysisAtASpeed._Cast_WormGearCompoundModalAnalysisAtASpeed",
        ) -> "_5325.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5325,
            )

            return self._parent._cast(_5325.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "WormGearCompoundModalAnalysisAtASpeed._Cast_WormGearCompoundModalAnalysisAtASpeed",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "WormGearCompoundModalAnalysisAtASpeed._Cast_WormGearCompoundModalAnalysisAtASpeed",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearCompoundModalAnalysisAtASpeed._Cast_WormGearCompoundModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def worm_gear_compound_modal_analysis_at_a_speed(
            self: "WormGearCompoundModalAnalysisAtASpeed._Cast_WormGearCompoundModalAnalysisAtASpeed",
        ) -> "WormGearCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "WormGearCompoundModalAnalysisAtASpeed._Cast_WormGearCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "WormGearCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2551.WormGear":
        """mastapy.system_model.part_model.gears.WormGear

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
    ) -> "List[_5241.WormGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.WormGearModalAnalysisAtASpeed]

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
    ) -> "List[_5241.WormGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.WormGearModalAnalysisAtASpeed]

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
    ) -> "WormGearCompoundModalAnalysisAtASpeed._Cast_WormGearCompoundModalAnalysisAtASpeed":
        return self._Cast_WormGearCompoundModalAnalysisAtASpeed(self)
