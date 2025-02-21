"""ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5025,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2344
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4882,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5052,
        _5022,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness"
)


class ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness(
    _5025.CouplingConnectionCompoundModalAnalysisAtAStiffness
):
    """ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness",
            parent: "ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5025.CouplingConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5025.CouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5052.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5052,
            )

            return self._parent._cast(
                _5052.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5022.ConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5022,
            )

            return self._parent._cast(_5022.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2344.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2344.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

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
    ) -> "List[_4882.ConceptCouplingConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ConceptCouplingConnectionModalAnalysisAtAStiffness]

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
    ) -> "List[_4882.ConceptCouplingConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ConceptCouplingConnectionModalAnalysisAtAStiffness]

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
    ) -> "ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness":
        return self._Cast_ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness(
            self
        )
