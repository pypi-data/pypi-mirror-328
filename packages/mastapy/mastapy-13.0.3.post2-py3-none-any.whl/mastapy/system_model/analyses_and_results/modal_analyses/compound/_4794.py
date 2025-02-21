"""CycloidalDiscCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4750
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "CycloidalDiscCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2589
    from mastapy.system_model.analyses_and_results.modal_analyses import _4639
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4751,
        _4774,
        _4828,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCompoundModalAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscCompoundModalAnalysis")


class CycloidalDiscCompoundModalAnalysis(_4750.AbstractShaftCompoundModalAnalysis):
    """CycloidalDiscCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscCompoundModalAnalysis")

    class _Cast_CycloidalDiscCompoundModalAnalysis:
        """Special nested class for casting CycloidalDiscCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCompoundModalAnalysis._Cast_CycloidalDiscCompoundModalAnalysis",
            parent: "CycloidalDiscCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_modal_analysis(
            self: "CycloidalDiscCompoundModalAnalysis._Cast_CycloidalDiscCompoundModalAnalysis",
        ) -> "_4750.AbstractShaftCompoundModalAnalysis":
            return self._parent._cast(_4750.AbstractShaftCompoundModalAnalysis)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis(
            self: "CycloidalDiscCompoundModalAnalysis._Cast_CycloidalDiscCompoundModalAnalysis",
        ) -> "_4751.AbstractShaftOrHousingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4751,
            )

            return self._parent._cast(_4751.AbstractShaftOrHousingCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "CycloidalDiscCompoundModalAnalysis._Cast_CycloidalDiscCompoundModalAnalysis",
        ) -> "_4774.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4774,
            )

            return self._parent._cast(_4774.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "CycloidalDiscCompoundModalAnalysis._Cast_CycloidalDiscCompoundModalAnalysis",
        ) -> "_4828.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "CycloidalDiscCompoundModalAnalysis._Cast_CycloidalDiscCompoundModalAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCompoundModalAnalysis._Cast_CycloidalDiscCompoundModalAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCompoundModalAnalysis._Cast_CycloidalDiscCompoundModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_modal_analysis(
            self: "CycloidalDiscCompoundModalAnalysis._Cast_CycloidalDiscCompoundModalAnalysis",
        ) -> "CycloidalDiscCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCompoundModalAnalysis._Cast_CycloidalDiscCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "CycloidalDiscCompoundModalAnalysis.TYPE"
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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4639.CycloidalDiscModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CycloidalDiscModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4639.CycloidalDiscModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CycloidalDiscModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCompoundModalAnalysis._Cast_CycloidalDiscCompoundModalAnalysis":
        return self._Cast_CycloidalDiscCompoundModalAnalysis(self)
