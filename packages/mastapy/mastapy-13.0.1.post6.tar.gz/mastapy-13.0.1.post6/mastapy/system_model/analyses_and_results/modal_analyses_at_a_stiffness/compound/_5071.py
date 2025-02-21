"""PlanetaryConnectionCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5085,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "PlanetaryConnectionCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2287
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4942,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _4991,
        _5023,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="PlanetaryConnectionCompoundModalAnalysisAtAStiffness")


class PlanetaryConnectionCompoundModalAnalysisAtAStiffness(
    _5085.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
):
    """PlanetaryConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryConnectionCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_PlanetaryConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting PlanetaryConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "PlanetaryConnectionCompoundModalAnalysisAtAStiffness._Cast_PlanetaryConnectionCompoundModalAnalysisAtAStiffness",
            parent: "PlanetaryConnectionCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "PlanetaryConnectionCompoundModalAnalysisAtAStiffness._Cast_PlanetaryConnectionCompoundModalAnalysisAtAStiffness",
        ) -> (
            "_5085.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
        ):
            return self._parent._cast(
                _5085.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "PlanetaryConnectionCompoundModalAnalysisAtAStiffness._Cast_PlanetaryConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_4991.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4991,
            )

            return self._parent._cast(
                _4991.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "PlanetaryConnectionCompoundModalAnalysisAtAStiffness._Cast_PlanetaryConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5023.ConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5023,
            )

            return self._parent._cast(_5023.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "PlanetaryConnectionCompoundModalAnalysisAtAStiffness._Cast_PlanetaryConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryConnectionCompoundModalAnalysisAtAStiffness._Cast_PlanetaryConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionCompoundModalAnalysisAtAStiffness._Cast_PlanetaryConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_connection_compound_modal_analysis_at_a_stiffness(
            self: "PlanetaryConnectionCompoundModalAnalysisAtAStiffness._Cast_PlanetaryConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "PlanetaryConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionCompoundModalAnalysisAtAStiffness._Cast_PlanetaryConnectionCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "PlanetaryConnectionCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2287.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2287.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

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
    ) -> "List[_4942.PlanetaryConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.PlanetaryConnectionModalAnalysisAtAStiffness]

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
    ) -> "List[_4942.PlanetaryConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.PlanetaryConnectionModalAnalysisAtAStiffness]

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
    ) -> "PlanetaryConnectionCompoundModalAnalysisAtAStiffness._Cast_PlanetaryConnectionCompoundModalAnalysisAtAStiffness":
        return self._Cast_PlanetaryConnectionCompoundModalAnalysisAtAStiffness(self)
