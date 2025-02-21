"""ShaftCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4737
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "ShaftCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2489
    from mastapy.system_model.analyses_and_results.modal_analyses import _4687
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4738,
        _4761,
        _4815,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ShaftCompoundModalAnalysis",)


Self = TypeVar("Self", bound="ShaftCompoundModalAnalysis")


class ShaftCompoundModalAnalysis(_4737.AbstractShaftCompoundModalAnalysis):
    """ShaftCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftCompoundModalAnalysis")

    class _Cast_ShaftCompoundModalAnalysis:
        """Special nested class for casting ShaftCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "ShaftCompoundModalAnalysis._Cast_ShaftCompoundModalAnalysis",
            parent: "ShaftCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_modal_analysis(
            self: "ShaftCompoundModalAnalysis._Cast_ShaftCompoundModalAnalysis",
        ) -> "_4737.AbstractShaftCompoundModalAnalysis":
            return self._parent._cast(_4737.AbstractShaftCompoundModalAnalysis)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis(
            self: "ShaftCompoundModalAnalysis._Cast_ShaftCompoundModalAnalysis",
        ) -> "_4738.AbstractShaftOrHousingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4738,
            )

            return self._parent._cast(_4738.AbstractShaftOrHousingCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "ShaftCompoundModalAnalysis._Cast_ShaftCompoundModalAnalysis",
        ) -> "_4761.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4761,
            )

            return self._parent._cast(_4761.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "ShaftCompoundModalAnalysis._Cast_ShaftCompoundModalAnalysis",
        ) -> "_4815.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "ShaftCompoundModalAnalysis._Cast_ShaftCompoundModalAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftCompoundModalAnalysis._Cast_ShaftCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftCompoundModalAnalysis._Cast_ShaftCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def shaft_compound_modal_analysis(
            self: "ShaftCompoundModalAnalysis._Cast_ShaftCompoundModalAnalysis",
        ) -> "ShaftCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftCompoundModalAnalysis._Cast_ShaftCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2489.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4687.ShaftModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ShaftModalAnalysis]

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
    def planetaries(self: Self) -> "List[ShaftCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.ShaftCompoundModalAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_4687.ShaftModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ShaftModalAnalysis]

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
    ) -> "ShaftCompoundModalAnalysis._Cast_ShaftCompoundModalAnalysis":
        return self._Cast_ShaftCompoundModalAnalysis(self)
