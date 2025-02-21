"""ZerolBevelGearCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5004,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "ZerolBevelGearCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2553
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4986,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _4992,
        _5020,
        _5046,
        _5065,
        _5013,
        _5067,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ZerolBevelGearCompoundModalAnalysisAtAStiffness")


class ZerolBevelGearCompoundModalAnalysisAtAStiffness(
    _5004.BevelGearCompoundModalAnalysisAtAStiffness
):
    """ZerolBevelGearCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_ZerolBevelGearCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting ZerolBevelGearCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ZerolBevelGearCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearCompoundModalAnalysisAtAStiffness",
            parent: "ZerolBevelGearCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5004.BevelGearCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(_5004.BevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_4992.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4992,
            )

            return self._parent._cast(
                _4992.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5020.ConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5020,
            )

            return self._parent._cast(
                _5020.ConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5046.GearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5046,
            )

            return self._parent._cast(_5046.GearCompoundModalAnalysisAtAStiffness)

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5065.MountableComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5065,
            )

            return self._parent._cast(
                _5065.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5013.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5013,
            )

            return self._parent._cast(_5013.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5067.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(_5067.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "ZerolBevelGearCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "ZerolBevelGearCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearCompoundModalAnalysisAtAStiffness",
        ) -> "ZerolBevelGearCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "ZerolBevelGearCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2553.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

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
    ) -> "List[_4986.ZerolBevelGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ZerolBevelGearModalAnalysisAtAStiffness]

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
    ) -> "List[_4986.ZerolBevelGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ZerolBevelGearModalAnalysisAtAStiffness]

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
    ) -> "ZerolBevelGearCompoundModalAnalysisAtAStiffness._Cast_ZerolBevelGearCompoundModalAnalysisAtAStiffness":
        return self._Cast_ZerolBevelGearCompoundModalAnalysisAtAStiffness(self)
