"""AbstractShaftModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4574
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "AbstractShaftModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2435
    from mastapy.system_model.analyses_and_results.system_deflections import _2687
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4618,
        _4679,
        _4597,
        _4662,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftModalAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftModalAnalysis")


class AbstractShaftModalAnalysis(_4574.AbstractShaftOrHousingModalAnalysis):
    """AbstractShaftModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftModalAnalysis")

    class _Cast_AbstractShaftModalAnalysis:
        """Special nested class for casting AbstractShaftModalAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
            parent: "AbstractShaftModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_4574.AbstractShaftOrHousingModalAnalysis":
            return self._parent._cast(_4574.AbstractShaftOrHousingModalAnalysis)

        @property
        def component_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_4597.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_4662.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_4618.CycloidalDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.CycloidalDiscModalAnalysis)

        @property
        def shaft_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_4679.ShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.ShaftModalAnalysis)

        @property
        def abstract_shaft_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "AbstractShaftModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftModalAnalysis.TYPE"):
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
    def system_deflection_results(self: Self) -> "_2687.AbstractShaftSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftSystemDeflection

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
    ) -> "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis":
        return self._Cast_AbstractShaftModalAnalysis(self)
