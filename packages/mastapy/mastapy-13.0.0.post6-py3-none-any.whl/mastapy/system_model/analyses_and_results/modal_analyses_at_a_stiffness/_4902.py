"""CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4859,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
        "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2338
    from mastapy.system_model.analyses_and_results.static_loads import _6860
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4891,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7540, _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness"
)


class CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness(
    _4859.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness
):
    """CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness",
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness",
            parent: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness",
        ) -> (
            "_4859.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness"
        ):
            return self._parent._cast(
                _4859.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_4891.ConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4891,
            )

            return self._parent._cast(_4891.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_7540.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness",
        ) -> "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2338.CycloidalDiscPlanetaryBearingConnection":
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
    def connection_load_case(
        self: Self,
    ) -> "_6860.CycloidalDiscPlanetaryBearingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase

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
    ) -> "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness":
        return (
            self._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness(
                self
            )
        )
