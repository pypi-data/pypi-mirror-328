"""BoltDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses", "BoltDynamicAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.static_loads import _6853
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BoltDynamicAnalysis",)


Self = TypeVar("Self", bound="BoltDynamicAnalysis")


class BoltDynamicAnalysis(_6323.ComponentDynamicAnalysis):
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
        ) -> "_6323.ComponentDynamicAnalysis":
            return self._parent._cast(_6323.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "BoltDynamicAnalysis._Cast_BoltDynamicAnalysis",
        ) -> "_6379.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "BoltDynamicAnalysis._Cast_BoltDynamicAnalysis",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BoltDynamicAnalysis._Cast_BoltDynamicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BoltDynamicAnalysis._Cast_BoltDynamicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BoltDynamicAnalysis._Cast_BoltDynamicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltDynamicAnalysis._Cast_BoltDynamicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltDynamicAnalysis._Cast_BoltDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

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
    def component_design(self: Self) -> "_2462.Bolt":
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
    def component_load_case(self: Self) -> "_6853.BoltLoadCase":
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
