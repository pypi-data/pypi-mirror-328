"""TorqueConverterTurbineModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5155
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "TorqueConverterTurbineModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.static_loads import _6976
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5195,
        _5142,
        _5197,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="TorqueConverterTurbineModalAnalysisAtASpeed")


class TorqueConverterTurbineModalAnalysisAtASpeed(
    _5155.CouplingHalfModalAnalysisAtASpeed
):
    """TorqueConverterTurbineModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineModalAnalysisAtASpeed"
    )

    class _Cast_TorqueConverterTurbineModalAnalysisAtASpeed:
        """Special nested class for casting TorqueConverterTurbineModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
            parent: "TorqueConverterTurbineModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis_at_a_speed(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
        ) -> "_5155.CouplingHalfModalAnalysisAtASpeed":
            return self._parent._cast(_5155.CouplingHalfModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
        ) -> "_5195.MountableComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5195,
            )

            return self._parent._cast(_5195.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
        ) -> "_5142.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5142,
            )

            return self._parent._cast(_5142.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
        ) -> "_5197.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(_5197.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_modal_analysis_at_a_speed(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
        ) -> "TorqueConverterTurbineModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "TorqueConverterTurbineModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2610.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6976.TorqueConverterTurbineLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase

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
    ) -> "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed":
        return self._Cast_TorqueConverterTurbineModalAnalysisAtASpeed(self)
