"""BoltDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses", "BoltDynamicAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2442
    from mastapy.system_model.analyses_and_results.static_loads import _6831
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7546,
        _7547,
        _7544,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("BoltDynamicAnalysis",)


Self = TypeVar("Self", bound="BoltDynamicAnalysis")


class BoltDynamicAnalysis(_6301.ComponentDynamicAnalysis):
    """BoltDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLT_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltDynamicAnalysis")

    class _Cast_BoltDynamicAnalysis:
        """Special nested class for casting BoltDynamicAnalysis to subclasses."""

        def __init__(
            self: "BoltDynamicAnalysis._Cast_BoltDynamicAnalysis",
            parent: "BoltDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def component_dynamic_analysis(
            self: "BoltDynamicAnalysis._Cast_BoltDynamicAnalysis",
        ) -> "_6301.ComponentDynamicAnalysis":
            return self._parent._cast(_6301.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "BoltDynamicAnalysis._Cast_BoltDynamicAnalysis",
        ) -> "_6357.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "BoltDynamicAnalysis._Cast_BoltDynamicAnalysis",
        ) -> "_7546.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BoltDynamicAnalysis._Cast_BoltDynamicAnalysis",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BoltDynamicAnalysis._Cast_BoltDynamicAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BoltDynamicAnalysis._Cast_BoltDynamicAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltDynamicAnalysis._Cast_BoltDynamicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltDynamicAnalysis._Cast_BoltDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bolt_dynamic_analysis(
            self: "BoltDynamicAnalysis._Cast_BoltDynamicAnalysis",
        ) -> "BoltDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BoltDynamicAnalysis._Cast_BoltDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2442.Bolt":
        """mastapy.system_model.part_model.Bolt

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6831.BoltLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BoltDynamicAnalysis._Cast_BoltDynamicAnalysis":
        return self._Cast_BoltDynamicAnalysis(self)
