"""PlanetaryConnectionModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5214
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "PlanetaryConnectionModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2287
    from mastapy.system_model.analyses_and_results.static_loads import _6932
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5119,
        _5151,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7540, _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="PlanetaryConnectionModalAnalysisAtASpeed")


class PlanetaryConnectionModalAnalysisAtASpeed(
    _5214.ShaftToMountableComponentConnectionModalAnalysisAtASpeed
):
    """PlanetaryConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryConnectionModalAnalysisAtASpeed"
    )

    class _Cast_PlanetaryConnectionModalAnalysisAtASpeed:
        """Special nested class for casting PlanetaryConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "PlanetaryConnectionModalAnalysisAtASpeed._Cast_PlanetaryConnectionModalAnalysisAtASpeed",
            parent: "PlanetaryConnectionModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "PlanetaryConnectionModalAnalysisAtASpeed._Cast_PlanetaryConnectionModalAnalysisAtASpeed",
        ) -> "_5214.ShaftToMountableComponentConnectionModalAnalysisAtASpeed":
            return self._parent._cast(
                _5214.ShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "PlanetaryConnectionModalAnalysisAtASpeed._Cast_PlanetaryConnectionModalAnalysisAtASpeed",
        ) -> "_5119.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5119,
            )

            return self._parent._cast(
                _5119.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "PlanetaryConnectionModalAnalysisAtASpeed._Cast_PlanetaryConnectionModalAnalysisAtASpeed",
        ) -> "_5151.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5151,
            )

            return self._parent._cast(_5151.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "PlanetaryConnectionModalAnalysisAtASpeed._Cast_PlanetaryConnectionModalAnalysisAtASpeed",
        ) -> "_7540.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionModalAnalysisAtASpeed._Cast_PlanetaryConnectionModalAnalysisAtASpeed",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionModalAnalysisAtASpeed._Cast_PlanetaryConnectionModalAnalysisAtASpeed",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionModalAnalysisAtASpeed._Cast_PlanetaryConnectionModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionModalAnalysisAtASpeed._Cast_PlanetaryConnectionModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_connection_modal_analysis_at_a_speed(
            self: "PlanetaryConnectionModalAnalysisAtASpeed._Cast_PlanetaryConnectionModalAnalysisAtASpeed",
        ) -> "PlanetaryConnectionModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionModalAnalysisAtASpeed._Cast_PlanetaryConnectionModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "PlanetaryConnectionModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2287.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6932.PlanetaryConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase

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
    ) -> "PlanetaryConnectionModalAnalysisAtASpeed._Cast_PlanetaryConnectionModalAnalysisAtASpeed":
        return self._Cast_PlanetaryConnectionModalAnalysisAtASpeed(self)
