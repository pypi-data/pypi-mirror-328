"""RingPinsToDiscConnectionCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3962
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "RingPinsToDiscConnectionCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2341
    from mastapy.system_model.analyses_and_results.stability_analyses import _3855
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3932,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="RingPinsToDiscConnectionCompoundStabilityAnalysis")


class RingPinsToDiscConnectionCompoundStabilityAnalysis(
    _3962.InterMountableComponentConnectionCompoundStabilityAnalysis
):
    """RingPinsToDiscConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsToDiscConnectionCompoundStabilityAnalysis"
    )

    class _Cast_RingPinsToDiscConnectionCompoundStabilityAnalysis:
        """Special nested class for casting RingPinsToDiscConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionCompoundStabilityAnalysis._Cast_RingPinsToDiscConnectionCompoundStabilityAnalysis",
            parent: "RingPinsToDiscConnectionCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "RingPinsToDiscConnectionCompoundStabilityAnalysis._Cast_RingPinsToDiscConnectionCompoundStabilityAnalysis",
        ) -> "_3962.InterMountableComponentConnectionCompoundStabilityAnalysis":
            return self._parent._cast(
                _3962.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "RingPinsToDiscConnectionCompoundStabilityAnalysis._Cast_RingPinsToDiscConnectionCompoundStabilityAnalysis",
        ) -> "_3932.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3932,
            )

            return self._parent._cast(_3932.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "RingPinsToDiscConnectionCompoundStabilityAnalysis._Cast_RingPinsToDiscConnectionCompoundStabilityAnalysis",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RingPinsToDiscConnectionCompoundStabilityAnalysis._Cast_RingPinsToDiscConnectionCompoundStabilityAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionCompoundStabilityAnalysis._Cast_RingPinsToDiscConnectionCompoundStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_stability_analysis(
            self: "RingPinsToDiscConnectionCompoundStabilityAnalysis._Cast_RingPinsToDiscConnectionCompoundStabilityAnalysis",
        ) -> "RingPinsToDiscConnectionCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionCompoundStabilityAnalysis._Cast_RingPinsToDiscConnectionCompoundStabilityAnalysis",
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
        instance_to_wrap: "RingPinsToDiscConnectionCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2341.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2341.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

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
    ) -> "List[_3855.RingPinsToDiscConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.RingPinsToDiscConnectionStabilityAnalysis]

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
    ) -> "List[_3855.RingPinsToDiscConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.RingPinsToDiscConnectionStabilityAnalysis]

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
    ) -> "RingPinsToDiscConnectionCompoundStabilityAnalysis._Cast_RingPinsToDiscConnectionCompoundStabilityAnalysis":
        return self._Cast_RingPinsToDiscConnectionCompoundStabilityAnalysis(self)
