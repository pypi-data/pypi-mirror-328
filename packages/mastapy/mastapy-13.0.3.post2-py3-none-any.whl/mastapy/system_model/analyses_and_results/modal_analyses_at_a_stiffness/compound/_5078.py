"""KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5075,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2558
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4949,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5041,
        _5067,
        _5086,
        _5034,
        _5088,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness"
)


class KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness(
    _5075.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness
):
    """KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = (
        _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
            parent: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
        ) -> (
            "_5075.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness"
        ):
            return self._parent._cast(
                _5075.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5041.ConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5041,
            )

            return self._parent._cast(
                _5041.ConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5067.GearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(_5067.GearCompoundModalAnalysisAtAStiffness)

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5086.MountableComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5086,
            )

            return self._parent._cast(
                _5086.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5034.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5034,
            )

            return self._parent._cast(_5034.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(_5088.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
        ) -> "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2558.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

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
    ) -> "List[_4949.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtAStiffness]

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
    ) -> "List[_4949.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtAStiffness]

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
    ) -> "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness(
            self
        )
