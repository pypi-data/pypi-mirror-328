"""CVTBeltConnectionCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5277,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "CVTBeltConnectionCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5178,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5333,
        _5303,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CVTBeltConnectionCompoundModalAnalysisAtASpeed")


class CVTBeltConnectionCompoundModalAnalysisAtASpeed(
    _5277.BeltConnectionCompoundModalAnalysisAtASpeed
):
    """CVTBeltConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTBeltConnectionCompoundModalAnalysisAtASpeed"
    )

    class _Cast_CVTBeltConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CVTBeltConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CVTBeltConnectionCompoundModalAnalysisAtASpeed._Cast_CVTBeltConnectionCompoundModalAnalysisAtASpeed",
            parent: "CVTBeltConnectionCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def belt_connection_compound_modal_analysis_at_a_speed(
            self: "CVTBeltConnectionCompoundModalAnalysisAtASpeed._Cast_CVTBeltConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5277.BeltConnectionCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5277.BeltConnectionCompoundModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "CVTBeltConnectionCompoundModalAnalysisAtASpeed._Cast_CVTBeltConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5333.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5333,
            )

            return self._parent._cast(
                _5333.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "CVTBeltConnectionCompoundModalAnalysisAtASpeed._Cast_CVTBeltConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5303.ConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5303,
            )

            return self._parent._cast(_5303.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysisAtASpeed._Cast_CVTBeltConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysisAtASpeed._Cast_CVTBeltConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysisAtASpeed._Cast_CVTBeltConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_speed(
            self: "CVTBeltConnectionCompoundModalAnalysisAtASpeed._Cast_CVTBeltConnectionCompoundModalAnalysisAtASpeed",
        ) -> "CVTBeltConnectionCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionCompoundModalAnalysisAtASpeed._Cast_CVTBeltConnectionCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "CVTBeltConnectionCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5178.CVTBeltConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CVTBeltConnectionModalAnalysisAtASpeed]

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
    ) -> "List[_5178.CVTBeltConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CVTBeltConnectionModalAnalysisAtASpeed]

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
    ) -> "CVTBeltConnectionCompoundModalAnalysisAtASpeed._Cast_CVTBeltConnectionCompoundModalAnalysisAtASpeed":
        return self._Cast_CVTBeltConnectionCompoundModalAnalysisAtASpeed(self)
