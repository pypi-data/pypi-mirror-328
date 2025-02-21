"""StraightBevelSunGearCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5352,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "StraightBevelSunGearCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5230,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5263,
        _5251,
        _5279,
        _5305,
        _5324,
        _5272,
        _5326,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="StraightBevelSunGearCompoundModalAnalysisAtASpeed")


class StraightBevelSunGearCompoundModalAnalysisAtASpeed(
    _5352.StraightBevelDiffGearCompoundModalAnalysisAtASpeed
):
    """StraightBevelSunGearCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed"
    )

    class _Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed:
        """Special nested class for casting StraightBevelSunGearCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "StraightBevelSunGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed",
            parent: "StraightBevelSunGearCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed",
        ) -> "_5352.StraightBevelDiffGearCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5352.StraightBevelDiffGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed",
        ) -> "_5263.BevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5263,
            )

            return self._parent._cast(_5263.BevelGearCompoundModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed",
        ) -> "_5251.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5251,
            )

            return self._parent._cast(
                _5251.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed",
        ) -> "_5279.ConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5279,
            )

            return self._parent._cast(_5279.ConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def gear_compound_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed",
        ) -> "_5305.GearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5305,
            )

            return self._parent._cast(_5305.GearCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed",
        ) -> "_5324.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5324,
            )

            return self._parent._cast(
                _5324.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed",
        ) -> "_5272.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5272,
            )

            return self._parent._cast(_5272.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed",
        ) -> "_5326.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5326,
            )

            return self._parent._cast(_5326.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "StraightBevelSunGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelSunGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed",
        ) -> "StraightBevelSunGearCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "StraightBevelSunGearCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5230.StraightBevelSunGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.StraightBevelSunGearModalAnalysisAtASpeed]

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
    ) -> "List[_5230.StraightBevelSunGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.StraightBevelSunGearModalAnalysisAtASpeed]

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
    ) -> "StraightBevelSunGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed":
        return self._Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed(self)
