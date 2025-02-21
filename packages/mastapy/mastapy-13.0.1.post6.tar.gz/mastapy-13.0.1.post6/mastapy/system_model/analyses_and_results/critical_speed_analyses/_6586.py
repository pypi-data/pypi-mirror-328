"""CVTBeltConnectionCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6552
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "CVTBeltConnectionCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2273
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6611,
        _6578,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CVTBeltConnectionCriticalSpeedAnalysis")


class CVTBeltConnectionCriticalSpeedAnalysis(_6552.BeltConnectionCriticalSpeedAnalysis):
    """CVTBeltConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTBeltConnectionCriticalSpeedAnalysis"
    )

    class _Cast_CVTBeltConnectionCriticalSpeedAnalysis:
        """Special nested class for casting CVTBeltConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CVTBeltConnectionCriticalSpeedAnalysis._Cast_CVTBeltConnectionCriticalSpeedAnalysis",
            parent: "CVTBeltConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def belt_connection_critical_speed_analysis(
            self: "CVTBeltConnectionCriticalSpeedAnalysis._Cast_CVTBeltConnectionCriticalSpeedAnalysis",
        ) -> "_6552.BeltConnectionCriticalSpeedAnalysis":
            return self._parent._cast(_6552.BeltConnectionCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "CVTBeltConnectionCriticalSpeedAnalysis._Cast_CVTBeltConnectionCriticalSpeedAnalysis",
        ) -> "_6611.InterMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6611,
            )

            return self._parent._cast(
                _6611.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "CVTBeltConnectionCriticalSpeedAnalysis._Cast_CVTBeltConnectionCriticalSpeedAnalysis",
        ) -> "_6578.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6578,
            )

            return self._parent._cast(_6578.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CVTBeltConnectionCriticalSpeedAnalysis._Cast_CVTBeltConnectionCriticalSpeedAnalysis",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CVTBeltConnectionCriticalSpeedAnalysis._Cast_CVTBeltConnectionCriticalSpeedAnalysis",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CVTBeltConnectionCriticalSpeedAnalysis._Cast_CVTBeltConnectionCriticalSpeedAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTBeltConnectionCriticalSpeedAnalysis._Cast_CVTBeltConnectionCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionCriticalSpeedAnalysis._Cast_CVTBeltConnectionCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_critical_speed_analysis(
            self: "CVTBeltConnectionCriticalSpeedAnalysis._Cast_CVTBeltConnectionCriticalSpeedAnalysis",
        ) -> "CVTBeltConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionCriticalSpeedAnalysis._Cast_CVTBeltConnectionCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "CVTBeltConnectionCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2273.CVTBeltConnection":
        """mastapy.system_model.connections_and_sockets.CVTBeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTBeltConnectionCriticalSpeedAnalysis._Cast_CVTBeltConnectionCriticalSpeedAnalysis":
        return self._Cast_CVTBeltConnectionCriticalSpeedAnalysis(self)
