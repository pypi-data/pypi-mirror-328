"""PointLoadModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5240
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "PointLoadModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.static_loads import _6939
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5195,
        _5142,
        _5197,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="PointLoadModalAnalysisAtASpeed")


class PointLoadModalAnalysisAtASpeed(_5240.VirtualComponentModalAnalysisAtASpeed):
    """PointLoadModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointLoadModalAnalysisAtASpeed")

    class _Cast_PointLoadModalAnalysisAtASpeed:
        """Special nested class for casting PointLoadModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "PointLoadModalAnalysisAtASpeed._Cast_PointLoadModalAnalysisAtASpeed",
            parent: "PointLoadModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def virtual_component_modal_analysis_at_a_speed(
            self: "PointLoadModalAnalysisAtASpeed._Cast_PointLoadModalAnalysisAtASpeed",
        ) -> "_5240.VirtualComponentModalAnalysisAtASpeed":
            return self._parent._cast(_5240.VirtualComponentModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "PointLoadModalAnalysisAtASpeed._Cast_PointLoadModalAnalysisAtASpeed",
        ) -> "_5195.MountableComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5195,
            )

            return self._parent._cast(_5195.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "PointLoadModalAnalysisAtASpeed._Cast_PointLoadModalAnalysisAtASpeed",
        ) -> "_5142.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5142,
            )

            return self._parent._cast(_5142.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "PointLoadModalAnalysisAtASpeed._Cast_PointLoadModalAnalysisAtASpeed",
        ) -> "_5197.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(_5197.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "PointLoadModalAnalysisAtASpeed._Cast_PointLoadModalAnalysisAtASpeed",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PointLoadModalAnalysisAtASpeed._Cast_PointLoadModalAnalysisAtASpeed",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PointLoadModalAnalysisAtASpeed._Cast_PointLoadModalAnalysisAtASpeed",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PointLoadModalAnalysisAtASpeed._Cast_PointLoadModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PointLoadModalAnalysisAtASpeed._Cast_PointLoadModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def point_load_modal_analysis_at_a_speed(
            self: "PointLoadModalAnalysisAtASpeed._Cast_PointLoadModalAnalysisAtASpeed",
        ) -> "PointLoadModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "PointLoadModalAnalysisAtASpeed._Cast_PointLoadModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PointLoadModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2471.PointLoad":
        """mastapy.system_model.part_model.PointLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6939.PointLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase

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
    ) -> "PointLoadModalAnalysisAtASpeed._Cast_PointLoadModalAnalysisAtASpeed":
        return self._Cast_PointLoadModalAnalysisAtASpeed(self)
