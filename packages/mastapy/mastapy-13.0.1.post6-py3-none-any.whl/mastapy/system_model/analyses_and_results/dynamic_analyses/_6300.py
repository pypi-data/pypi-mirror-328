"""ClutchHalfDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "ClutchHalfDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2579
    from mastapy.system_model.analyses_and_results.static_loads import _6834
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
__all__ = ("ClutchHalfDynamicAnalysis",)


Self = TypeVar("Self", bound="ClutchHalfDynamicAnalysis")


class ClutchHalfDynamicAnalysis(_6316.CouplingHalfDynamicAnalysis):
    """ClutchHalfDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchHalfDynamicAnalysis")

    class _Cast_ClutchHalfDynamicAnalysis:
        """Special nested class for casting ClutchHalfDynamicAnalysis to subclasses."""

        def __init__(
            self: "ClutchHalfDynamicAnalysis._Cast_ClutchHalfDynamicAnalysis",
            parent: "ClutchHalfDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_dynamic_analysis(
            self: "ClutchHalfDynamicAnalysis._Cast_ClutchHalfDynamicAnalysis",
        ) -> "_6316.CouplingHalfDynamicAnalysis":
            return self._parent._cast(_6316.CouplingHalfDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "ClutchHalfDynamicAnalysis._Cast_ClutchHalfDynamicAnalysis",
        ) -> "_6356.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356

            return self._parent._cast(_6356.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "ClutchHalfDynamicAnalysis._Cast_ClutchHalfDynamicAnalysis",
        ) -> "_6302.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "ClutchHalfDynamicAnalysis._Cast_ClutchHalfDynamicAnalysis",
        ) -> "_6358.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "ClutchHalfDynamicAnalysis._Cast_ClutchHalfDynamicAnalysis",
        ) -> "_7547.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ClutchHalfDynamicAnalysis._Cast_ClutchHalfDynamicAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ClutchHalfDynamicAnalysis._Cast_ClutchHalfDynamicAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ClutchHalfDynamicAnalysis._Cast_ClutchHalfDynamicAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchHalfDynamicAnalysis._Cast_ClutchHalfDynamicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHalfDynamicAnalysis._Cast_ClutchHalfDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_half_dynamic_analysis(
            self: "ClutchHalfDynamicAnalysis._Cast_ClutchHalfDynamicAnalysis",
        ) -> "ClutchHalfDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ClutchHalfDynamicAnalysis._Cast_ClutchHalfDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchHalfDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2579.ClutchHalf":
        """mastapy.system_model.part_model.couplings.ClutchHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6834.ClutchHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase

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
    ) -> "ClutchHalfDynamicAnalysis._Cast_ClutchHalfDynamicAnalysis":
        return self._Cast_ClutchHalfDynamicAnalysis(self)
