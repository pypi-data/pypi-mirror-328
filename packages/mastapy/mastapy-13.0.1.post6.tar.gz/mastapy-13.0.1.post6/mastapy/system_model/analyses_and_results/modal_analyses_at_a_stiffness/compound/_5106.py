"""TorqueConverterConnectionCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5026,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2352
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4976,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5053,
        _5023,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="TorqueConverterConnectionCompoundModalAnalysisAtAStiffness"
)


class TorqueConverterConnectionCompoundModalAnalysisAtAStiffness(
    _5026.CouplingConnectionCompoundModalAnalysisAtAStiffness
):
    """TorqueConverterConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting TorqueConverterConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
            parent: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5026.CouplingConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5026.CouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5053.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5053,
            )

            return self._parent._cast(
                _5053.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5023.ConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5023,
            )

            return self._parent._cast(_5023.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_stiffness(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2352.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2352.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

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
    ) -> "List[_4976.TorqueConverterConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.TorqueConverterConnectionModalAnalysisAtAStiffness]

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
    ) -> "List[_4976.TorqueConverterConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.TorqueConverterConnectionModalAnalysisAtAStiffness]

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
    ) -> "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness":
        return self._Cast_TorqueConverterConnectionCompoundModalAnalysisAtAStiffness(
            self
        )
