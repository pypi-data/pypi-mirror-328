"""AbstractShaftModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5140
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "AbstractShaftModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5183,
        _5235,
        _5163,
        _5218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AbstractShaftModalAnalysisAtASpeed")


class AbstractShaftModalAnalysisAtASpeed(
    _5140.AbstractShaftOrHousingModalAnalysisAtASpeed
):
    """AbstractShaftModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftModalAnalysisAtASpeed")

    class _Cast_AbstractShaftModalAnalysisAtASpeed:
        """Special nested class for casting AbstractShaftModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AbstractShaftModalAnalysisAtASpeed._Cast_AbstractShaftModalAnalysisAtASpeed",
            parent: "AbstractShaftModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_speed(
            self: "AbstractShaftModalAnalysisAtASpeed._Cast_AbstractShaftModalAnalysisAtASpeed",
        ) -> "_5140.AbstractShaftOrHousingModalAnalysisAtASpeed":
            return self._parent._cast(_5140.AbstractShaftOrHousingModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "AbstractShaftModalAnalysisAtASpeed._Cast_AbstractShaftModalAnalysisAtASpeed",
        ) -> "_5163.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5163,
            )

            return self._parent._cast(_5163.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "AbstractShaftModalAnalysisAtASpeed._Cast_AbstractShaftModalAnalysisAtASpeed",
        ) -> "_5218.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5218,
            )

            return self._parent._cast(_5218.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftModalAnalysisAtASpeed._Cast_AbstractShaftModalAnalysisAtASpeed",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftModalAnalysisAtASpeed._Cast_AbstractShaftModalAnalysisAtASpeed",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftModalAnalysisAtASpeed._Cast_AbstractShaftModalAnalysisAtASpeed",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftModalAnalysisAtASpeed._Cast_AbstractShaftModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftModalAnalysisAtASpeed._Cast_AbstractShaftModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_modal_analysis_at_a_speed(
            self: "AbstractShaftModalAnalysisAtASpeed._Cast_AbstractShaftModalAnalysisAtASpeed",
        ) -> "_5183.CycloidalDiscModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5183,
            )

            return self._parent._cast(_5183.CycloidalDiscModalAnalysisAtASpeed)

        @property
        def shaft_modal_analysis_at_a_speed(
            self: "AbstractShaftModalAnalysisAtASpeed._Cast_AbstractShaftModalAnalysisAtASpeed",
        ) -> "_5235.ShaftModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5235,
            )

            return self._parent._cast(_5235.ShaftModalAnalysisAtASpeed)

        @property
        def abstract_shaft_modal_analysis_at_a_speed(
            self: "AbstractShaftModalAnalysisAtASpeed._Cast_AbstractShaftModalAnalysisAtASpeed",
        ) -> "AbstractShaftModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AbstractShaftModalAnalysisAtASpeed._Cast_AbstractShaftModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "AbstractShaftModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2455.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftModalAnalysisAtASpeed._Cast_AbstractShaftModalAnalysisAtASpeed":
        return self._Cast_AbstractShaftModalAnalysisAtASpeed(self)
