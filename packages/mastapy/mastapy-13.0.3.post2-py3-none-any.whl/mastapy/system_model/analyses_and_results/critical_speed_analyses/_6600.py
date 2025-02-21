"""ConnectorCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6644
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ConnectorCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2467
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6572,
        _6645,
        _6663,
        _6589,
        _6646,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConnectorCriticalSpeedAnalysis")


class ConnectorCriticalSpeedAnalysis(_6644.MountableComponentCriticalSpeedAnalysis):
    """ConnectorCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorCriticalSpeedAnalysis")

    class _Cast_ConnectorCriticalSpeedAnalysis:
        """Special nested class for casting ConnectorCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
            parent: "ConnectorCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_critical_speed_analysis(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_6644.MountableComponentCriticalSpeedAnalysis":
            return self._parent._cast(_6644.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_6589.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6589,
            )

            return self._parent._cast(_6589.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_6646.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bearing_critical_speed_analysis(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_6572.BearingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6572,
            )

            return self._parent._cast(_6572.BearingCriticalSpeedAnalysis)

        @property
        def oil_seal_critical_speed_analysis(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_6645.OilSealCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6645,
            )

            return self._parent._cast(_6645.OilSealCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_critical_speed_analysis(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "_6663.ShaftHubConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6663,
            )

            return self._parent._cast(_6663.ShaftHubConnectionCriticalSpeedAnalysis)

        @property
        def connector_critical_speed_analysis(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
        ) -> "ConnectorCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2467.Connector":
        """mastapy.system_model.part_model.Connector

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
    ) -> "ConnectorCriticalSpeedAnalysis._Cast_ConnectorCriticalSpeedAnalysis":
        return self._Cast_ConnectorCriticalSpeedAnalysis(self)
