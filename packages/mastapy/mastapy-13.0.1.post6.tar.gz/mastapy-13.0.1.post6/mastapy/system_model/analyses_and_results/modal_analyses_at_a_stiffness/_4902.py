"""CycloidalDiscModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4858,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "CycloidalDiscModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2569
    from mastapy.system_model.analyses_and_results.static_loads import _6860
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4859,
        _4882,
        _4938,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CycloidalDiscModalAnalysisAtAStiffness")


class CycloidalDiscModalAnalysisAtAStiffness(
    _4858.AbstractShaftModalAnalysisAtAStiffness
):
    """CycloidalDiscModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscModalAnalysisAtAStiffness"
    )

    class _Cast_CycloidalDiscModalAnalysisAtAStiffness:
        """Special nested class for casting CycloidalDiscModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CycloidalDiscModalAnalysisAtAStiffness._Cast_CycloidalDiscModalAnalysisAtAStiffness",
            parent: "CycloidalDiscModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def abstract_shaft_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscModalAnalysisAtAStiffness._Cast_CycloidalDiscModalAnalysisAtAStiffness",
        ) -> "_4858.AbstractShaftModalAnalysisAtAStiffness":
            return self._parent._cast(_4858.AbstractShaftModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscModalAnalysisAtAStiffness._Cast_CycloidalDiscModalAnalysisAtAStiffness",
        ) -> "_4859.AbstractShaftOrHousingModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4859,
            )

            return self._parent._cast(
                _4859.AbstractShaftOrHousingModalAnalysisAtAStiffness
            )

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscModalAnalysisAtAStiffness._Cast_CycloidalDiscModalAnalysisAtAStiffness",
        ) -> "_4882.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4882,
            )

            return self._parent._cast(_4882.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscModalAnalysisAtAStiffness._Cast_CycloidalDiscModalAnalysisAtAStiffness",
        ) -> "_4938.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(_4938.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalDiscModalAnalysisAtAStiffness._Cast_CycloidalDiscModalAnalysisAtAStiffness",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscModalAnalysisAtAStiffness._Cast_CycloidalDiscModalAnalysisAtAStiffness",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscModalAnalysisAtAStiffness._Cast_CycloidalDiscModalAnalysisAtAStiffness",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscModalAnalysisAtAStiffness._Cast_CycloidalDiscModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscModalAnalysisAtAStiffness._Cast_CycloidalDiscModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscModalAnalysisAtAStiffness._Cast_CycloidalDiscModalAnalysisAtAStiffness",
        ) -> "CycloidalDiscModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscModalAnalysisAtAStiffness._Cast_CycloidalDiscModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "CycloidalDiscModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2569.CycloidalDisc":
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
    def component_load_case(self: Self) -> "_6860.CycloidalDiscLoadCase":
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
    ) -> "CycloidalDiscModalAnalysisAtAStiffness._Cast_CycloidalDiscModalAnalysisAtAStiffness":
        return self._Cast_CycloidalDiscModalAnalysisAtAStiffness(self)
