"""CoaxialConnectionLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6952
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CoaxialConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2269
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6859,
        _6810,
        _6850,
    )
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionLoadCase",)


Self = TypeVar("Self", bound="CoaxialConnectionLoadCase")


class CoaxialConnectionLoadCase(_6952.ShaftToMountableComponentConnectionLoadCase):
    """CoaxialConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CoaxialConnectionLoadCase")

    class _Cast_CoaxialConnectionLoadCase:
        """Special nested class for casting CoaxialConnectionLoadCase to subclasses."""

        def __init__(
            self: "CoaxialConnectionLoadCase._Cast_CoaxialConnectionLoadCase",
            parent: "CoaxialConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_load_case(
            self: "CoaxialConnectionLoadCase._Cast_CoaxialConnectionLoadCase",
        ) -> "_6952.ShaftToMountableComponentConnectionLoadCase":
            return self._parent._cast(_6952.ShaftToMountableComponentConnectionLoadCase)

        @property
        def abstract_shaft_to_mountable_component_connection_load_case(
            self: "CoaxialConnectionLoadCase._Cast_CoaxialConnectionLoadCase",
        ) -> "_6810.AbstractShaftToMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6810

            return self._parent._cast(
                _6810.AbstractShaftToMountableComponentConnectionLoadCase
            )

        @property
        def connection_load_case(
            self: "CoaxialConnectionLoadCase._Cast_CoaxialConnectionLoadCase",
        ) -> "_6850.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6850

            return self._parent._cast(_6850.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionLoadCase._Cast_CoaxialConnectionLoadCase",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionLoadCase._Cast_CoaxialConnectionLoadCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionLoadCase._Cast_CoaxialConnectionLoadCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_load_case(
            self: "CoaxialConnectionLoadCase._Cast_CoaxialConnectionLoadCase",
        ) -> "_6859.CycloidalDiscCentralBearingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(
                _6859.CycloidalDiscCentralBearingConnectionLoadCase
            )

        @property
        def coaxial_connection_load_case(
            self: "CoaxialConnectionLoadCase._Cast_CoaxialConnectionLoadCase",
        ) -> "CoaxialConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionLoadCase._Cast_CoaxialConnectionLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CoaxialConnectionLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2269.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

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
    ) -> "CoaxialConnectionLoadCase._Cast_CoaxialConnectionLoadCase":
        return self._Cast_CoaxialConnectionLoadCase(self)
