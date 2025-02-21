"""VirtualComponentDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "VirtualComponentDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2479
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6354,
        _6355,
        _6365,
        _6366,
        _6400,
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
__all__ = ("VirtualComponentDynamicAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentDynamicAnalysis")


class VirtualComponentDynamicAnalysis(_6356.MountableComponentDynamicAnalysis):
    """VirtualComponentDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentDynamicAnalysis")

    class _Cast_VirtualComponentDynamicAnalysis:
        """Special nested class for casting VirtualComponentDynamicAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
            parent: "VirtualComponentDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6356.MountableComponentDynamicAnalysis":
            return self._parent._cast(_6356.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6302.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6358.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_7547.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def mass_disc_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6354.MassDiscDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(_6354.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6355.MeasurementComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.MeasurementComponentDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6365.PointLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365

            return self._parent._cast(_6365.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6366.PowerLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.PowerLoadDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6400.UnbalancedMassDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6400

            return self._parent._cast(_6400.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "VirtualComponentDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualComponentDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2479.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis":
        return self._Cast_VirtualComponentDynamicAnalysis(self)
