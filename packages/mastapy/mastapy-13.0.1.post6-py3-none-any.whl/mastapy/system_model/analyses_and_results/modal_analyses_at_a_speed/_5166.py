"""CylindricalGearSetModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5177
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "CylindricalGearSetModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526
    from mastapy.system_model.analyses_and_results.static_loads import _6866
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5165,
        _5164,
        _5202,
        _5216,
        _5117,
        _5197,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CylindricalGearSetModalAnalysisAtASpeed")


class CylindricalGearSetModalAnalysisAtASpeed(_5177.GearSetModalAnalysisAtASpeed):
    """CylindricalGearSetModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSetModalAnalysisAtASpeed"
    )

    class _Cast_CylindricalGearSetModalAnalysisAtASpeed:
        """Special nested class for casting CylindricalGearSetModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CylindricalGearSetModalAnalysisAtASpeed._Cast_CylindricalGearSetModalAnalysisAtASpeed",
            parent: "CylindricalGearSetModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "CylindricalGearSetModalAnalysisAtASpeed._Cast_CylindricalGearSetModalAnalysisAtASpeed",
        ) -> "_5177.GearSetModalAnalysisAtASpeed":
            return self._parent._cast(_5177.GearSetModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "CylindricalGearSetModalAnalysisAtASpeed._Cast_CylindricalGearSetModalAnalysisAtASpeed",
        ) -> "_5216.SpecialisedAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5216,
            )

            return self._parent._cast(_5216.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "CylindricalGearSetModalAnalysisAtASpeed._Cast_CylindricalGearSetModalAnalysisAtASpeed",
        ) -> "_5117.AbstractAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5117,
            )

            return self._parent._cast(_5117.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "CylindricalGearSetModalAnalysisAtASpeed._Cast_CylindricalGearSetModalAnalysisAtASpeed",
        ) -> "_5197.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(_5197.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearSetModalAnalysisAtASpeed._Cast_CylindricalGearSetModalAnalysisAtASpeed",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSetModalAnalysisAtASpeed._Cast_CylindricalGearSetModalAnalysisAtASpeed",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSetModalAnalysisAtASpeed._Cast_CylindricalGearSetModalAnalysisAtASpeed",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSetModalAnalysisAtASpeed._Cast_CylindricalGearSetModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetModalAnalysisAtASpeed._Cast_CylindricalGearSetModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_gear_set_modal_analysis_at_a_speed(
            self: "CylindricalGearSetModalAnalysisAtASpeed._Cast_CylindricalGearSetModalAnalysisAtASpeed",
        ) -> "_5202.PlanetaryGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5202,
            )

            return self._parent._cast(_5202.PlanetaryGearSetModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_speed(
            self: "CylindricalGearSetModalAnalysisAtASpeed._Cast_CylindricalGearSetModalAnalysisAtASpeed",
        ) -> "CylindricalGearSetModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetModalAnalysisAtASpeed._Cast_CylindricalGearSetModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "CylindricalGearSetModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2526.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6866.CylindricalGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gears_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5165.CylindricalGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CylindricalGearModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5164.CylindricalGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CylindricalGearMeshModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetModalAnalysisAtASpeed._Cast_CylindricalGearSetModalAnalysisAtASpeed":
        return self._Cast_CylindricalGearSetModalAnalysisAtASpeed(self)
