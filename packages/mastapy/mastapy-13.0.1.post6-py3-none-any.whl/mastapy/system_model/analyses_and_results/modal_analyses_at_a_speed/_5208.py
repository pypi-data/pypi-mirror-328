"""RingPinsToDiscConnectionModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5182
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "RingPinsToDiscConnectionModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2341
    from mastapy.system_model.analyses_and_results.static_loads import _6945
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5152,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="RingPinsToDiscConnectionModalAnalysisAtASpeed")


class RingPinsToDiscConnectionModalAnalysisAtASpeed(
    _5182.InterMountableComponentConnectionModalAnalysisAtASpeed
):
    """RingPinsToDiscConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsToDiscConnectionModalAnalysisAtASpeed"
    )

    class _Cast_RingPinsToDiscConnectionModalAnalysisAtASpeed:
        """Special nested class for casting RingPinsToDiscConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionModalAnalysisAtASpeed._Cast_RingPinsToDiscConnectionModalAnalysisAtASpeed",
            parent: "RingPinsToDiscConnectionModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "RingPinsToDiscConnectionModalAnalysisAtASpeed._Cast_RingPinsToDiscConnectionModalAnalysisAtASpeed",
        ) -> "_5182.InterMountableComponentConnectionModalAnalysisAtASpeed":
            return self._parent._cast(
                _5182.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "RingPinsToDiscConnectionModalAnalysisAtASpeed._Cast_RingPinsToDiscConnectionModalAnalysisAtASpeed",
        ) -> "_5152.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5152,
            )

            return self._parent._cast(_5152.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "RingPinsToDiscConnectionModalAnalysisAtASpeed._Cast_RingPinsToDiscConnectionModalAnalysisAtASpeed",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RingPinsToDiscConnectionModalAnalysisAtASpeed._Cast_RingPinsToDiscConnectionModalAnalysisAtASpeed",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RingPinsToDiscConnectionModalAnalysisAtASpeed._Cast_RingPinsToDiscConnectionModalAnalysisAtASpeed",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsToDiscConnectionModalAnalysisAtASpeed._Cast_RingPinsToDiscConnectionModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionModalAnalysisAtASpeed._Cast_RingPinsToDiscConnectionModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_modal_analysis_at_a_speed(
            self: "RingPinsToDiscConnectionModalAnalysisAtASpeed._Cast_RingPinsToDiscConnectionModalAnalysisAtASpeed",
        ) -> "RingPinsToDiscConnectionModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionModalAnalysisAtASpeed._Cast_RingPinsToDiscConnectionModalAnalysisAtASpeed",
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
        self: Self,
        instance_to_wrap: "RingPinsToDiscConnectionModalAnalysisAtASpeed.TYPE",
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
    def connection_load_case(self: Self) -> "_6945.RingPinsToDiscConnectionLoadCase":
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
    ) -> "RingPinsToDiscConnectionModalAnalysisAtASpeed._Cast_RingPinsToDiscConnectionModalAnalysisAtASpeed":
        return self._Cast_RingPinsToDiscConnectionModalAnalysisAtASpeed(self)
