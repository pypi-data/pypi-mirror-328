"""RingPinsModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4936,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "RingPinsModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2570
    from mastapy.system_model.analyses_and_results.static_loads import _6944
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4882,
        _4938,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="RingPinsModalAnalysisAtAStiffness")


class RingPinsModalAnalysisAtAStiffness(
    _4936.MountableComponentModalAnalysisAtAStiffness
):
    """RingPinsModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _RING_PINS_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsModalAnalysisAtAStiffness")

    class _Cast_RingPinsModalAnalysisAtAStiffness:
        """Special nested class for casting RingPinsModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "RingPinsModalAnalysisAtAStiffness._Cast_RingPinsModalAnalysisAtAStiffness",
            parent: "RingPinsModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "RingPinsModalAnalysisAtAStiffness._Cast_RingPinsModalAnalysisAtAStiffness",
        ) -> "_4936.MountableComponentModalAnalysisAtAStiffness":
            return self._parent._cast(_4936.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "RingPinsModalAnalysisAtAStiffness._Cast_RingPinsModalAnalysisAtAStiffness",
        ) -> "_4882.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4882,
            )

            return self._parent._cast(_4882.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "RingPinsModalAnalysisAtAStiffness._Cast_RingPinsModalAnalysisAtAStiffness",
        ) -> "_4938.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(_4938.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "RingPinsModalAnalysisAtAStiffness._Cast_RingPinsModalAnalysisAtAStiffness",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RingPinsModalAnalysisAtAStiffness._Cast_RingPinsModalAnalysisAtAStiffness",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RingPinsModalAnalysisAtAStiffness._Cast_RingPinsModalAnalysisAtAStiffness",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsModalAnalysisAtAStiffness._Cast_RingPinsModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsModalAnalysisAtAStiffness._Cast_RingPinsModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def ring_pins_modal_analysis_at_a_stiffness(
            self: "RingPinsModalAnalysisAtAStiffness._Cast_RingPinsModalAnalysisAtAStiffness",
        ) -> "RingPinsModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "RingPinsModalAnalysisAtAStiffness._Cast_RingPinsModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "RingPinsModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2570.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6944.RingPinsLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RingPinsModalAnalysisAtAStiffness._Cast_RingPinsModalAnalysisAtAStiffness":
        return self._Cast_RingPinsModalAnalysisAtAStiffness(self)
