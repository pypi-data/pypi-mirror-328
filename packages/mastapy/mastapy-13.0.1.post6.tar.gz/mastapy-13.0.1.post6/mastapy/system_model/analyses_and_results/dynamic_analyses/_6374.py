"""ShaftDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6278
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "ShaftDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2482
    from mastapy.system_model.analyses_and_results.static_loads import _6951
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6279,
        _6302,
        _6358,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7547,
        _7548,
        _7545,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ShaftDynamicAnalysis",)


Self = TypeVar("Self", bound="ShaftDynamicAnalysis")


class ShaftDynamicAnalysis(_6278.AbstractShaftDynamicAnalysis):
    """ShaftDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftDynamicAnalysis")

    class _Cast_ShaftDynamicAnalysis:
        """Special nested class for casting ShaftDynamicAnalysis to subclasses."""

        def __init__(
            self: "ShaftDynamicAnalysis._Cast_ShaftDynamicAnalysis",
            parent: "ShaftDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_dynamic_analysis(
            self: "ShaftDynamicAnalysis._Cast_ShaftDynamicAnalysis",
        ) -> "_6278.AbstractShaftDynamicAnalysis":
            return self._parent._cast(_6278.AbstractShaftDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_dynamic_analysis(
            self: "ShaftDynamicAnalysis._Cast_ShaftDynamicAnalysis",
        ) -> "_6279.AbstractShaftOrHousingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6279

            return self._parent._cast(_6279.AbstractShaftOrHousingDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "ShaftDynamicAnalysis._Cast_ShaftDynamicAnalysis",
        ) -> "_6302.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "ShaftDynamicAnalysis._Cast_ShaftDynamicAnalysis",
        ) -> "_6358.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "ShaftDynamicAnalysis._Cast_ShaftDynamicAnalysis",
        ) -> "_7547.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ShaftDynamicAnalysis._Cast_ShaftDynamicAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftDynamicAnalysis._Cast_ShaftDynamicAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftDynamicAnalysis._Cast_ShaftDynamicAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftDynamicAnalysis._Cast_ShaftDynamicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftDynamicAnalysis._Cast_ShaftDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def shaft_dynamic_analysis(
            self: "ShaftDynamicAnalysis._Cast_ShaftDynamicAnalysis",
        ) -> "ShaftDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftDynamicAnalysis._Cast_ShaftDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2482.Shaft":
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
    def component_load_case(self: Self) -> "_6951.ShaftLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ShaftDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ShaftDynamicAnalysis]

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
    def cast_to(self: Self) -> "ShaftDynamicAnalysis._Cast_ShaftDynamicAnalysis":
        return self._Cast_ShaftDynamicAnalysis(self)
