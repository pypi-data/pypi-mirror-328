"""ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7200,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2364
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7059,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7227,
        _7197,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = (
    "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
)


Self = TypeVar(
    "Self",
    bound="ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
)


class ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7200.CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7200.CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            return self._parent._cast(
                _7200.CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7227.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7227,
            )

            return self._parent._cast(
                _7227.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7197.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7197,
            )

            return self._parent._cast(
                _7197.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_analysis(
            self: "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2364.ConceptCouplingConnection":
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
    def connection_design(self: Self) -> "_2364.ConceptCouplingConnection":
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
    ) -> (
        "List[_7059.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation]"
    ):
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> (
        "List[_7059.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation]"
    ):
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
