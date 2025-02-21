"""RollingRingConnectionCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5333,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "RollingRingConnectionCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2312
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5231,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5303,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingConnectionCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="RollingRingConnectionCompoundModalAnalysisAtASpeed")


class RollingRingConnectionCompoundModalAnalysisAtASpeed(
    _5333.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
):
    """RollingRingConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingConnectionCompoundModalAnalysisAtASpeed"
    )

    class _Cast_RollingRingConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting RollingRingConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "RollingRingConnectionCompoundModalAnalysisAtASpeed._Cast_RollingRingConnectionCompoundModalAnalysisAtASpeed",
            parent: "RollingRingConnectionCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "RollingRingConnectionCompoundModalAnalysisAtASpeed._Cast_RollingRingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5333.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5333.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "RollingRingConnectionCompoundModalAnalysisAtASpeed._Cast_RollingRingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5303.ConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5303,
            )

            return self._parent._cast(_5303.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "RollingRingConnectionCompoundModalAnalysisAtASpeed._Cast_RollingRingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingConnectionCompoundModalAnalysisAtASpeed._Cast_RollingRingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingConnectionCompoundModalAnalysisAtASpeed._Cast_RollingRingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def rolling_ring_connection_compound_modal_analysis_at_a_speed(
            self: "RollingRingConnectionCompoundModalAnalysisAtASpeed._Cast_RollingRingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "RollingRingConnectionCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "RollingRingConnectionCompoundModalAnalysisAtASpeed._Cast_RollingRingConnectionCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "RollingRingConnectionCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2312.RollingRingConnection":
        """mastapy.system_model.connections_and_sockets.RollingRingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2312.RollingRingConnection":
        """mastapy.system_model.connections_and_sockets.RollingRingConnection

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
    ) -> "List[_5231.RollingRingConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.RollingRingConnectionModalAnalysisAtASpeed]

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
    def planetaries(
        self: Self,
    ) -> "List[RollingRingConnectionCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.RollingRingConnectionCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5231.RollingRingConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.RollingRingConnectionModalAnalysisAtASpeed]

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
    ) -> "RollingRingConnectionCompoundModalAnalysisAtASpeed._Cast_RollingRingConnectionCompoundModalAnalysisAtASpeed":
        return self._Cast_RollingRingConnectionCompoundModalAnalysisAtASpeed(self)
