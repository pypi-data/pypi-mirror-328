"""BeltConnectionCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5312,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "BeltConnectionCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2268
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5126,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5287,
        _5282,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="BeltConnectionCompoundModalAnalysisAtASpeed")


class BeltConnectionCompoundModalAnalysisAtASpeed(
    _5312.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
):
    """BeltConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltConnectionCompoundModalAnalysisAtASpeed"
    )

    class _Cast_BeltConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting BeltConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "BeltConnectionCompoundModalAnalysisAtASpeed._Cast_BeltConnectionCompoundModalAnalysisAtASpeed",
            parent: "BeltConnectionCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "BeltConnectionCompoundModalAnalysisAtASpeed._Cast_BeltConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5312.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5312.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "BeltConnectionCompoundModalAnalysisAtASpeed._Cast_BeltConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5282.ConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5282,
            )

            return self._parent._cast(_5282.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "BeltConnectionCompoundModalAnalysisAtASpeed._Cast_BeltConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltConnectionCompoundModalAnalysisAtASpeed._Cast_BeltConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionCompoundModalAnalysisAtASpeed._Cast_BeltConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_speed(
            self: "BeltConnectionCompoundModalAnalysisAtASpeed._Cast_BeltConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5287.CVTBeltConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5287,
            )

            return self._parent._cast(
                _5287.CVTBeltConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def belt_connection_compound_modal_analysis_at_a_speed(
            self: "BeltConnectionCompoundModalAnalysisAtASpeed._Cast_BeltConnectionCompoundModalAnalysisAtASpeed",
        ) -> "BeltConnectionCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "BeltConnectionCompoundModalAnalysisAtASpeed._Cast_BeltConnectionCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "BeltConnectionCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2268.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2268.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

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
    ) -> "List[_5126.BeltConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.BeltConnectionModalAnalysisAtASpeed]

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
    ) -> "List[_5126.BeltConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.BeltConnectionModalAnalysisAtASpeed]

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
    ) -> "BeltConnectionCompoundModalAnalysisAtASpeed._Cast_BeltConnectionCompoundModalAnalysisAtASpeed":
        return self._Cast_BeltConnectionCompoundModalAnalysisAtASpeed(self)
