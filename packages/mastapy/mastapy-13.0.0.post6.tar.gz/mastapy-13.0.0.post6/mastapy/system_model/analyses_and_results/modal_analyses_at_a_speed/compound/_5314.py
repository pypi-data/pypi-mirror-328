"""KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5280,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
        "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5184,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5317,
        _5320,
        _5306,
        _5344,
        _5246,
        _5325,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed"
)


class KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed(
    _5280.ConicalGearSetCompoundModalAnalysisAtASpeed
):
    """KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = (
        _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
            parent: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5280.ConicalGearSetCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5280.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5306.GearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5306,
            )

            return self._parent._cast(_5306.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5344.SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5344,
            )

            return self._parent._cast(
                _5344.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5246.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5246,
            )

            return self._parent._cast(
                _5246.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5325.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5325,
            )

            return self._parent._cast(_5325.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5317.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5317,
            )

            return self._parent._cast(
                _5317.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5320.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5320,
            )

            return self._parent._cast(
                _5320.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5184.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5184.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed(
            self
        )
