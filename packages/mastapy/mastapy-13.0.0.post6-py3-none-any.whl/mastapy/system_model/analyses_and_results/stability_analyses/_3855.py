"""RingPinsToDiscConnectionStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3830
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "RingPinsToDiscConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2341
    from mastapy.system_model.analyses_and_results.static_loads import _6944
    from mastapy.system_model.analyses_and_results.stability_analyses import _3798
    from mastapy.system_model.analyses_and_results.analysis_cases import _7540, _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="RingPinsToDiscConnectionStabilityAnalysis")


class RingPinsToDiscConnectionStabilityAnalysis(
    _3830.InterMountableComponentConnectionStabilityAnalysis
):
    """RingPinsToDiscConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsToDiscConnectionStabilityAnalysis"
    )

    class _Cast_RingPinsToDiscConnectionStabilityAnalysis:
        """Special nested class for casting RingPinsToDiscConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionStabilityAnalysis._Cast_RingPinsToDiscConnectionStabilityAnalysis",
            parent: "RingPinsToDiscConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "RingPinsToDiscConnectionStabilityAnalysis._Cast_RingPinsToDiscConnectionStabilityAnalysis",
        ) -> "_3830.InterMountableComponentConnectionStabilityAnalysis":
            return self._parent._cast(
                _3830.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "RingPinsToDiscConnectionStabilityAnalysis._Cast_RingPinsToDiscConnectionStabilityAnalysis",
        ) -> "_3798.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3798,
            )

            return self._parent._cast(_3798.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "RingPinsToDiscConnectionStabilityAnalysis._Cast_RingPinsToDiscConnectionStabilityAnalysis",
        ) -> "_7540.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RingPinsToDiscConnectionStabilityAnalysis._Cast_RingPinsToDiscConnectionStabilityAnalysis",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RingPinsToDiscConnectionStabilityAnalysis._Cast_RingPinsToDiscConnectionStabilityAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsToDiscConnectionStabilityAnalysis._Cast_RingPinsToDiscConnectionStabilityAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionStabilityAnalysis._Cast_RingPinsToDiscConnectionStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_stability_analysis(
            self: "RingPinsToDiscConnectionStabilityAnalysis._Cast_RingPinsToDiscConnectionStabilityAnalysis",
        ) -> "RingPinsToDiscConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionStabilityAnalysis._Cast_RingPinsToDiscConnectionStabilityAnalysis",
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
        self: Self, instance_to_wrap: "RingPinsToDiscConnectionStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2341.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6944.RingPinsToDiscConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsToDiscConnectionLoadCase

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
    ) -> "RingPinsToDiscConnectionStabilityAnalysis._Cast_RingPinsToDiscConnectionStabilityAnalysis":
        return self._Cast_RingPinsToDiscConnectionStabilityAnalysis(self)
