"""CycloidalDiscModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5139
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "CycloidalDiscModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2589
    from mastapy.system_model.analyses_and_results.static_loads import _6881
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5140,
        _5163,
        _5218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CycloidalDiscModalAnalysisAtASpeed")


class CycloidalDiscModalAnalysisAtASpeed(_5139.AbstractShaftModalAnalysisAtASpeed):
    """CycloidalDiscModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscModalAnalysisAtASpeed")

    class _Cast_CycloidalDiscModalAnalysisAtASpeed:
        """Special nested class for casting CycloidalDiscModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CycloidalDiscModalAnalysisAtASpeed._Cast_CycloidalDiscModalAnalysisAtASpeed",
            parent: "CycloidalDiscModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def abstract_shaft_modal_analysis_at_a_speed(
            self: "CycloidalDiscModalAnalysisAtASpeed._Cast_CycloidalDiscModalAnalysisAtASpeed",
        ) -> "_5139.AbstractShaftModalAnalysisAtASpeed":
            return self._parent._cast(_5139.AbstractShaftModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_speed(
            self: "CycloidalDiscModalAnalysisAtASpeed._Cast_CycloidalDiscModalAnalysisAtASpeed",
        ) -> "_5140.AbstractShaftOrHousingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5140,
            )

            return self._parent._cast(_5140.AbstractShaftOrHousingModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "CycloidalDiscModalAnalysisAtASpeed._Cast_CycloidalDiscModalAnalysisAtASpeed",
        ) -> "_5163.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5163,
            )

            return self._parent._cast(_5163.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "CycloidalDiscModalAnalysisAtASpeed._Cast_CycloidalDiscModalAnalysisAtASpeed",
        ) -> "_5218.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5218,
            )

            return self._parent._cast(_5218.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalDiscModalAnalysisAtASpeed._Cast_CycloidalDiscModalAnalysisAtASpeed",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscModalAnalysisAtASpeed._Cast_CycloidalDiscModalAnalysisAtASpeed",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscModalAnalysisAtASpeed._Cast_CycloidalDiscModalAnalysisAtASpeed",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscModalAnalysisAtASpeed._Cast_CycloidalDiscModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscModalAnalysisAtASpeed._Cast_CycloidalDiscModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_modal_analysis_at_a_speed(
            self: "CycloidalDiscModalAnalysisAtASpeed._Cast_CycloidalDiscModalAnalysisAtASpeed",
        ) -> "CycloidalDiscModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscModalAnalysisAtASpeed._Cast_CycloidalDiscModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "CycloidalDiscModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2589.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6881.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

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
    ) -> "CycloidalDiscModalAnalysisAtASpeed._Cast_CycloidalDiscModalAnalysisAtASpeed":
        return self._Cast_CycloidalDiscModalAnalysisAtASpeed(self)
