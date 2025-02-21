"""FEPartCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4729
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "FEPartCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2453
    from mastapy.system_model.analyses_and_results.modal_analyses import _4631
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4752,
        _4806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("FEPartCompoundModalAnalysis",)


Self = TypeVar("Self", bound="FEPartCompoundModalAnalysis")


class FEPartCompoundModalAnalysis(_4729.AbstractShaftOrHousingCompoundModalAnalysis):
    """FEPartCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_PART_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartCompoundModalAnalysis")

    class _Cast_FEPartCompoundModalAnalysis:
        """Special nested class for casting FEPartCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "FEPartCompoundModalAnalysis._Cast_FEPartCompoundModalAnalysis",
            parent: "FEPartCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_modal_analysis(
            self: "FEPartCompoundModalAnalysis._Cast_FEPartCompoundModalAnalysis",
        ) -> "_4729.AbstractShaftOrHousingCompoundModalAnalysis":
            return self._parent._cast(_4729.AbstractShaftOrHousingCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "FEPartCompoundModalAnalysis._Cast_FEPartCompoundModalAnalysis",
        ) -> "_4752.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4752,
            )

            return self._parent._cast(_4752.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "FEPartCompoundModalAnalysis._Cast_FEPartCompoundModalAnalysis",
        ) -> "_4806.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4806,
            )

            return self._parent._cast(_4806.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "FEPartCompoundModalAnalysis._Cast_FEPartCompoundModalAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FEPartCompoundModalAnalysis._Cast_FEPartCompoundModalAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartCompoundModalAnalysis._Cast_FEPartCompoundModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def fe_part_compound_modal_analysis(
            self: "FEPartCompoundModalAnalysis._Cast_FEPartCompoundModalAnalysis",
        ) -> "FEPartCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "FEPartCompoundModalAnalysis._Cast_FEPartCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2453.FEPart":
        """mastapy.system_model.part_model.FEPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4631.FEPartModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.FEPartModalAnalysis]

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
    def planetaries(self: Self) -> "List[FEPartCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.FEPartCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(self: Self) -> "List[_4631.FEPartModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.FEPartModalAnalysis]

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
    ) -> "FEPartCompoundModalAnalysis._Cast_FEPartCompoundModalAnalysis":
        return self._Cast_FEPartCompoundModalAnalysis(self)
