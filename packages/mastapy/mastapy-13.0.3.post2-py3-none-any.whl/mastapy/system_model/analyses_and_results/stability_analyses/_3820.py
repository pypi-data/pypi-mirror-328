"""ConnectorStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3863
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ConnectorStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2467
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3792,
        _3864,
        _3881,
        _3809,
        _3865,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorStabilityAnalysis",)


Self = TypeVar("Self", bound="ConnectorStabilityAnalysis")


class ConnectorStabilityAnalysis(_3863.MountableComponentStabilityAnalysis):
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
        ) -> "_3863.MountableComponentStabilityAnalysis":
            return self._parent._cast(_3863.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3809.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(_3809.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bearing_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3792.BearingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3792,
            )

            return self._parent._cast(_3792.BearingStabilityAnalysis)

        @property
        def oil_seal_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3864.OilSealStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3864,
            )

            return self._parent._cast(_3864.OilSealStabilityAnalysis)

        @property
        def shaft_hub_connection_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3881.ShaftHubConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3881,
            )

            return self._parent._cast(_3881.ShaftHubConnectionStabilityAnalysis)

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
    ) -> "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis":
        return self._Cast_ConnectorStabilityAnalysis(self)
