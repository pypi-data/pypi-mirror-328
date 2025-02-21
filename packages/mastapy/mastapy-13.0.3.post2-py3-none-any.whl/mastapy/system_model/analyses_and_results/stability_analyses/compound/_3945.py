"""ConceptCouplingConnectionCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3956
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "ConceptCouplingConnectionCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2364
    from mastapy.system_model.analyses_and_results.stability_analyses import _3810
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3983,
        _3953,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingConnectionCompoundStabilityAnalysis")


class ConceptCouplingConnectionCompoundStabilityAnalysis(
    _3956.CouplingConnectionCompoundStabilityAnalysis
):
    """ConceptCouplingConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingConnectionCompoundStabilityAnalysis"
    )

    class _Cast_ConceptCouplingConnectionCompoundStabilityAnalysis:
        """Special nested class for casting ConceptCouplingConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionCompoundStabilityAnalysis._Cast_ConceptCouplingConnectionCompoundStabilityAnalysis",
            parent: "ConceptCouplingConnectionCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_stability_analysis(
            self: "ConceptCouplingConnectionCompoundStabilityAnalysis._Cast_ConceptCouplingConnectionCompoundStabilityAnalysis",
        ) -> "_3956.CouplingConnectionCompoundStabilityAnalysis":
            return self._parent._cast(_3956.CouplingConnectionCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "ConceptCouplingConnectionCompoundStabilityAnalysis._Cast_ConceptCouplingConnectionCompoundStabilityAnalysis",
        ) -> "_3983.InterMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3983,
            )

            return self._parent._cast(
                _3983.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "ConceptCouplingConnectionCompoundStabilityAnalysis._Cast_ConceptCouplingConnectionCompoundStabilityAnalysis",
        ) -> "_3953.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3953,
            )

            return self._parent._cast(_3953.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "ConceptCouplingConnectionCompoundStabilityAnalysis._Cast_ConceptCouplingConnectionCompoundStabilityAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingConnectionCompoundStabilityAnalysis._Cast_ConceptCouplingConnectionCompoundStabilityAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionCompoundStabilityAnalysis._Cast_ConceptCouplingConnectionCompoundStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_compound_stability_analysis(
            self: "ConceptCouplingConnectionCompoundStabilityAnalysis._Cast_ConceptCouplingConnectionCompoundStabilityAnalysis",
        ) -> "ConceptCouplingConnectionCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionCompoundStabilityAnalysis._Cast_ConceptCouplingConnectionCompoundStabilityAnalysis",
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
        instance_to_wrap: "ConceptCouplingConnectionCompoundStabilityAnalysis.TYPE",
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
    ) -> "List[_3810.ConceptCouplingConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConceptCouplingConnectionStabilityAnalysis]

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
    ) -> "List[_3810.ConceptCouplingConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConceptCouplingConnectionStabilityAnalysis]

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
    ) -> "ConceptCouplingConnectionCompoundStabilityAnalysis._Cast_ConceptCouplingConnectionCompoundStabilityAnalysis":
        return self._Cast_ConceptCouplingConnectionCompoundStabilityAnalysis(self)
