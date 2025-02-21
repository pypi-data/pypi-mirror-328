"""AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5022,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4859,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5011,
        _5031,
        _5033,
        _5070,
        _5084,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = (
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
)


Self = TypeVar(
    "Self",
    bound="AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
)


class AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness(
    _5022.ConnectionCompoundModalAnalysisAtAStiffness
):
    """AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
            parent: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5022.ConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(_5022.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5011.CoaxialConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5011,
            )

            return self._parent._cast(
                _5011.CoaxialConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5031.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5031,
            )

            return self._parent._cast(
                _5031.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5033.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5033,
            )

            return self._parent._cast(
                _5033.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def planetary_connection_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5070.PlanetaryConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5070,
            )

            return self._parent._cast(
                _5070.PlanetaryConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> (
            "_5084.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5084,
            )

            return self._parent._cast(
                _5084.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4859.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4859.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness]

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
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness(
            self
        )
