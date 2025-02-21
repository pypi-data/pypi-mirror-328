"""CycloidalDiscPlanetaryBearingConnectionLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6831
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CycloidalDiscPlanetaryBearingConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2358
    from mastapy.system_model.analyses_and_results.static_loads import _6871
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingConnectionLoadCase",)


Self = TypeVar("Self", bound="CycloidalDiscPlanetaryBearingConnectionLoadCase")


class CycloidalDiscPlanetaryBearingConnectionLoadCase(
    _6831.AbstractShaftToMountableComponentConnectionLoadCase
):
    """CycloidalDiscPlanetaryBearingConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscPlanetaryBearingConnectionLoadCase"
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionLoadCase:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionLoadCase to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionLoadCase._Cast_CycloidalDiscPlanetaryBearingConnectionLoadCase",
            parent: "CycloidalDiscPlanetaryBearingConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_load_case(
            self: "CycloidalDiscPlanetaryBearingConnectionLoadCase._Cast_CycloidalDiscPlanetaryBearingConnectionLoadCase",
        ) -> "_6831.AbstractShaftToMountableComponentConnectionLoadCase":
            return self._parent._cast(
                _6831.AbstractShaftToMountableComponentConnectionLoadCase
            )

        @property
        def connection_load_case(
            self: "CycloidalDiscPlanetaryBearingConnectionLoadCase._Cast_CycloidalDiscPlanetaryBearingConnectionLoadCase",
        ) -> "_6871.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6871

            return self._parent._cast(_6871.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionLoadCase._Cast_CycloidalDiscPlanetaryBearingConnectionLoadCase",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionLoadCase._Cast_CycloidalDiscPlanetaryBearingConnectionLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionLoadCase._Cast_CycloidalDiscPlanetaryBearingConnectionLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_load_case(
            self: "CycloidalDiscPlanetaryBearingConnectionLoadCase._Cast_CycloidalDiscPlanetaryBearingConnectionLoadCase",
        ) -> "CycloidalDiscPlanetaryBearingConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionLoadCase._Cast_CycloidalDiscPlanetaryBearingConnectionLoadCase",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionLoadCase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2358.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

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
    ) -> "CycloidalDiscPlanetaryBearingConnectionLoadCase._Cast_CycloidalDiscPlanetaryBearingConnectionLoadCase":
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionLoadCase(self)
