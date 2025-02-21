"""CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5271,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
        "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2358
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5184,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5303,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self", bound="CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed"
)


class CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed(
    _5271.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
):
    """CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = (
        _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed",
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed",
            parent: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5271.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5271.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5303.ConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5303,
            )

            return self._parent._cast(_5303.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis_at_a_speed(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2358.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5184.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5184.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed":
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed(
            self
        )
