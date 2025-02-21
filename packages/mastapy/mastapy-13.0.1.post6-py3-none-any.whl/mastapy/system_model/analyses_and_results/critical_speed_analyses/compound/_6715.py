"""CVTBeltConnectionCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6684,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "CVTBeltConnectionCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6586
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6740,
        _6710,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CVTBeltConnectionCompoundCriticalSpeedAnalysis")


class CVTBeltConnectionCompoundCriticalSpeedAnalysis(
    _6684.BeltConnectionCompoundCriticalSpeedAnalysis
):
    """CVTBeltConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTBeltConnectionCompoundCriticalSpeedAnalysis"
    )

    class _Cast_CVTBeltConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting CVTBeltConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CVTBeltConnectionCompoundCriticalSpeedAnalysis._Cast_CVTBeltConnectionCompoundCriticalSpeedAnalysis",
            parent: "CVTBeltConnectionCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def belt_connection_compound_critical_speed_analysis(
            self: "CVTBeltConnectionCompoundCriticalSpeedAnalysis._Cast_CVTBeltConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6684.BeltConnectionCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6684.BeltConnectionCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "CVTBeltConnectionCompoundCriticalSpeedAnalysis._Cast_CVTBeltConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6740.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6740,
            )

            return self._parent._cast(
                _6740.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "CVTBeltConnectionCompoundCriticalSpeedAnalysis._Cast_CVTBeltConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6710.ConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6710,
            )

            return self._parent._cast(_6710.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "CVTBeltConnectionCompoundCriticalSpeedAnalysis._Cast_CVTBeltConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTBeltConnectionCompoundCriticalSpeedAnalysis._Cast_CVTBeltConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionCompoundCriticalSpeedAnalysis._Cast_CVTBeltConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_critical_speed_analysis(
            self: "CVTBeltConnectionCompoundCriticalSpeedAnalysis._Cast_CVTBeltConnectionCompoundCriticalSpeedAnalysis",
        ) -> "CVTBeltConnectionCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionCompoundCriticalSpeedAnalysis._Cast_CVTBeltConnectionCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "CVTBeltConnectionCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6586.CVTBeltConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CVTBeltConnectionCriticalSpeedAnalysis]

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
    ) -> "List[_6586.CVTBeltConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CVTBeltConnectionCriticalSpeedAnalysis]

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
    ) -> "CVTBeltConnectionCompoundCriticalSpeedAnalysis._Cast_CVTBeltConnectionCompoundCriticalSpeedAnalysis":
        return self._Cast_CVTBeltConnectionCompoundCriticalSpeedAnalysis(self)
