"""BearingDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "BearingDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2439
    from mastapy.system_model.analyses_and_results.static_loads import _6820
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6356,
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
__all__ = ("BearingDynamicAnalysis",)


Self = TypeVar("Self", bound="BearingDynamicAnalysis")


class BearingDynamicAnalysis(_6313.ConnectorDynamicAnalysis):
    """BearingDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEARING_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingDynamicAnalysis")

    class _Cast_BearingDynamicAnalysis:
        """Special nested class for casting BearingDynamicAnalysis to subclasses."""

        def __init__(
            self: "BearingDynamicAnalysis._Cast_BearingDynamicAnalysis",
            parent: "BearingDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def connector_dynamic_analysis(
            self: "BearingDynamicAnalysis._Cast_BearingDynamicAnalysis",
        ) -> "_6313.ConnectorDynamicAnalysis":
            return self._parent._cast(_6313.ConnectorDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "BearingDynamicAnalysis._Cast_BearingDynamicAnalysis",
        ) -> "_6356.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356

            return self._parent._cast(_6356.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "BearingDynamicAnalysis._Cast_BearingDynamicAnalysis",
        ) -> "_6302.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "BearingDynamicAnalysis._Cast_BearingDynamicAnalysis",
        ) -> "_6358.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "BearingDynamicAnalysis._Cast_BearingDynamicAnalysis",
        ) -> "_7547.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BearingDynamicAnalysis._Cast_BearingDynamicAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BearingDynamicAnalysis._Cast_BearingDynamicAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BearingDynamicAnalysis._Cast_BearingDynamicAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BearingDynamicAnalysis._Cast_BearingDynamicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BearingDynamicAnalysis._Cast_BearingDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bearing_dynamic_analysis(
            self: "BearingDynamicAnalysis._Cast_BearingDynamicAnalysis",
        ) -> "BearingDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BearingDynamicAnalysis._Cast_BearingDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2439.Bearing":
        """mastapy.system_model.part_model.Bearing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6820.BearingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[BearingDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BearingDynamicAnalysis]

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
    def cast_to(self: Self) -> "BearingDynamicAnalysis._Cast_BearingDynamicAnalysis":
        return self._Cast_BearingDynamicAnalysis(self)
