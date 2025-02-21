"""CoaxialConnectionCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6793,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "CoaxialConnectionCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2289
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6588
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6740,
        _6699,
        _6731,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CoaxialConnectionCompoundCriticalSpeedAnalysis")


class CoaxialConnectionCompoundCriticalSpeedAnalysis(
    _6793.ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
):
    """CoaxialConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CoaxialConnectionCompoundCriticalSpeedAnalysis"
    )

    class _Cast_CoaxialConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting CoaxialConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CoaxialConnectionCompoundCriticalSpeedAnalysis._Cast_CoaxialConnectionCompoundCriticalSpeedAnalysis",
            parent: "CoaxialConnectionCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_critical_speed_analysis(
            self: "CoaxialConnectionCompoundCriticalSpeedAnalysis._Cast_CoaxialConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6793.ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6793.ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_critical_speed_analysis(
            self: "CoaxialConnectionCompoundCriticalSpeedAnalysis._Cast_CoaxialConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6699.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6699,
            )

            return self._parent._cast(
                _6699.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "CoaxialConnectionCompoundCriticalSpeedAnalysis._Cast_CoaxialConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6731.ConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6731,
            )

            return self._parent._cast(_6731.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "CoaxialConnectionCompoundCriticalSpeedAnalysis._Cast_CoaxialConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CoaxialConnectionCompoundCriticalSpeedAnalysis._Cast_CoaxialConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionCompoundCriticalSpeedAnalysis._Cast_CoaxialConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_critical_speed_analysis(
            self: "CoaxialConnectionCompoundCriticalSpeedAnalysis._Cast_CoaxialConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6740.CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6740,
            )

            return self._parent._cast(
                _6740.CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def coaxial_connection_compound_critical_speed_analysis(
            self: "CoaxialConnectionCompoundCriticalSpeedAnalysis._Cast_CoaxialConnectionCompoundCriticalSpeedAnalysis",
        ) -> "CoaxialConnectionCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionCompoundCriticalSpeedAnalysis._Cast_CoaxialConnectionCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "CoaxialConnectionCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2289.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2289.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

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
    ) -> "List[_6588.CoaxialConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CoaxialConnectionCriticalSpeedAnalysis]

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
    ) -> "List[_6588.CoaxialConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CoaxialConnectionCriticalSpeedAnalysis]

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
    ) -> "CoaxialConnectionCompoundCriticalSpeedAnalysis._Cast_CoaxialConnectionCompoundCriticalSpeedAnalysis":
        return self._Cast_CoaxialConnectionCompoundCriticalSpeedAnalysis(self)
