"""KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4783
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
        "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4666
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4820,
        _4823,
        _4809,
        _4847,
        _4749,
        _4828,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis"
)


class KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis(
    _4783.ConicalGearSetCompoundModalAnalysis
):
    """KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ) -> "_4783.ConicalGearSetCompoundModalAnalysis":
            return self._parent._cast(_4783.ConicalGearSetCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ) -> "_4809.GearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4809,
            )

            return self._parent._cast(_4809.GearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ) -> "_4847.SpecialisedAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4847,
            )

            return self._parent._cast(_4847.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ) -> "_4749.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4749,
            )

            return self._parent._cast(_4749.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ) -> "_4828.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ) -> "_4820.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4820,
            )

            return self._parent._cast(
                _4820.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ) -> "_4823.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4823,
            )

            return self._parent._cast(
                _4823.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4666.KlingelnbergCycloPalloidConicalGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearSetModalAnalysis]

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
    ) -> "List[_4666.KlingelnbergCycloPalloidConicalGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearSetModalAnalysis]

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
    ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis(
            self
        )
