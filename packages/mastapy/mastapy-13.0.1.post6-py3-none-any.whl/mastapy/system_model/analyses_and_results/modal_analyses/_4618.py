"""CycloidalDiscModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4573
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "CycloidalDiscModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2569
    from mastapy.system_model.analyses_and_results.static_loads import _6860
    from mastapy.system_model.analyses_and_results.system_deflections import _2738
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4574,
        _4597,
        _4662,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscModalAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscModalAnalysis")


class CycloidalDiscModalAnalysis(_4573.AbstractShaftModalAnalysis):
    """CycloidalDiscModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscModalAnalysis")

    class _Cast_CycloidalDiscModalAnalysis:
        """Special nested class for casting CycloidalDiscModalAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
            parent: "CycloidalDiscModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_modal_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "_4573.AbstractShaftModalAnalysis":
            return self._parent._cast(_4573.AbstractShaftModalAnalysis)

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "_4574.AbstractShaftOrHousingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4574

            return self._parent._cast(_4574.AbstractShaftOrHousingModalAnalysis)

        @property
        def component_modal_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "_4597.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "_4662.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_modal_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "CycloidalDiscModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscModalAnalysis.TYPE"):
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
    def system_deflection_results(self: Self) -> "_2738.CycloidalDiscSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis":
        return self._Cast_CycloidalDiscModalAnalysis(self)
