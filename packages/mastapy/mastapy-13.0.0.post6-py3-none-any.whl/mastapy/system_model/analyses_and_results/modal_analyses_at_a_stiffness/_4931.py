"""KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4925,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
        "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.static_loads import _6920
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4930,
        _4929,
        _4890,
        _4917,
        _4956,
        _4856,
        _4937,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness"
)


class KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness(
    _4925.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = (
        _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4925.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4925.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4890.ConicalGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4890,
            )

            return self._parent._cast(_4890.ConicalGearSetModalAnalysisAtAStiffness)

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4917.GearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4917,
            )

            return self._parent._cast(_4917.GearSetModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4956.SpecialisedAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4956,
            )

            return self._parent._cast(
                _4956.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4856.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4856,
            )

            return self._parent._cast(_4856.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_4937.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4937,
            )

            return self._parent._cast(_4937.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(
        self: Self,
    ) -> "_2541.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(
        self: Self,
    ) -> "_6920.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4930.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsModalAnalysisAtAStiffness
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4929.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesModalAnalysisAtAStiffness
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness(
            self
        )
