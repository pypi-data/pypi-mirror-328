"""BeltConnectionCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6494
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "BeltConnectionCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2288
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6469,
        _6464,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="BeltConnectionCompoundDynamicAnalysis")


class BeltConnectionCompoundDynamicAnalysis(
    _6494.InterMountableComponentConnectionCompoundDynamicAnalysis
):
    """BeltConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltConnectionCompoundDynamicAnalysis"
    )

    class _Cast_BeltConnectionCompoundDynamicAnalysis:
        """Special nested class for casting BeltConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "BeltConnectionCompoundDynamicAnalysis._Cast_BeltConnectionCompoundDynamicAnalysis",
            parent: "BeltConnectionCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "BeltConnectionCompoundDynamicAnalysis._Cast_BeltConnectionCompoundDynamicAnalysis",
        ) -> "_6494.InterMountableComponentConnectionCompoundDynamicAnalysis":
            return self._parent._cast(
                _6494.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "BeltConnectionCompoundDynamicAnalysis._Cast_BeltConnectionCompoundDynamicAnalysis",
        ) -> "_6464.ConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6464,
            )

            return self._parent._cast(_6464.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "BeltConnectionCompoundDynamicAnalysis._Cast_BeltConnectionCompoundDynamicAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltConnectionCompoundDynamicAnalysis._Cast_BeltConnectionCompoundDynamicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionCompoundDynamicAnalysis._Cast_BeltConnectionCompoundDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_dynamic_analysis(
            self: "BeltConnectionCompoundDynamicAnalysis._Cast_BeltConnectionCompoundDynamicAnalysis",
        ) -> "_6469.CVTBeltConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6469,
            )

            return self._parent._cast(_6469.CVTBeltConnectionCompoundDynamicAnalysis)

        @property
        def belt_connection_compound_dynamic_analysis(
            self: "BeltConnectionCompoundDynamicAnalysis._Cast_BeltConnectionCompoundDynamicAnalysis",
        ) -> "BeltConnectionCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BeltConnectionCompoundDynamicAnalysis._Cast_BeltConnectionCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "BeltConnectionCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2288.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2288.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

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
    ) -> "List[_6307.BeltConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BeltConnectionDynamicAnalysis]

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
    ) -> "List[_6307.BeltConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BeltConnectionDynamicAnalysis]

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
    ) -> "BeltConnectionCompoundDynamicAnalysis._Cast_BeltConnectionCompoundDynamicAnalysis":
        return self._Cast_BeltConnectionCompoundDynamicAnalysis(self)
