"""AbstractShaftModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4858,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "AbstractShaftModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2435
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4901,
        _4954,
        _4881,
        _4937,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="AbstractShaftModalAnalysisAtAStiffness")


class AbstractShaftModalAnalysisAtAStiffness(
    _4858.AbstractShaftOrHousingModalAnalysisAtAStiffness
):
    """AbstractShaftModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftModalAnalysisAtAStiffness"
    )

    class _Cast_AbstractShaftModalAnalysisAtAStiffness:
        """Special nested class for casting AbstractShaftModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
            parent: "AbstractShaftModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_stiffness(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "_4858.AbstractShaftOrHousingModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4858.AbstractShaftOrHousingModalAnalysisAtAStiffness
            )

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "_4881.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4881,
            )

            return self._parent._cast(_4881.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "_4937.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4937,
            )

            return self._parent._cast(_4937.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_modal_analysis_at_a_stiffness(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "_4901.CycloidalDiscModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4901,
            )

            return self._parent._cast(_4901.CycloidalDiscModalAnalysisAtAStiffness)

        @property
        def shaft_modal_analysis_at_a_stiffness(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "_4954.ShaftModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4954,
            )

            return self._parent._cast(_4954.ShaftModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_modal_analysis_at_a_stiffness(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "AbstractShaftModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "AbstractShaftModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2435.AbstractShaft":
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
    ) -> "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness":
        return self._Cast_AbstractShaftModalAnalysisAtAStiffness(self)
