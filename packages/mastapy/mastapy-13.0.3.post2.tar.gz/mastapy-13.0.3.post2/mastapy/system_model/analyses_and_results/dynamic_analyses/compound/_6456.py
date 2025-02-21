"""ConceptCouplingConnectionCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6467
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ConceptCouplingConnectionCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2364
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6324
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6494,
        _6464,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingConnectionCompoundDynamicAnalysis")


class ConceptCouplingConnectionCompoundDynamicAnalysis(
    _6467.CouplingConnectionCompoundDynamicAnalysis
):
    """ConceptCouplingConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingConnectionCompoundDynamicAnalysis"
    )

    class _Cast_ConceptCouplingConnectionCompoundDynamicAnalysis:
        """Special nested class for casting ConceptCouplingConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionCompoundDynamicAnalysis._Cast_ConceptCouplingConnectionCompoundDynamicAnalysis",
            parent: "ConceptCouplingConnectionCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_dynamic_analysis(
            self: "ConceptCouplingConnectionCompoundDynamicAnalysis._Cast_ConceptCouplingConnectionCompoundDynamicAnalysis",
        ) -> "_6467.CouplingConnectionCompoundDynamicAnalysis":
            return self._parent._cast(_6467.CouplingConnectionCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "ConceptCouplingConnectionCompoundDynamicAnalysis._Cast_ConceptCouplingConnectionCompoundDynamicAnalysis",
        ) -> "_6494.InterMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6494,
            )

            return self._parent._cast(
                _6494.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "ConceptCouplingConnectionCompoundDynamicAnalysis._Cast_ConceptCouplingConnectionCompoundDynamicAnalysis",
        ) -> "_6464.ConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6464,
            )

            return self._parent._cast(_6464.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "ConceptCouplingConnectionCompoundDynamicAnalysis._Cast_ConceptCouplingConnectionCompoundDynamicAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingConnectionCompoundDynamicAnalysis._Cast_ConceptCouplingConnectionCompoundDynamicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionCompoundDynamicAnalysis._Cast_ConceptCouplingConnectionCompoundDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_compound_dynamic_analysis(
            self: "ConceptCouplingConnectionCompoundDynamicAnalysis._Cast_ConceptCouplingConnectionCompoundDynamicAnalysis",
        ) -> "ConceptCouplingConnectionCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionCompoundDynamicAnalysis._Cast_ConceptCouplingConnectionCompoundDynamicAnalysis",
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
        instance_to_wrap: "ConceptCouplingConnectionCompoundDynamicAnalysis.TYPE",
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
    ) -> "List[_6324.ConceptCouplingConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptCouplingConnectionDynamicAnalysis]

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
    ) -> "List[_6324.ConceptCouplingConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptCouplingConnectionDynamicAnalysis]

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
    ) -> "ConceptCouplingConnectionCompoundDynamicAnalysis._Cast_ConceptCouplingConnectionCompoundDynamicAnalysis":
        return self._Cast_ConceptCouplingConnectionCompoundDynamicAnalysis(self)
