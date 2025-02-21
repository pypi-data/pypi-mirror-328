"""SpiralBevelGearCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5003,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "SpiralBevelGearCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4958,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _4991,
        _5019,
        _5045,
        _5064,
        _5012,
        _5066,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="SpiralBevelGearCompoundModalAnalysisAtAStiffness")


class SpiralBevelGearCompoundModalAnalysisAtAStiffness(
    _5003.BevelGearCompoundModalAnalysisAtAStiffness
):
    """SpiralBevelGearCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_SpiralBevelGearCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting SpiralBevelGearCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "SpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_SpiralBevelGearCompoundModalAnalysisAtAStiffness",
            parent: "SpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "SpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_SpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5003.BevelGearCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(_5003.BevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "SpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_SpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_4991.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4991,
            )

            return self._parent._cast(
                _4991.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "SpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_SpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5019.ConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5019,
            )

            return self._parent._cast(
                _5019.ConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "SpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_SpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5045.GearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5045,
            )

            return self._parent._cast(_5045.GearCompoundModalAnalysisAtAStiffness)

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "SpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_SpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5064.MountableComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5064,
            )

            return self._parent._cast(
                _5064.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "SpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_SpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5012.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5012,
            )

            return self._parent._cast(_5012.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "SpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_SpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5066.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5066,
            )

            return self._parent._cast(_5066.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "SpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_SpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_SpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_SpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "SpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_SpiralBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "SpiralBevelGearCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_SpiralBevelGearCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "SpiralBevelGearCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2543.SpiralBevelGear":
        """mastapy.system_model.part_model.gears.SpiralBevelGear

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
    ) -> "List[_4958.SpiralBevelGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.SpiralBevelGearModalAnalysisAtAStiffness]

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
    ) -> "List[_4958.SpiralBevelGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.SpiralBevelGearModalAnalysisAtAStiffness]

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
    ) -> "SpiralBevelGearCompoundModalAnalysisAtAStiffness._Cast_SpiralBevelGearCompoundModalAnalysisAtAStiffness":
        return self._Cast_SpiralBevelGearCompoundModalAnalysisAtAStiffness(self)
