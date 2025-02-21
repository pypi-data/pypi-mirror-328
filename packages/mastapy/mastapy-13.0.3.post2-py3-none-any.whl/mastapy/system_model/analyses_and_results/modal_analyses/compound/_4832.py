"""PlanetaryConnectionCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4846
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "PlanetaryConnectionCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2307
    from mastapy.system_model.analyses_and_results.modal_analyses import _4687
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4752,
        _4784,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionCompoundModalAnalysis",)


Self = TypeVar("Self", bound="PlanetaryConnectionCompoundModalAnalysis")


class PlanetaryConnectionCompoundModalAnalysis(
    _4846.ShaftToMountableComponentConnectionCompoundModalAnalysis
):
    """PlanetaryConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryConnectionCompoundModalAnalysis"
    )

    class _Cast_PlanetaryConnectionCompoundModalAnalysis:
        """Special nested class for casting PlanetaryConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryConnectionCompoundModalAnalysis._Cast_PlanetaryConnectionCompoundModalAnalysis",
            parent: "PlanetaryConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "PlanetaryConnectionCompoundModalAnalysis._Cast_PlanetaryConnectionCompoundModalAnalysis",
        ) -> "_4846.ShaftToMountableComponentConnectionCompoundModalAnalysis":
            return self._parent._cast(
                _4846.ShaftToMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "PlanetaryConnectionCompoundModalAnalysis._Cast_PlanetaryConnectionCompoundModalAnalysis",
        ) -> "_4752.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4752,
            )

            return self._parent._cast(
                _4752.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "PlanetaryConnectionCompoundModalAnalysis._Cast_PlanetaryConnectionCompoundModalAnalysis",
        ) -> "_4784.ConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4784,
            )

            return self._parent._cast(_4784.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "PlanetaryConnectionCompoundModalAnalysis._Cast_PlanetaryConnectionCompoundModalAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryConnectionCompoundModalAnalysis._Cast_PlanetaryConnectionCompoundModalAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionCompoundModalAnalysis._Cast_PlanetaryConnectionCompoundModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_connection_compound_modal_analysis(
            self: "PlanetaryConnectionCompoundModalAnalysis._Cast_PlanetaryConnectionCompoundModalAnalysis",
        ) -> "PlanetaryConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionCompoundModalAnalysis._Cast_PlanetaryConnectionCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryConnectionCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2307.PlanetaryConnection":
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
    def connection_design(self: Self) -> "_2307.PlanetaryConnection":
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
    ) -> "List[_4687.PlanetaryConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.PlanetaryConnectionModalAnalysis]

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
    ) -> "List[_4687.PlanetaryConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.PlanetaryConnectionModalAnalysis]

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
    ) -> "PlanetaryConnectionCompoundModalAnalysis._Cast_PlanetaryConnectionCompoundModalAnalysis":
        return self._Cast_PlanetaryConnectionCompoundModalAnalysis(self)
