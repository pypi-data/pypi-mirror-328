"""CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7150,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7052,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7206,
        _7176,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7150.BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def belt_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7150.BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7150.BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7206.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7206,
            )

            return self._parent._cast(
                _7206.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7176.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7176,
            )

            return self._parent._cast(
                _7176.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_analysis(
            self: "CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7052.CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7052.CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
