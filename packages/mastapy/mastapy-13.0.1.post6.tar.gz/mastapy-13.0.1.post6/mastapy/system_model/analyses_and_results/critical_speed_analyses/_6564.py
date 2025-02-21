"""ClutchConnectionCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6580
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ClutchConnectionCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2342
    from mastapy.system_model.analyses_and_results.static_loads import _6833
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6611,
        _6578,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ClutchConnectionCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ClutchConnectionCriticalSpeedAnalysis")


class ClutchConnectionCriticalSpeedAnalysis(
    _6580.CouplingConnectionCriticalSpeedAnalysis
):
    """ClutchConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ClutchConnectionCriticalSpeedAnalysis"
    )

    class _Cast_ClutchConnectionCriticalSpeedAnalysis:
        """Special nested class for casting ClutchConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ClutchConnectionCriticalSpeedAnalysis._Cast_ClutchConnectionCriticalSpeedAnalysis",
            parent: "ClutchConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_critical_speed_analysis(
            self: "ClutchConnectionCriticalSpeedAnalysis._Cast_ClutchConnectionCriticalSpeedAnalysis",
        ) -> "_6580.CouplingConnectionCriticalSpeedAnalysis":
            return self._parent._cast(_6580.CouplingConnectionCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "ClutchConnectionCriticalSpeedAnalysis._Cast_ClutchConnectionCriticalSpeedAnalysis",
        ) -> "_6611.InterMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6611,
            )

            return self._parent._cast(
                _6611.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "ClutchConnectionCriticalSpeedAnalysis._Cast_ClutchConnectionCriticalSpeedAnalysis",
        ) -> "_6578.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6578,
            )

            return self._parent._cast(_6578.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ClutchConnectionCriticalSpeedAnalysis._Cast_ClutchConnectionCriticalSpeedAnalysis",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ClutchConnectionCriticalSpeedAnalysis._Cast_ClutchConnectionCriticalSpeedAnalysis",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ClutchConnectionCriticalSpeedAnalysis._Cast_ClutchConnectionCriticalSpeedAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchConnectionCriticalSpeedAnalysis._Cast_ClutchConnectionCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchConnectionCriticalSpeedAnalysis._Cast_ClutchConnectionCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_connection_critical_speed_analysis(
            self: "ClutchConnectionCriticalSpeedAnalysis._Cast_ClutchConnectionCriticalSpeedAnalysis",
        ) -> "ClutchConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ClutchConnectionCriticalSpeedAnalysis._Cast_ClutchConnectionCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "ClutchConnectionCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2342.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6833.ClutchConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ClutchConnectionCriticalSpeedAnalysis._Cast_ClutchConnectionCriticalSpeedAnalysis":
        return self._Cast_ClutchConnectionCriticalSpeedAnalysis(self)
