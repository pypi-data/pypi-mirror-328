"""MassDiscCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6667
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "MassDiscCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.static_loads import _6921
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6622,
        _6567,
        _6624,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="MassDiscCriticalSpeedAnalysis")


class MassDiscCriticalSpeedAnalysis(_6667.VirtualComponentCriticalSpeedAnalysis):
    """MassDiscCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MassDiscCriticalSpeedAnalysis")

    class _Cast_MassDiscCriticalSpeedAnalysis:
        """Special nested class for casting MassDiscCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
            parent: "MassDiscCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_critical_speed_analysis(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
        ) -> "_6667.VirtualComponentCriticalSpeedAnalysis":
            return self._parent._cast(_6667.VirtualComponentCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
        ) -> "_6622.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
        ) -> "_6567.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6567,
            )

            return self._parent._cast(_6567.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
        ) -> "_6624.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(_6624.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def mass_disc_critical_speed_analysis(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
        ) -> "MassDiscCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MassDiscCriticalSpeedAnalysis.TYPE"):
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
    def planetaries(self: Self) -> "List[MassDiscCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.MassDiscCriticalSpeedAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis":
        return self._Cast_MassDiscCriticalSpeedAnalysis(self)
