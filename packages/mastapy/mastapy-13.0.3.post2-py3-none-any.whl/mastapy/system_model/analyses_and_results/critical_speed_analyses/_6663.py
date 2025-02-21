"""ShaftHubConnectionCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6600
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ShaftHubConnectionCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2619
    from mastapy.system_model.analyses_and_results.static_loads import _6971
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6644,
        _6589,
        _6646,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ShaftHubConnectionCriticalSpeedAnalysis")


class ShaftHubConnectionCriticalSpeedAnalysis(_6600.ConnectorCriticalSpeedAnalysis):
    """ShaftHubConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftHubConnectionCriticalSpeedAnalysis"
    )

    class _Cast_ShaftHubConnectionCriticalSpeedAnalysis:
        """Special nested class for casting ShaftHubConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ShaftHubConnectionCriticalSpeedAnalysis._Cast_ShaftHubConnectionCriticalSpeedAnalysis",
            parent: "ShaftHubConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def connector_critical_speed_analysis(
            self: "ShaftHubConnectionCriticalSpeedAnalysis._Cast_ShaftHubConnectionCriticalSpeedAnalysis",
        ) -> "_6600.ConnectorCriticalSpeedAnalysis":
            return self._parent._cast(_6600.ConnectorCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "ShaftHubConnectionCriticalSpeedAnalysis._Cast_ShaftHubConnectionCriticalSpeedAnalysis",
        ) -> "_6644.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(_6644.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "ShaftHubConnectionCriticalSpeedAnalysis._Cast_ShaftHubConnectionCriticalSpeedAnalysis",
        ) -> "_6589.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6589,
            )

            return self._parent._cast(_6589.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "ShaftHubConnectionCriticalSpeedAnalysis._Cast_ShaftHubConnectionCriticalSpeedAnalysis",
        ) -> "_6646.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ShaftHubConnectionCriticalSpeedAnalysis._Cast_ShaftHubConnectionCriticalSpeedAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftHubConnectionCriticalSpeedAnalysis._Cast_ShaftHubConnectionCriticalSpeedAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftHubConnectionCriticalSpeedAnalysis._Cast_ShaftHubConnectionCriticalSpeedAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftHubConnectionCriticalSpeedAnalysis._Cast_ShaftHubConnectionCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHubConnectionCriticalSpeedAnalysis._Cast_ShaftHubConnectionCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def shaft_hub_connection_critical_speed_analysis(
            self: "ShaftHubConnectionCriticalSpeedAnalysis._Cast_ShaftHubConnectionCriticalSpeedAnalysis",
        ) -> "ShaftHubConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionCriticalSpeedAnalysis._Cast_ShaftHubConnectionCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "ShaftHubConnectionCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2619.ShaftHubConnection":
        """mastapy.system_model.part_model.couplings.ShaftHubConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6971.ShaftHubConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ShaftHubConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ShaftHubConnectionCriticalSpeedAnalysis]

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
    ) -> "ShaftHubConnectionCriticalSpeedAnalysis._Cast_ShaftHubConnectionCriticalSpeedAnalysis":
        return self._Cast_ShaftHubConnectionCriticalSpeedAnalysis(self)
