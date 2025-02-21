"""FlexiblePinAssemblyModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5216
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "FlexiblePinAssemblyModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.static_loads import _6889
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5117,
        _5197,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyModalAnalysisAtASpeed")


class FlexiblePinAssemblyModalAnalysisAtASpeed(
    _5216.SpecialisedAssemblyModalAnalysisAtASpeed
):
    """FlexiblePinAssemblyModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FlexiblePinAssemblyModalAnalysisAtASpeed"
    )

    class _Cast_FlexiblePinAssemblyModalAnalysisAtASpeed:
        """Special nested class for casting FlexiblePinAssemblyModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyModalAnalysisAtASpeed._Cast_FlexiblePinAssemblyModalAnalysisAtASpeed",
            parent: "FlexiblePinAssemblyModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "FlexiblePinAssemblyModalAnalysisAtASpeed._Cast_FlexiblePinAssemblyModalAnalysisAtASpeed",
        ) -> "_5216.SpecialisedAssemblyModalAnalysisAtASpeed":
            return self._parent._cast(_5216.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "FlexiblePinAssemblyModalAnalysisAtASpeed._Cast_FlexiblePinAssemblyModalAnalysisAtASpeed",
        ) -> "_5117.AbstractAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5117,
            )

            return self._parent._cast(_5117.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "FlexiblePinAssemblyModalAnalysisAtASpeed._Cast_FlexiblePinAssemblyModalAnalysisAtASpeed",
        ) -> "_5197.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(_5197.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "FlexiblePinAssemblyModalAnalysisAtASpeed._Cast_FlexiblePinAssemblyModalAnalysisAtASpeed",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FlexiblePinAssemblyModalAnalysisAtASpeed._Cast_FlexiblePinAssemblyModalAnalysisAtASpeed",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FlexiblePinAssemblyModalAnalysisAtASpeed._Cast_FlexiblePinAssemblyModalAnalysisAtASpeed",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FlexiblePinAssemblyModalAnalysisAtASpeed._Cast_FlexiblePinAssemblyModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyModalAnalysisAtASpeed._Cast_FlexiblePinAssemblyModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_speed(
            self: "FlexiblePinAssemblyModalAnalysisAtASpeed._Cast_FlexiblePinAssemblyModalAnalysisAtASpeed",
        ) -> "FlexiblePinAssemblyModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyModalAnalysisAtASpeed._Cast_FlexiblePinAssemblyModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "FlexiblePinAssemblyModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2454.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6889.FlexiblePinAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "FlexiblePinAssemblyModalAnalysisAtASpeed._Cast_FlexiblePinAssemblyModalAnalysisAtASpeed":
        return self._Cast_FlexiblePinAssemblyModalAnalysisAtASpeed(self)
