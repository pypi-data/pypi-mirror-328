"""ConnectorStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3842
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ConnectorStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2447
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3771,
        _3843,
        _3860,
        _3788,
        _3844,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorStabilityAnalysis",)


Self = TypeVar("Self", bound="ConnectorStabilityAnalysis")


class ConnectorStabilityAnalysis(_3842.MountableComponentStabilityAnalysis):
    """ConnectorStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorStabilityAnalysis")

    class _Cast_ConnectorStabilityAnalysis:
        """Special nested class for casting ConnectorStabilityAnalysis to subclasses."""

        def __init__(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
            parent: "ConnectorStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3842.MountableComponentStabilityAnalysis":
            return self._parent._cast(_3842.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3788.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3844.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bearing_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3771.BearingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3771,
            )

            return self._parent._cast(_3771.BearingStabilityAnalysis)

        @property
        def oil_seal_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3843.OilSealStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3843,
            )

            return self._parent._cast(_3843.OilSealStabilityAnalysis)

        @property
        def shaft_hub_connection_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3860.ShaftHubConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3860,
            )

            return self._parent._cast(_3860.ShaftHubConnectionStabilityAnalysis)

        @property
        def connector_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "ConnectorStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2447.Connector":
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
    ) -> "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis":
        return self._Cast_ConnectorStabilityAnalysis(self)
