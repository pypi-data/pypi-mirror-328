"""MassDiscDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6400
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "MassDiscDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.static_loads import _6921
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6355,
        _6301,
        _6357,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7546,
        _7547,
        _7544,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscDynamicAnalysis",)


Self = TypeVar("Self", bound="MassDiscDynamicAnalysis")


class MassDiscDynamicAnalysis(_6400.VirtualComponentDynamicAnalysis):
    """MassDiscDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MassDiscDynamicAnalysis")

    class _Cast_MassDiscDynamicAnalysis:
        """Special nested class for casting MassDiscDynamicAnalysis to subclasses."""

        def __init__(
            self: "MassDiscDynamicAnalysis._Cast_MassDiscDynamicAnalysis",
            parent: "MassDiscDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_dynamic_analysis(
            self: "MassDiscDynamicAnalysis._Cast_MassDiscDynamicAnalysis",
        ) -> "_6400.VirtualComponentDynamicAnalysis":
            return self._parent._cast(_6400.VirtualComponentDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "MassDiscDynamicAnalysis._Cast_MassDiscDynamicAnalysis",
        ) -> "_6355.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "MassDiscDynamicAnalysis._Cast_MassDiscDynamicAnalysis",
        ) -> "_6301.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301

            return self._parent._cast(_6301.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "MassDiscDynamicAnalysis._Cast_MassDiscDynamicAnalysis",
        ) -> "_6357.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "MassDiscDynamicAnalysis._Cast_MassDiscDynamicAnalysis",
        ) -> "_7546.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MassDiscDynamicAnalysis._Cast_MassDiscDynamicAnalysis",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MassDiscDynamicAnalysis._Cast_MassDiscDynamicAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MassDiscDynamicAnalysis._Cast_MassDiscDynamicAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MassDiscDynamicAnalysis._Cast_MassDiscDynamicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscDynamicAnalysis._Cast_MassDiscDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def mass_disc_dynamic_analysis(
            self: "MassDiscDynamicAnalysis._Cast_MassDiscDynamicAnalysis",
        ) -> "MassDiscDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "MassDiscDynamicAnalysis._Cast_MassDiscDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MassDiscDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2462.MassDisc":
        """mastapy.system_model.part_model.MassDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6921.MassDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[MassDiscDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.MassDiscDynamicAnalysis]

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
    def cast_to(self: Self) -> "MassDiscDynamicAnalysis._Cast_MassDiscDynamicAnalysis":
        return self._Cast_MassDiscDynamicAnalysis(self)
