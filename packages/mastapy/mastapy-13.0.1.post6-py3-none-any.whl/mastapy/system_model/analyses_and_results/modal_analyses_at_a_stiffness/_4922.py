"""HypoidGearSetModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4863,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "HypoidGearSetModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2535
    from mastapy.system_model.analyses_and_results.static_loads import _6908
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4921,
        _4920,
        _4891,
        _4918,
        _4957,
        _4857,
        _4938,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="HypoidGearSetModalAnalysisAtAStiffness")


class HypoidGearSetModalAnalysisAtAStiffness(
    _4863.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness
):
    """HypoidGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearSetModalAnalysisAtAStiffness"
    )

    class _Cast_HypoidGearSetModalAnalysisAtAStiffness:
        """Special nested class for casting HypoidGearSetModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
            parent: "HypoidGearSetModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_4863.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4863.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_4891.ConicalGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4891,
            )

            return self._parent._cast(_4891.ConicalGearSetModalAnalysisAtAStiffness)

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_4918.GearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4918,
            )

            return self._parent._cast(_4918.GearSetModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_4957.SpecialisedAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4957,
            )

            return self._parent._cast(
                _4957.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_4857.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4857,
            )

            return self._parent._cast(_4857.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_4938.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(_4938.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
        ) -> "HypoidGearSetModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "HypoidGearSetModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2535.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6908.HypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hypoid_gears_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4921.HypoidGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.HypoidGearModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4920.HypoidGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.HypoidGearMeshModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearSetModalAnalysisAtAStiffness._Cast_HypoidGearSetModalAnalysisAtAStiffness":
        return self._Cast_HypoidGearSetModalAnalysisAtAStiffness(self)
