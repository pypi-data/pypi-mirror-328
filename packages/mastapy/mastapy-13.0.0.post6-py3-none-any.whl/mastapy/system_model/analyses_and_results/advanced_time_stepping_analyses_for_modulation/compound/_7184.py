"""CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7164,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7055,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7237,
        _7143,
        _7175,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = (
    "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
)


Self = TypeVar(
    "Self",
    bound="CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
)


class CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7164.CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7164.CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7164.CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_to_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7237.ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7237,
            )

            return self._parent._cast(
                _7237.ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7143.AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7143,
            )

            return self._parent._cast(
                _7143.AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7175.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7175,
            )

            return self._parent._cast(
                _7175.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7055.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7055.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
