"""PowerLoadDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6422
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "PowerLoadDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2492
    from mastapy.system_model.analyses_and_results.static_loads import _6961
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6377,
        _6323,
        _6379,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadDynamicAnalysis",)


Self = TypeVar("Self", bound="PowerLoadDynamicAnalysis")


class PowerLoadDynamicAnalysis(_6422.VirtualComponentDynamicAnalysis):
    """PowerLoadDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerLoadDynamicAnalysis")

    class _Cast_PowerLoadDynamicAnalysis:
        """Special nested class for casting PowerLoadDynamicAnalysis to subclasses."""

        def __init__(
            self: "PowerLoadDynamicAnalysis._Cast_PowerLoadDynamicAnalysis",
            parent: "PowerLoadDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_dynamic_analysis(
            self: "PowerLoadDynamicAnalysis._Cast_PowerLoadDynamicAnalysis",
        ) -> "_6422.VirtualComponentDynamicAnalysis":
            return self._parent._cast(_6422.VirtualComponentDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "PowerLoadDynamicAnalysis._Cast_PowerLoadDynamicAnalysis",
        ) -> "_6377.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377

            return self._parent._cast(_6377.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "PowerLoadDynamicAnalysis._Cast_PowerLoadDynamicAnalysis",
        ) -> "_6323.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(_6323.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "PowerLoadDynamicAnalysis._Cast_PowerLoadDynamicAnalysis",
        ) -> "_6379.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "PowerLoadDynamicAnalysis._Cast_PowerLoadDynamicAnalysis",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PowerLoadDynamicAnalysis._Cast_PowerLoadDynamicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PowerLoadDynamicAnalysis._Cast_PowerLoadDynamicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PowerLoadDynamicAnalysis._Cast_PowerLoadDynamicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PowerLoadDynamicAnalysis._Cast_PowerLoadDynamicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadDynamicAnalysis._Cast_PowerLoadDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def power_load_dynamic_analysis(
            self: "PowerLoadDynamicAnalysis._Cast_PowerLoadDynamicAnalysis",
        ) -> "PowerLoadDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "PowerLoadDynamicAnalysis._Cast_PowerLoadDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerLoadDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2492.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6961.PowerLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase

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
    ) -> "PowerLoadDynamicAnalysis._Cast_PowerLoadDynamicAnalysis":
        return self._Cast_PowerLoadDynamicAnalysis(self)
