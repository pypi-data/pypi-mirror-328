"""MeasurementComponentModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4981,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "MeasurementComponentModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2463
    from mastapy.system_model.analyses_and_results.static_loads import _6923
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4936,
        _4882,
        _4938,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="MeasurementComponentModalAnalysisAtAStiffness")


class MeasurementComponentModalAnalysisAtAStiffness(
    _4981.VirtualComponentModalAnalysisAtAStiffness
):
    """MeasurementComponentModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MeasurementComponentModalAnalysisAtAStiffness"
    )

    class _Cast_MeasurementComponentModalAnalysisAtAStiffness:
        """Special nested class for casting MeasurementComponentModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "MeasurementComponentModalAnalysisAtAStiffness._Cast_MeasurementComponentModalAnalysisAtAStiffness",
            parent: "MeasurementComponentModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def virtual_component_modal_analysis_at_a_stiffness(
            self: "MeasurementComponentModalAnalysisAtAStiffness._Cast_MeasurementComponentModalAnalysisAtAStiffness",
        ) -> "_4981.VirtualComponentModalAnalysisAtAStiffness":
            return self._parent._cast(_4981.VirtualComponentModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "MeasurementComponentModalAnalysisAtAStiffness._Cast_MeasurementComponentModalAnalysisAtAStiffness",
        ) -> "_4936.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4936,
            )

            return self._parent._cast(_4936.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "MeasurementComponentModalAnalysisAtAStiffness._Cast_MeasurementComponentModalAnalysisAtAStiffness",
        ) -> "_4882.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4882,
            )

            return self._parent._cast(_4882.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "MeasurementComponentModalAnalysisAtAStiffness._Cast_MeasurementComponentModalAnalysisAtAStiffness",
        ) -> "_4938.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(_4938.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "MeasurementComponentModalAnalysisAtAStiffness._Cast_MeasurementComponentModalAnalysisAtAStiffness",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MeasurementComponentModalAnalysisAtAStiffness._Cast_MeasurementComponentModalAnalysisAtAStiffness",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MeasurementComponentModalAnalysisAtAStiffness._Cast_MeasurementComponentModalAnalysisAtAStiffness",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MeasurementComponentModalAnalysisAtAStiffness._Cast_MeasurementComponentModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentModalAnalysisAtAStiffness._Cast_MeasurementComponentModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def measurement_component_modal_analysis_at_a_stiffness(
            self: "MeasurementComponentModalAnalysisAtAStiffness._Cast_MeasurementComponentModalAnalysisAtAStiffness",
        ) -> "MeasurementComponentModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentModalAnalysisAtAStiffness._Cast_MeasurementComponentModalAnalysisAtAStiffness",
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
        instance_to_wrap: "MeasurementComponentModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2463.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6923.MeasurementComponentLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase

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
    ) -> "MeasurementComponentModalAnalysisAtAStiffness._Cast_MeasurementComponentModalAnalysisAtAStiffness":
        return self._Cast_MeasurementComponentModalAnalysisAtAStiffness(self)
