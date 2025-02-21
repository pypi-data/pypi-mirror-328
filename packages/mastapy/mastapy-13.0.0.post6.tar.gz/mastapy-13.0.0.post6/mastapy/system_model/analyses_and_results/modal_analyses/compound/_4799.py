"""KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4793
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
        "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540
    from mastapy.system_model.analyses_and_results.modal_analyses import _4649
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4759,
        _4785,
        _4804,
        _4752,
        _4806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis"
)


class KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis(
    _4793.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
):
    """KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
        ) -> "_4793.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis":
            return self._parent._cast(
                _4793.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
            )

        @property
        def conical_gear_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
        ) -> "_4759.ConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4759,
            )

            return self._parent._cast(_4759.ConicalGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
        ) -> "_4785.GearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
        ) -> "_4804.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
        ) -> "_4752.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4752,
            )

            return self._parent._cast(_4752.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
        ) -> "_4806.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4806,
            )

            return self._parent._cast(_4806.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2540.KlingelnbergCycloPalloidSpiralBevelGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear

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
    ) -> "List[_4649.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis]

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
    ) -> "List[_4649.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis]

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis(
            self
        )
